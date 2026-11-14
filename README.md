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
