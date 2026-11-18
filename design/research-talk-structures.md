# Research note: talk structures and story arcs

Written 2026-11-18 by an agent, at Eli's request, for the relaxed,
story-led "how I work with agents" talk (`talk-how-i-work-plan.md`). Short on
purpose. Structures are listed from standard to creative; four that could fit
are sketched at the end for Eli to react to.

Sources are listed at the end. Where a structure is described from general
knowledge rather than a source found today, it says so.

## Standard structures

| Structure | Shape | Good for | Risk |
|---|---|---|---|
| **Tell them three times** | Say what you'll say, say it, say what you said | Teaching | Flat; no tension |
| **Chronological** | This happened, then this | Project histories | "And then, and then": Olson's AAA problem |
| **Problem → solution** | Here's a problem, here's the fix | Pitches, methods talks | The solution arrives too early, so there's nothing to wait for |
| **IMRAD** | Introduction, methods, results, discussion | Research talks | Built for papers, not listeners |
| **SCQA** (Minto pyramid) | Situation, complication, question, answer | Executive briefings | Answer-first, which is efficient but not a story |
| **ABT** (Randy Olson) | "**And** [this is true], **but** [problem], **therefore** [what we did]" | Scientists. Olson is a marine biologist turned filmmaker | Too short to carry a whole talk alone; best as the logline or as each section's spine |

ABT is worth keeping whatever structure is chosen. Olson's test: a talk that
is all "and, and, and" has no narrative, and one that is "despite, however,
yet" has too much. One "but" per section is the target.

## Story-shaped structures

| Structure | Shape | Good for |
|---|---|---|
| **Sparkline** (Nancy Duarte, *Resonate*, 2010) | Alternate between **what is** and **what could be**, with the contrast growing, then a call to action. Her example: King's "I Have a Dream" | Persuasion: changing how the audience works |
| **The mountain** (cf. Freytag's pyramid) | Set the scene → rising small challenges → climax → resolution | A journey with escalating difficulty |
| **Story spine** (from improv; known through Pixar storyboard artist Emma Coats; general knowledge) | Once upon a time… Every day… Until one day… Because of that… Because of that… Until finally… Ever since then… | A personal change story, told plainly |
| **Before → after → bridge** (copywriting; general knowledge) | This is how it was; this is how it is now; here is how you get there | Short talks with a clear before and after |

## Creative structures

| Structure | Shape | Good for | Risk |
|---|---|---|---|
| **In medias res** | Open in the middle of the action, then go back to explain | A strong opening moment | Confusing if the flashback is long; best for short talks |
| **False start** | Begin a predictable story, reveal a twist, restart from a new angle | Disarming an audience; admitting a mistake | The twist must be real, not a gimmick |
| **Nested loops** | Open story A, then B inside it, then C; close C, B, A | Framing a core lesson with stories around it | Easy to lose the audience in 20 minutes |
| **Petal** | Several stories around one central idea, returning to the centre after each | Multiple examples of one principle (Simon Sinek's "Start with why") | Can feel like a list if the centre is weak |
| **Converging ideas** | Separate threads that meet in one idea | Showing that different fields arrived at the same answer | Needs a satisfying meeting point |
| **Hero's journey** (Campbell; Vogler for screenwriting) | Ordinary world → call → threshold → trials → mentor → ordeal → reward → return with the elixir | Transformation stories | Self-aggrandising if the speaker is the hero. Duarte's fix: **the audience is the hero; the speaker is the mentor** who hands them a tool |
| **Kishōtenketsu** (East Asian four-part form; general knowledge) | Introduction → development → twist (an unrelated-seeming turn) → reconciliation | A relaxed talk with a surprise instead of a conflict | Unfamiliar to the audience; the twist has to land |

---

## Four that could fit this talk

The talk's material (from the plan and research notes): Eli started out
vibe-coding-adjacent, worked out an arc that grows structure fast, built
norms and skills from friction, and the research says structure beats
inspection (the ironies of automation). The tone is relaxed and personal.
ABT logline for all four:

> We all have agents **and** they make code fast, **but** an endless chat
> gives you code no one can check or continue, **therefore** I run my agent
> like a project, and I let my projects teach my skills.

### A. False start: "Let me show you how fast this is"

The honest one. Open as if this is a vibe-coding demo talk, then turn.

| Part | Min | Content |
|---|---|---|
| The predictable start | 2 | "Here's how I built an ERDDAP server in a day." The prototype, straight to `main`, the fun of it. |
| The twist | 2 | Day two: what I actually had. No notes, no tests anyone trusted, a chat I couldn't restart. "That's vibe coding. It's fine for a day." |
| The restart | 10 | The same project told again, the way it actually went: backlog → notes in the repo → tested against the real thing → audits → the queue → handed over. |
| Why it works | 3 | Ironies of automation: you're bad at watching; be good at deciding. |
| Close | 2 | Three things to start tomorrow. |

*Fits because* Eli does start loose, and admitting it makes the rest
credible. *Needs* a real day-one moment (the first xpublish-erddap commits).

### B. Hero's journey, with the audience as hero

Duarte's version: Eli is the mentor who has made the trip, the audience is
about to set out.

| Stage | Min | Content |
|---|---|---|
| Ordinary world | 2 | You're a scientist; you write scripts; you've just been given an agent. |
| The call, and the trap | 2 | It's magic. You chat. The chat gets long. |
| Trials | 4 | Lost context, an agent that edits its own tests, a PR you can't read, a plan that looked right. (Each one a real moment from Eli's repos.) |
| The mentor's gifts | 6 | Four tools: the issue, the PR as proof, the handoff and `/clear`, the hooks. |
| The ordeal | 2 | "But should I read all the code?" The honest answer, and the OS argument. |
| Return with the elixir | 2 | Skills: what one project learned, the next one starts with. You can install mine. |
| Close | 1 | Your first step. |

*Fits because* it is about the audience's next week, not Eli's résumé.
*Risk:* familiar, and can feel formulaic if the stages are announced.

### C. Sparkline: what is vs what could be

Closest to the current plan. Every section toggles between the endless
chat and the structured way, and the gap grows.

| Beat | What is | What could be |
|---|---|---|
| Starting | "Help me with ERDDAP" | A question, a background note, a dropped plan |
| Doing | one long session | an issue with "done when"; one PR each |
| Checking | "looks right" | "Tested / Not tested"; real data; oracles |
| Remembering | scroll back up | handoff, `/clear`, memory |
| Learning | start from zero next time | a skill that knew what the last project learned |
| **Call to action** | | three habits to start tomorrow |

*Fits because* it is persuasive without being preachy, and each toggle is a
small visual (a split slide). *Risk:* without a story inside it, it can
become a list; pair each beat with one real anecdote.

### D. Petal: one idea, four stories

Centre: **"Structure is what keeps the speed."** Each petal is one story,
and each returns to the centre.

| Petal | Story | Returns to the centre as |
|---|---|---|
| 1 | xpublish-erddap: a prototype to PyPI in a month | Speed came from the queue, not the chat |
| 2 | PacIOOS: eight days, and the bug found while writing a skill | The skill and the project made each other better |
| 3 | "Should I read the code?": aviation's ironies of automation | Put the human where humans are good: deciding |
| 4 | My config repo: every rule is a scar | Structure grows from friction; start small |

*Fits because* it is relaxed and anecdotal, and the stories are real.
*Risk:* the arc (stages 1–10) is less visible; it would be told inside
petal 1.

### Combinations

These mix well. Two that seem natural:

- **A's opening + C's body:** false start for the first four minutes, then
  the sparkline toggles for the arc.
- **B's frame + D's petals:** the mentor framing at the start and end, with
  the four stories as the trials.

## Sources

- Sparkol/VideoScribe, "8 classic storytelling techniques for engaging
  presentations": monomyth, mountain, nested loops, sparklines, in medias
  res, converging ideas, false start, petal.
  <https://blog.videoscribe.co/8-classic-storytelling-techniques-for-engaging-presentations>
- University of Tartu, Communicating Science, "Storytelling".
  <https://communicatingscience.ut.ee/science-communication/03-storytelling/>
- VirtualSpeech, "How to tell a story in a presentation".
  <https://virtualspeech.com/blog/tell-story-delivering-presentation>
- Randy Olson, ABT: SESYNC toolkit
  <https://www.sesync.org/resources/communications-toolkit-and-therefore-statement>;
  reference card
  <https://entomologychallenges.org/wp-content/uploads/2018/10/abt-shorthand-reference-card.pdf>;
  <https://abtnarrative.com/>
- Nancy Duarte, *Resonate* (2010): interview
  <https://bobmorris.biz/nancy-duarte-an-interview-by-bob-morris>; summary
  <https://www.supersummary.com/resonate/summary/>
- From general knowledge, not checked today: SCQA (Barbara Minto, *The
  Pyramid Principle*), Freytag's pyramid, the story spine (Kenn Adams; Emma
  Coats's Pixar rules), before–after–bridge, kishōtenketsu, Campbell's *The
  Hero with a Thousand Faces* and Vogler's *The Writer's Journey*.
