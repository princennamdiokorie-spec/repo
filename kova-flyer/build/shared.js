// Shared flyer furniture: the minimal contact line and deterministic sparkles.
const ICON_FILL = '#4fc3ff';
const ICONS = {
  phone: `<svg viewBox="0 0 24 24"><path fill="${ICON_FILL}" d="M6.6 10.8a15.2 15.2 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>`,
  mail: `<svg viewBox="0 0 24 24"><path fill="${ICON_FILL}" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>`,
  insta: `<svg viewBox="0 0 24 24"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5" fill="none" stroke="${ICON_FILL}" stroke-width="2.4"/><circle cx="12" cy="12" r="4.3" fill="none" stroke="${ICON_FILL}" stroke-width="2.4"/><circle cx="17.4" cy="6.6" r="1.4" fill="${ICON_FILL}"/></svg>`,
  snap: `<svg viewBox="0 0 24 24"><path fill="${ICON_FILL}" d="M12 2.2c3 0 5.3 2.3 5.3 5.4v2.6c.5.2 1.2-.3 1.7-.1.6.3.4 1-.1 1.3-.6.3-1.6.5-1.7 1 .6 1.9 2.2 3.5 4.1 4 .4.1.5.6.1.8-.7.4-1.7.4-2 .8-.2.5-.2 1-.7 1.1-.7.1-1.5-.3-2.4.1-1 .5-1.7 1.6-4.3 1.6s-3.3-1.1-4.3-1.6c-.9-.4-1.7 0-2.4-.1-.5-.1-.5-.6-.7-1.1-.3-.4-1.3-.4-2-.8-.4-.2-.3-.7.1-.8 1.9-.5 3.5-2.1 4.1-4-.1-.5-1.1-.7-1.7-1-.5-.3-.7-1-.1-1.3.5-.2 1.2.3 1.7.1V7.6c0-3.1 2.3-5.4 5.3-5.4z"/></svg>`,
};

const contact = document.getElementById('contact');
if (contact) {
  contact.innerHTML = [
    `<span class="it">${ICONS.phone}09166586974</span>`,
    `<span class="it">${ICONS.mail}info@kova-lifestyle.com</span>`,
    `<span class="it">${ICONS.insta}${ICONS.snap}@kova.lifestyle</span>`,
  ].join('<span class="dot"></span>');
}

const sparks = document.getElementById('sparks');
if (sparks) {
  let seed = 7;
  const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  let html = '';
  for (let i = 0; i < 60; i++) {
    const size = 1 + rand() * 3;
    html += `<div class="spark" style="left:${rand() * 1080}px;top:${rand() * 1100}px;width:${size}px;height:${size}px;opacity:${0.3 + rand() * 0.7}"></div>`;
  }
  sparks.innerHTML = html;
}
