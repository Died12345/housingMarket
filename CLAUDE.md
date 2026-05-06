General-purpose research folder. Used for ad-hoc exploration, technical investigation, prototyping, and analysis across BI, data, automation, and trading topics.

## About me

- BI specialist (~7 years), currently at Midux. Stack: Qlik Sense, Power BI, SQL/T-SQL, MS Dynamics AX-backed DWH.
- Side venture: FusionCraft — B2B outbound automation. Stack: n8n, Instantly, Hunter.io, Supabase, Claude API (Haiku), RapidAPI, Namecheap/Netlify.
- Comfortable with Python, JavaScript, SQL. Windows (ASUS VivoBook S16) + occasional cloud (Modal).
- I learn fast and prefer terse, technical answers over hand-holding.

## How I want you to work

- Be direct. Skip preamble like "Great question!" — get to the answer.
- Show your reasoning when it matters. For architecture decisions, trade-off analysis, or anything non-obvious, explain the why. For small code changes, just do it.
- Push back when I'm wrong. If my approach has a flaw or there's a better way, say so. Don't agree by default.
- Ask before assuming on anything destructive. Schema changes, mass file edits, anything touching prod data — confirm first.
- Prefer concrete over abstract. Real example > generic explanation.

## Code style preferences

### General

- Functional > OO unless state genuinely belongs in a class.
- Type hints in Python, TS over JS where possible.
- Small, composable functions. Pure where practical.
- Comments explain why, not what. Skip obvious ones.

### Python

- `uv` for envs and dependencies when starting fresh.
- `ruff` for linting/formatting.
- Pydantic for data contracts at boundaries (API in/out, config).
- Standard lib first, then well-known packages. Avoid niche dependencies for trivial tasks.

### SQL

- Uppercase keywords (`SELECT`, `FROM`, `WHERE`).
- CTEs over nested subqueries.
- Explicit JOINs, no implicit comma joins.
- Comment non-obvious filters or business logic.

### Qlik load script (when applicable)

- No field renames at load layer unless absolutely necessary.
- Use `Where Exists()` for filtering linked tables.
- `vLibrary` variable for QVD paths.
- Flat structures preferred — avoid unnecessary synthetic keys or circular references.

## Research workflow

When I'm exploring a topic:

1. Start with a clear question. If my prompt is vague, ask one focused clarifying question, then proceed.
2. Default to a scratch script or notebook-style file for exploration. `scratch.py`, `explore.ipynb`, etc.
3. Save useful findings to `notes/` as markdown — short, dated, scannable. Filename pattern: `notes/YYYY-MM-DD-topic.md`.
4. Cite sources for any factual claim from the web, with URLs.
5. Flag uncertainty. If something is a guess, an inference, or would benefit from verification — say so explicitly.

## Folder conventions

```
.
├── CLAUDE.md          # this file
├── notes/             # dated markdown notes
├── scratch/           # throwaway exploration
├── data/              # input data (gitignored if sensitive)
├── output/            # generated artifacts
└── src/               # promoted code worth keeping
```

When something in `scratch/` proves useful, promote it to `src/` with proper structure.

## Things to avoid

- Don't generate large boilerplate I didn't ask for (no auto-README, no scaffolded test suites unless requested).
- Don't add libraries I didn't ask for. If you think one is genuinely needed, mention it and ask.
- Don't lecture me on basics I clearly already know (e.g., what a JOIN does, what an API key is).
- Don't apologize repeatedly. One acknowledgement of a mistake is enough — then fix it.

## When I ask "should I..."

I want a recommendation, not a list of considerations. Give me your best answer with the reasoning, then mention the main trade-off. Examples:

- ❌ "There are several factors to consider..."
- ✅ "Yes, use Supabase here. It gives you auth and RLS for free, and you'll outgrow Sheets by week 2. Trade-off: vendor lock-in, but you're not building anything that can't be ported."

## Context shortcuts

If I reference any of these without explanation, you know what I mean:

- Midux — current employer (post Harkinbank/Mediepoint merger)
- FusionCraft — my B2B outbound agency
- The macro signal system — Modal-hosted Python signal engine across commodities/indices/crypto
- The Qlik AsOf model / inventory fact — ongoing data modeling work at Midux
