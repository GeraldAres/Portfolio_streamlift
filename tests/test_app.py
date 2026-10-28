from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest

import content
from app import image_data_uri, load_image


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def run(app: AppTest) -> AppTest:
    app.run()
    assert not app.exception, [exception.message for exception in app.exception]
    return app


def select_page(app: AppTest, page: str) -> AppTest:
    app.radio(key="page").set_value(page)
    return run(app)


def test_real_assets_content_and_contact_links() -> None:
    assert load_image("assets/OFFICIAL_FORMALPHOTO.png")
    assert load_image("assets/missing-image.jpg") is None
    assert load_image("../app.py") is None
    for certificate in content.CERTIFICATES:
        if certificate["image"]:
            assert load_image(certificate["image"])
    for achievement in content.ACHIEVEMENTS:
        assert load_image(achievement["image"])
    assert image_data_uri(content.ACHIEVEMENTS[0]["image"]).startswith("data:image/jpeg;base64,")
    assert len(content.PROJECTS) == 8
    assert len(content.CERTIFICATES) == 5
    assert len(content.ACHIEVEMENTS) == 4
    assert content.SECTION == "CS365 F1"
    assert content.CONTACT_URL == "https://forms.gle/UyrUjb1ToZGKccnj6"
    for source in [Path(content.__file__).read_text(encoding="utf-8")]:
        assert "TODO" not in source
        assert "placeholder" not in source.casefold()


def test_home_about_case_studies_and_playground_interactions() -> None:
    app = run(AppTest.from_file(APP_PATH, default_timeout=60))
    assert app.radio(key="page").value == "★ HOME"
    assert "Featured projects" in [header.value for header in app.header]

    app.selectbox(key="accent_theme").set_value("Blue")
    app.toggle(key="carousel_autoplay").set_value(True)
    app.toggle(key="reduce_motion").set_value(True)
    app.checkbox(key="show_fun_facts").check()
    app.checkbox(key="compact_view").check()
    run(app)
    assert app.session_state["accent_theme"] == "Blue"
    assert app.session_state["carousel_autoplay"] is True
    assert app.session_state["reduce_motion"] is True

    app.button(key="home_achievement_carousel_next").click()
    run(app)
    assert app.session_state["achievement_index"] == 1
    app.selectbox(key="featured_project").set_value(content.PROJECTS[1]["title"])
    run(app)

    app = select_page(app, "ABOUT")
    assert any("Background" in header.value for header in app.header)
    app.select_slider(key="about_milestone_range").set_value((2026, 2026))
    app.multiselect(key="about_certificate_filter").set_value(["Programming"])
    run(app)
    assert any(
        "CITU C Programming 2 Certification" in row["title"]
        for row in app.dataframe[0].value.to_dict("records")
    )
    app.button(key="about_certificate_carousel_next").click()
    run(app)
    assert app.session_state["certificate_index"] == 1

    app = select_page(app, "CASE STUDIES")
    app.text_input(key="case_project_search").set_value("BantAI")
    run(app)
    assert app.selectbox(key="case_project_selection").options == ["BantAI Buddy"]
    app.button(key="case_like_0").click()
    run(app)
    assert app.session_state["project_likes"]["BantAI Buddy"] == 1
    app.text_input(key="case_project_search").set_value("no matching project")
    run(app)
    assert any("could not find a project" in warning.value.lower() for warning in app.warning)

    app = select_page(app, "PLAYGROUND")
    app.multiselect(key="play_skill_categories").set_value(["Programming"])
    app.slider(key="play_min_proficiency").set_value(50)
    app.selectbox(key="play_skill_sort").set_value("Proficiency (high to low)")
    app.text_input(key="sticker_text").set_value("Design with care")
    app.selectbox(key="sticker_color").set_value("Pink")
    app.checkbox(key="sticker_rotate").uncheck()
    run(app)
    assert app.dataframe
    assert app.download_button(key="download_sticker")


def test_contact_page_validates_and_saves_feedback() -> None:
    app = run(AppTest.from_file(APP_PATH, default_timeout=60))
    app = select_page(app, "CONTACT")
    app.text_input(key="contact_name").set_value("Alex Example")
    app.text_input(key="contact_email").set_value("not-an-email")
    app.text_area(key="contact_message").set_value("I enjoyed exploring the scrapbook.")
    app.checkbox(key="contact_consent").check()
    app.button(key="FormSubmitter:contact_form-Send my note").click()
    run(app)
    assert len(app.session_state["contact_messages"]) == 0

    app.text_input(key="contact_email").set_value("alex@example.com")
    app.selectbox(key="contact_purpose").set_value("Feedback")
    app.slider(key="contact_rating").set_value(4)
    app.button(key="FormSubmitter:contact_form-Send my note").click()
    run(app)
    assert len(app.session_state["contact_messages"]) == 1
    saved = app.session_state["contact_messages"][0]
    assert saved["Name"] == "Alex Example"
    assert saved["Rating"] == 4
    assert saved["Purpose"] == "Feedback"
    assert app.download_button(key="contact_download_csv")
