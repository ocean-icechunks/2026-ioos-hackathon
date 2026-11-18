# Plan: "Working with an agent" (15–20 min talk)

Revision 3, 2026-11-18. Eli changed the plan an hour before the talk: keep it
simple and not story-shaped. Revisions 1 and 2 (the ten-stage arc, the
sparkline and petal options) are in git history (`bef1910`, `5e8a0cb`) and
in `research-talk-structures.md`. The evidence behind each slide is in
`research-how-eli-works.md` and `research-agent-practice-literature.md`.

Deck: `slides/07-how-i-work.qmd`, listed under Lectures as chapter 7.

## Title

**Working with an agent: brainstorming, planning and directing; less coding.**
Opens on the pie chart from chapter 2 (`images/fig_agent_time.png`).

## Shape

Each section goes the same way: **the recommended practice (with a reference)
→ how I implement it, which goes further → what it looks like in my real
PRs and issues.**

| # | Slide | Content |
|---|---|---|
| 1 | Title | |
| 2 | Pie chart | Without an agent most time is coding; with one, most is defining and directing |
| **A** | **Handoff and notes** | |
| 3 | Recommended: keep the context in files | Anthropic best practices (the context window fills fast; put the plan in docs or issues); OpenAI harness engineering ("if knowledge isn't in the repository, it doesn't exist for agents"); Ten Simple Rules rule 5 |
| 4 | How I do it | `AGENTS.md`, `agent/handoff.md`, `docs/design/`, one-fact memory; a hook loads the handoff at session start; the "I am about to clear" routine |
| 5 | In practice | xpublish-erddap: notes moved into the repo on day 2; 14 "Handoff:" PRs; decisions recorded with a name and date ("because she will forget"); PacIOOS's guide for the data owner |
| **B** | **Ten Simple Rules** | |
| 6 | The ten rules, low text | Bridgeford et al. 2025, arXiv 2510.22254 |
| 7 | How my rules and skills implement them | Rule → my setup, in a table; eight of ten match; I differ on 3 and 9 (closeness to the code) |
| 8 | In practice: xpublish-erddap | Scope in my words; backlog #1–#12 on day one; "propose, do not fix" audit (#50 → #55–#72, one PR each); 478 of 974 tests replay real ERDDAP responses; PyPI in a month |
| **C** | **Reviewing without reading every line** | |
| 9 | I don't read all the code (and nor do you) | OS argument; skimming glazes over and pulls toward familiar, minimal code; trust comes from design, evidence and process; read where the science or the risk lives |
| 10 | 1 · Design notes are a must | For agents and people; talk the design through before code |
| 11 | 2 · Know what is in the PR | The agent summarises; ask it questions (conceptual questions helped understanding in Anthropic's study); Tested / Not tested |
| 12 | 3 · Break work into tasks and phases | Order N of M, done when; big unstructured chunks are how you lose track |
| 13 | 4 · Clean up after each task | Handoff, then `/clear`; the routine phrases |
| **D** | **Security** | |
| 14 | How I approach security | Sandbox; all work in PRs; production/sensitive work reviewed by agent + human; control GitHub access; let the agent keep you honest about credentials; link to the safe-practices page |
| 15 | Close | Links |

## Open items

- The pie chart is my own rough estimate (chapter 2 says so in the notes).
- Not yet checked in a browser.

## Revision 3b (2026-11-18, while drafting)

Eli added three slides after the daily workflow: what the handoff is, what
`AGENTS.md` is (and why `CLAUDE.md` is `@AGENTS.md`), and what the design
docs are. They replaced the "How I do it" layout slide. In the review
section, "Design notes are a must" and "Clean up after each task" became one
summary slide of the four review methods, because the first section already
covers both; "Know what is in the PR" and "Break the work into tasks" keep
their own slides. 16 slides plus 4 section dividers, for 15–20 minutes.
