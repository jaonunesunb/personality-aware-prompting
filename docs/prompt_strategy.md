# Prompt Strategy

The material generation script used a controlled prompt construction strategy.

## Shared components

Both conditions used:

- the same controlled technical domain base;
- the same participant task structure;
- the same mandatory output format;
- the same requirement to separate concepts, rules, validations, exceptions, document relations, ambiguities, and final observations.

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

## Condition B

Condition B used the same structure as Condition A, with the addition of an anonymized didactic strategy.

The didactic strategy was used only to adapt the form of the explanation, not the technical content.

The prompt explicitly instructed the LLM to:

- adapt the form, not the technical content;
- not mention that a psychological profile was being used;
- not praise, judge, or label the participant;
- use the profile only as a didactic strategy.
