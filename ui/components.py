from __future__ import annotations

import json
from html import escape
from typing import Any

import streamlit as st

import content


def image_data_uri(path: str) -> str | None:
    from app import image_data_uri as load_uri

    return load_uri(path)


def sticker(label: str, color: str = "mint", icon: str = "") -> str:
    return (
        f'<span class="sticker {escape(color, quote=True)}">'
        f'{escape(icon)} {escape(label)}</span>'
    )


def polaroid(path: str, caption: str, side: str = "left") -> str:
    uri = image_data_uri(path)
    if uri is None:
        image = '<div class="folder-css-art">GA</div>'
    else:
        image = f'<img src="{uri}" alt="{escape(caption, quote=True)}">'
    return (
        f'<figure class="polaroid {escape(side, quote=True)}">{image}'
        f'<figcaption>{escape(caption)}</figcaption></figure>'
    )


def tape() -> str:
    return '<span class="tape" aria-hidden="true"></span>'


def folder_card(project: dict[str, Any], index: int, selected: bool = True) -> str:
    colors = ["black", "yellow", "blue", "pink", "green", "orange"]
    color = colors[index % len(colors)]
    image_uri = image_data_uri(project.get("image", "")) if project.get("image") else None
    title = escape(project["title"])
    tagline = escape(project["tagline"])
    tools = "".join(f'<span class="tool-pill">{escape(tool)}</span>' for tool in project["tools"])
    year = ""
    for known_year in ("2025", "2026", "2024"):
        if known_year in f"{project.get('outcome', '')} {project.get('tagline', '')}":
            year = known_year
            break
    year_label = year or "PROJECT NOTES"
    if image_uri:
        art = f'<img src="{image_uri}" alt="{title} project art">'
    else:
        initials = "".join(word[:1] for word in project["title"].split()[:3]).upper()
        art = f'<div class="folder-css-art">{escape(initials)}</div>'
    link = (
        f'<a href="{escape(project["url"], quote=True)}" target="_blank" rel="noopener noreferrer">'
        "VIEW PROJECT ↗</a>"
        if project.get("url")
        else '<span class="mono-label">PROJECT OVERVIEW</span>'
    )
    active_class = "selected" if selected else ""
    return (
        f'<div class="folder-card color-{color} {active_class}">'
        f'<div class="folder-copy"><div class="folder-meta">● {year_label}</div>'
        f'<h2 class="folder-title">{title}</h2><p class="folder-tagline">{tagline}</p>'
        f'<div class="tool-badges">{tools}</div><p class="folder-link">{link}</p></div>'
        f'<div class="folder-art-wrap">{tape()}{art}</div></div>'
    )


def nav() -> None:
    with st.container(key="top_nav"):
        left, middle, right = st.columns([0.45, 6, 3.6], vertical_alignment="center")
        with left:
            st.markdown('<div class="brand-smile" aria-label="Gerald Ares">☺</div>', unsafe_allow_html=True)
        with middle:
            st.radio(
                "Site navigation",
                ["★ HOME", "ABOUT", "CASE STUDIES", "PLAYGROUND", "CONTACT"],
                key="page",
                horizontal=True,
                label_visibility="collapsed",
            )
        with right:
            st.markdown(
                f'<div class="nav-social">'
                f'<a href="{escape(content.LINKEDIN_URL, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">in</a>'
                f'<a href="{escape(content.GITHUB_URL, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="GitHub">GH</a>'
                f'<a href="{escape(content.CONTACT_URL, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Google contact form">↗</a>'
                f'<a class="contact-pill" href="{escape(content.CONTACT_URL, quote=True)}" target="_blank" rel="noopener noreferrer">♥ CONTACT</a>'
                "</div>",
                unsafe_allow_html=True,
            )


@st.fragment
def carousel(
    items: list[dict[str, Any]],
    state_key: str,
    carousel_key: str,
    autoplay: bool,
    reduce_motion: bool = False,
) -> None:
    slides: list[dict[str, str]] = []
    for item in items:
        image = image_data_uri(item.get("image", "")) if item.get("image") else None
        slides.append(
            {
                "title": item["title"],
                "subtitle": item.get("result") or item.get("issuer") or item.get("category", ""),
                "description": item.get("description", ""),
                "image": image or "",
                "url": item.get("url") or item.get("credential_url", ""),
            }
        )
    data = json.dumps(slides, ensure_ascii=False).replace("</", "<\\/")
    autoplay_value = "true" if autoplay else "false"
    initial_index = st.session_state[state_key] % len(items)
    document = f"""<!doctype html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{{box-sizing:border-box}} body{{margin:0;background:transparent;color:#141414;font-family:Inter,Arial,sans-serif}}
.outer{{position:relative;padding:14px 18px 18px;min-height:290px}}
.photo{{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:22px;align-items:center;padding:18px;background:#fffefa;border:2px solid #141414;box-shadow:6px 6px 0 #141414;transform:rotate(-.3deg);transition:opacity .25s,transform .25s}}
.photo.fade{{opacity:.4;transform:translateY(5px) rotate(.3deg)}}
.visual{{position:relative;padding:8px;background:#fff;box-shadow:2px 4px 10px #0003;transform:rotate(-1deg)}}
.visual:before,.visual:after{{position:absolute;top:-6px;width:62px;height:14px;background:#f8e7a6bb;content:"";z-index:2}}
.visual:before{{left:-16px;transform:rotate(-32deg)}}.visual:after{{right:-16px;transform:rotate(32deg)}}
img{{display:block;width:100%;height:230px;object-fit:contain}} .art{{height:230px;display:grid;place-items:center;background:repeating-linear-gradient(135deg,#fff 0 10px,#eee 10px 20px);font:700 2rem monospace}}
.tag{{font:700 .65rem 'Courier New',monospace;text-transform:uppercase;letter-spacing:.08em;color:#b24b33}}
h2{{font-size:clamp(1.25rem,3vw,2rem);line-height:1.04;margin:.5rem 0}} p{{line-height:1.45;font-size:.88rem}}
.link{{display:inline-block;margin-top:.4rem;color:#141414;font:bold .7rem 'Courier New',monospace;text-underline-offset:4px}}
.arrows{{position:absolute;right:26px;bottom:17px;display:flex;gap:7px;z-index:3}}
button{{width:35px;height:35px;border:2px solid #141414;border-radius:50%;background:#f5c542;box-shadow:2px 2px 0 #141414;font-size:18px;cursor:pointer}}
.dots{{display:flex;justify-content:center;gap:7px;margin-top:12px}} .dots button{{width:9px;height:9px;min-width:9px;padding:0;border:1px solid #141414;background:#fff;border-radius:50%;box-shadow:none}}.dots button.on{{background:#141414}}
{".photo,.visual,.photo *{animation:none!important;transition:none!important}" if reduce_motion else ""}
@media(max-width:650px){{.photo{{grid-template-columns:1fr}}img,.art{{height:160px}}.outer{{padding:8px}}}}
</style></head>
<body><main class="outer"><section class="photo" id="photo"></section><div class="arrows"><button id="prev" aria-label="Previous slide">←</button><button id="next" aria-label="Next slide">→</button></div><div class="dots" id="dots"></div></main>
<script>
const slides={data}; let index={initial_index}, timer=null, startX=0; const autoplay={autoplay_value}&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const photo=document.getElementById('photo'), dots=document.getElementById('dots');
function show(n){{index=(n+slides.length)%slides.length;const s=slides[index];photo.classList.add('fade');setTimeout(()=>{{photo.innerHTML=`<div class="visual">${{s.image?`<img src="${{s.image}}" alt="">`:`<div class="art">GA</div>`}}</div><div><div class="tag">${{s.subtitle}}</div><h2>${{s.title}}</h2><p>${{s.description}}</p>${{s.url?`<a class="link" href="${{s.url}}" target="_blank" rel="noopener noreferrer">OPEN ↗</a>`:''}}</div>`;photo.classList.remove('fade');dots.innerHTML=slides.map((_,i)=>`<button class="${{i===index?'on':''}}" aria-label="Slide ${{i+1}}" data-index="${{i}}"></button>`).join('');dots.querySelectorAll('button').forEach(b=>b.onclick=()=>show(Number(b.dataset.index))) }},130)}}
document.getElementById('prev').onclick=()=>show(index-1);document.getElementById('next').onclick=()=>show(index+1);
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')show(index+1);if(e.key==='ArrowLeft')show(index-1)}});
photo.addEventListener('touchstart',e=>startX=e.changedTouches[0].screenX,{{passive:true}});
photo.addEventListener('touchend',e=>{{const delta=e.changedTouches[0].screenX-startX;if(Math.abs(delta)>45)show(index+(delta<0?1:-1))}},{{passive:true}});
const outer=document.querySelector('.outer');outer.addEventListener('mouseenter',()=>clearInterval(timer));outer.addEventListener('mouseleave',()=>{{if(autoplay)timer=setInterval(()=>show(index+1),5000)}});
show(index);if(autoplay)timer=setInterval(()=>show(index+1),5000);
</script></body></html>"""
    try:
        st.iframe(document, height=430, tab_index=0, alt="Interactive scrapbook carousel")
    except Exception:
        index = st.session_state[state_key] % len(items)
        item = items[index]
        st.markdown('<div class="achievement-panel">', unsafe_allow_html=True)
        st.subheader(item["title"])
        st.write(item.get("description", ""))
        st.markdown("</div>", unsafe_allow_html=True)
    previous, dots, following = st.columns([1, 4, 1], vertical_alignment="center")
    with previous:
        st.button(
            "← Previous",
            key=f"{carousel_key}_previous",
            on_click=_step_carousel,
            args=(state_key, len(items), -1),
        )
    with dots:
        st.progress(
            (st.session_state[state_key] + 1) / len(items),
            text=f"{st.session_state[state_key] + 1} / {len(items)}",
        )
    with following:
        st.button(
            "Next →",
            key=f"{carousel_key}_next",
            on_click=_step_carousel,
            args=(state_key, len(items), 1),
        )


def _step_carousel(key: str, count: int, direction: int) -> None:
    st.session_state[key] = (st.session_state[key] + direction) % count
