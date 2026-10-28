from __future__ import annotations

import base64
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st

import content
from ui import pages
from ui.components import nav
from ui.styles import STYLES


ROOT = Path(__file__).parent
ACCENTS = {
    "Orange": "#F2683C",
    "Blue": "#2B4FE0",
    "Pink": "#FF4F8B",
    "Green": "#1FA971",
}


def init_state() -> None:
    defaults: dict[str, Any] = {
        "page": "★ HOME",
        "accent_theme": "Orange",
        "show_fun_facts": False,
        "compact_view": False,
        "carousel_autoplay": False,
        "reduce_motion": False,
        "achievement_index": 0,
        "certificate_index": 0,
        "project_likes": {project["title"]: 0 for project in content.PROJECTS},
        "contact_messages": [],
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


@st.cache_data(show_spinner=False)
def load_skills() -> pd.DataFrame:
    return pd.DataFrame(content.SKILLS)


def load_image(path: str) -> bytes | None:
    candidate = (ROOT / path).resolve()
    try:
        candidate.relative_to((ROOT / "assets").resolve())
    except ValueError:
        return None
    if not candidate.is_file():
        return None
    try:
        return candidate.read_bytes()
    except OSError:
        return None


def image_data_uri(path: str) -> str | None:
    image = load_image(path)
    if image is None:
        return None
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(Path(path).suffix.lower())
    if mime is None:
        return None
    return f"data:{mime};base64,{base64.b64encode(image).decode('ascii')}"


def render_image(path: str, alt: str, **kwargs: Any) -> None:
    image = load_image(path)
    if image is None:
        st.info(f"I could not load the image for {alt}.")
        return
    st.image(image, caption=None, alt=alt, **kwargs)


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("### Controls")
        render_image("assets/OFFICIAL_FORMALPHOTO.png", content.NAME, width=145)
        st.markdown(f"**{content.NAME}**")
        st.caption(f"{content.PROGRAM} · {content.SECTION}")
        st.selectbox("Accent color", list(ACCENTS), key="accent_theme")
        st.checkbox("Show fun facts", key="show_fun_facts")
        st.checkbox("Compact view", key="compact_view")
        st.toggle("Auto-play carousels", key="carousel_autoplay")
        st.toggle("Reduce motion", key="reduce_motion")
        st.link_button("LinkedIn ↗", content.LINKEDIN_URL, width="stretch")
        st.link_button("GitHub ↗", content.GITHUB_URL, width="stretch")


def render_styles() -> None:
    accent = ACCENTS[st.session_state["accent_theme"]]
    reduced = st.session_state["reduce_motion"]
    motion_rule = (
        ".stApp *,.stApp *::before,.stApp *::after{animation:none!important;transition:none!important}"
        if reduced
        else ""
    )
    st.markdown(
        f'<style>{STYLES}:root{{--accent:{accent};--orange:{accent}}}{motion_rule}</style>',
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        f'<div class="tiny-footer"><span>{content.NAME} · {content.SECTION}</span>'
        f'<span>CSIT 349 Applied AI · {content.SCHOOL}</span>'
        f'<span><a href="{content.CONTACT_URL}" target="_blank" rel="noopener noreferrer">♥ CONTACT ↗</a></span>'
        "</div>",
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title=f"{content.NAME} | Portfolio",
        page_icon="👋",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    init_state()
    render_sidebar()
    render_styles()
    nav()
    page_key = st.session_state["page"]
    st.markdown(
        f'<div class="page-marker" data-page="{page_key}"></div>',
        unsafe_allow_html=True,
    )
    routes = {
        "★ HOME": pages.render_home,
        "ABOUT": pages.render_about,
        "CASE STUDIES": pages.render_case_studies,
        "PLAYGROUND": pages.render_playground,
        "CONTACT": pages.render_contact,
    }
    routes[page_key]()
    render_footer()


if __name__ == "__main__":
    main()
