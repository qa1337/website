# QA1337 Guidelines

A static documentation site (plain HTML, CSS, JS). No build step.

```
index.html                          Getting started
ios/        index.html (tiles) + device-logs, simulators, version-coverage
android/    index.html (tiles) + adb-logs, emulators, device-fragmentation
web/        index.html (tiles) + console-logs, network-debugging, storage-and-cookies
resources/  checklists, bug-reports
assets/style.css                    All styling. Colors are variables at the top.
assets/site.js                      Header menu, sidebar, heading links, theme toggle
assets/favicon.svg
```

## Deploy on GitHub Pages
1. Push these files to a repository (the files go in the repo root).
2. Repo Settings → Pages → Build and deployment → Deploy from a branch → `main` / root.
3. The site appears at `https://<user>.github.io/<repo>/`. For a custom domain, add a `CNAME` file containing the domain.

Paths are relative, so it works from a project URL or a custom domain.

## Add a page to an existing platform (for example iOS)
1. Copy any page in that folder (for example `ios/simulators.html`). Edit the title, description, `data-page` value and content. Keep `data-section` and the `data-root` on the script tag as they are.
2. Add the page to the platform’s `items` list in the `NAV` list at the top of `assets/site.js` (the `id` must match `data-page`).
3. Add a tile to the platform’s `index.html`: copy one `<a class="tile">` line and change the link, title and icon name.

## Add a new platform or section
Copy a whole folder, then add a new category to `NAV` and a link to `LINKS` in `assets/site.js`. Add a gradient class (like `.g-ios`) in `style.css` if you want its own tile color.

## Sign-up button
The header “Sign up” button opens a popup that posts the email to your Google Apps Script web app (same method as the old site). The URL is `SIGNUP_URL` at the top of `assets/site.js`. If you redeploy the script and get a new URL, change it there. The old `thankyou.html` is no longer needed.

## Notes
- `data-root` is the path back to the site root: `""` for files in the root, `"../"` for files one folder deep.
- Every `h1`, `h2` and `h3` in `<main>` gets a link icon that copies a direct link. The link comes from the heading text, so renaming a heading changes its link. To pin one, give the heading an `id` yourself.
- The header menu and sidebar are built by `site.js`, so there is one list to maintain, but they are empty if JavaScript is off.
- Visitors without SF Pro see Segoe UI, Roboto or Arial. To use one font everywhere, self-host Inter and put it first in `body` in `style.css`.
