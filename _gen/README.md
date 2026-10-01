# Site generators (not deployed; GitHub Pages skips _-prefixed dirs)

- `pages.py` - guide content, guide clusters and the hub/home FAQ. Starts with the FEATURE TRUTH list
  verified against the app source; re-check it before changing copy.
- `gen_site.py` - builds `guides/**`, `guides/index.html`, `support/index.html`, `404.html`, `sitemap.xml`,
  `robots.txt`: `python3 _gen/gen_site.py`. Those files are build output, never hand-edit them.
  `index.html`, `privacy.html`, `terms.html` are hand-written. The analytics snippet is copied from
  `index.html` at build time.
- `frame_web.py` - frames `raw/*.png` (iPhone 17 sim, 1206x2622, light mode, status bar 9:41) in an
  iPhone shell and writes WebP to `assets/guides/`. Needs Pillow. simctl screenshots often omit the
  Dynamic Island; the raws here have it painted in (x 415-790, y 42-151).
