STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Inter:wght@400;500;600;700;800&family=Pixelify+Sans:wght@600;700&family=Space+Mono:wght@400;700&display=swap');
:root {
  --paper: #FBFAF6;
  --ink: #141414;
  --orange: #F2683C;
  --yellow: #F5C542;
  --green: #1FA971;
  --pink: #FF4F8B;
  --blue: #2B4FE0;
  --mint: #BFE8D2;
  --butter: #F8E7A6;
  --line: rgba(36, 45, 59, .09);
  --accent: var(--orange);
}
html, body, [class*="stApp"] { font-family: 'Inter', sans-serif; color: var(--ink); }
.stApp {
  background-color: #929292;
  background-image: linear-gradient(rgba(255,255,255,.26) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255,255,255,.26) 1px, transparent 1px);
  background-size: 30px 30px;
}
[data-testid="stAppViewContainer"] { background: transparent; }
[data-testid="stMain"] { background: transparent; }
[data-testid="stMainBlockContainer"] {
  box-sizing: border-box;
  max-width: 1120px;
  margin: 24px auto 38px;
  padding: 1.2rem clamp(1rem, 5vw, 4.2rem) 3rem !important;
  background-color: var(--paper);
  background-image: repeating-linear-gradient(
    to bottom, transparent 0, transparent 30px, var(--line) 31px, transparent 32px
  );
  box-shadow: 0 18px 55px rgba(0,0,0,.24);
  min-height: calc(100vh - 60px);
}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stFooter"], #MainMenu { visibility: hidden; height: 0; }
.block-container { padding-top: 0 !important; }
[data-testid="stSidebar"] { background: #fffdf8; border-right: 2px solid var(--ink); }
[data-testid="stSidebar"] [data-testid="stSidebarContent"] { padding-top: 1rem; }
h1, h2, h3, p, label { color: var(--ink); }
h1, h2, h3 { font-family: 'Inter', sans-serif; letter-spacing: -.04em; }
.brand-smile {
  display: inline-flex; width: 30px; height: 30px; flex: 0 0 30px;
  align-items: center; justify-content: center; border: 2px solid var(--ink);
  border-radius: 50%; background: var(--pink); font-size: 17px;
}
.nav-radio [role="radiogroup"] { gap: .2rem; }
.nav-radio label {
  min-height: 32px; border: 1px solid transparent; border-radius: 3px;
  padding: .35rem .58rem; background: transparent;
  font: 700 .63rem 'Space Mono', monospace; letter-spacing: .01em;
}
.nav-radio label:has(input:checked) { background: var(--yellow); border-color: var(--ink); box-shadow: 2px 2px 0 var(--ink); }
.nav-radio label > div:first-child { display: none; }
.nav-social { display: flex; justify-content: flex-end; gap: .35rem; align-items: center; }
.nav-social a {
  display: inline-flex; width: 28px; height: 28px; align-items: center; justify-content: center;
  border: 1.5px solid var(--ink); border-radius: 50%; color: var(--ink) !important;
  text-decoration: none !important; font: 700 .7rem 'Space Mono', monospace;
}
.nav-social a:nth-child(1) { background: var(--yellow); }
.nav-social a:nth-child(2) { background: var(--pink); }
.nav-social a:nth-child(3) { background: var(--mint); }
.nav-social a.contact-pill {
  width: auto; height: 28px; padding: 0 .55rem; border-radius: 2px;
  background: transparent; font-size: .58rem;
}
.nav-contact a, .scrapbook-contact a {
  color: var(--ink) !important; border: 2px solid var(--ink) !important;
  border-radius: 2px !important; background: var(--paper) !important;
  box-shadow: 3px 3px 0 var(--ink); font: 700 .68rem 'Space Mono', monospace !important;
}
.st-key-top_nav {
  position: sticky; top: 0; z-index: 20; display: flex; align-items: center;
  margin: -.3rem 0 1.4rem; padding: .3rem .2rem .65rem;
  background: rgba(251,250,246,.96); border-bottom: 1px solid rgba(20,20,20,.14);
}
.st-key-top_nav [data-testid="stRadio"] { margin-bottom: 0; }
.st-key-top_nav [data-testid="stRadio"] > label { display: none; }
.st-key-top_nav [data-testid="stRadio"] [role="radiogroup"] { gap: .15rem; flex-wrap: nowrap; }
.st-key-top_nav [data-testid="stRadio"] label {
  min-height: 31px; border: 1px solid transparent; border-radius: 2px;
  padding: .32rem .48rem; background: transparent;
  font: 700 .59rem 'Space Mono', monospace; white-space: nowrap;
}
.st-key-top_nav [data-testid="stRadio"] label:has(input:checked) {
  background: var(--yellow); border-color: var(--ink); box-shadow: 2px 2px 0 var(--ink);
}
.st-key-top_nav [data-testid="stRadio"] label > div > div:first-child { display: none; }
.hero { position: relative; text-align: center; padding: 2rem 0 2.6rem; }
.hand-label { font: 600 1.45rem 'Caveat', cursive; }
.hand-label.underline { text-decoration: underline; text-decoration-color: var(--ink); text-underline-offset: 5px; }
.name-frame {
  display: inline-block; position: relative; margin: .1rem auto .7rem; padding: .2rem 1.35rem;
  border: 3px solid var(--orange); border-radius: 14px 5px 13px 7px;
  transform: rotate(-1deg);
}
div[data-testid="stMarkdownContainer"] h1.name-pixel,
div[data-testid="stMarkdownContainer"] h1.pixel-heading {
  margin: .25rem 0 1rem;
  font-family: 'Pixelify Sans', 'Courier New', monospace !important;
  font-size: clamp(2.7rem, 9vw, 6rem) !important;
  font-weight: 700 !important; line-height: 1 !important; letter-spacing: .02em;
  text-shadow: 2px 0 currentColor, -2px 0 currentColor;
}
div[data-testid="stMarkdownContainer"] h1.pixel-heading { font-size: clamp(2.5rem,8vw,5rem) !important; }
.sticker {
  display: inline-flex; gap: .4rem; align-items: center; justify-content: center;
  padding: .32rem .75rem; border: 1.5px solid var(--ink); color: var(--ink);
  font: 700 .67rem 'Space Mono', monospace; box-shadow: 2px 2px 0 var(--ink);
  transition: transform .18s ease, box-shadow .18s ease;
}
.sticker:hover { transform: rotate(-3deg) translateY(-3px); box-shadow: 4px 4px 0 var(--ink); }
.sticker.mint { background: var(--mint); border-radius: 18px; }
.sticker.butter { background: var(--butter); border-radius: 3px; }
.sticker.pink { background: #ffd1df; }
.sticker.blue { background: #cbd4ff; }
.hero-stickers { display: flex; justify-content: center; flex-wrap: wrap; gap: .55rem; margin: .55rem 0; }
.sticky-note { display: inline-block; padding: .42rem .7rem; background: var(--yellow); border: 1px solid var(--ink); transform: rotate(-3deg); font: 600 1rem 'Caveat', cursive; }
.sticky-note.green { background: var(--mint); transform: rotate(2deg); }
.status-line { margin: .65rem 0 1rem; font: 700 .63rem 'Space Mono', monospace; letter-spacing: .08em; }
.status-dot { display: inline-block; width: 8px; height: 8px; margin-right: .4rem; border-radius: 50%; background: var(--blue); }
div[data-testid="stMarkdownContainer"] p.hero-tagline {
  max-width: 720px; margin: 1rem auto 1.3rem; font-size: clamp(1.45rem, 3.2vw, 2.4rem) !important;
  font-weight: 800 !important; line-height: 1.18 !important; letter-spacing: -.055em;
}
.hero-avatar {
  position: absolute; top: 47%; width: 62px; height: 62px; object-fit: cover; object-position: center 26%;
  padding: 3px; border: 3px solid var(--orange); border-radius: 50%; background: var(--paper);
}
.hero-avatar.left { left: 2%; transform: rotate(-8deg); }
.hero-avatar.right { right: 2%; transform: rotate(7deg); }
.contact-black a {
  display: inline-flex; align-items: center; gap: .7rem; padding: .75rem 1.1rem;
  border: 2px solid var(--ink); background: var(--ink); color: white !important;
  text-decoration: none !important; font: 700 .72rem 'Space Mono', monospace;
  box-shadow: 4px 4px 0 var(--blue); transition: transform .16s ease, box-shadow .16s ease;
}
.contact-black a:hover { transform: translate(-2px,-2px); box-shadow: 6px 6px 0 var(--blue); }
.contact-black a:active { transform: translate(3px,3px); box-shadow: 1px 1px 0 var(--blue); }
.hero-divider { width: 100%; height: 34px; margin: .6rem 0 1rem; }
.section-label { margin: .4rem 0; font: 600 1.5rem 'Caveat', cursive; }
.boxed-heading {
  display: table; margin: .1rem auto 1rem; padding: .1rem .75rem;
  border: 2px solid var(--ink); font: 600 1.8rem 'Caveat', cursive; transform: rotate(-1deg);
}
div[data-testid="stMarkdownContainer"] p.about-copy {
  max-width: 580px; margin: .5rem auto 1.5rem; text-align: center;
  font: 600 1.5rem/1.3 'Caveat', cursive !important;
}
.polaroid-row { display: flex; justify-content: space-around; align-items: center; gap: 1rem; margin: .4rem auto 1.3rem; }
.about-layout {
  display: grid; grid-template-columns: minmax(130px, .75fr) minmax(260px, 2fr) minmax(130px, .75fr);
  gap: 1.2rem; align-items: center; margin: .6rem 0 1.4rem;
}
.about-layout .polaroid { width: 100%; }
.polaroid {
  position: relative; width: min(230px, 42%); padding: 10px 10px 35px;
  background: white; border: 1px solid #ddd; box-shadow: 3px 5px 11px rgba(0,0,0,.17);
  transition: transform .25s ease, box-shadow .25s ease;
}
.polaroid.left { transform: rotate(-4deg); }
.polaroid.right { transform: rotate(3deg); }
.polaroid:hover { z-index: 3; transform: rotate(0) translateY(-7px) scale(1.03); box-shadow: 8px 12px 24px rgba(0,0,0,.22); }
.polaroid img { display: block; width: 100%; height: 220px; object-fit: cover; }
.polaroid figcaption { position: absolute; right: 4px; bottom: 7px; left: 4px; text-align: center; font: 600 1.1rem 'Caveat', cursive; }
.polaroid::before, .polaroid::after { position: absolute; z-index: 2; width: 68px; height: 17px; content: ""; opacity: .7; }
.polaroid::before { top: -8px; left: -20px; background: #f7dc73; transform: rotate(-36deg); }
.polaroid::after { top: -7px; right: -20px; background: #a9c5f3; transform: rotate(37deg); }
.skill-stickers { display: flex; flex-wrap: wrap; justify-content: center; gap: .65rem; margin: 1.2rem 0 2.5rem; }
.skill-sticker {
  padding: .45rem .8rem; color: var(--ink); border: 1px solid rgba(20,20,20,.3);
  font-weight: 800; clip-path: polygon(3% 0,97% 2%,100% 88%,96% 100%,4% 97%,0 12%);
  transition: transform .2s ease;
}
.skill-sticker:hover { transform: rotate(3deg) scale(1.08); }
.skill-sticker:nth-child(4n+1) { background: var(--yellow); }
.skill-sticker:nth-child(4n+2) { background: var(--mint); }
.skill-sticker:nth-child(4n+3) { background: #ffd1df; }
.skill-sticker:nth-child(4n) { background: #cbd4ff; }
.folder-tabs { display: flex; align-items: end; gap: .15rem; margin-top: 1.2rem; }
.folder-tab {
  padding: .55rem .85rem .42rem; color: white; background: var(--blue);
  clip-path: polygon(0 0,84% 0,100% 100%,0 100%);
  font: 700 .63rem 'Space Mono', monospace; letter-spacing: .04em;
}
.folder-tab:nth-child(2) { background: var(--ink); }
.folder-tab:nth-child(3) { background: var(--orange); }
.folder-tab.active { position: relative; z-index: 2; transform: translateY(-4px); outline: 1.5px solid var(--ink); }
.folder-card {
  --folder-bg: var(--ink); --folder-fg: white;
  position: relative; display: grid; grid-template-columns: 1.2fr .8fr;
  gap: 1.2rem; align-items: center; overflow: hidden; min-height: 290px;
  margin: -1px 0 -18px; padding: clamp(1.2rem,4vw,2.4rem);
  color: var(--folder-fg); background: var(--folder-bg);
  clip-path: polygon(0 0,84% 0,88% 5%,100% 5%,100% 100%,0 100%);
  box-shadow: 0 8px 20px rgba(0,0,0,.15);
}
.folder-card.color-yellow { --folder-bg: var(--yellow); --folder-fg: var(--ink); }
.folder-card.color-blue { --folder-bg: var(--blue); --folder-fg: white; }
.folder-card.color-pink { --folder-bg: var(--pink); --folder-fg: var(--ink); }
.folder-card.color-green { --folder-bg: var(--green); --folder-fg: white; }
.folder-card.color-orange { --folder-bg: var(--orange); --folder-fg: var(--ink); }
.folder-meta { font: 700 .65rem 'Space Mono', monospace; letter-spacing: .08em; }
.tool-badges { display: flex; flex-wrap: wrap; gap: .35rem; margin-top: .65rem; }
.tool-pill { padding: .25rem .42rem; border: 1px solid currentColor; border-radius: 2px; font: 700 .58rem 'Space Mono', monospace; }
.folder-title { margin: .55rem 0; color: var(--folder-fg); font-size: clamp(1.8rem,4vw,3rem); font-weight: 800; line-height: 1.02; letter-spacing: -.06em; }
.folder-tagline { font-size: .98rem; line-height: 1.45; }
.folder-link a { color: inherit !important; font: 700 .72rem 'Space Mono', monospace; text-underline-offset: 4px; }
.folder-art-wrap { position: relative; padding: 9px; background: white; transform: rotate(1deg); box-shadow: 3px 5px 10px rgba(0,0,0,.25); }
.folder-art-wrap::before, .folder-art-wrap::after { position: absolute; z-index: 2; top: -7px; width: 68px; height: 15px; content: ""; background: rgba(255,255,255,.65); }
.folder-art-wrap::before { left: -18px; transform: rotate(-34deg); }
.folder-art-wrap::after { right: -18px; transform: rotate(34deg); }
.folder-art-wrap img { display: block; width: 100%; height: 195px; object-fit: cover; }
.folder-css-art { display: grid; height: 195px; place-items: center; background: repeating-linear-gradient(135deg,#fff 0 10px,#eee 10px 20px); color: var(--ink); font: 700 2rem 'Pixelify Sans', monospace; }
.folder-list .stButton button, [data-testid="stButton"] button {
  border: 2px solid var(--ink); border-radius: 2px; color: var(--ink);
  background: var(--paper); box-shadow: 3px 3px 0 var(--ink);
  font: 700 .7rem 'Space Mono', monospace; transition: transform .14s ease, box-shadow .14s ease;
}
[data-testid="stButton"] button:hover { border-color: var(--ink); color: var(--ink); background: var(--yellow); transform: translate(-2px,-2px); box-shadow: 5px 5px 0 var(--ink); }
[data-testid="stButton"] button:active { transform: translate(2px,2px); box-shadow: 1px 1px 0 var(--ink); }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-testid="stSelectbox"] [role="combobox"], [data-testid="stMultiSelect"] [role="combobox"] {
  border: 1.5px solid var(--ink); border-radius: 3px; background: #fffefa; color: var(--ink);
}
[data-testid="stExpander"] { border: 1.5px solid var(--ink); border-radius: 3px; background: rgba(255,255,255,.58); }
[data-testid="stDataFrame"], [data-testid="stTable"] { border: 1.5px solid var(--ink); background: #fffefa; }
[data-testid="stMetric"] {
  padding: .65rem .75rem; border: 1.5px solid var(--ink); background: #fffefa;
  box-shadow: 3px 3px 0 var(--ink);
}
[data-testid="stMetricLabel"] { font: 700 .63rem 'Space Mono', monospace; text-transform: uppercase; }
.achievement-panel, .contact-panel {
  padding: clamp(1rem,3vw,2rem); border: 2px solid var(--ink);
  background: #fffefa; box-shadow: 6px 6px 0 var(--ink);
}
.achievement-panel { background: var(--butter); }
.carousel-picture { position: relative; padding: 9px; background: white; box-shadow: 3px 5px 12px rgba(0,0,0,.2); transform: rotate(-1deg); }
.carousel-picture img { width: 100%; height: 280px; object-fit: contain; display: block; }
.mono-label { font: 700 .68rem 'Space Mono', monospace; text-transform: uppercase; }
.tiny-footer { display: flex; flex-wrap: wrap; justify-content: space-between; gap: .7rem; margin-top: 2.6rem; padding-top: .9rem; border-top: 2px solid var(--ink); font: 700 .65rem 'Space Mono', monospace; }
.milestone-note {
  max-width: 720px; margin: .8rem auto; padding: .85rem 1rem;
  border: 1.5px solid var(--ink); box-shadow: 3px 3px 0 var(--ink);
  transform: rotate(-.35deg); background: var(--butter);
}
.milestone-note.mint { background: var(--mint); transform: rotate(.35deg); }
.milestone-note.pink { background: #ffd1df; transform: rotate(-.5deg); }
.milestone-note.blue { background: #cbd4ff; transform: rotate(.45deg); }
.milestone-note h3 { margin: .3rem 0; font-size: 1rem; letter-spacing: -.02em; }
.milestone-note p { margin: .2rem 0 0; }
.sticker-live {
  display: inline-block; min-width: 180px; padding: .7rem 1rem; border: 2px solid var(--ink);
  background: var(--yellow); box-shadow: 4px 4px 0 var(--ink); font-weight: 800;
}
.motion-off *, .motion-off *::before, .motion-off *::after { animation: none !important; transition: none !important; scroll-behavior: auto !important; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
@keyframes paper-in { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
@keyframes card-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
@keyframes bob { 0%,100% { margin-top: 0; } 50% { margin-top: -9px; } }
@keyframes frame-wiggle { 0%,96%,100% { transform: rotate(-1deg); } 98% { transform: rotate(1deg); } }
@media (prefers-reduced-motion: no-preference) {
  .stApp:has(.page-marker) [data-testid="stMainBlockContainer"] { animation: paper-in .48s cubic-bezier(.2,.8,.2,1) both; }
  .name-frame { animation: frame-wiggle 5s ease-in-out infinite; }
  .hero-avatar { animation: bob 3.4s ease-in-out infinite; }
  .hero-avatar.right { animation-delay: .6s; }
  .folder-card { animation: card-in .38s ease both; }
  .polaroid { animation: settle .42s ease both; }
  .carousel-picture img { animation: paper-in .35s ease both; }
  [data-testid="stProgressBar"] > div > div { transition: width .55s ease; }
  @keyframes settle { from { opacity: 0; transform: rotate(0) translateY(8px); } to { opacity: 1; } }
}
@media (max-width: 800px) {
  [data-testid="stMainBlockContainer"] { margin: 0 auto; padding: .7rem 1rem 2rem !important; }
  .hero-avatar { width: 46px; height: 46px; top: 62%; }
  .folder-card { grid-template-columns: 1fr; }
  .folder-art-wrap img, .folder-css-art { height: 175px; }
  .polaroid img { height: 160px; }
  .about-layout { grid-template-columns: 1fr 1.25fr; }
  .about-layout .about-copy { grid-column: 1 / -1; grid-row: 2; }
  .about-layout .polaroid { width: min(230px, 100%); justify-self: center; }
  .about-layout .polaroid.right { grid-column: 2; grid-row: 1; }
  .st-key-top_nav [data-testid="stRadio"] label { padding: .3rem .35rem; font-size: .54rem; }
  .st-key-top_nav [data-testid="stRadio"] [role="radiogroup"] { overflow-x: auto; }
}
"""


def inject_styles(reduce_motion: bool = False) -> None:
    import streamlit as st

    st.markdown(
        f'<style>{STYLES}</style><div class="{"motion-off" if reduce_motion else ""}"></div>',
        unsafe_allow_html=True,
    )
