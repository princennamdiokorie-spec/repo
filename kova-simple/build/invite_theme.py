"""Make a themed, dated copy of the blue invite (invite.html -> invite-<theme>.html) using the
same colour maps as the flyers (make_theme.py), plus the invite-only colours below.
Usage: python3 invite_theme.py <theme> <DAY> <DATE>   e.g. red FRIDAY 11TH"""
import re, sys
src = open('make_theme.py').read()
ns = {}; exec(src[:src.index('name = sys.argv')], ns)          # THEMES only
EXTRA = {
  'red':     {'rgba(4,10,28,': 'rgba(36,1,21,', 'rgba(124,196,255,': 'rgba(255,138,152,', '#e8edf5': '#f5e8ec', '#dde4ee': '#eedde2'},
  'emerald': {'rgba(4,10,28,': 'rgba(1,20,14,', 'rgba(124,196,255,': 'rgba(232,207,154,', '#e8edf5': '#e8f5ef', '#dde4ee': '#ddeee6'},
}
name, day, date = sys.argv[1], sys.argv[2], sys.argv[3]
cmap = {**ns['THEMES'][name]['map'], **EXTRA[name]}
s = open('invite.html').read()
for a, b in sorted(cmap.items(), key=lambda kv: -len(kv[0])):
    s = re.sub(re.escape(a), b, s, flags=re.I)
for asset in ['kova-logo-transparent', 'kova-symbol-hd']:
    s = s.replace(f'../assets/{asset}.png', f'../assets/{asset}-{name}.png')
for a, b in [('<div class="cell s">THURSDAY</div>', f'<div class="cell s">{day}</div>'),
             ('<div class="big chrome">10TH</div>', f'<div class="big chrome">{date}</div>')]:
    assert s.count(a) == 1, a; s = s.replace(a, b)
left = [c for c in ['#2a8cff', '#7cc4ff', '#040a1c', '#0b2257', 'rgba(42,140,255', 'rgba(124,196,255', 'rgba(4,10,28'] if c in s.lower()]
assert not left, ('blue left over', left)
open(f'invite-{name}.html', 'w').write(s); print('wrote', f'invite-{name}.html', day, date)
