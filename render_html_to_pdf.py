"""Convert markdown to PDF with proper formatting and embedded images."""

from pathlib import Path
import markdown2
from playwright.sync_api import sync_playwright

BASE_DIR = Path("03 - Python Basics/08 - Comparison Operators")
MARKDOWN_FILE = BASE_DIR / "Virtual Blue Book Prototype for Academic Integrity.md"
OUTPUT_PDF = BASE_DIR / "Virtual Blue Book Prototype for Academic Integrity.pdf"

# CSS for styling
CSS_STYLE = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 1000px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    h1, h2, h3, h4, h5, h6 {
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        font-weight: 600;
    }
    h1 { font-size: 2.2em; color: #1a1a1a; }
    h2 { font-size: 1.8em; border-bottom: 2px solid #eee; padding-bottom: 0.3em; color: #1a1a1a; }
    h3 { font-size: 1.4em; color: #2c2c2c; }
    h4 { font-size: 1.1em; }
    
    p { margin: 1em 0; text-align: justify; }
    li { margin: 0.5em 0; }
    ul, ol { margin: 1em 0; }
    
    code {
        background: #f4f4f4;
        padding: 0.2em 0.4em;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        font-size: 0.9em;
    }
    
    pre {
        background: #f4f4f4;
        padding: 12px;
        border-radius: 4px;
        overflow-x: auto;
        border-left: 4px solid #0066cc;
        margin: 1em 0;
    }
    
    pre code {
        background: none;
        padding: 0;
        font-size: 0.85em;
    }
    
    blockquote {
        border-left: 4px solid #0066cc;
        padding-left: 16px;
        margin: 1em 0;
        color: #666;
        font-style: italic;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
        font-size: 0.95em;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 10px 12px;
        text-align: left;
    }
    
    th {
        background: #f8f8f8;
        font-weight: 600;
    }
    
    tr:nth-child(even) {
        background: #f9f9f9;
    }
    
    img {
        max-width: 100%;
        height: auto;
        margin: 1.5em 0;
        border: 1px solid #ddd;
        padding: 8px;
        border-radius: 4px;
    }
    
    a {
        color: #0066cc;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    em { font-style: italic; }
    strong { font-weight: bold; }
    
    @page {
        size: A4;
        margin: 20mm 15mm;
    }
    
    @media print {
        body { padding: 0; }
        h2 { page-break-after: avoid; }
        h3 { page-break-after: avoid; }
        img { page-break-inside: avoid; }
        table { page-break-inside: avoid; }
        p { orphans: 3; widows: 3; }
    }
</style>
"""

def build_pdf():
    """Convert markdown to PDF with proper formatting."""
    
    # Read markdown
    with open(MARKDOWN_FILE, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown2.markdown(
        md_content,
        extras=['fenced-code-blocks', 'tables', 'wiki-tables']
    )
    
    # Wrap in HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Blue Book Prototype for Academic Integrity</title>
    {CSS_STYLE}
</head>
<body>
    {html_content}
</body>
</html>"""
    
    # Use Playwright to render to PDF
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(full_html, wait_until="networkidle")
        page.wait_for_timeout(500)
        page.pdf(path=str(OUTPUT_PDF), format="A4", print_background=True, margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"})
        browser.close()
    
    print(f"✓ PDF created: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()