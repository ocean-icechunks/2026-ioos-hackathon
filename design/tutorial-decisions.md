# Tutorial decisions

Why the 2026 IOOS Hackathon tutorial is built the way it is, so a later edit
does not undo something deliberate. Decisions are Eli Holmes's, from
2026-11-13 and 2026-11-14, unless marked otherwise.

## Format

- **A Quarto website, not a book.** Each chapter is a `talk-revealjs` deck that
  Eli clicks through. Quarto's `book` project type cannot render revealjs
  chapters. The deck format comes from `eeholmes/quarto-talk-template`
  (`quarto add`, installed at `_extensions/eeholmes/talk/`; the poster format was
  removed). Setup pages are plain HTML pages, because people follow them step by
  step.
- **The rendered site is committed in `docs/`.** When GitHub Pages serves from a
  branch, it only looks at `/` or `/docs`, so `_site/` would not be served.
  This matches NMFSHackDays-2026. The other option, a GitHub Action that renders
  on push, was offered and not chosen.
- **Navigation is a docked left sidebar** (modeled on NMFSHackDays-2026's
  `_quarto.yml`), with the IOOS Code Sprint logo, a local copy in `images/`.
  The decks are full-screen pages and do not show the sidebar. Wrapping each
  deck in an HTML chapter page with an iframe was offered and declined
  (2026-11-14); instead every deck's footer has a **⌂ Home** link, shown on the
  title slide too (`slides/slides.css` overrides the theme hiding it there).
- **Sidebar sections (revision 3, 2026-11-14):** JupyterHub Skills, Lectures
  (the six decks), Examples, then Resources. Examples are notebooks in
  `examples/` that render as ordinary HTML pages beside the sidebar, not as
  decks. Quarto does not execute `.ipynb` files, so each example is run once in
  a clean venv and committed with its outputs (the `%pip` cell's output is
  cleared, because it prints the venv path). Example 1 is a copy of
  `ocean-icechunks/hycom`'s `bering-sea-snow-crab-demo.ipynb` with an
  "adapted from" link; the copy here is the one to edit for the site.
  Example 2 (PacIOOS ROMS reanalysis at Station ALOHA: how deep the seasons
  reach, and water masses in T–S) was chosen by Eli from five ideas as
  "textbook material". A mixed-layer-depth calculation was dropped as too much
  code; a plain plot of temperature at four depths replaced it.
  Example 3 (NCEI OA indicators: aragonite saturation horizon map, as a
  textbook acidification example) was chosen by Eli after being told the store
  has no time axis and is only 82 MB, so its selling point is one usable grid
  (the source files' coordinates are placeholder zeros), not saved downloads.
  Eli wanted a time-heavy example too, which led to examples 4 and 5.
- **Examples 4 and 5 read OISST's `daily/` group on purpose** (Eli: "doing
  something fast with 16,000 daily files is the real wow example"), not the
  cheaper `monthly/` group. Each daily chunk is NOAA's whole global map, so a
  point, a box and the globe cost the same reads. Example 4 reads every 7th day
  (`step = 7`, ~40 s; `step = 1` is ~5 min), at Eli's request. Example 5 must
  read every day (heatwaves are 5 consecutive days) and takes ~2.5–3 min; it
  reads a year at a time with retries, because two of four long runs died on
  one dropped S3 connection ("connection closed before message completed").
  The OISST container is S3, so it needs
  `containers_credentials({...: s3_anonymous_credentials()})`, not `HttpAccess`.
- **Example 6 (GOBAI HR oxygen minimum zone)** measures the northern edge along
  130 °W, not 120 °W: at 120 °W the < 60 µmol/kg water reaches the coast
  (32.9 °N) and the "edge" just tracked land. GOBAI HR is preliminary, so the
  notebook presents its expansion as something to check, not a result.
  It reads one 02:00 HST profile on the 15th of each month, 2009–2020,
  because each chunk is one depth at one time step and long series are costly.
  The rendered figures sit in `docs/examples/*_files/`, which `.gitignore`
  un-ignores; before that exception, Example 1's figures were not committed.
- **Mermaid on slides uses `htmlLabels: false` and `fig-width: 11`.** HTML
  labels were clipped (the deck's fonts change the text after Mermaid measures
  it) and the default size was tiny. Eli rejected a two-row layout made with
  subgraphs (2026-11-14): keep flowcharts on one row.
- **Design notes live in `design/`, not `docs/design/`.** Here `docs/` is Quarto's
  output folder, and a render rewrites it.
- **Figures follow the template's convention:** a script per generated figure
  (`scripts/fig_*.py`, styled by `scripts/talk_style.py`), with the PNG
  committed.

## Audience and setup

- **Workshop hub:** `workshop.nmfs-openscapes.2i2c.cloud`. The username is the
  participant's email, and everyone shares one password that Eli gives out at the
  event. **Never write the password into the repo.** The hub is deleted a week
  after the hackathon, so the setup pages tell people to push their work to
  GitHub. The hub URL lives only in `_variables.yml`.
- **Participants bring their own agent subscription** (Claude, ChatGPT/Codex,
  or Google Antigravity). There is no gateway and no organizer keys. Agents
  install into `~/.local/bin` so they survive a server restart. Codex needs
  `npm install -g --prefix ~/.local`, because npm's default prefix is the image's
  conda env, which is reset.
- **Git goes through the agent.** People log in once with `gh auth login` (token
  for one repository, or full access) and ask for outcomes, not commands. The
  2025 git-terminal lesson is linked only for background.

## Content

- **Kept short throughout.** Eli asked for brevity at every chapter.
- **The quick wins are part of chapter 1,** not a separate deck. The order is:
  the problem (too many files) → a product, not files → servers versus object
  storage → snow-crab Colab → VirtualiZarr → new tools → NDVI Colab. Figures come
  from Eli's ESIP July 2026 talk (`resources/`).
- **NDVI is the worked example,** reused from the June 5, 2026 HackHours, because
  it is tested and public. Kerchunk is deliberately left out.
- **Chapter 2's pie charts are Eli's own estimate**, labelled as such in the
  speaker notes. She chose four shared activities (fixed colour per activity,
  shared legend) over a seven-activity version.
- **Chapter 4 (audit) has one slide per key idea**, each with a real case: grids
  (CoastWatch OHC), chunking (NDVI `QA`), encoding (PacIOOS), appendability
  (CEFI 365/366-day files with a 100-day chunk), data bugs (missing HYCOM
  analyses), and metadata. The last slide is having the agent write the report,
  after it has been told where the files are.
- **Chapter 5 (build) has no code,** because the code is in chapter 3. Eli's
  point: a store's layout is mostly decided by the files, and the skill works it
  out and asks you to confirm. What only the user can supply is where the files
  are, the scope, the destination bucket, who will read it, and whether it is
  built once or kept up to date. A local store is never the goal, so the example
  prompt publishes to a bucket and there is an authentication slide.
- **Chapter 6's live gridlook link is OA indicators,** not HYCOM. On 2026-11-14 a
  ranged GET showed HYCOM's AWS bucket sends no CORS header (axes, no data),
  while NCEI and the NDVI bucket send `Access-Control-Allow-Origin: *`. Eli had
  confirmed in a browser on 2026-09-18 that OA indicators renders.

## Facts found by running (things that look wrong but are deliberate)

- **The time-coordinate chunk is set with `vds["time"].encoding["chunks"]`.**
  `to_icechunk()` has no `encoding` argument in virtualizarr 2.0.0–2.8.0, so the
  skill's documented form raises `TypeError`
  (ocean-icechunks/ocean-icechunks-skills#13). Left unset, a multi-file store
  gets one time chunk per file.
- **The scratch-bucket Icechunk snippet passes boto3 credentials explicitly.**
  On the main hub, `s3_storage(..., from_env=True)` got `AccessDenied` with
  icechunk 2.3.1, while explicit frozen credentials worked. The workshop hub was
  not tested.
- **`dask` must be installed** for `xr.open_zarr(..., chunks={})`. It is in the
  notebook's `%pip` line for that reason.
- **The NDVI notebook was executed end to end** in a clean venv (2026-11-13,
  re-run 2026-11-14 after the time-chunk line was added): a 54 kB store pointing
  at 303 MB of NetCDF. The snow-crab notebook was also executed, and its two
  figures were taken from that run.
