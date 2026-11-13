# 2026-ioos-hackathon

Tutorials and materials for the 2026 IOOS Hackathon: an introduction to
virtual Icechunk stores, built and checked mostly with a coding agent.

**Site:** <https://ocean-icechunks.github.io/2026-ioos-hackathon>

## Build the site

You need [Quarto](https://quarto.org) 1.6 or later.

```bash
quarto render      # writes the site to docs/
quarto preview     # live preview while editing
```

GitHub Pages serves `docs/` from `main`, so **run `quarto render` and commit
`docs/` along with every source change.** Otherwise the live site goes out of
date.
