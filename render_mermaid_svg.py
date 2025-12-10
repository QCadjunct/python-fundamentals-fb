"""Render Mermaid diagrams to SVG using Playwright."""

from pathlib import Path

from playwright.sync_api import sync_playwright


DIAGRAMS = {
    "workflow_monitoring_1a": """
flowchart LR
    Start[Exam Start 🚀] -->|Trigger Scheduler ⏰| Block[Block Internet 🔒]
    Block --> LocalWork[Local Tools Only 🛠️]
    LocalWork -->|Monitor Logs 👀| Flag[Flag Violations 📢]
    Flag -->|Alert Proctors 🚨| Audit[Post-Exam Audit 📊]
    LocalWork --> End[Exam End 🛑]
    End -->|Revert & Copy 🔄| Submit[Submissions Secured 📂]

    style Start fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    style Block fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style LocalWork fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Flag fill:#fef7f7,stroke:#c2185b,stroke-width:2px,color:#000
    style Audit fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
    style End fill:#fff8e1,stroke:#f57c00,stroke-width:2px,color:#000
    style Submit fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
""",
    "workflow_monitoring_1b": """
flowchart LR
    Connect[VPN Connect 🚀] -->|Allow Specific ☑️| Access[Restricted Access 🔐]
    Access --> Work[Offline + Allowed Sites 🛠️]
    Work -->|Track Usage 👀| Log[Log Violations 📊]
    Log -.->|Flag 🚨| Alert[Proctor Alert 📢]
    Work --> Submit[Upload & Copy 📤]
    Submit --> Audit[Audit Logs 📄]

    style Connect fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    style Access fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Work fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Log fill:#fef7f7,stroke:#c2185b,stroke-width:2px,color:#000
    style Alert fill:#fef7f7,stroke:#c2185b,stroke-width:2px,color:#000
    style Submit fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
    style Audit fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
""",
    "workflow_scalable_1c": """
flowchart LR
    Setup[Policy Setup 📋] -->|Course Type 📚| Tailor[Tailor Access ⚖️]
    Tailor --> Enforce[Enforce Zero-Trust 🔐]
    Enforce --> Work[Departmental Work 🛠️]
    Work -->|Monitor 👀| Log[Log Activity 📊]
    Log -.-> Audit[Department Audit 📄]
    Work --> Submit[Submissions 📤]
    Submit --> Scale[Scale to Depts 🚀]

    style Setup fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    style Tailor fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Enforce fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Work fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Log fill:#fef7f7,stroke:#c2185b,stroke-width:2px,color:#000
    style Audit fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
    style Submit fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
    style Scale fill:#fff8e1,stroke:#f57c00,stroke-width:3px,color:#000
""",
}

OUTPUT_DIR = Path("03 - Python Basics/08 - Comparison Operators")


def render_mermaid_to_svg(mermaid_code: str, name: str) -> str:
    """Render Mermaid diagram to SVG using Playwright and mermaid.live API."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        
        # Use mermaid.live to render diagram
        html = """
        <html>
        <head>
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        </head>
        <body>
            <div class="mermaid">
""" + mermaid_code + """
            </div>
            <script>
                mermaid.initialize({ startOnLoad: true, theme: 'default' });
            </script>
        </body>
        </html>
        """
        
        page.set_content(html, wait_until="networkidle")
        page.wait_for_timeout(2000)
        
        # Get SVG content from the rendered diagram
        svg_content = page.locator(".mermaid").inner_html()
        browser.close()
        
        return svg_content


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    for name, mermaid_code in DIAGRAMS.items():
        print(f"Rendering {name}...")
        try:
            svg = render_mermaid_to_svg(mermaid_code, name)
            svg_path = OUTPUT_DIR / f"{name}.svg"
            with open(svg_path, "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"  ✓ Saved to {svg_path}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\nAll diagrams rendered successfully!")


if __name__ == "__main__":
    main()
