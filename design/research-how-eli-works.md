# Research note: how Eli works with coding agents

Written 2026-11-18 by an agent, from Eli's repositories and agent config.
It is research data, not the talk; the talk plan
(`talk-how-i-work-plan.md`) draws on it. Point an agent here when it needs
to know how Eli runs a project with agents.

Each claim names its source. Where something is only a memory title (the
memory body was not read), it says so. What was not read is listed at the end.

## Sources

| Source | What was read |
|---|---|
| `~/xpublish-erddap` (github.com/xpublish-community/xpublish-erddap) | `git log` (236 commits, 2026-09-15 → 10-14; 158 carry an agent co-author line); titles of issues and PRs #1–#129; bodies of #50, #110, #111; `claude/handoff.md` (first 60 lines); `claude/notes/design-and-history.md` (first 60 lines); memory index (28 memories) |
| `~/pacioos` (github.com/ocean-icechunks/pacioos) | `git log` (68 commits, 2026-11-12 → 11-17); titles of issues and PRs #1–#30; bodies of #1, #2, #9, #15, #18, #24 (first 1,200–2,500 characters each); memory index (5 memories) |
| `~/ocean-icechunks-skills` | `agent/handoff.md`, `CONTRIBUTING.md`, `docs/design/virtual-icechunk-skill.md`, `skills/virtual-icechunk/references/learn-and-evolve.md` (first 40 lines), start of `docs/virtual-icechunk-patterns.md`; issues and PRs #1–#18; memory index |
| `~/agent-skills` | history of `skills/virtual-icechunk` before it moved (#6, #10, #13, #15, #17, #19, #41) |
| `~/claude-config` | `CLAUDE.md` (global instructions), `docs/agent-guards.md`, `common/skills.txt`, git history (201 commits since 2026-08-28), memory directories (29 projects) |
| agent-coders `content/skills-100.qmd` … `skills-103.qmd` | the four pages in full (the teaching version of the same workflow) |

---

## 1. The project arc

Both projects go through the same stages, in about the same order, even
though one is a month-long software package and the other an eight-day data
project. The early stage is loose; structure is added quickly and then held.

### 1.1 Start with a question, and write down the answer

- xpublish-erddap's first session was research: how does xpublish-opendap
  work, and what would ERDDAP need? The background went in a note
  (`opendap-background.md`). (`design-and-history.md`)
- The first plan (be reachable from a real ERDDAP via `EDDGridFromDap`) was
  dropped on day one because Eli has no ERDDAP server and does not want one.
  The note records the dropped plan and why. (`design-and-history.md`)
- Eli set the scope in her own words, and the note quotes them: *"goal is not
  a ERDDAP like UI, rather to have erddapy and rerddap code work."* The note
  then says "Do not let it grow into a full ERDDAP."
- PacIOOS started with "a gentle probe" of the provider's public servers
  (2026-11-10), which showed the files are not reachable over HTTPS. That
  finding is the reason the files are copied. (pacioos #1)

### 1.2 Prototype fast, then write the backlog the same day

- xpublish-erddap day one (2026-09-15): a prototype router, CI, and badges,
  committed straight to `main`. No PR until #15 on day two. (`git log`)
- The same day, issues #1–#12 were filed: parity with real ERDDAP, `.dods`,
  catalog caching, search, categorize, tabledap scope, auth pass-through,
  client-version coverage, tie-breaking, and **#12 "Settle repo ownership,
  attribution and citation"**. The non-code questions are filed alongside the
  code ones. (issue list)
- Scope questions are filed as decisions to make ("Decide whether tabledap is
  in scope", #7; "Decide on `/erddap/convert/` services", #70) and answered on
  the issue.

### 1.3 Move the notes into the repo early

- Day two of xpublish-erddap: "Move session notes and handoff into this
  repo" (`b7b35f9`), then "Handoff: trim; move environment details to
  notes/dev-environment.md". The handoff is kept short from the start.
- PacIOOS work began in a shared repo (ocean-icechunks/icechunks) and was
  moved to its own repo as the first PR (#5) once it was big enough to need
  one.
- Older repos use `claude/handoff.md` + `claude/notes/`; newer ones
  `agent/handoff.md` + `docs/design/`. (global `CLAUDE.md`)

### 1.4 Think about failure before building

- PacIOOS #2, filed before any store was built: what happens when a source
  file changes or a new version arrives. It works out that virtual stores
  point at byte offsets, so the copies must be write-once, and that the
  upload script did not yet guarantee that.
- xpublish-erddap filed limits and edges as their own issues early: maximum
  response size (#16), auth (#8), and later "refuse coordinate values outside
  an axis instead of snapping" (#57), "skip a failing source instead of
  failing every request" (#56).

### 1.5 Test against the real thing

- xpublish-erddap's first big task (#1, PR #15): output parity against real
  ERDDAP servers, and the users' own tutorials run against the plugin. Later
  the parity tests are the contract: 478 of 974 tests replay 239 responses
  captured from 10 real ERDDAP datasets. (#110)
- A Flux-like test server on AWS (#17), so collaborators could test real
  clients against it. It had a teardown date and a budget cap (memory
  titles "AWS demo server budget": $100 cap, tear down 2026-11-13).
- ERDDAP behaviour is ported from ERDDAP's own source, citing the method,
  then checked on a live server. (memory title "Port ERDDAP behaviour from its
  source")
- PacIOOS stores go local smoke test → scratch prefix on the real object store
  → production, with the scratch copies deleted afterwards and the deletion
  recorded. Notebooks run in a clean venv from `requirements.txt`. (#15, #18,
  commit log)
- PRs carry a "Tested" section, often a table of cases and results, and a
  "Not tested" line. PacIOOS #24 tested wrong keys, first upload, rerun,
  deleted sidecar, changed file, and a faked empty listing, all against a
  scratch prefix. PacIOOS #18: *"Everything was run, not read."*

### 1.6 Ask the agent for a report, not a fix

At each turning point a session is asked to look widely and **propose**, not
change anything. Eli decides, and the decisions become issues.

| Report | Became |
|---|---|
| xpublish-erddap #29: compare with the other xpublish-community plugins | plan items opened as #32–#37 |
| xpublish-erddap #50: "Audit the repository and propose work … Do not fix anything or open other issues while doing it." | findings filed as #55–#72, shipped as one PR each over 2026-10-07 → 10-09 |
| xpublish-erddap #110: test-suite review before the transfer | #111–#114, which included "tests that cannot fail" |
| PacIOOS #16: file audit of the copies | store plans #10–#14, plus a prompt to recreate the audit (`how_audit_created.md`) |

The audit issue (#50) is itself written as an agent brief: why now, what to
read first (handoff, design notes, decisions already made "do not re-propose
them as problems"), how to set up, check open issues to avoid duplicates, then
what to look at, in priority order.

### 1.7 Run a queue

Once the plan exists, the work is a queue of small issues:

- Each issue has **"Order N of M"**, dependencies, a **"Done when:"** that can
  be checked, and a **suggested model** (Opus, Sonnet, or Haiku). #110 says
  "None needs Opus: the judgment is in the note; the work is checking each
  claim … and editing." (#110, #111; memory "Issues in order, with a model
  suggestion")
- If the session's model doesn't match the issue's, the agent says so and
  waits. (memory title "Flag a model mismatch before starting")
- One issue → one branch → one PR, titled with the issue number. A related
  issue may jump the order if the agent suggests it with a reason and Eli
  agrees. (memory titles)
- Small issues run in parallel, one agent per issue, each reviewed and
  trial-merged before it is called ready. (memory title "Parallel agents for
  small issues")
- After merged work, a separate small "Handoff: …" PR updates the handoff
  (xpublish-erddap #23, #30, #41, #51, #73, #79, #85, #87, #97, #102, #107,
  #109, #121, #128; PacIOOS #7, #17, #19, #23, #25, #28, #30).
- PR bodies say "Part of #N", not "Closes #N". Issues close when Eli says.
- Automated review is used and answered ("Address Copilot's review of #15").
- xpublish-erddap's daily commit counts show the queue: 50 on 2026-10-08 and
  83 on 2026-10-09, during the audit findings.

### 1.8 Record decisions with a name and a date

- PR bodies have a "Decisions (Eli, 2026-11-14)" section (PacIOOS #18).
- Design notes list "Decisions Eli made, that a reader should not silently
  revisit" and "facts Eli supplied that contradict the repositories' own
  artifacts" (`virtual-icechunk-skill.md`).
- The handoff flags deliberate oddities: BSD-3 license "on purpose … Do not
  flag or change it"; the next release uses a bare tag, "EH decided this on
  2026-10-14 and asked for it to be written here because she will forget."
- Decisions that belong to a partner are marked as theirs: "Hindcast years:
  PacIOOS decides." (pacioos memory)
- Corrections become memory, e.g. "Examples are not requirements", "Numbered
  choices get per-item answers — 'I don't know' means decide and explain",
  "Demo catalog: readable over complete". (xpublish-erddap memory titles)

### 1.9 Harden and hand over

- xpublish-erddap before its transfer: test-suite review (#110–#114), repo
  hygiene (#55), packaging (#66), "say what is stable" (#125), Beta classifier
  (#126), first PyPI release 0.1.0 (2026-10-14) through trusted publishing,
  with Eli approving each upload, then transfer to xpublish-community.
- `docs/hosting.md` is written for the eventual host (Earthmover): every choice
  a host may need to change.
- PacIOOS writes for the data owner: `how_store_created.md` ("for the PacIOOS
  team": how to run each step, the decisions, things that look wrong and are
  deliberate, and a prompt for a coding agent), product READMEs beside the
  stores, and a daily updater (#21, #27).

### 1.10 Lessons go back to the skill

- PacIOOS #9 (an upload script could overwrite finished copies) was found
  "by reading the script while writing the `archive-to-cloud` skill". The
  fix (#24) was then tested and its lessons filed back as a skill issue
  (ocean-icechunks-skills #15).
- PacIOOS build lessons filed as ocean-icechunks-skills #14 ("[Update skill]:
  virtual-icechunk lessons from the PacIOOS reanalysis build").

### Pace

| | xpublish-erddap | PacIOOS |
|---|---|---|
| Span | 2026-09-15 → 10-14 (work on 9 days) | 2026-11-10 → 11-17 |
| Commits | 236 | 68 |
| Issues + PRs | ~129 | 30 |
| Ended with | PyPI 0.1.0, transfer to xpublish-community | 3 published stores, daily updaters, team guide |

---

## 2. Norms with the agent (`~/claude-config`)

The global instructions (`CLAUDE.md`, read by Claude Code and Antigravity)
and the hooks, in short:

- **One config, every machine, both agents.** Instructions, hooks, skills and
  memory live in one git repo, linked in by `bootstrap.sh`. Auth and account
  settings are machine-local and never in the repo.
- **Enforced, not requested.** A pre-command hook refuses destructive git
  (`reset --hard`, force push, `clean -f`), `rm -r` outside the project, and
  pushes to `main`; it asks before merges, branch deletes, issue closes, PRs to
  repos Eli doesn't own, and installing a named package.
- **GitHub actions are in Eli's name**, so: never push to `main`; merge only
  when she says, after saying what is being merged and asking; suggest, don't
  do, branch deletes and issue closes; "Part of #N", not "Closes #N"; work only
  in the repo the session started in.
- **Disclose and write for review.** Agent co-author line on commits, a note
  on PRs, a README statement. Comment the *why*, not what each line does. PR
  bodies state intent, what was run, and what was not.
- **Verify dependencies** before installing, and list new ones in the PR.
- **Verify by running, in a clean venv,** at the smallest real size. Report
  what printed. Retry before calling a failure a bug.
- **Notes live with the repo:** `AGENTS.md` (with `CLAUDE.md` = `@AGENTS.md`),
  `agent/handoff.md`, `docs/design/`. The handoff is orientation, not an
  assignment: "I will say what I want done."
- **Phrases start routines:** "I am about to clear" (update handoff and
  memory, commit, push, say "Ready to clear."), "This task is done" (open the
  PR, then stop and ask), "I am about to sign off" (ask about each open loop).
- **Project memory**, one fact per file, shared by both agents, backed up in
  the config repo.
- **License and reuse** is a one-sentence side note, raised only before a
  publish, release or PR.
- **The config grows from friction.** Its history adds rules as they were
  needed: the git guard (09-02), loading the handoff at session start (09-03),
  the routine phrases (09-03), "an explicit merge sequence is per-message, not
  standing permission" (09-03), verify by running (09-17), Antigravity support
  (10-02), pass commit text as a file (10-03), GitHub guard rules (10-03). A
  memory was corrected by measurement: "the quota is ~20 GiB, measured, not
  the remembered 50 GB" (09-17).

## 3. Work requirements (high level)

`docs/agent-guards.md` maps the agency's AI-assisted coding practices to
Eli's setup, and labels each control as a hook (enforced outside the model),
an instruction (the model follows it), or workflow (PR review).

| Practice | How it is met |
|---|---|
| Code attribution | co-author line on commits, note on PRs, README section |
| Intent and SME review | everything reaches `main` through a PR Eli reviews and often tests; comments explain the why; agent docs state intent |
| Dependency verification | install of a named package needs approval after a check that it is real; new packages go in the dependency file and the PR |
| Sandboxing | agents run only on cloud VMs, unprivileged (no `sudo`); hooks refuse or gate risky actions; Claude's classifier and Antigravity's allowlist gate the terminal |
| Credentials and telemetry | no keys in code or config; keys in one private file per machine, time-limited; telemetry off where the tool allows; NOAA work on Vertex AI (FedRAMP Moderate) |

The note's point: most controls are habits of the workflow itself (PRs,
running tests, notes), with hooks for the few that must not depend on the
model.

---

## 4. How Eli develops skills

From ocean-icechunks-skills and the history of virtual-icechunk in
nmfs-opensci/agent-skills.

1. **Skills start from evidence, not from a prompt.** virtual-icechunk began
   with a provisional analysis of three existing store repos plus an example
   notebook and official docs for pinned versions
   (`docs/virtual-icechunk-patterns.md`, 2026-09-03, "provisional analysis
   for project-owner review"). The skill was then built from that analysis.
2. **The agent asks; Eli answers on the issue.** 16 questions were answered on
   agent-skills #4 before the skill was written. The durable answers went into
   `references/learn-and-evolve.md`; the rest stay on the issue.
3. **Eli's knowledge goes in as decisions,** recorded as hers in the design
   note: ERDDAP out until there is a real example; rebuilding source files is
   the exception; facts that contradict the repos' own artifacts (some stores
   the notebooks make look unfinished are complete). Two performance traps that
   "had bitten real builds" came from her directly, not the analysis.
4. **A skill is a gated playbook.** virtual-icechunk: `SKILL.md` (175 lines)
   plus 15 reference files; modes Research & plan → Create → Audit →
   Diagnose → Learn. Create is gated: reviewed plan → smoke test against a
   local store → production script → README. It stops for review between
   steps.
5. **Strict packaging rules** (`CONTRIBUTING.md`): open an issue describing the
   repeated workflow first; one `SKILL.md` with only `name` and `description`
   in the frontmatter; detail in `references/`; scripts only when deterministic
   and tested; evals in `evals/<skill>/`, outside the bundle; no README in a
   skill folder; mark uncertain guidance Experimental or Provisional; run the
   validator (which also scans for secrets) before every commit; every change
   through an issue, branch and PR.
6. **Knowledge, not one-off scripts.** Only generic, safe, tested scripts are
   bundled (archive-to-cloud bundles the verify script, not the upload
   scripts); the rest are written as rebuild notes. (memory title; handoff)
7. **Evals exist but are honest about it.** Scenarios and expected behaviours
   are written; dry-running them on paper found three real gaps before release.
   The design note says plainly: "used on a real build, never systematically
   evaluated."
8. **Lessons are written in the build repo first, then harvested on purpose.**
   Each lesson is classified (core workflow, source-specific,
   destination-specific, validation, known issue, provisional). "One success
   is an anecdote": a core change needs to hold on more than one dataset. The
   skill is updated only when asked. (`learn-and-evolve.md`)
9. **The skill gets corrected by real builds.** The OA-indicators build showed
   the skill was "flatly wrong" (it said no virtual store had rendered in a
   browser) and had a mechanism wrong that would have misdirected a diagnosis.
   Earlier exclusions (browser, CORS) were superseded twice as tested evidence
   arrived. The note also records a process failure: a build's lessons "sat
   uncollected for two weeks", because "someone has to carry it across".
10. **Participants feed it too.** An "Update skill" issue template; the
    tutorial (deck 02) asks users to report lessons.
11. **Skills move with their history.** virtual-icechunk moved from
    nmfs-opensci/agent-skills to ocean-icechunks/ocean-icechunks-skills on
    2026-11-13 with `git-filter-repo`. License chosen for the new home (CC0,
    "not really code"), after checking every commit was Eli's or her agents'.
12. **Installed from the checkout.** `common/skills.txt` lists each skill and
    its repo; `bootstrap.sh` links them into both agents, so a skill follows
    the branch checked out.
13. **Project repos adopt the skill as the authority.** ocean-icechunks/icechunks's
    `CLAUDE.md` names the skill as the authority over that repo's own
    notebooks. (design note)
14. **New skills come from a project's experience.** archive-to-cloud (#4 → #8)
    came out of the PacIOOS, CEFI and icechunks copy work; two more skills
    (FMRC builds, UGRID conventions, #16–#18) are proposed as Experimental.

---

## Not read

- Most PR and issue bodies (only those listed under Sources), and none of the
  code.
- Memory bodies: only memory titles and index lines were read. Claims sourced
  to a "memory title" rest on the one-line summary.
- `~/claude-config/AGENTS.md`, `common/AGENTS.md`, the hook scripts' code,
  and `bootstrap.sh`.
- Other repos where the same patterns may appear (icechunks, hycom,
  cefi-icechunks, gridlook).
