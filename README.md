# 2026-ioos-hackathon

Tutorials and materials for the 2026 IOOS Hackathon: an introduction to
virtual Icechunk stores, built and checked mostly with a coding agent.

**Site:** <https://ocean-icechunks.github.io/2026-ioos-hackathon>

## Make changes

The site is [Quarto](https://quarto.org) source (`.qmd` files) rendered into
`docs/`, which GitHub Pages serves from `main` as it is committed. Nothing
renders it on GitHub, so **every change needs a `quarto render` before it is
pushed**, or the live site goes out of date.

### 1. Install Quarto

On a laptop, use the installer from <https://quarto.org/docs/get-started/>.
On a JupyterHub or other Linux machine without admin rights:

```bash
QV=1.7.34
curl -sL -o /tmp/quarto.tar.gz \
  https://github.com/quarto-dev/quarto-cli/releases/download/v$QV/quarto-$QV-linux-amd64.tar.gz
mkdir -p ~/.local/opt && tar -xzf /tmp/quarto.tar.gz -C ~/.local/opt
mkdir -p ~/.local/bin && ln -sf ~/.local/opt/quarto-$QV/bin/quarto ~/.local/bin/quarto
quarto --version   # open a new terminal if it is not found
```

### 2. Edit, preview, render, push

Work on a branch and open a pull request.

```bash
quarto preview                          # live preview while you edit
quarto render && touch docs/.nojekyll   # rebuild docs/ (a full render deletes .nojekyll)
git add -A                              # commit the source *and* docs/ together
```

Where things live: the sidebar is in `_quarto.yml`, the chapter decks are
`slides/*.qmd`, and the setup pages are `setup/*.qmd`.

### Working with a coding agent

Agents read [`AGENTS.md`](AGENTS.md) (Claude Code reads it through
`CLAUDE.md`). It tells them to run `quarto render`, keep `docs/.nojekyll`,
and commit `docs/` before pushing, so you do not have to repeat it. If an
agent pushes a `.qmd` change without the matching `docs/` change, ask it to
render and push again.

## Reuse and citation

This work is released under [CC0 1.0 Universal](LICENSE) and is free of known
copyright restrictions. You are free to use, copy, modify, and redistribute it,
in whole or in part, for any purpose, including commercially, and you do not
need to ask permission.

If you reuse or adapt this material, please acknowledge **Eli Holmes** and
**Rich Signell**, who led this 2026 IOOS Hackathon project and developed the
material:

> Holmes, E.E. and Signell, R. (2026). *Virtual Icechunk tutorial, 2026 IOOS
> Hackathon*. ocean-icechunks/2026-ioos-hackathon.
> https://github.com/ocean-icechunks/2026-ioos-hackathon

The datasets used in the examples are not part of this repository and carry
their own terms: follow each data provider's use and citation guidance.
