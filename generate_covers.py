"""
Generate stylish SVG book cover placeholders for books missing cover images.
Each cover gets a unique gradient and icon based on its category.
"""
import os

COVERS = {
    "devotional_3": {"title": "The Daily\nStoic", "color1": "#1B2A4A", "color2": "#2C3E6B", "accent": "#C8A951", "icon": "☀"},
    "devotional_4": {"title": "Streams in\nthe Desert", "color1": "#2C3E6B", "color2": "#1B2A4A", "accent": "#D4BC72", "icon": "🌊"},
    "business_1": {"title": "Zero\nto One", "color1": "#1B2A4A", "color2": "#0D1B2A", "accent": "#C8A951", "icon": "🚀"},
    "business_2": {"title": "The Lean\nStartup", "color1": "#0D1B2A", "color2": "#1B2A4A", "accent": "#E8D5A3", "icon": "⚡"},
    "business_3": {"title": "Good to\nGreat", "color1": "#1B2A4A", "color2": "#2C3E6B", "accent": "#C8A951", "icon": "📈"},
    "business_4": {"title": "Think &\nGrow Rich", "color1": "#2C3E6B", "color2": "#0D1B2A", "accent": "#D4BC72", "icon": "💡"},
    "education_1": {"title": "Sapiens", "color1": "#1B2A4A", "color2": "#2C3E6B", "accent": "#C8A951", "icon": "🌍"},
    "education_2": {"title": "Cosmos", "color1": "#0D1B2A", "color2": "#1B2A4A", "accent": "#E8D5A3", "icon": "✨"},
    "education_3": {"title": "A Short\nHistory", "color1": "#2C3E6B", "color2": "#1B2A4A", "accent": "#C8A951", "icon": "🔬"},
    "education_4": {"title": "Educated", "color1": "#1B2A4A", "color2": "#0D1B2A", "accent": "#D4BC72", "icon": "🎓"},
}

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="560" viewBox="0 0 400 560">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color1}"/>
      <stop offset="100%" style="stop-color:{color2}"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="400" height="560" rx="8" fill="url(#bg)"/>
  <rect x="30" y="30" width="340" height="500" rx="4" fill="none" stroke="{accent}" stroke-width="1" opacity="0.3"/>
  <line x1="50" y1="380" x2="350" y2="380" stroke="{accent}" stroke-width="1" opacity="0.4"/>
  <text x="200" y="240" text-anchor="middle" fill="{accent}" font-size="64" font-family="serif">{icon}</text>
  {title_lines}
  <text x="200" y="430" text-anchor="middle" fill="{accent}" font-size="14" font-family="serif" opacity="0.6">PAGETURN BOOKS</text>
</svg>"""

def make_title_lines(title, accent):
    lines = title.split("\n")
    start_y = 310 if len(lines) == 1 else 300
    result = []
    for i, line in enumerate(lines):
        y = start_y + i * 36
        result.append(f'<text x="200" y="{y}" text-anchor="middle" fill="white" font-size="28" font-family="serif" font-weight="bold" filter="url(#shadow)">{line}</text>')
    return "\n  ".join(result)

def main():
    out_dir = os.path.join("static", "images")
    os.makedirs(out_dir, exist_ok=True)
    for name, cfg in COVERS.items():
        title_lines = make_title_lines(cfg["title"], cfg["accent"])
        svg = SVG_TEMPLATE.format(
            color1=cfg["color1"], color2=cfg["color2"],
            accent=cfg["accent"], icon=cfg["icon"],
            title_lines=title_lines,
        )
        path = os.path.join(out_dir, f"{name}.webp")
        # Save as SVG with .webp extension — browsers handle SVG content fine via img tags
        # Actually, let's save as proper SVG
        svg_path = os.path.join(out_dir, f"{name}.svg")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"  [OK] Generated {svg_path}")
    print(f"\n[DONE] Generated {len(COVERS)} cover images.")

if __name__ == "__main__":
    main()
