from __future__ import annotations

from html import escape
from typing import Any

import pandas as pd
import streamlit as st

import content
from ui.components import carousel, folder_card, polaroid, sticker


def _render_about_intro() -> None:
    st.markdown('<p class="section-label">about me!</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="boxed-heading">what\'s up</h2>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="about-layout">'
        f'{polaroid("assets/OFFICIAL_FORMALPHOTO.png", "me, Gerald", "left")}'
        '<p class="about-copy">I am Gerald, a third-year Computer Science student who loves '
        'connecting thoughtful design with useful technology. I care about the small details, '
        'the way people move through an interface, and making digital experiences feel human. '
        '✨ 🎨</p>'
        f'{polaroid("assets/springrainglobal_achievement.jpg", "pitch day · Spring Rain Global 2026", "right")}'
        "</div>",
        unsafe_allow_html=True,
    )
    skill_tiles = [
        ("UI/UX Design", "🎯"),
        ("Figma", "✦"),
        ("Graphic Design", "🎨"),
        ("Brand Marketing", "✺"),
        ("Game Dev", "🎮"),
        ("Web Development", "⌘"),
        ("AI for Good", "✳"),
    ]
    html = '<div class="skill-stickers">'
    for label, icon in skill_tiles:
        html += (
            f'<span class="skill-sticker">{escape(label)} '
            f'<b style="display:inline-grid;place-items:center;width:22px;height:22px;'
            f'border:1.5px solid #141414;background:#fffefa">{escape(icon)}</b></span>'
        )
    st.markdown(html + "</div>", unsafe_allow_html=True)


def _render_project_card(project: dict[str, Any], index: int, selected: bool = True) -> None:
    st.markdown(folder_card(project, index, selected), unsafe_allow_html=True)


def render_home() -> None:
    photo_uri = _image_uri("assets/OFFICIAL_FORMALPHOTO.png")
    avatar_left = f'<img class="hero-avatar left" src="{photo_uri}" alt="Gerald">' if photo_uri else ""
    avatar_right = (
        f'<img class="hero-avatar right" src="{_image_uri("assets/OFFICIAL_FORMALPHOTO.png")}" alt="Gerald">'
        if photo_uri else ""
    )
    st.markdown(
        f"""
        <section class="hero">
          {avatar_left}{avatar_right}
          <div class="hand-label underline">my name is</div>
          <div class="hero-stickers">{sticker("MADE THINGS", "mint")}</div>
          <div class="name-frame"><h1 class="name-pixel">GERALD ARES</h1></div>
          <div class="hero-stickers">
            {sticker("SWEAT THE DETAILS", "butter")}
            <span class="sticky-note">UI/UX Designer &amp; Developer ↙</span>
            <span class="sticky-note green">Cebu City, PH</span>
          </div>
          <div class="status-line"><span class="status-dot"></span>OPEN TO NEW WORK AND GOOD PROBLEMS</div>
          <p class="hero-tagline">I design and build things that make technology feel human. 🎯 🌸</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="contact-black" style="text-align:center"><a href="{content.CONTACT_URL}" '
        'target="_blank" rel="noopener noreferrer"><span style="display:inline-block;width:15px;height:15px;'
        'background:#2B4FE0"></span> CONTACT ME ↗</a></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<svg class="hero-divider" viewBox="0 0 1100 40" preserveAspectRatio="none" aria-hidden="true">'
        '<path d="M5 22 C240 4, 420 35, 620 18 S910 6,1090 21" fill="none" '
        'stroke="#141414" stroke-width="1.5" stroke-linecap="round"/></svg>',
        unsafe_allow_html=True,
    )
    _render_about_intro()
    st.markdown('<p class="mono-label">A QUICK NOTEBOOK SNAPSHOT</p>', unsafe_allow_html=True)
    stats = st.columns(4)
    stats[0].metric("Year", content.YEAR_LEVEL)
    stats[1].metric("Projects", len(content.PROJECTS))
    stats[2].metric("Certificates", len(content.CERTIFICATES))
    stats[3].metric("Skills", len(content.SKILLS))
    st.divider()

    st.markdown('<p class="section-label">a few things I made</p>', unsafe_allow_html=True)
    st.header("Featured projects")
    featured = content.PROJECTS[:3]
    chosen = st.selectbox(
        "Pick a featured project",
        [project["title"] for project in featured],
        key="featured_project",
        label_visibility="collapsed",
    )
    tabs = '<div class="folder-tabs">'
    for index, project in enumerate(featured):
        state = "active" if project["title"] == chosen else ""
        tabs += f'<span class="folder-tab {state}">✦ PROJECT {index + 1:02d}</span>'
    st.markdown(tabs + "</div>", unsafe_allow_html=True)
    project_index = next(i for i, project in enumerate(featured) if project["title"] == chosen)
    _render_project_card(featured[project_index], project_index)
    if not st.session_state["compact_view"]:
        for index, project in enumerate(featured):
            if project["title"] != chosen:
                _render_project_card(project, index, False)

    st.header("A few proud moments")
    carousel(
        content.ACHIEVEMENTS,
        "achievement_index",
        "home_achievement_carousel",
        st.session_state["carousel_autoplay"] and not st.session_state["reduce_motion"],
        st.session_state["reduce_motion"],
    )
    _contact_callout()


def _image_uri(path: str) -> str | None:
    from app import image_data_uri

    return image_data_uri(path)


def _contact_callout() -> None:
    st.markdown(
        f'<section class="contact-panel" style="text-align:center;margin:2rem 0">'
        '<p class="hand-label">have a good idea?</p><h2>Let’s make something meaningful.</h2>'
        f'<div class="scrapbook-contact"><a href="{content.CONTACT_URL}" target="_blank" '
        'rel="noopener noreferrer">♥ LET’S TALK</a></div></section>',
        unsafe_allow_html=True,
    )


def render_about() -> None:
    st.markdown('<p class="section-label">the person behind the pixels</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="pixel-heading">ABOUT</h1>', unsafe_allow_html=True)
    st.header("Background")
    st.write(content.BACKGROUND)
    st.subheader("Education")
    for item in content.EDUCATION:
        st.markdown(f"**{item['program']} · {item['year']}**  \n{item['school']}  \n{item['details']}")
    st.subheader("Interests")
    st.write(", ".join(content.INTERESTS[:-1]) + f", and {content.INTERESTS[-1]}.")

    st.header("Milestones")
    years = sorted({item["year"] for item in content.MILESTONES if isinstance(item.get("year"), int)})
    if years:
        selected_years = st.select_slider(
            "Filter my timeline",
            options=years,
            value=(years[0], years[-1]),
            key="about_milestone_range",
        )
        milestones = [
            item for item in content.MILESTONES
            if item.get("year") is None or selected_years[0] <= item["year"] <= selected_years[1]
        ]
    else:
        milestones = content.MILESTONES
    for index, item in enumerate(milestones):
        year = item.get("year") or "MY JOURNEY"
        color = ["yellow", "mint", "pink", "blue"][index % 4]
        st.markdown(
            f'<div class="milestone-note {color}"><span class="mono-label">{year}</span>'
            f'<h3>{escape(item["title"])}</h3><p>{escape(item["description"])}</p></div>',
            unsafe_allow_html=True,
        )
    if st.session_state["show_fun_facts"]:
        st.header("A few fun facts")
        for fact in content.FUN_FACTS:
            st.markdown(f'<div class="skill-sticker">{escape(fact)}</div>', unsafe_allow_html=True)

    st.header("Certificates")
    carousel(
        content.CERTIFICATES,
        "certificate_index",
        "about_certificate_carousel",
        st.session_state["carousel_autoplay"] and not st.session_state["reduce_motion"],
        st.session_state["reduce_motion"],
    )
    categories = sorted({certificate["category"] for certificate in content.CERTIFICATES})
    selected = st.multiselect(
        "Filter certificates",
        categories,
        default=categories,
        key="about_certificate_filter",
    )
    certificate_df = pd.DataFrame(content.CERTIFICATES)
    filtered = certificate_df[certificate_df["category"].isin(selected)]
    if filtered.empty:
        st.warning("I have no certificates in the selected categories.")
    else:
        st.dataframe(
            filtered[["title", "issuer", "category", "date", "description"]],
            hide_index=True,
            width="stretch",
            key="about_certificate_table",
        )
        columns = st.columns(2)
        for index, certificate in enumerate(filtered.to_dict("records")):
            with columns[index % 2]:
                with st.container(border=True, key=f"about_certificate_{index}"):
                    st.subheader(certificate["title"])
                    st.caption(" · ".join([certificate["issuer"], certificate["date"]]).strip(" ·"))
                    st.write(certificate["description"])
                    if certificate["image"]:
                        from app import render_image

                        render_image(certificate["image"], certificate["title"], width="stretch")
                    if certificate["credential_url"]:
                        st.link_button("View credential", certificate["credential_url"])


def _like_project(title: str) -> None:
    st.session_state["project_likes"][title] += 1


@st.fragment
def _project_browser() -> None:
    query = st.text_input("Search projects by name or tool", key="case_project_search").strip().casefold()
    all_tools = sorted({tool for project in content.PROJECTS for tool in project["tools"]})
    selected_tools = st.multiselect("Filter by tools", all_tools, key="case_project_tools")
    projects = [
        project for project in content.PROJECTS
        if (not query or query in project["title"].casefold()
            or any(query in tool.casefold() for tool in project["tools"]))
        and (not selected_tools or any(tool in selected_tools for tool in project["tools"]))
    ]
    if not projects:
        st.warning("I could not find a project with those filters.")
        return
    title = st.selectbox(
        "Choose a project",
        [project["title"] for project in projects],
        key="case_project_selection",
    )
    project = next(project for project in projects if project["title"] == title)
    index = content.PROJECTS.index(project)
    tabs = '<div class="folder-tabs">'
    for number, item in enumerate(content.PROJECTS):
        state = "active" if item["title"] == title else ""
        tabs += f'<span class="folder-tab {state}">✦ PROJECT {number + 1:02d}</span>'
    st.markdown(tabs + "</div>", unsafe_allow_html=True)
    st.markdown(folder_card(project, index), unsafe_allow_html=True)
    st.markdown(f"**My role:** {project['role']}")
    st.markdown(f"**Outcome:** {project['outcome']}")
    with st.expander("What I learned"):
        st.write(project["learned"])
    like_col, link_col = st.columns([1, 4], vertical_alignment="center")
    with like_col:
        st.button(
            f"♥ Like · {st.session_state['project_likes'][title]}",
            key=f"case_like_{index}",
            on_click=_like_project,
            args=(title,),
        )
    with link_col:
        if project["url"]:
            st.link_button("Open project ↗", project["url"])
    if not st.session_state["compact_view"]:
        st.subheader("All project folders")
        for project_index, item in enumerate(content.PROJECTS):
            st.markdown(folder_card(item, project_index, item["title"] == title), unsafe_allow_html=True)


def render_case_studies() -> None:
    st.markdown('<p class="section-label">things I have been making</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="pixel-heading">CASE STUDIES</h1>', unsafe_allow_html=True)
    _project_browser()


def _render_sticker_maker() -> None:
    st.header("Sticker maker")
    text = st.text_input("Sticker text", value="Made with care", key="sticker_text")
    color = st.selectbox(
        "Sticker color",
        ["Yellow", "Mint", "Pink", "Blue"],
        key="sticker_color",
    )
    rotate = st.checkbox("Tilt my sticker", value=True, key="sticker_rotate")
    color_map = {"Yellow": "#F5C542", "Mint": "#BFE8D2", "Pink": "#FF4F8B", "Blue": "#cbd4ff"}
    rotation = "-3deg" if rotate else "0deg"
    text_html = escape(text) or "Your sticker"
    st.markdown(
        f'<div style="padding:1.7rem 0"><div class="sticker-live" style="background:{color_map[color]};'
        f'transform:rotate({rotation})">{text_html} ✦</div></div>',
        unsafe_allow_html=True,
    )
    sticker_html = (
        f'<!doctype html><meta charset="utf-8"><div style="display:inline-block;padding:20px;'
        f'font:800 22px Arial;background:{color_map[color]};border:2px solid #141414;'
        f'box-shadow:4px 4px #141414;transform:rotate({rotation})">{text_html} ✦</div>'
    )
    st.download_button(
        "Download my sticker",
        sticker_html,
        file_name="gerald-sticker.html",
        mime="text/html",
        key="download_sticker",
    )


def render_playground() -> None:
    st.markdown('<p class="section-label">small experiments and skill notes</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="pixel-heading">PLAYGROUND</h1>', unsafe_allow_html=True)
    skills = pd.DataFrame(content.SKILLS)
    categories = sorted(skills["category"].unique())
    selected_categories = st.multiselect(
        "Skill categories",
        categories,
        default=categories,
        key="play_skill_categories",
    )
    minimum = st.slider("Minimum proficiency", 0, 100, 0, key="play_min_proficiency")
    filtered = skills[
        skills["category"].isin(selected_categories)
        & (skills["proficiency"] >= minimum)
    ].copy()
    if filtered.empty:
        st.warning("I do not have skills at or above that threshold in these categories.")
    else:
        sort_by = st.selectbox(
            "Sort skills",
            ["Name", "Proficiency (high to low)", "Category"],
            key="play_skill_sort",
        )
        sort_column = {"Name": "skill", "Proficiency (high to low)": "proficiency", "Category": "category"}[sort_by]
        filtered = filtered.sort_values(sort_column, ascending=sort_by != "Proficiency (high to low)")
        editable = filtered[["skill", "category", "proficiency", "description"]].rename(
            columns={"skill": "Skill", "category": "Category", "proficiency": "Proficiency", "description": "How I use it"}
        )
        edited = st.data_editor(
            editable,
            hide_index=True,
            width="stretch",
            key="play_skills_editor",
            column_config={
                "Proficiency": st.column_config.ProgressColumn(
                    "Proficiency", min_value=0, max_value=100, format="%d%%"
                )
            },
            disabled=["Skill", "Category", "How I use it"],
        )
        chart_col, line_col = st.columns(2)
        with chart_col:
            st.subheader("Skill snapshot")
            st.bar_chart(edited.set_index("Skill")["Proficiency"])
        with line_col:
            st.subheader("Practice over time")
            st.line_chart(pd.DataFrame(content.SKILL_GROWTH).set_index("year"))
        st.subheader("Progress")
        for _, skill in edited.iterrows():
            st.markdown(f"**{skill['Skill']}** · {int(skill['Proficiency'])}%")
            st.progress(int(skill["Proficiency"]))
        category_average = (
            edited.groupby("Category", as_index=False)["Proficiency"]
            .mean()
            .round(1)
            .rename(columns={"Proficiency": "Average"})
        )
        st.subheader("Category snapshot")
        st.table(category_average)
    _render_sticker_maker()


def render_contact() -> None:
    st.markdown('<p class="section-label">good things start with hello</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="pixel-heading">CONTACT</h1>', unsafe_allow_html=True)
    st.markdown(
        f'<section class="contact-panel" style="text-align:center;margin-bottom:1.5rem">'
        '<div class="hand-label">☺</div><h2>Let’s build something good.</h2>'
        '<p>I am open to conversations about thoughtful design, creative technology, and good problems.</p>'
        f'<div class="contact-black"><a href="{content.CONTACT_URL}" target="_blank" '
        'rel="noopener noreferrer">♥ CONTACT ME ↗</a></div></section>',
        unsafe_allow_html=True,
    )
    st.subheader("Or leave a note here")
    with st.form("contact_form"):
        name = st.text_input("Name", key="contact_name")
        email = st.text_input("Email", key="contact_email")
        purpose = st.selectbox("Purpose", content.CONTACT_PURPOSES, key="contact_purpose")
        rating = st.slider("Rate this portfolio", 1, 5, 5, key="contact_rating")
        message = st.text_area("Message", key="contact_message")
        consent = st.checkbox(
            "I understand this note is only stored for this browser session.",
            key="contact_consent",
        )
        submitted = st.form_submit_button("Send my note")
    if submitted:
        if not name.strip() or not message.strip():
            st.error("Please add your name and message.")
        elif not _valid_email(email.strip()):
            st.error("Please enter a valid email address.")
        elif not consent:
            st.error("Please confirm the session-only storage notice.")
        else:
            submission = {
                "Name": name.strip(),
                "Email": email.strip(),
                "Purpose": purpose,
                "Rating": rating,
                "Message": message.strip(),
            }
            st.session_state["contact_messages"].append(submission)
            st.success(f"Thanks, {name.strip()}! I saved your note for this session.")
            st.write("Here is the note I saved:", submission)
            st.toast("Your note is saved for this session.")
            st.balloons()
    messages = st.session_state["contact_messages"]
    st.subheader("Messages sent this session")
    message_df = pd.DataFrame(
        messages,
        columns=["Name", "Email", "Purpose", "Rating", "Message"],
    )
    if messages:
        st.dataframe(message_df, hide_index=True, width="stretch", key="contact_messages_table")
    else:
        st.caption("No messages yet.")
    st.download_button(
        "Download session messages as CSV",
        message_df.to_csv(index=False).encode("utf-8"),
        file_name="portfolio-notes.csv",
        mime="text/csv",
        key="contact_download_csv",
    )
    _contact_callout()


def _valid_email(email: str) -> bool:
    import re

    return re.fullmatch(
        r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+",
        email,
    ) is not None
