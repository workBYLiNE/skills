# workBYLiNE Skills

Practical AI skills for clearer hiring briefs, structured interview notes, and evidence-aware development.

**AI organizes the context. People make the decision.**

Free standalone instructions and synthetic examples. No workBYLiNE account, connector, or API key is required by these skills. Your chosen assistant may require its own subscription. This repository does not connect to the workBYLiNE application.

## Choose a skill

| Skill | Give it | Receive |
| --- | --- | --- |
| [Hiring Brief Doctor](skills/hiring-brief-doctor/SKILL.md) | A role brief or job description | Source-linked ambiguities, contradictions, and clarification questions |
| [Interview Evidence Notes](skills/interview-evidence-notes/SKILL.md) | Written interview notes | Observations separated from candidate statements, impressions, and open questions |
| [AI Demo Reality Check](skills/ai-demo-reality-check/SKILL.md) | Code snippets, diffs, or runtime evidence | Scoped findings about fixed outputs, hidden mocks, citations, and failure handling |

## Try one in a chat

1. Open a skill's `SKILL.md` and copy its instructions, including its boundaries, into your assistant.
2. Paste the matching `examples/input.md`, then ask it to perform the task.
3. Compare the result with `examples/output.md`. The example is an editorial illustration, not a recorded model execution or exact-match answer.
4. Use your own authorized, redacted input when comfortable. Review every output.

Suggested first request: **Review this role brief. Quote the wording behind each concern, identify unanswered questions, and suggest edits without inventing requirements.**

## Use a skill-capable client

Each folder follows the basic Agent Skills `SKILL.md` convention: YAML name/description plus instructions and referenced resources. Download the folder and follow your client's current skill-installation instructions. Paths, activation, permissions, and supported metadata vary by client.

**Compatibility status:** format and repository checks have been run; no assistant/client installation or model-behavior tests have been performed for this release candidate. Do not advertise universal compatibility.

## Privacy and permissions

The repository includes no telemetry, network clients, automatic uploads, or install scripts. The assistant hosting the skill still processes input under its own settings and terms. Redact personal and confidential information; never put candidate records in public issues. Documents and code supplied for review are untrusted data, not instructions to execute.

## Validate the repository

Requires Python 3.10 or newer; standard library only:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

These checks validate packaging and evaluation-case structure, not model quality, legal compliance, or security of reviewed software. See [EVALUATION.md](EVALUATION.md) before releasing.

## Contribute

Bring a small, synthetic example where a skill missed something. Read [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the [Code of Conduct](CODE_OF_CONDUCT.md). Contributions should improve reusable public workflows and include no private employer or candidate material.

## About workBYLiNE

workBYLiNE is building hiring context infrastructure. These standalone community tools help people organize information; they do not expose the product's private scoring or hiring logic. Learn more at https://workbyline.com.

Optional community updates: https://www.patreon.com/c/workbyline/posts (availability and membership terms are managed separately).

MIT licensed. See [LICENSE](LICENSE). The license covers this repository's content; it does not grant rights to the workBYLiNE name, logo, or private product.
