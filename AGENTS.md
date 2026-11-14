# Agent instructions: 2026-ioos-hackathon

Edit `AGENTS.md`, not `CLAUDE.md`. `CLAUDE.md` holds only `@AGENTS.md`, so
Claude Code reads this file too.

## What this repository is

The virtual Icechunk tutorial for the 2026 IOOS Hackathon: a Quarto website
served by GitHub Pages.

```text
_quarto.yml        website config, with the navbar (chapter list)
_variables.yml     hub URLs, used as {{< var hub.url >}}
index.qmd          landing page
setup/*.qmd        JupyterHub Skills pages (ordinary HTML pages)
slides/*.qmd       one talk-revealjs deck per chapter (format set in slides/_metadata.yml)
slides/images/     figures used by the decks
notebooks/         Colab-ready notebooks
_extensions/eeholmes/talk/   the deck format, from eeholmes/quarto-talk-template
docs/              the rendered site, committed: GitHub Pages serves main /docs
agent/handoff.md   rolling session state: read this first
design/*.md        design notes: decisions and why (not docs/design: docs/ is Quarto's output)
```

## Run `quarto render` before every commit

GitHub Pages serves the committed `docs/` folder as it is. Nothing renders it
on push, so a commit that changes a `.qmd` file without re-rendering leaves the
live site out of date.

```bash
quarto render && touch docs/.nojekyll   # rebuild docs/, keep .nojekyll
git add -A docs                         # commit the rendered output with the source change
```

`docs/.nojekyll` must stay. **A full `quarto render` deletes it** (observed
2026-11-14), so always follow a full render with `touch docs/.nojekyll`.

## Conventions

- Check code shown on a slide or page by running it in a clean venv
  (`/srv/conda/bin/python3.12 -m venv …`) before it goes in. Say in the commit
  message what was run.
- Never write the workshop hub's shared password anywhere in this repository.
- The hub URL lives only in `_variables.yml`.
