# Handoff: 2026-ioos-hackathon

Rolling state for agents. This is orientation, not a task list.

## Repo state (2026-11-17, after PR #17)

- The virtual Icechunk tutorial site for the 2026 IOOS Hackathon. Eli Holmes and
  Rich Signell lead the project.
- Sidebar: Home, JupyterHub Skills, **Agent Skills** (one page so far),
  **Lectures** (six decks), **Examples**
  (landing page `examples/index.qmd` + six notebooks), Resources.
- Live at
  <https://ocean-icechunks.github.io/2026-ioos-hackathon> (GitHub Pages, `main`
  `/docs`).
- Layout and the render rule are in `AGENTS.md`. Decisions and why are in
  [`design/tutorial-decisions.md`](../design/tutorial-decisions.md).

## Working principles

- **Run `quarto render` and commit `docs/` with every source change.** Pages
  serves `docs/` as committed. Keep `docs/.nojekyll`.
- **`docs/` is Quarto's output, not design notes.** Design notes live in
  `design/` for that reason.
- **Run any code shown on a slide or page in a clean venv first**
  (`/srv/conda/bin/python3.12 -m venv`), and say what ran in the commit message.
  The scratchpad venv used so far had icechunk 2.3.1, virtualizarr 2.8.0,
  xarray 2026.9.0 and zarr 3.4.2.
- **Eli wants chapters short.** Lead with the skill and what the agent needs,
  rather than with code. Code lives in chapter 3 (pipeline) and the NDVI
  notebook.
- **Headless Chrome screenshots of the decks are unreliable.** They time out,
  lazy images are missing, and Mermaid did not draw. A failed screenshot is not
  evidence of a broken slide. Ask Eli to check in a browser. Quarto's bundled
  Chrome (`~/.local/share/quarto/chromium`, version 92) is too old to run the
  site's Mermaid at all, and `npx mermaid-cli` was blocked by the permission
  classifier.
- **Mermaid on slides:** keep `htmlLabels: false` and a `fig-width`, and keep
  flowcharts on one row. Eli rejected a two-row subgraph layout.
- **Example notebooks render from their stored outputs** (Quarto does not
  execute `.ipynb`). To change one, re-run it end to end in a clean venv
  (nbclient worked), clear the `%pip` cell's output (it prints the venv path),
  check every number the text quotes against the run, look at the figures, then
  render. Figures land in `docs/examples/*_files/`, which `.gitignore`
  un-ignores on purpose.
- **Long OISST `daily/` reads can die on one dropped S3 connection.** Example 5
  reads a year at a time with retries for that reason. Run long examples one at
  a time so their quoted timings are honest.

## Open threads

- **The skill's bad `to_icechunk(encoding=...)` snippet:**
  ocean-icechunks/ocean-icechunks-skills#13 is filed, and the skill is not
  fixed yet. The tutorial already uses the working form.
- **Never verified on the workshop hub:** scratch bucket, the custom image,
  machine sizes. Only the main hub was checked.
- **Agent Skills section is a stub on purpose.** Eli asked for only the
  human-in-the-loop page for now ("don't flesh it out yet"), and said it is
  fine that the home page and setup pages do not link to it yet.
- **Examples not checked:** run times on Colab (only the hub was timed; OISST
  may be slower there, GOBAI faster), and the landing page's sample prompt has
  not been run through an agent. The home page's Examples paragraph does not
  link to `examples/index.qmd`; pointed out to Eli, left as she wrote it.
- **Never seen by me:** the agents' first-start sign-in screens, and some slides
  headless Chrome never captured (the chapter 5 four-step table and prompt
  slides). Eli checked chapter 2's flowcharts in a browser on 2026-11-14.

## Recently shipped

- PR #17 (merged 2026-11-17): `hub.image` is now the workshop image
  `ghcr.io/nmfs-opensci/py-rocket-geospatial-2:2026.11.17`, replacing the
  test tag. Participants paste it under "Image: Other". Not yet started on
  the workshop hub. Branch `workshop-image` not deleted yet.
- PR #16 (merged 2026-11-17, branch deleted): Agent Skills section with
  `agent-skills/01-safe-agent-practices.qmd`, seven practices adapted from
  `~/claude-config/docs/agent-guards.md` for participants. Eli's own hooks,
  Vertex and telemetry were left out on purpose. Section 6 on non-public data
  is in Eli's framing: personal info in a chatbot is your own risk, but work
  data at NOAA, other agencies and companies is under actual rules; use public
  data and public or non-sensitive code. No "adapted from" credit line (Eli
  had it removed).
- PR #15 (merged 2026-11-17, branch deleted): login step 3 uses the custom
  image (`hub.image`); the password is given in person or by DM.

- PR #8 (merged 2026-11-14, branch deleted): the example notebooks' Colab
  badge is an HTML `<a><img alt=...></a>` on purpose. Markdown `![Open In
  Colab](...)` alone on a line becomes a centered figure with the alt text as
  a caption. Each example also prints `ds.nbytes` after opening (HYCOM 1.24 PB,
  four times the 306 TB of int16 files, because xarray counts decoded float64;
  a note in the notebook says so). Only the setup, open and new cells were run
  for that; the rest of each notebook's stored outputs predate it.

- PR #6 (merged 2026-11-14, branch deleted): revision 3. Lectures and Examples
  sidebar sections; six examples (HYCOM snow crab, PacIOOS ALOHA seasons and
  T–S, OA saturation horizon, OISST world SST, Gulf of Maine heatwaves, GOBAI
  oxygen minimum zone); the Examples landing page with store URLs and a sample
  agent prompt; Eli's home-page edits. Which ideas Eli picked, and why, are in
  `design/tutorial-decisions.md`.

- PR #4 (merged 2026-11-14, branch deleted): docked left sidebar with the
  IOOS Code Sprint logo (`images/`), a ⌂ Home link in every deck's footer
  (title slide included), readable chapter 2 flowcharts, and a README
  "Make changes" section (Quarto install, render before push). Embedding the
  decks in sidebar pages was offered and declined; see
  `design/tutorial-decisions.md`.
- PR #2: this handoff, `design/tutorial-decisions.md`, and the `AGENTS.md`
  note that a full `quarto render` deletes `docs/.nojekyll`. Merged branches
  `tutorial-book` and `handoff` were deleted on 2026-11-14.
- PR #1: setup pages, six slide-deck chapters, the NDVI Colab notebook,
  `AGENTS.md`, the ESIP July 2026 talk PDF in `resources/`, and the README
  "Reuse and citation" section (CC0, acknowledgement requested for Holmes and
  Signell).
