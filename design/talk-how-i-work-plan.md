# Plan: "How I work with agents" (15–20 min talk)

Status: **draft plan for Eli to edit.** No slides are written yet. Edit in
place; put questions or comments as `> EH:` lines and I will work from those.

Revision 2: the talk is about **patterns of work**, learned from how two
projects grew from a first prototype to a mature project, not about what
those projects did. xpublish-erddap and PacIOOS are illustrations only.

## Brief

- **Audience:** IOOS Hackathon participants. Ocean scientists and data people;
  most have used a chatbot, some a coding agent, few have a workflow.
- **Length:** 15–20 min, about 16 slides.
- **What it is:** opinionated: how *I* work. Deck 02 and the Agent Skills
  pages are the tutorial; this is the why behind them.
- **One sentence they leave with (draft):** *Structure is what lets you go
  fast with an agent: questions before code, every task written down, every
  result checked, and every lesson kept.*

> EH: Replacement for deck 02, a new deck 07, or a talk outside the lecture
> sequence?

---

## 1. The pattern: how a project grows

What I see in both repos, in the order it happens. The same arc shows up
in a month-long software project (xpublish-erddap) and an eight-day data
project (PacIOOS).

| Stage | What I do | Why |
|---|---|---|
| **1. Start with a question** | First session is research: how does the thing work, what would it need, a gentle probe of the source. The agent writes a background note. I set the scope in my own words. | Direction changes are cheap here. xpublish-erddap's first plan was dropped on day one, and the note says why. |
| **2. Prototype fast, then stop** | A quick prototype, loosely, even straight to `main`. Then, the same day, every gap it shows becomes an issue, including the boring ones (ownership, license, attribution). | A prototype tells you what the work is. The backlog is what you keep from it. |
| **3. Move the notes into the repo** | By day two: `AGENTS.md`, a handoff note, topic notes. When work outgrows its home repo, it moves to its own (PacIOOS moved out of a shared repo). | From here on, any session can start cold. |
| **4. Think about failure first** | Before building, ask what breaks: what if files change, what if a request is huge, what if keys expire. These become issues too. | Failure modes are cheaper on paper than in production. |
| **5. Test against the real thing** | Real servers, real client code, real data. Local smoke test → scratch copy → production. Clean venv, every time. The PR says what ran and what did not. | "I read it and it looks right" is not a test. |
| **6. Ask for reports, not code** | Big questions go to the agent as research: compare with the sibling projects, audit the repo, review the test suite. It proposes; I decide; the decisions become issues. | The agent is good at a wide look. The choices stay mine. |
| **7. Run a queue** | Issues numbered "order N of M", with dependencies, a "done when" and a suggested model. One issue, one branch, one PR, then a handoff and `/clear`. Small ones in parallel. | At this point the work is mostly execution, and it is easy to review. |
| **8. Record decisions with a name and date** | "Decisions (Eli, 2026-11-14)" in PRs and design notes; "looks wrong but is deliberate"; corrections become memory. | So the next session, or person, doesn't undo them. |
| **9. Harden and hand over** | Tests that can't fail, hygiene, packaging, a release; docs for the people who will own it, including a prompt to recreate the work. | The project must outlive my sessions. |
| **10. Feed the lessons back** | What a project taught goes into its notes, then into the skill. | The next project starts further along. |

**The opinion this supports:** vibe coding isn't wrong for stage 2. It's
wrong as the *whole* method. The loose part lasts hours; the rest is
structure, and the structure is what keeps the speed.

> EH: Is this arc right? Anything missing, especially from the early stage?
> One thing I noticed: you pick a model per task (Opus for judgment, Sonnet or
> Haiku for execution). Is that worth a point?

## 2. My norms with the agent (gist of `~/claude-config`)

- **One setup, everywhere.** Instructions, hooks, skills and memory are in a
  git repo, linked into each machine and into both agents (Claude Code and
  Antigravity).
- **Rules that matter are enforced, not requested.** Hooks refuse destructive
  git and pushes to `main`, and ask me before a merge or a new package. The
  model cannot argue its way past a hook.
- **Every change goes through a PR I review.** The agent never merges on its
  own; "done" means done writing, not done checking.
- **Short phrases start routines.** "I am about to clear", "This task is
  done", "I am about to sign off".
- **Notes live with the repository** (handoff, design notes, `AGENTS.md`),
  written for people and agents. The handoff is orientation, not a to-do list.
- **Verify by running, in a clean environment;** report what ran.
- **Corrections become memory:** one fact per file, backed up in git.
- **Ask me only what is mine to decide**; a question from me gets an answer,
  not an edit.
- **The config grows from friction.** Most rules trace to something that went
  wrong once (a quota memory corrected by measurement; a guard added after a
  near miss).

## 3. Work requirements and how I meet them (high level)

My agency's AI-assisted coding practices, and the short answer for each
(detail in `~/claude-config/docs/agent-guards.md`):

| Requirement | How |
|---|---|
| Disclose AI-generated code | Agent co-author line on every commit, a note in every PR, a README section |
| Human review; explain intent | Everything reaches `main` through a PR I review; the agent comments the *why*; design notes state intent |
| Verify dependencies | Installing a new package needs my approval and a check that it is real; it goes in the dependency file and the PR |
| Sandboxing and approval gates | Agents run only on cloud VMs, no root; hooks and a command classifier gate risky actions |
| Credentials and telemetry | No keys in code; telemetry off where possible; work code runs on Vertex (FedRAMP Moderate) |

**Point for the talk:** a structured workflow and the compliance rules are the
same thing. Almost every requirement is met by habits I'd keep anyway.

> EH: For a hackathon audience, one slide on this, or leave it out? It may
> matter most to the federal people in the room.

---

## Spine (about 16 slides)

Rough times: hook 3 min, the arc 8, norms 3, skills 4, close 2.

### Part 1 · The hook (3 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 1 | Title | title | |
| 2 | **Vibe coding is one endless script** | statement | One chat, no ends, nothing written down. Like the 3,000-line `analysis.R` you're afraid to touch. |
| 3 | It works for an afternoon | 3 bullets | Then: you can't review it, the agent loses the thread, nobody (including you next week) can pick it up. |
| 4 | **Structure is what keeps the speed** | statement | The claim of the talk. |

### Part 2 · How a project grows (8 min)

The arc in section 1, compressed to six slides. Each slide is one pattern,
with one small real example as the illustration, not the topic.

| # | Slide | Pattern (stages) | Illustration |
|---|---|---|---|
| 5 | **The arc** | all | One-row diagram: question → prototype → backlog → test for real → reports → queue → hand over. Overlaid: the loose part is a sliver at the start. Could use the xpublish-erddap timeline (first PR is on day two; ~129 issues and PRs by release). |
| 6 | **Start with a question** | 1, 4 | First session writes a background note and drops the first plan. Ask what breaks before building. |
| 7 | **Prototype, then write the backlog** | 2, 3 | A prototype on day one; a dozen issues filed the same day; notes in the repo on day two. |
| 8 | **Ask for a report, not a fix** | 6 | "Audit the repository and propose work. Do not fix anything." → findings → issues. |
| 9 | **The issue is the prompt** | 7 | A real issue: what's wrong, *Done when*, *Order 1 of 4*, *Model: Sonnet*. A fresh session can do it with no chat history. |
| 10 | **A PR is proof** | 5, 8 | A "Tested" table and a "Not tested" line; decisions with a name and a date. |

### Part 3 · Norms (3 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 11 | **My rules, in one repo** | two columns | Enforced (hooks): no `main`, no destructive git, ask before merge/install. Asked (instructions): phrases as routines, notes in the repo, verify by running, corrections as memory. |
| 12 | **The rules are the compliance** (optional) | table | Section 3, five rows. |

### Part 4 · Skills (4 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 13 | **A skill is experience, written down** | figure + text | Built from an analysis of earlier projects plus my answers to the agent's questions. A playbook with gates, not a prompt. |
| 14 | **Projects teach the skill** | diagram | Build → lessons in the project's notes → "Update skill" issue → harvested → next project starts better. One example of the skill being flatly wrong until a build showed it. |
| 15 | **Rules for a skill** | bullets | One success is an anecdote. Mark guesses Experimental. Knowledge, not one-off scripts. Lessons don't move by themselves. |

### Part 5 · Close (2 min)

| # | Slide | Form | Content |
|---|---|---|---|
| 16 | **Where my time goes** | visual | `fig_agent_time.png` from deck 02, labelled as my estimate. |
| 17 | **Start tomorrow** | 3 bullets | Global instructions with your phrases (Skills 100). One task per session, handoff, `/clear` (101). Make it prove its work (103). Skills (102) once you've done a thing twice. |
| 18 | Thank you / links | closing | Skills 100–103, ocean-icechunks-skills, tutorial QR. |

---

## Evidence for the patterns

Where each stage in section 1 is seen. Illustrations on slides come from here.

| Stage | xpublish-erddap (2026-09-15 → 10-14) | PacIOOS (2026-11-10 → 11-17) |
|---|---|---|
| 1 Question | `design-and-history.md`: first question, first plan dropped, scope in Eli's words | #1: a gentle server probe explains why the files must be copied |
| 2 Prototype → backlog | prototype committed to `main` 09-15; issues #1–#12 filed 09-15 (incl. #12 ownership/citation) | — (prototype lived in a shared repo first) |
| 3 Notes in repo | notes and handoff moved in 09-16 | #5 moves the work into its own repo |
| 4 Failure first | #16 max response size, #8 auth | #2 write-once copies, before the build |
| 5 Real thing | #1 parity with real ERDDAP servers; Flux-like server on AWS (#17) | #15 smoke test vs netCDF-C; local → scratch → production in #18 |
| 6 Reports | #29 plugin comparison → #32–#37; #50 audit → #55–#72; #110 test review → #111–#114 | #16 file audit, with a prompt to recreate it |
| 7 Queue | #110/#111: order, done-when, model; memory "parallel agents for small issues" | one store issue per product (#10–#14) |
| 8 Decisions | memories: "examples are not requirements", "'I don't know' means decide and explain" | #18 "Decisions (Eli, 2026-11-14)"; "hindcast years are PacIOOS's call" |
| 9 Harden, hand over | #111 tests that cannot fail; packaging #66; PyPI 0.1.0; transfer to xpublish-community | `how_store_created.md` for the PacIOOS team; daily updater |
| 10 Lessons back | — | #9 found while writing archive-to-cloud; skills issue #14 |

Skill evidence: `ocean-icechunks-skills/docs/design/virtual-icechunk-skill.md`
(built 2026-09-03 from three repos and 16 answered questions; the browser
claim was "flatly wrong"; a lesson sat uncollected for two weeks) and
`references/learn-and-evolve.md` ("One success is an anecdote").

Norms and requirements: `~/claude-config/CLAUDE.md`,
`docs/agent-guards.md`, and its git history (rules added as they were needed,
2026-08-28 onward).

Opinion, presented as mine: "vibe coding works for an afternoon"; the time
split in `fig_agent_time.png` (an estimate, labelled on the slide).

## Figures

| Figure | What they should see | Status |
|---|---|---|
| The arc | the stages in one row; the loose part is short | Mermaid or drawn |
| xpublish-erddap timeline (optional) | commits/issues per day, phases marked | script from git log + GitHub API |
| Skill ↔ project loop | lessons flow back | Mermaid, one row |
| `fig_agent_time.png` | my time split | exists |

## Making it punchy

- Statement slides open each part (2, 4, 8, 9, 10, 13).
- Real artifacts, small: one issue, one "Tested" table, a few memory titles.
- The running contrast: "endless chat" vs "issue → PR → handoff".
- Be honest that I start loose. It makes the rest believable.

## Not in this talk

Install and sign-in; how to write a `SKILL.md`; Vertex and telemetry detail.

## Sources read

agent-coders Skills 100–103; deck 02; `~/claude-config` (`CLAUDE.md`,
`docs/agent-guards.md`, memory indexes, git history); xpublish-erddap git
history, issues and PRs #1–#129, `claude/notes/design-and-history.md`,
`claude/handoff.md`; pacioos git history, issues and PRs #1–#30;
ocean-icechunks-skills issues/PRs, handoff, design note, `CONTRIBUTING.md`.
