from flask import Flask, render_template, request, abort, Response
from translations import UI, PROJECTS, EXPERIENCE, CASE_STUDIES, SUPPORTED

app = Flask(__name__)

def detect_lang() -> str:
    forced = request.args.get("lang", "").lower()
    if forced in SUPPORTED:
        return forced
    best = request.accept_languages.best_match(list(SUPPORTED))
    return best or "en"

@app.route("/")
def index():
    lang = detect_lang()
    return render_template(
        "index.html",
        lang=lang,
        dir="rtl" if lang == "ar" else "ltr",
        t=UI[lang],
        projects=PROJECTS[lang],
        experience=EXPERIENCE[lang],
    )

@app.route("/work/<slug>")
def work(slug):
    lang = detect_lang()
    projects = PROJECTS[lang]
    
    project = next((p for p in projects if p["slug"] == slug), None)
    if not project:
        abort(404)
        
    study = CASE_STUDIES[lang].get(slug)
    if not study:
        abort(404)

    return render_template(
        "case_study.html",
        lang=lang,
        dir="rtl" if lang == "ar" else "ltr",
        t=UI[lang],
        project=project,
        study=study
    )

@app.route("/sitemap.xml")
def sitemap():
    """Generates a basic sitemap for search engines."""
    base_url = "https://mohamedbelali.pythonanywhere.com"
    pages = []
    
    # Homepages for both languages
    pages.append(f"{base_url}/?lang=en")
    pages.append(f"{base_url}/?lang=ar")
    
    # Case studies for both languages
    for slug in CASE_STUDIES["en"].keys():
        pages.append(f"{base_url}/work/{slug}?lang=en")
    for slug in CASE_STUDIES["ar"].keys():
        pages.append(f"{base_url}/work/{slug}?lang=ar")
        
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        xml += f'  <url>\n    <loc>{page}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    xml += '</urlset>'
    
    return Response(xml, mimetype='application/xml')

@app.route("/robots.txt")
def robots():
    """Tells search engines to crawl the site and where the sitemap is."""
    content = "User-agent: *\nAllow: /\nSitemap: https://mohamedbelali.pythonanywhere.com/sitemap.xml"
    return Response(content, mimetype="text/plain")

@app.errorhandler(404)
def not_found(e):
    lang = detect_lang()
    return render_template(
        "404.html",
        lang=lang,
        dir="rtl" if lang == "ar" else "ltr",
        t=UI[lang]
    ), 404

@app.after_request
def add_vary_header(response):
    response.headers["Vary"] = "Accept-Language"
    return response

if __name__ == "__main__":
    app.run(debug=True)
