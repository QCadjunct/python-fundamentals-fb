"""Build PDF with diagrams using ReportLab."""

from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# File paths
BASE_DIR = Path("03 - Python Basics/08 - Comparison Operators")
MARKDOWN_FILE = BASE_DIR / "Virtual Blue Book Prototype for Academic Integrity.md"
OUTPUT_PDF = BASE_DIR / "Virtual Blue Book Prototype for Academic Integrity.pdf"

DIAGRAMS = [
    ("workflow_monitoring_1a.png", "Workflow Diagram for Monitoring (Option 1A)"),
    ("workflow_monitoring_1b.png", "Workflow Diagram for Monitoring in Hybrid (Option 1B)"),
    ("workflow_scalable_1c.png", "Workflow Diagram for Scalable Scaffolding (Option 1C)"),
]


def build_pdf():
    """Build PDF from markdown with embedded diagrams."""
    story = []
    styles = getSampleStyleSheet()
    
    # Add title
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
    )
    story.append(Paragraph("Virtual Blue Book Prototype for Academic Integrity", title_style))
    story.append(Spacer(1, 12))
    
    # Read markdown content
    with open(MARKDOWN_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract text before first diagram
    lines = content.split("\n")
    diagram_count = 0
    
    for i, line in enumerate(lines):
        if "```mermaid" in line:
            # Add paragraph of text before diagram
            if i > 0:
                text = "\n".join(lines[max(0, i-5):i]).strip()
                if text:
                    story.append(Paragraph(text, styles["Normal"]))
                    story.append(Spacer(1, 12))
            
            # Add diagram if available
            if diagram_count < len(DIAGRAMS):
                diagram_file, diagram_title = DIAGRAMS[diagram_count]
                diagram_path = BASE_DIR / diagram_file
                
                if diagram_path.exists():
                    story.append(Paragraph(f"<b>{diagram_title}</b>", styles["Heading3"]))
                    story.append(Spacer(1, 12))
                    try:
                        img = Image(str(diagram_path), width=6*inch, height=4*inch)
                        story.append(img)
                        story.append(Spacer(1, 12))
                    except Exception as e:
                        story.append(Paragraph(f"[Image could not be loaded: {diagram_file}]", styles["Normal"]))
                        story.append(Spacer(1, 6))
            
            diagram_count += 1
            
            # Skip to end of code block
            for j in range(i+1, len(lines)):
                if "```" in lines[j]:
                    i = j
                    break
    
    # Add remaining content
    remaining_text = "\n".join(lines[i+1:]).strip()
    if remaining_text:
        story.append(Paragraph(remaining_text, styles["Normal"]))
    
    # Build PDF
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
    )
    doc.build(story)
    print(f"✓ PDF created: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
