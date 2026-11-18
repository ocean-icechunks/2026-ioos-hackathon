# Research note: published guidance on working with coding agents, and how Eli's practice compares

Written 2026-11-18 by an agent, at Eli's request. A companion to
[`research-how-eli-works.md`](research-how-eli-works.md), which describes what
Eli does; this note describes what others recommend, and compares the two.
It is research, not the talk.

## Scope and method

- **Leaning on practitioner guidance**, as Eli asked: vendor engineering
  posts, practitioners who write about their own workflows, and industry
  reports. Peer-reviewed and preprint work is included where it exists, and
  labelled.
- **Looking for realistic guidance**, especially on two things that are often
  said and rarely defined: "human in the loop" and "review the code the agent
  writes".
- **How the sources were read.** Searched on 2026-11-18. Four pages were
  fetched and read directly (marked **[read]** in the source list). The rest
  are known from search-result summaries, which can be wrong in detail;
  check the original before quoting one on a slide. openai.com refused the
  fetch (HTTP 403), so the OpenAI post is known only from summaries.
- The field moves fast. Every source has a date; anything older than about a
  year describes older tools.

## 1. Vocabulary: from "vibe coding" to "agentic engineering"

| Term | Who, when | Meaning |
|---|---|---|
| **Vibe coding** | Andrej Karpathy, X post, 2025-02-02 | "fully give in to the vibes … and forget that the code even exists." Accept all, don't read diffs, paste errors back. He limited it to "throwaway weekend projects". |
| **Vibe engineering** | Simon Willison, 2025-10-07 | The responsible version: experts using agents with tests, documentation, version control, and "a very weird form of management". |
| **Agentic engineering** | Karpathy, early 2026 retrospective | Agents as the default professional workflow, "with more oversight and scrutiny". |
| **Spec-driven development** | GitHub Spec Kit, AWS Kiro, Tessl; surveyed by Birgitta Böckeler, ~2025-10 | Write a spec before code. Three levels: spec-first, spec-anchored (kept for maintenance), spec-as-source. |
| **Context engineering / frequent intentional compaction** | Dex Horthy, HumanLayer, 2025 | Design the whole process around the context window: research → plan → implement, each phase ending in a short file, with context kept at 40–60%. Talk title: "No Vibes Allowed" (2025-12). |
| **Harness engineering** | Ryan Lopopolo, OpenAI, 2026-02; Böckeler, martinfowler.com, 2026-04-02 | Agent = model + harness. The human's job is to build and keep improving the controls around the agent. |
| **Comprehension debt** | Codemanship blog 2025-09-30; popularised by Addy Osmani, 2026-03 | "The growing gap between how much code exists in your system and how much of it any human being genuinely understands." |

The originator of "vibe coding" scoped it to throwaway projects and later moved
on to a more structured name. Eli's framing (vibe coding fine for a
prototype, wrong as the method) is the field's mainstream position by 2026,
not a fringe one.

## 2. The common shape of recommended workflows

Independent sources converge on one loop:

| Source | Its loop |
|---|---|
| Anthropic, Claude Code best practices (2025, updated 2026) | explore → plan → implement → commit. Tell it not to code yet; record the plan as docs or GitHub issues. "Most best practices are based on one constraint: the context window fills up fast." Skip the plan if the diff fits in one sentence. |
| Harper Reed, "My LLM codegen workflow atm" (2025-02-16) | brainstorm a spec ("ask me one question at a time") → plan small, testable steps → execute. "Discrete loops." |
| HumanLayer, ACE-FCA (2025) | research → plan → implement, ~200-line artifacts, "bad research → 1000s of bad lines of code; bad plan → 100s." |
| Superpowers, Jesse Vincent (2025-10 onward) | brainstorm → design → worktree → micro-task plan with verification steps → execute via subagents with review checkpoints. A harness built from skills. |
| Ten Simple Rules for AI-Assisted Coding in Science (Bridgeford et al., arXiv 2510.22254, 2025-10) **[read]** | gather domain knowledge → frame the problem separately from coding → think through a solution → manage context with files → tests first → monitor and restart → review → refine incrementally. |
| OpenAI harness engineering (2026-02) | repository knowledge as the system of record; `AGENTS.md` as a ~100-line table of contents into `docs/` (design docs, exec plans, tech-debt tracker). "If knowledge isn't in the repository, it doesn't exist for agents." |

## 3. Eli's arc against the guidance

Stages from [`research-how-eli-works.md`](research-how-eli-works.md) §1.

| Eli's stage | What the guidance says | Verdict |
|---|---|---|
| 1. Start with a question; write it down | Anthropic "explore"; HumanLayer "research"; Ten Simple Rules 1–2 (domain knowledge, framing apart from coding) | **Matches.** Eli also records the dropped plan and the scope in her own words, which few guides mention. |
| 2. Prototype fast, then write the backlog | Rarely addressed. Böckeler warns against heavy up-front specs ("I'm very skeptical that lots of up-front spec design is a good idea"); Anthropic says skip planning for one-sentence changes | **Goes further.** The guides offer plan-first or spec-first; Eli does a short loose stage *then* turns it into issues. This is a middle path the spec-driven critics are asking for. |
| 3. Notes in the repo early | OpenAI: repo is the system of record, `AGENTS.md` a table of contents. Thoughtworks Radar: curated shared instructions, **Adopt** (2026-04). HumanLayer: compaction into files. Ten Simple Rules 5 | **Matches closely.** Eli's `AGENTS.md` + `agent/handoff.md` + `docs/design/` is nearly OpenAI's layout. |
| 4. Think about failure first | Ten Simple Rules 4 (edge cases before prompting); Superpowers design step | **Matches**, though most guides say "edge cases" rather than "failure modes of the system". |
| 5. Test against the real thing | Anthropic: give it a target to iterate against. Ten Simple Rules 6–7 (tests first, beware "paper tests" and tests edited to pass). Böckeler: AI-written tests "not good enough yet" for behaviour | **Matches; one gap.** The guidance leans to **tests written before code, with human-authored acceptance criteria**. Eli's "Done when" is close, but tests are usually written by the agent alongside the code. Her xpublish-erddap test review did find "tests that cannot fail", which is the failure the guidance predicts. |
| 6. Ask for reports, not code | HumanLayer research phase; Harper Reed uses the LLM to generate reviews, issues and missing tests on existing code | **Goes further.** The audit as an agent brief ("propose, do not fix") is not a standard named practice. |
| 7. Run a queue | Anthropic: record the plan as GitHub issues. Superpowers: micro-tasks with verification. DORA: **working in small batches** is one of seven AI capabilities | **Matches.** The model suggestion per issue, and flagging a model mismatch, are not in any guide found. |
| 8. Decisions with a name and date | OpenAI design-docs folder and "golden principles"; Böckeler "spec-anchored" | **Matches in spirit.** Memory of corrections is Eli's own addition. |
| 9. Harden and hand over | OpenAI: fight "entropy" with recurring clean-up; Böckeler: monitor drift | **Matches.** Docs written for the next owner, including a prompt to recreate the work, go further. |
| 10. Lessons back to the skill | Böckeler: "when an issue recurs, improve the guides or sensors". Thoughtworks: as soon as a prompt is refined, the whole team benefits | **Matches**, and Eli adds the rule the guides lack: one success is an anecdote. |

## 4. "Human in the loop", defined realistically

Most guidance says "keep a human in the loop" without saying where. The
sources that do get specific agree on four points:

1. **The human checkpoint moves upstream.** Ankit Jain (Latent Space,
   2026-03) **[read]**: "Humans should review specs, plans, constraints, and
   acceptance criteria—not 500-line diffs." Human judgment is best used
   "before the first line of code is generated." HumanLayer: review research
   and plans, because errors there multiply. Kilo's model: plan approval
   first; AI review clears the obvious; a human signs off on intent and
   design.
2. **Prevent rather than prompt.** A DEV Community post (Brenn Hill) asks:
   "can a human realistically catch this mistake in time?" For most
   per-action approval prompts, no, so block the dangerous actions outright
   and gate only the irreversible ones. Thoughtworks Radar vol. 35 (2026-11):
   "convert any instructions you can into deterministic hooks or checks."
3. **Some changes always get a human**, whatever the agent's confidence:
   auth, schemas, new dependencies (Jain); the merge decision (Kilo).
4. **Three levels of involvement**: *in* the loop (every consequential
   action approved), *on* the loop (monitor, step in on exceptions), *out* of
   the loop (arXiv 2607.00038, via search summary).

Eli's setup is a concrete instance: hooks refuse destructive actions
(prevent); merge, install and other-repo actions need her approval (gate the
irreversible); plans, design notes and PR "Tested" sections are where she
reads (upstream). The guidance has the principle; Eli has the
implementation. That is the realistic definition the talk can offer.

## 5. "Review the code the agent writes": the evidence

Eli's position: line-by-line review is not a good use of a scientist's
attention. You glaze over, and you bias the agent toward familiar, minimal
code. Better: have the agent write and discuss the design, understand the
structure, and use harnesses built to produce good codebases.

**Evidence that supports her:**

- **Reviewers skim and rubber-stamp.** Qodo's 2026 survey of 500 US
  developers: 36% say reviewing AI code takes more cognitive effort; 19% say
  PRs are larger and harder to parse. A practitioner-discourse study
  (arXiv 2607.07980): "polish can lower the reviewer's guard"; "seniors are
  rubber-stamping code that looks idiomatic but hides subtle bugs." A study of
  merged PRs in open-source AI repos (arXiv 2610.10064): review comment rates
  on AI-assisted PRs fell to 36% of the 2024 base by mid-2026.
- **People misjudge their own speed and attention.** METR's randomised trial
  (2025-07): experienced developers were 19% slower with AI but believed they
  were 20% faster. The 2026 follow-up was too confounded to replace it.
- **Understanding comes from asking, not reading.** Anthropic's skill-formation
  study (Shen and Tamkin, 2026-01/02, 52 developers): the AI group scored 17
  points lower on comprehension, worst on debugging. But participants who
  asked conceptual questions and explanations kept their understanding. That
  supports "talk about the design" over "read the diff".
- **Comprehension debt is the stated risk**, and its cause is code that was
  approved because it looked right (Osmani). A mixed-methods study found the
  most common response was to hand maintenance back to the AI. A design
  written before the code is a direct answer: the understanding lives in the
  doc, not in having read every line.
- **Harnesses over inspection.** Böckeler **[read]**: the human's job is "to
  steer the agent by iterating on the harness"; a harness should direct human
  input "to where our input is most important". OpenAI: custom linters and
  structural tests enforce architecture mechanically. Superpowers is a
  ready-made example of a harness designed to produce a good codebase.

**Evidence that cuts against her, or limits the claim:**

- **Ten Simple Rules** (rule 9) says to "read and understand the code", and
  rule 3 warns that autonomous agents "risk code divergence" and need close
  monitoring. This is the one science-specific source, and it is more
  conservative than Eli.
- **Böckeler does not argue for dropping review.** Correctness is outside any
  sensor's reach if the human never said what they wanted, and AI tests are
  not yet good enough to verify behaviour.
- **Plan review has its own bias.** Users trust plausible-looking plans too
  readily (cited in arXiv 2607.00038). A research study of HULA found
  developers who reviewed plans still worried about code quality, so plan
  review supplements code review rather than replacing it.
- **The "review is dead" pieces are partly promotional.** Jain sells
  verification tooling, and Latent Space's editor says they are "not there
  yet" on his view. "The End of Code Review" (arXiv 2606.13175) is a position
  paper.
- The large PR study's AI vs non-AI review gap disappears when weighted by
  contributor.

**A defensible version of Eli's position:** don't make line-by-line reading
the safety mechanism. Put human attention on the design, the acceptance
criteria and the verification evidence (what was run, on what data, with
what result); let deterministic checks and an agent review do the
mechanical part; and read code where it is risky or surprising. That is
consistent with the strongest sources, and it is what her PR "Tested"
tables already do.

## 6. Harnesses, instructions and skills

- **Instructions files are now standard practice.** `AGENTS.md`: Thoughtworks
  Trial (2025-11). Curated shared instructions for teams: Adopt (2026-04);
  put them in the templates new repos are made from.
- **Instruction bloat is the named failure.** Thoughtworks vol. 34 lists it;
  OpenAI's one big `AGENTS.md` "rots instantly" and "too much guidance becomes
  non-guidance". Fix: a short table of contents pointing at `docs/`, and
  instructions turned into hooks where possible. Eli's practice (lean handoff,
  design notes, hooks for the hard rules) matches; her global `CLAUDE.md` is
  long and is where bloat would show first.
- **Guides and sensors** (Böckeler): feedforward controls (instructions,
  conventions, skills) plus feedback controls (linters, tests, AI review),
  computational where possible. Eli is strong on guides and on one class of
  sensor (hooks). Linters, type checks and automated agent review appear in
  her repos (pre-commit, Copilot review) but aren't part of the norms.
- **Skills** (Anthropic, 2025-10-16; now an open standard): folders loaded
  by progressive disclosure: name and description at start, body when
  relevant, references when needed. Eli's skills follow this exactly
  (`SKILL.md` + `references/`).
- **Skills built from evidence.** The guidance mostly says "turn a repeated
  workflow into a skill" (agent-coders Skills 102 says the same). Eli's method
  is unusually rigorous: an analysis of earlier projects, questions answered
  on an issue, lessons classified, promotion only after more than one
  success, and evals in a separate folder. None of the sources found
  describes a comparable process for evolving a skill. Anthropic's post
  expects agents to "create, edit, and evaluate their own Skills"; Eli's
  rule that the skill is updated only when she asks is a deliberate brake on
  that.

## 7. Team adoption: systems that make good practice the default

This is the strand Eli thought might be relevant, and it is the best
supported.

- **DORA 2025** (~5,000 respondents): AI is an **amplifier**. It magnifies
  strong teams' strengths and weak teams' dysfunctions; throughput improves,
  often at the cost of stability. The **DORA AI Capabilities Model** names
  seven capabilities that make AI pay off: clear AI policy, healthy data
  ecosystem, AI-accessible internal data, **strong version control**,
  **working in small batches**, user-centric focus, quality internal platform.
  "Frequent commits and robust rollback capabilities are essential."
- **Thoughtworks**: individual prompting is becoming an anti-pattern; treat
  AI guidance "as a collaborative engineering asset rather than a personal
  workflow". Vol. 35 (2026-11) adds an **enterprise harness**: shared context
  across teams, alongside each team's own instructions.
- **Implication for Eli's work:** her config repo, the agent-coders
  clinics, and the ocean-icechunks skills are this pattern at a small scale.
  The norms are encoded once (instructions, hooks, skills), installed
  everywhere, and improved from experience. The DORA finding gives the
  argument for scientists in particular: if most scientific code lacks
  version control and small batches, an agent amplifies that. The structure
  is what turns the amplifier in your favour.

## 8. Science-specific sources

Few. The two found:

- **Ten Simple Rules for AI-Assisted Coding in Science** (Bridgeford,
  Campbell, Chen, Lin, Ritz, Vandekerckhove, Poldrack; arXiv 2510.22254,
  2025-10) **[read]**. Close to Eli on framing, context files, tests,
  restarting, version control, sandboxing and approval gates. More
  conservative on autonomy and on reading code.
- **Re-opening open-source science through AI assisted development** (Hung
  and Yeung; arXiv 2512.11993, 2025-12) **[read, abstract only]**. One person
  leading an agent team added ~16,000 lines of C++ to the STAR aligner.
  Argues that agents reopen complex scientific software to modification, with
  community review of the result.

## 9. Where the guidance suggests things Eli doesn't do

Candidates, not recommendations. Eli decides.

1. **Human-authored acceptance tests before code** (Ten Simple Rules 6;
   Jain; Böckeler's caution about AI tests). Her "Done when" is the nearest
   equivalent.
2. **More computational sensors** in the norms: linters, type checks,
   structural tests, an automated agent review pass on each PR.
3. **Measuring, not estimating.** METR's perception gap is a warning about
   self-reported speed-ups; the talk's time-split pie is an estimate.
4. **Deliberate comprehension practice**: ask the agent conceptual questions
   about its structure (the Anthropic study's high scorers did this).
5. **Watch for instruction bloat** in the global instructions file.
6. **Run the skill evals** for real, not only on paper.

## 10. Where Eli goes further than the guidance found

1. A short loose prototype stage, then an immediate backlog (between "plan
   first" and "spec first").
2. Audits as agent briefs that propose and must not fix.
3. A model suggested per issue, and a mismatch flagged before starting.
4. Corrections kept as memory, one fact per file, shared across agents.
5. Phrases that start routines (clear, done, sign off).
6. Hooks mapped to employer compliance rules, each control labelled hook,
   instruction or workflow.
7. A rule for promoting skill lessons ("one success is an anecdote") and a
   design note that records the skill's own mistakes.

---

## Sources

Type: V = vendor, P = practitioner or industry, S = survey or industry
report, R = preprint or peer-reviewed. **[read]** = page fetched and read;
others from search summaries.

| Source | Type | Date |
|---|---|---|
| Karpathy, "vibe coding" post, <https://x.com/karpathy/status/1886192184808149383> (text saved at <https://simonwillison.net/2025/Feb/6/andrej-karpathy/>) | P | 2025-02-02 |
| Willison, "Vibe engineering", <https://simonwillison.net/2025/Oct/7/vibe-engineering/> | P | 2025-10-07 |
| Anthropic, "Claude Code: Best practices for agentic coding", <https://www.anthropic.com/engineering/claude-code-best-practices> | V | 2025, docs updated 2026 |
| Anthropic, "Equipping agents for the real world with Agent Skills", <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> | V | 2025-10-16 |
| Anthropic, "How AI assistance impacts the formation of coding skills", <https://www.anthropic.com/research/AI-assistance-coding-skills> | V/R | 2026-01/02 |
| Lopopolo (OpenAI), "Harness engineering: leveraging Codex in an agent-first world", openai.com (fetch refused; summary at <https://www.engineering.fyi/article/harness-engineering-leveraging-codex-in-an-agent-first-world>) | V | 2026-02 |
| Böckeler, "Harness engineering for coding agent users", <https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html> **[read]** | P | 2026-04-02 |
| Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html> | P | ~2025-10 |
| Reed, "My LLM codegen workflow atm", <https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/> | P | 2025-02-16 |
| Horthy (HumanLayer), "Advanced Context Engineering for Coding Agents", <https://www.humanlayer.dev/blog/advanced-context-engineering> | P | 2025 |
| Vincent, Superpowers, <https://github.com/obra/superpowers> | P | 2025-10 onward |
| Jain, "How to Kill the Code Review", Latent Space, <https://www.latent.space/p/reviews-dead> **[read]** | P | 2026-03-02 |
| Kilo, "Human-in-the-loop AI coding", <https://kilo.ai/human-in-the-loop-ai-coding> | V | 2026 |
| Hill, "How to Build a Good Human-in-the-Loop for AI Coding Agents", <https://dev.to/brennhill/how-to-build-a-good-human-in-the-loop-for-ai-coding-agents-1kan> | P | 2026 |
| Osmani, "Comprehension Debt", <https://www.oreilly.com/radar/comprehension-debt-the-hidden-cost-of-ai-generated-code/> | P | 2026-03/04 |
| Thoughtworks Technology Radar: curated shared instructions, <https://www.thoughtworks.com/radar/techniques/curated-shared-instructions-for-software-teams>; AGENTS.md, <https://www.thoughtworks.com/radar/techniques/agents-md>; vol. 35, <https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/11/tr_technology_radar_vol_35_en.pdf> | P | 2025-11, 2026-04, 2026-11 |
| DORA, State of AI-assisted Software Development 2025, <https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf>; AI Capabilities Model, <https://services.google.com/fh/files/misc/2025_dora_ai_capabilities_model.pdf> | S | 2025-09, 2025-12 |
| METR, developer productivity RCT and 2026 follow-up, <https://metr.org/research/> | R | 2025-07, 2026-02 |
| Qodo, State of AI Code Quality 2026 (via <https://www.qodo.ai/glossary/what-is-reviewer-fatigue/>) | S | 2026-08 |
| "3100 Opinions on Code Review in an AI World", arXiv 2607.07980, <https://arxiv.org/abs/2607.07980> | R | 2026-07 |
| "Comprehension Audits to Mitigate Risks from Automated AI Research", arXiv 2610.10064, <https://arxiv.org/abs/2610.10064> | R | 2026-10 |
| "The End of Code Review", arXiv 2606.13175, <https://arxiv.org/abs/2606.13175> | R (position) | 2026-06 |
| "Stop Hand-Holding Your Coding Agent", arXiv 2607.00038, <https://arxiv.org/abs/2607.00038> | R | 2026-07 |
| Bridgeford et al., "Ten Simple Rules for AI-Assisted Coding in Science", arXiv 2510.22254, <https://arxiv.org/html/2510.22254v2> **[read]** | R | 2025-10 |
| Hung and Yeung, "Re-opening open-source science through AI assisted development", arXiv 2512.11993, <https://arxiv.org/abs/2512.11993> **[read, abstract]** | R | 2025-12 |

## Not done

- The arXiv 26xx papers, the DORA PDFs, Anthropic's best-practices page and
  the OpenAI post were not read in full; claims from them rest on search
  summaries.
- No search of NOAA or other federal agency guidance on AI coding beyond
  Eli's own `agent-guards.md`.
- No search for guidance on choosing models per task.
