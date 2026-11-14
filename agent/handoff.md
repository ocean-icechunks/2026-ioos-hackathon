# Handoff: 2026-ioos-hackathon

Rolling state for agents. This is orientation, not a task list.

## Repo state (2026-11-14)

- The virtual Icechunk tutorial site for the 2026 IOOS Hackathon. Eli Holmes and
  Rich Signell lead the project.
- Merged to `main` in PR #1. Live at
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
  evidence of a broken slide. Ask Eli to check in a browser.

## Open threads

- **The skill's bad `to_icechunk(encoding=...)` snippet:**
  ocean-icechunks/ocean-icechunks-skills#13 is filed, and the skill is not
  fixed yet. The tutorial already uses the working form.
- **Never verified on the workshop hub:** scratch bucket, image, machine sizes.
  Only the main hub was checked.
- **Never seen by me:** the agents' first-start sign-in screens, and some slides
  headless Chrome never captured (chapter 2's Mermaid flowcharts, the chapter 5
  four-step table and prompt slides).
- The merged `tutorial-book` branch still exists on GitHub. Delete it only if
  Eli asks.

## Recently shipped

- PR #1: setup pages, six slide-deck chapters, the NDVI Colab notebook,
  `AGENTS.md`, the ESIP July 2026 talk PDF in `resources/`, and the README
  "Reuse and citation" section (CC0, acknowledgement requested for Holmes and
  Signell).
