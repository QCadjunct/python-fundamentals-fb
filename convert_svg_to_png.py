"""Convert SVG diagrams to PNG."""

from pathlib import Path
import cairosvg

BASE_DIR = Path("03 - Python Basics/08 - Comparison Operators")

DIAGRAMS = [
    "workflow_monitoring_1a.svg",
    "workflow_monitoring_1b.svg",
    "workflow_scalable_1c.svg",
]

for diagram in DIAGRAMS:
    svg_path = BASE_DIR / diagram
    png_path = BASE_DIR / diagram.replace(".svg", ".png")
    
    if svg_path.exists():
        print(f"Converting {svg_path.name}...")
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), dpi=150)
        print(f"  ✓ Created {png_path.name}")
    else:
        print(f"  ✗ File not found: {svg_path}")

print("\nAll diagrams converted!")
