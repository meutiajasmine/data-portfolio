# Personal Data Portfolio — Starter

A beginner-friendly portfolio website built with Python, Flask, HTML, and CSS.

## 1. Requirements
- Python 3.11 or 3.12
- pip

## 2. Create and activate a virtual environment (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you already created and activated `.venv`, just run `pip install -r requirements.txt`.

## 3. Run locally
```powershell
python app.py
```
Open the local address shown in the terminal, usually http://127.0.0.1:5000.

## 4. Customize before publishing
Search for and replace:
- `Your Name` / `yourname`
- the placeholder degree and university
- LinkedIn and GitHub links
- `your.email@example.com`
- project descriptions and project links
- the resume file link

Put your final CV PDF at `static/files/resume.pdf`.

Do not publish private information or project data you do not have permission to share.

## 5. Project structure
- `app.py`: Flask application and homepage route
- `templates/index.html`: page content and layout
- `static/css/style.css`: colors, spacing, cards, responsive styling
- `static/js/main.js`: mobile menu and footer year
- `static/files/`: CV PDF
- `static/images/`: optional project screenshots or profile photo
