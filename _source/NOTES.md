# Maintenance notes

Files in folders starting with an underscore are not published by GitHub Pages.

- `index.html` is the whole homepage. Edit it directly.
- `cv.pdf` is generated from `_source/cv.html`:
  `python3 _source/printpdf.py "$PWD/_source/cv.html" "$PWD/cv.pdf"`
  (needs Playwright with Chrome; fonts load from Google Fonts).
- Update the "Last updated" line in `index.html` and the date in the CV footer
  (in `printpdf.py`) when content changes.
- `CNAME` holds the custom domain eikeduevel.com. Do not delete it.
- `og.jpg` is the link-preview image, rendered from `_source/og.html` at 1200x630
  (screenshot with Playwright, then save as JPEG). Re-render it when the
  affiliation or blurb changes.
- `favicon.svg` is Literata's phi glyph; `favicon.ico`, `favicon-32.png` and
  `apple-touch-icon.png` are rendered from it.
- Abstracts sit in `<details class="abstract">` under each paper.
