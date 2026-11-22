import numpy as np
from PIL import Image
from scipy import ndimage as ndi
src='/tmp/claude-0/-home-user-repo/5e1ab526-a972-5fdd-8ff6-5df0838f7cd4/images/1.jpg'
a=np.asarray(Image.open(src).convert('RGB')).astype(np.float64)/255
H,W,_=a.shape
mx=a.max(2)
# 1) Glow layer: colour-to-alpha against pure black (removes black without a dark halo)
floor=0.045  # JPEG noise floor on the black background
alpha=np.clip((mx-floor)/(1-floor),0,1)
rgb=np.where(alpha[...,None]>0, a/np.maximum(mx,1e-6)[...,None], 0)
# 2) Solid core: the chrome/blue letterforms, fully opaque
lum=a@[0.299,0.587,0.114]
core=mx>0.42
core=ndi.binary_opening(core,iterations=1)
lab,n=ndi.label(core); sizes=ndi.sum(core,lab,range(1,n+1))
core=np.isin(lab,1+np.where(sizes>150)[0])
# fill only small dark pockets inside the chrome (keep the O / diamond / loop holes open)
holes=ndi.binary_fill_holes(core)&~core
hl,hn=ndi.label(holes); hs=ndi.sum(holes,hl,range(1,hn+1))
core|=np.isin(hl,1+np.where(hs<400)[0])
# soften the core edge by 1px so it is anti-aliased, then combine
soft=ndi.gaussian_filter(core.astype(float),0.7)
A=np.maximum(alpha,np.clip(soft*1.6,0,1))
out_rgb=np.where(core[...,None],a,np.where(A[...,None]>0,np.clip(a/np.maximum(A,1e-6)[...,None],0,1),0))
A[A<0.02]=0
img=np.dstack([out_rgb,A])
im=Image.fromarray((img*255+0.5).astype(np.uint8),'RGBA')
bb=im.getbbox(); pad=12
im=im.crop((max(bb[0]-pad,0),max(bb[1]-pad,0),min(bb[2]+pad,W),min(bb[3]+pad,H)))
im.save('kova-logo-transparent.png')
# hard version: no outer glow, just the chrome/blue letterforms
A2=np.clip(soft*1.6,0,1); A2[A2<0.02]=0
im2=Image.fromarray((np.dstack([a,A2])*255+0.5).astype(np.uint8),'RGBA').crop((max(bb[0]-pad,0),max(bb[1]-pad,0),min(bb[2]+pad,W),min(bb[3]+pad,H)))
im2.save('kova-logo-transparent-noglow.png')
# preview on several backgrounds
def onbg(i,c):
    bg=Image.new('RGBA',i.size,c); bg.alpha_composite(i); return bg.convert('RGB')
ck=Image.new('RGBA',im.size)
t=np.indices(im.size[::-1]).sum(0)//1
chk=((np.indices(im.size[::-1])//16).sum(0)%2)*80+150
ck=Image.fromarray(np.dstack([chk]*3+[np.full_like(chk,255)]).astype(np.uint8),'RGBA')
ck.alpha_composite(im)
w,h=im.size; sheet=Image.new('RGB',(w*2,h*3),'white')
for k,(i,c) in enumerate([(im,'white'),(im,(200,30,40)),(im,(20,20,20)),(im2,'white'),(im2,(230,180,40))]):
    sheet.paste(onbg(i,c),((k%2)*w,(k//2)*h))
sheet.paste(ck.convert('RGB'),(w,2*h))
sheet.save('preview.png')
print(im.size)
