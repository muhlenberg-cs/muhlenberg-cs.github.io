# muhlenberg-cs.github.io

The public site for CSI 370 (CUE) at Muhlenberg College: setup guide, schedule, MuleCode and GitHub guides, and tutorial videos. Built with [Astro Starlight](https://starlight.astro.build) and deployed to GitHub Pages by `.github/workflows/deploy.yml` on every push to `main`.

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # also checks every internal link
```

- Pages: `src/content/docs/`. The sidebar is in `astro.config.mjs`.
- Decks and the syllabus PDF: `npm run sync` shows what would be copied from the course Drive folder, and `python3 scripts/sync-from-drive.py --copy` copies it. Open each new PDF before pushing: the site is public.
- Videos: `public/videos/<ID>.mp4` with `<ID>.vtt` captions. A page shows its video with `<TutorialVideo id="A1" title="…" />`, and until the file exists it shows a short placeholder.
- Terminal profiles in `public/terminal/` are copied from `mulecode/config/terminal/`.

Never commit student names, rosters or grades here.
