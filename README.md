# QA1337 Guidelines

Source for [qa1337.com](https://qa1337.com): practical QA guides for mobile and web.

A static site in plain HTML, CSS and JS. No framework and no build step. URLs are clean, without `.html` (for example `ios/crash-logs`).

```
index.html     Getting started (home tiles)
ios/           index (tiles) + crash-logs, device-logs, simulators
android/       index (tiles) + crash-logs, adb, emulators, device-fragmentation
web/           index (tiles) + crash-logs, console-logs, network-debugging, storage-and-cookies
resources/     checklists, bug-reports
assets/        style.css, site.js, qa.css, icons
images/        Screenshots used in the guides
.github/       Deploy workflows and the QA build script
```

`ios-logs`, `android-device-logs`, `browser-logs` (in the root) and `android/adb-logs` are redirects to the newer pages. Keep them so old links still work.

## Workflow

All work happens on the `qa` branch. `master` is production.

```
qa      --push-->      qa.yml     -->  qa.qa1337.com   (staging)
qa -> master (PR) -->  static.yml -->  qa1337.com      (live)
```

1. Commit to `qa` and push. `.github/workflows/qa.yml` builds a QA copy and publishes it to the `qa1337/website-qa` repository, which serves the staging site.
2. Check the change on the staging site.
3. Open a pull request from `qa` to `master` and merge it with a merge commit. `.github/workflows/static.yml` publishes `master` to GitHub Pages.
4. Bring `qa` back in line with `master` (fast-forward and push).

Never edit `qa1337/website-qa` directly: every QA deploy replaces its contents.

The QA copy is kept out of search engines. `.github/qa-inject.py` adds `noindex`, a `[QA]` title prefix and the yellow banner from `assets/qa.css`, and the workflow writes a `robots.txt` that blocks everything.

Commit messages use the format `WEBSITE - <description>`.

## How pages are built

`assets/site.js` builds everything shared across pages: the header, the top menu (`LINKS`), the sidebar (`NAV`), the theme toggle, heading links, the sign-up popup and the footer. There is one list to maintain, but these parts are empty if JavaScript is off.

Each page sets:

- `data-page` and `data-section` on `<body>`
- `data-root` on the `site.js` script tag: the path back to the site root, `""` in the root and `"../"` one folder deep

Every `h1`, `h2` and `h3` in `<main>` gets a link icon that copies a direct link. The link comes from the heading text, so renaming a heading changes its link. To pin one, give the heading an `id` yourself.

The footer year updates automatically.

## Add a page

1. Copy a page in the same folder. Change the title, description, `data-page` value and content. Keep `data-section` and `data-root` as they are.
2. Add the page to that platform's `items` in `NAV` in `assets/site.js`. The `id` must match `data-page`.
3. Add a tile to the platform's `index.html`: copy one `<a class="tile">` and change the link, title and icon.

To add a new platform or section, copy a whole folder, then add a category to `NAV` and a link to `LINKS`. Add a gradient class (like `.g-ios`) in `style.css` for its own tile color.

## Styling

All styling is in `assets/style.css`. Colors are variables in `:root`, with light and dark values. The font is the system font (SF Pro), falling back to Segoe UI, Roboto and Arial.

Code is formatted with Prettier (`.prettierrc`).

## Sign-up

The "Sign up" button opens a popup that posts the email to a Google Apps Script web app. Its URL is `SIGNUP_URL` at the top of `assets/site.js`. The script itself is not in this repository.

When updating the script, publish a new version of the existing deployment. A new deployment gets a new URL and breaks the form.
