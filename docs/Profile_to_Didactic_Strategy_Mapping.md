# Profile to Didactic Strategy Mapping

This file explains how personality information was transformed into anonymized didactic strategies for Condition B.

Raw IPIP-NEO/OCEAN answers are not included in this repository.

The study did not use personality profiles to evaluate competence, classify participants, diagnose behavior, or make decisions about individuals.

Personality information was used only to derive anonymized didactic strategies for adapting the form of the explanation in Condition B.

## Purpose

The purpose of the profile-to-strategy mapping was to adapt the instructional style of the LLM-generated material while preserving the same technical content used in Condition A.

The mapping was used to guide how the explanation should be presented, not what domain rules should be included.

## Transformation logic

The transformation followed this general path:

```text
IPIP/OCEAN profile
        ↓
anonymized profile interpretation
        ↓
didactic strategy
        ↓
Condition B prompt
        ↓
LLM-generated instructional material
```

## Use in Condition B

In Condition B, the didactic strategy was added to the prompt as an instruction about explanatory style.

The strategy could affect:

- level of structure;
- degree of step-by-step explanation;
- use of examples;
- use of checkpoints;
- emphasis on rules and validation;
- degree of practical framing;
- degree of conceptual framing;
- reduction of cognitive overload;
- tone of explanation;
- organization of the material.

The strategy could not affect:

- business rules;
- document relationships;
- validation rules;
- exceptions;
- ambiguities;
- expected technical content;
- scoring criteria;
- participant evaluation.

## Prompt constraints

The Condition B prompt instructed the LLM to:

- adapt the form of explanation, not the technical content;
- not mention that a psychological profile was being used;
- not label the participant;
- not judge the participant;
- not infer competence from personality;
- not change business rules based on personality;
- preserve the same domain rules used in Condition A;
- preserve the same document relations used in Condition A;
- preserve the same validation concerns used in Condition A;
- preserve the same ambiguity warnings used in Condition A.

## Anonymized didactic strategies

| Participant | Didactic strategy summary |
|---|---|
| P01 | Use an objective, structured, and criteria-based explanation. Avoid rhetorical excess. Emphasize rules, validations, logical order, and explicit constraints. |
| P02 | Use a welcoming explanation organized into short steps. Reduce overload. Provide examples before abstraction. Include understanding checkpoints and avoid excessive density. |
| P03 | Use technical, direct, and logical language. Avoid motivational tone. Focus on structure, precision, dependencies, exceptions, and implementation consequences. |
| P04 | Use a decision-oriented and management-oriented explanation. Emphasize practical impact, accountability, prioritization, and concise blocks that support coordination. |
| P05 | Use a practical, stable, and operational explanation. Avoid excessive abstraction. Provide concrete examples of fields, rules, validations, and expected system behavior. |
| P06 | Use a dynamic explanation with examples and checkpoints. Break the task into small steps. Avoid too many open options at once. Reinforce the distinction between similar documents. |
| P07 | Use a formal, logical, and well-delimited explanation. Emphasize rules, consistency, criteria, constraints, and validation logic. Avoid vague analogies. |
| P08 | Use a collaborative, structured, and requirements-oriented explanation. Emphasize roles, consensus, validation, traceability, document relations, and ambiguity management. |

## Condition A versus Condition B

The intended contrast was not between more information and less information.

Both conditions received the same technical domain base.

Both conditions received the same task structure.

Both conditions received the same mandatory output format.

The intended contrast was:

- Condition A: standard structured explanation;
- Condition B: structured explanation adapted by anonymized didactic strategy.

## Methodological caution

The observed difference between conditions was small:

| Condition | Score | Percentage |
|---|---:|---:|
| Condition A | 164/176 | 93.18% |
| Condition B | 165/176 | 93.75% |

Difference B - A:

- +1 point out of 176;
- +0.57 percentage points.

This difference should be interpreted as a small descriptive advantage, not as conclusive evidence that personality-aware prompting outperformed the structured baseline.

## Privacy note

The repository includes only didactic strategy summaries.

It does not include:

- raw personality answers;
- full psychological reports;
- participant names;
- informal participant labels;
- identifiable interpretations;
- individual psychological scores;
- facet-level personality reports.

## Scope

This file documents how personality information was operationalized as didactic strategy.

It does not provide enough information to reconstruct individual psychological profiles.

It is intended to support methodological transparency while preserving participant privacy.