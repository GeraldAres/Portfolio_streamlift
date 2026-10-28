# Gerald Benedict S. Ares · CS365 F1

My CSIT 349 Applied AI portfolio is a playful scrapbook-style site for my
autobiography, projects, skills, certificates, and team achievements.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Start the app:

   ```powershell
   python -m streamlit run app.py
   ```

5. Open Streamlit's local URL, usually <http://localhost:8501>.
6. Run the tests with `python -m pytest tests/`.

## Edit my content and assets

My biography, interests, milestones, skills, projects, certificates, and
achievements are in `content.py`. The reusable scrapbook CSS, HTML components,
and page renderers are under `ui/`. My photo, certificates, achievement images,
and generated project images are in `assets/`.

## Package for class submission

Include `app.py`, `content.py`, `requirements.txt`, `.streamlit/config.toml`,
`ui/`, `README.md`, `assets/`, and `tests/`. Exclude `.venv/`, `.env`, and any
`.streamlit/secrets.toml` file.

## Deploy to Streamlit Community Cloud

1. Push this project to a **public GitHub repository** with `requirements.txt`
   at its root.
2. Visit <https://share.streamlit.io> and sign in with GitHub.
3. Choose **Create app**, select the repository and branch, and set the main
   file path to `app.py`.
4. Deploy the app. It does not need API keys, email credentials, or secrets.
