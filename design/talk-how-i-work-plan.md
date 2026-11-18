# Plan: "How I work with agents" (15–20 min talk)

Status: **draft plan for Eli to edit.** No slides are written yet. Edit
anything in place; put questions or comments as `> EH:` lines and I will
work from those.

## Brief

- **Audience:** IOOS Hackathon participants. Ocean scientists and data people;
  most have used a chatbot, some have used a coding agent, few have a workflow.
- **Length:** 15–20 min, about 16 slides.
- **What it is:** an opinionated talk about how *I* work, with evidence from my
  own repos. Not a tutorial (deck 02 and the Agent Skills pages are the
  tutorial).
- **One sentence they leave with (draft):**
  *Don't chat with an agent. Run it like a project, with issues, branches,
  PRs, notes and skills, so the work is small, checked and written down.*

> EH: Is this a replacement for deck 02, a new deck 07, or a talk outside the
> lecture sequence? It changes how much setup I can assume.

## The argument in one paragraph

Vibe coding is like working in one endless script: one long conversation, no
boundaries, nothing written down, and no point where anyone checks the work.
It feels fast for an afternoon and falls apart in a week. I work the other
way. Every piece of work is an issue with a "done when". The agent does it on
a branch and proves it in a PR that says what was run. The session ends with a
handoff note and `/clear`. Hooks enforce the rules the model must not break,
and memory keeps my corrections. Skills are where the experience from many
projects is collected, and they get better only because each project reports
its lessons back. My time goes to deciding and checking, not typing.

## Title options (pick or rewrite)

1. **Stop vibe coding** — How I actually work with agents
2. **Not one endless script** — Structure for working with coding agents
3. **Run it like a project** — Issues, PRs, notes and skills with a coding agent
4. **The agent types; I decide**

## Spine (about 16 slides)

Times are rough: Hook 3 min, the loop 7, guardrails 3, skills 5, close 2.

### Part 1 · The hook (3 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 1 | Title | title | Title, subtitle, me |
| 2 | **Vibe coding is one endless script** | statement | One long chat. Every idea goes in. Nothing has an end. Like a 3,000-line `analysis.R` you are afraid to touch. |
| 3 | What that costs | 3 bullets | You can't review it. The agent loses the thread (and burns budget) as the chat grows. Nobody else, including you next week, can pick it up. |
| 4 | **Run it like a project** | statement | The same tools a software team uses: issues, branches, PRs, notes. The agent is fast and new to the project, so give it a team's structure. |

> EH: Do you want a real (anonymized) "before" example on slide 2, e.g. an old
> notebook of yours, or keep it as an image people recognize?

### Part 2 · The loop (7 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 5 | **One month, one plugin** | visual | xpublish-erddap timeline: 236 commits, ~129 issues and PRs, 2026-09-15 → v0.1.0 on PyPI 2026-10-14. Figure: issues opened and PRs merged per day (from git/GitHub). Point: this volume is only reviewable because every step is an issue and a PR. |
| 6 | The loop | diagram | Issue → branch → plan → small change → PR "what was run" → I review and merge → handoff → `/clear` → next issue. (One-row Mermaid, as in deck 02.) |
| 7 | **The issue is the prompt** | code/quote | Excerpt of xpublish-erddap #111: what is wrong, **Done when:** …, *Order 1 of 4*, *Model: Sonnet*. The issue is written so a fresh session can do it with no chat history. |
| 8 | **Ask for an audit, not a fix** | figure + text | #50 "Audit the repository and propose work. Do not fix anything." → findings filed as #55–#72 → shipped one PR each, Oct 7–9. Same move for the test suite: #110 → #111–#114 (it found tests that could not fail). |
| 9 | **A PR is proof, not a diff** | table | PacIOOS #24 "Tested" table: wrong keys → stops, exit 3; rerun → 0 uploads; changed file → `CHANGED`, copy untouched. And the line I want in every PR: **"Not tested: …"**. Quote from #18: *"Everything was run, not read."* |
| 10 | **Clear often; the notes are the memory** | 3 bullets | `agent/handoff.md` (where things stand, short), `docs/design/` (decisions and why), git history. The chat is disposable; the repo is not. |
| 11 | **My phrases are routines** | two-column | "I am about to clear" → update handoff, commit, push, memory. "This task is done" → PR, then stop and ask. Set once in my global instructions file (Skills 100). |

> EH: Slide 8 is my favourite "punchy" moment. Is it accurate that the audit
> issue is your habit, or was that a one-off for the transfer?

### Part 3 · Guardrails (3 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 12 | **Some rules are not up to the model** | table | Hook (can't be argued with): no push to `main`, no force push / `reset --hard`, ask before installing a package, ask before merging. Instruction (the model follows): comment the *why*, say what was tested, work only in this repo. Workflow: I read every PR. From `claude-config/docs/agent-guards.md`. |
| 13 | **Corrections become memory** | list of real memory titles | "Examples are not requirements." "'I don't know' means decide and explain." "Answer questions before acting." "Skills carry knowledge, not one-off scripts." One correction, said once, kept for every future session. |

> EH: OK to show real memory titles from your config? They are harmless, but
> they are yours.

### Part 4 · Skills (5 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 14 | **A skill is experience, written down** | figure + text | virtual-icechunk started (2026-09-03) from an analysis of three of my store repos plus 16 questions I answered on the issue. `SKILL.md` (175 lines) + 15 reference files. Not a prompt; a playbook with gates: plan → local smoke test → production build → README. |
| 15 | **Projects teach the skill** | diagram | Build in a project repo → lessons go in that repo's notes → "Update skill" issue → harvested into the skill → next project starts better. Real examples: OA-indicators build (skill was *flatly wrong* that no virtual store had rendered in a browser); PacIOOS #14 lessons; PacIOOS #9, a bug found by reading the upload script *while writing* archive-to-cloud. |
| 16 | **Rules for a skill** | 3–4 bullets | One success is an anecdote: promote a lesson only when it holds on more than one dataset. Mark guesses Experimental. Bundle knowledge, not one-off scripts. Lessons don't move by themselves: one sat uncollected for two weeks. |

> EH: Do you want to show the archive-to-cloud skill too, or keep the skills
> part on virtual-icechunk only?

### Part 5 · Close (2 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 17 | **Where my time goes now** | visual | Reuse `fig_agent_time.png` from deck 02 (my estimate, not a measurement). |
| 18 | **Start tomorrow** | 3 bullets | 1. Write your workflow phrases into a global instructions file (Skills 100). 2. One task per session; handoff, then `/clear` (Skills 101). 3. Make the agent prove it: real data, "try to break it", a "Tested / Not tested" section (Skills 103). Skills (102) come once you have done something twice. |
| 19 | Thank you / links | closing | agent-coders Skills 100–103, ocean-icechunks-skills, claude-config (if public). QR to the tutorial site. |

## Evidence ledger

Every number above comes from these. Nothing on a slide that isn't here.

| Claim | Evidence | Source | Status |
|---|---|---|---|
| xpublish-erddap: 236 commits, 2026-09-15 → 2026-10-14 | `git log` in `~/xpublish-erddap` | local clone, 2026-11-18 | settled |
| ~129 issues + PRs in that time; 158 commits carry an agent co-author line | GitHub API numbering; `git log` grep | xpublish-community/xpublish-erddap | settled (re-count at build time) |
| v0.1.0 on PyPI 2026-10-14 | handoff | `claude/handoff.md` | settled |
| Audit #50 → findings #55–#72, shipped Oct 7–9 | issue + PR list | GitHub | settled |
| Test review #110: 974 tests, tests that cannot fail (#111) | issue bodies | GitHub #110, #111 | settled |
| Issues carry order, "done when", model suggestion | #110, #111; memory "issues-ordered-with-model-suggestion" | GitHub, memory | settled |
| PacIOOS: 30 issues/PRs, 68 commits, 2026-11-10 → 11-17 | GitHub API, `git log` | ocean-icechunks/pacioos | settled |
| PacIOOS #24 tested table; #18 "Everything was run, not read" | PR bodies | GitHub | settled |
| PacIOOS #9 found while writing archive-to-cloud | issue #9 body | GitHub | settled |
| virtual-icechunk built 2026-09-03 from 3 repos + 16 answered questions | design note | `ocean-icechunks-skills/docs/design/virtual-icechunk-skill.md` | settled |
| Skill was "flatly wrong" about browser rendering; lesson sat two weeks | same note | same | settled |
| SKILL.md 175 lines, 15 references | `wc -l`, `ls` | local clone | settled |
| Evals dry-run on paper only; found 3 gaps | same note | same | settled (say "on paper") |
| Hooks: what is refused vs needs approval | `agent-guards.md` | `~/claude-config/docs/` | settled |
| Time split pie | Eli's estimate | deck 02 notes | **tentative**: label it as an estimate on the slide |
| "Vibe coding falls apart in a week" | opinion | — | opinion; present as mine |

## Figures

| Figure | What they should see | Data | Status |
|---|---|---|---|
| `fig_xpe_timeline` | A month of steady small PRs, with the audit burst on Oct 7–9 | GitHub issues/PRs of xpublish-erddap (dates, type) | to make; script in `slides/scripts/` |
| Loop diagram | the cycle, one row | none | Mermaid |
| Skill ↔ project loop | lessons flow back into the skill | none | Mermaid, one row |
| `fig_agent_time.png` | where my time goes | Eli's estimate | exists (deck 02) |

> EH: For slide 5, would a screenshot of the real GitHub PR list be punchier
> than a chart? It is more recognizable, less precise.

## Making it punchier (ideas, pick any)

- **Statement slides as the backbone.** Each section opens with one sentence
  on a plain slide (slides 2, 4, 7, 8, 9, 12, 14). Fewer bullets overall.
- **Real artifacts on screen**, not paraphrase: an actual issue, an actual
  "Tested" table, actual memory titles. The evidence is what makes it an
  opinion worth hearing.
- **A running contrast**: a small "vibe" vs "project" tag in the corner of
  slides 5–11 (e.g. "endless chat" vs "issue #111").
- **One live-feeling moment**: show a real prompt I typed ("I am about to
  clear") and what the agent did, as a before/after screenshot.

## Not in this talk (on purpose)

- Install and sign-in (Agent Skills pages).
- How to write a `SKILL.md` (Skills 102).
- Vertex, telemetry, NOAA rules (agent-guards covers it; too much for 20 min).

## Sources read

- agent-coders `content/skills-100.qmd` … `skills-103.qmd` (local clone,
  same as the live pages on 2026-11-18)
- `slides/02-agent-and-skills.qmd` in this repo
- `~/claude-config`: `CLAUDE.md`, `docs/agent-guards.md`, memory indexes
- ocean-icechunks/pacioos: issues #1–#14, PRs #5–#30, bodies of #9, #18, #24
- xpublish-community/xpublish-erddap: issues and PRs #15–#129, bodies of #50,
  #110, #111; `claude/handoff.md`
- ocean-icechunks/ocean-icechunks-skills: issues/PRs #1–#18, `agent/handoff.md`,
  `CONTRIBUTING.md`, `docs/design/virtual-icechunk-skill.md`,
  `skills/virtual-icechunk/references/learn-and-evolve.md`
- nmfs-opensci/agent-skills: history of `skills/virtual-icechunk` (#6, #10,
  #13, #41)
