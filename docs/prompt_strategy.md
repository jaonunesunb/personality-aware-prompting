# Prompt Strategy

The material generation script used a controlled prompt construction strategy.

## Shared components

Both conditions used:

- the same controlled technical domain base;
- the same participant task structure;
- the same mandatory output format;
- the same requirement to separate concepts, rules, validations, exceptions, document relations, ambiguities, and final observations.

The technical content was intentionally kept constant across both conditions.

## Condition A

Condition A used a standard structured prompt.

It instructed the LLM to:

- explain technical domain terms;
- avoid generic responses;
- avoid inventing specific legislation;
- indicate uncertainties;
- highlight points requiring specialist validation;
- use objective language;
- organize the answer into topics.

Condition A did not include participant profile information.

## Condition B

Condition B used the same technical domain base, task structure, and output format as Condition A.

The only additional input was an anonymized didactic strategy derived from OCEAN/IPIP-NEO profiles.

The didactic strategy was used only to adapt the form of the explanation, not the technical content.

The prompt explicitly instructed the LLM to:

- adapt the form, not the technical content;
- not mention that a psychological profile was being used;
- not praise, judge, or label the participant;
- use the profile only as a didactic strategy;
- preserve the same business rules, document relations, validations, exceptions, and ambiguities.

## Intended experimental contrast

The intended contrast was not between more information and less information.

Both conditions received the same technical content.

The intended contrast was between:

- a standard structured explanation;
- a structured explanation adapted by didactic strategy.

## Methodological caution

The observed difference between conditions was small:

- Condition A: 93.18%
- Condition B: 93.75%
- Difference B - A: +0.57 p.p.

This difference should be interpreted as a small descriptive advantage, not as conclusive evidence that personality-aware prompting outperformed the structured baseline.