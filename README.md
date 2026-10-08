# Gym Watch / 健身人

Bilingual public product, support, and privacy website. Static HTML, CSS, and JavaScript; no analytics, ads, cookies, or external web fonts.

## App Store Connect URLs

| Locale | Support | Privacy |
|---|---|---|
| English | https://winston-tao1.github.io/gymwatch-support/support/ | https://winston-tao1.github.io/gymwatch-support/privacy/ |
| 简体中文 | https://winston-tao1.github.io/gymwatch-support/zh/support/ | https://winston-tao1.github.io/gymwatch-support/zh/privacy/ |

Product homepage: https://winston-tao1.github.io/gymwatch-support/ (English), or `/zh/` (Chinese).

## Update

Edit `scripts/build.py` for page copy and structure, `assets/site.css` for appearance, and `site.json` for the public support email. Use Python 3.12+.

```sh
python3 scripts/build.py
python3 scripts/check.py
```

Pushing to `main` triggers the GitHub Pages workflow. Repository Settings → Pages must use **GitHub Actions** as the source.

For local preview with correct repository paths, serve the parent directory and open `/gymwatch-support/`.

## Assets and data

Screens and illustrations originate from the Gym Watch project. Screens may contain demo data; they are illustrative and are not clinical measurements. Device render cutouts are derived from Apple official product images and simulator device frames, with background removal. Real UI screenshots are layered in HTML/CSS; see ASSETS.md for provenance. No Lumy imagery is distributed; its website provided layout inspiration.

Privacy copy describes version 1.0 and should be reviewed whenever the app's data flow changes. GitHub Pages' own security access logs are covered in the policy.
