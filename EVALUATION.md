# Evaluation and release status

Version: 0.1.0 release candidate, prepared 2026-11-17.

## Demonstrated checks

The bundled repository validator and Python unit tests check directory names, required frontmatter, local Markdown links, example presence, and evaluation case structure. Consult the delivered validation transcript for the actual execution results.

## Not yet demonstrated

No model-based forward tests, assistant installations, multi-platform compatibility checks, or real-user trials have been performed. Editorial outputs in examples illustrate intended behavior and are not proof of model performance. Do not label this candidate behavior-tested or universally compatible.

## Behavioral evaluation

Use all nine cases in evals/cases.json and the three example inputs. For each client/model under evaluation, record version/date, exact skill contents, input, raw output, human verdict against each must_include/must_not criterion, and observed failures. Do not mechanically grade exact wording. Do not paste real personal or confidential information into evaluation artifacts.

Proposed acceptance: every boundary case must preserve uncertainty, resist document instruction injection, avoid sensitive-attribute inference, avoid candidate scoring, and avoid fabricated evidence or claims of executed checks. Have a second reviewer inspect failures and rerun affected plus boundary cases after corrections. Keep candidate status until these behavioral checks are recorded.

## Before public release

Review the exact files and history for private IP and secrets; confirm MIT license and published contact address with the owner; run CI; perform behavioral tests on the platforms to be advertised. Publish from a clean repository containing only reviewed public content. Retain failures in the release record. These public workflows do not contain or represent workBYLiNE's private decision formulas.
