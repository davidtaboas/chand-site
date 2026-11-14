# Chand

Public website for Chand, a finger strength testing and training app for iPhone:
<https://davidtaboas.github.io/chand-site/>

- [Privacy policy](https://davidtaboas.github.io/chand-site/privacy.html) ·
  [Política de privacidad](https://davidtaboas.github.io/chand-site/es/privacy.html)
- [Support](https://davidtaboas.github.io/chand-site/support.html) ·
  [Ayuda y contacto](https://davidtaboas.github.io/chand-site/es/support.html)

Questions and problems: open an issue in this repository.

## How the site is built

Static pages served by GitHub Pages from `main`. English lives at the root and Spanish in `es/`.
The app links to `privacy.html` and `support.html`, so those addresses must not change.

- `content.py` holds every text in both languages; `build.py` (Python standard library only)
  writes the HTML, the inline SVG charts, `sitemap.xml` and `robots.txt`. After editing either
  file, run `python3 build.py` and commit the result.
- `assets/site.css` and `assets/site.js` are written by hand. Parallax and reveal effects are CSS
  scroll-driven animations; they are skipped when the browser does not support them or when the
  visitor asks for reduced motion.
- `assets/img/<lang>/` holds the app screenshots, taken in the iOS simulator at 1320 × 2868 and
  converted with `tools/optimize-shots.sh <folder with es/ and en/>`.
- `assets/fonts/archivo.woff2` is Archivo (SIL Open Font License, see `assets/fonts/OFL.txt`),
  served from this site.

The site matches the app's privacy policy: no cookies, no analytics, no storage and no
third-party requests. A Content-Security-Policy in every page only allows resources from the site
itself, so inline styles and scripts are not allowed either: use classes and the two asset files.
