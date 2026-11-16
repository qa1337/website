# Used by .github/workflows/qa.yml: turns the copied site into the QA version.
# Run locally to preview:  python3 .github/qa-inject.py <folder with a copy of the site>
import pathlib
import re
import sys

HEAD = '<meta name="robots" content="noindex, nofollow">\n'
# Loaded last in <head> so it overrides assets/style.css
QA_CSS = '<link rel="stylesheet" href="/assets/qa.css">\n'
BANNER = (
    '<div class="qa-banner">QA version · not the live site'
    ' <a id="qa-live" href="https://qa1337.com/">View this page on live</a></div>\n'
    "<script>document.getElementById('qa-live').href="
    "'https://qa1337.com'+location.pathname+location.search+location.hash</script>\n"
)

for page in pathlib.Path(sys.argv[1]).rglob("*.html"):
    html = page.read_text(encoding="utf-8")
    html = html.replace("<head>", "<head>\n" + HEAD, 1)
    html = html.replace("</head>", QA_CSS + "</head>", 1)
    html = html.replace("<title>", "<title>[QA] ", 1)
    # QA keeps the test-tube emoji icon so its tabs look different from live
    html = re.sub(r'assets/favicon\.png" type="image/png"', 'assets/favicon.svg" type="image/svg+xml"', html)
    html = re.sub(r'\s*<link rel="apple-touch-icon"[^>]*>', "", html)
    # Only real pages get the banner (redirect stubs have no <body data-page>)
    if "<body data-page" in html:
        start = html.index("<body data-page")
        end = html.index(">", start) + 1
        html = html[:end] + "\n" + BANNER + html[end:]
    page.write_text(html, encoding="utf-8")
