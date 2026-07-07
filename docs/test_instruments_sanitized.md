# Test Instruments Sanitized

This file provides a sanitized description of the test instruments used in the pilot study.

It does not include raw participant answers, real participant names, informal profile labels, or open-ended responses that could compromise anonymity.

## Purpose

The instruments were used to evaluate initial domain learning in a Requirements Engineering task supported by LLM-generated instructional materials.

The study used:

- one pre-test, referred to as K0;
- two task-specific post-tests, referred to as K1;
- one self-confidence item after each K1 post-test.

## K0 pre-test

K0 measured initial familiarity with the public works monitoring domain.

It evaluated whether participants understood basic distinctions related to:

- planning versus execution;
- measurement documents;
- monitoring reports;
- evidence;
- responsibilities;
- delays;
- validation rules;
- business rules in public works monitoring.

Maximum score: 44 points.

Corrected average:

- 14.00/44
- 31.82%

The raw K0 participant answers are not included in this repository.

## K1 post-tests

K1 was applied after exposure to the LLM-generated instructional materials.

There were two K1 versions:

- Measurement Bulletin;
- Construction Monitoring Report.

Each K1 version had 11 knowledge questions.

Each question was scored from 0 to 2.

Scoring rubric:

- 0: incorrect, absent, or outside the domain;
- 1: partially correct, generic, or containing relevant imprecision;
- 2: correct and adequate.

Each K1 version had a maximum of 22 points.

Each participant completed two K1 post-tests, for a total maximum of 44 points.

Corrected average:

- 41.13/44
- 93.47%

## K1 Measurement Bulletin instrument

The Measurement Bulletin post-test evaluated whether participants could answer the following types of questions:

1. Explain the purpose of the Measurement Bulletin.
2. Distinguish the Physical-Financial Schedule from the Measurement Bulletin.
3. Identify what the Measurement Bulletin primarily represents.
4. Cite essential fields in a Measurement Bulletin form.
5. Explain why the Measurement Bulletin must be linked to the contract.
6. Explain what should happen when the accumulated measured quantity exceeds the contracted quantity.
7. Cite important validations for measured items.
8. Identify the document that serves as the basis for items, quantities, and prices.
9. Cite evidence that can be attached to prove a measurement.
10. Explain what glosa or partial rejection of a measurement means.
11. Cite an ambiguity that would require validation by a domain specialist.

The confidence item asked participants how secure they felt, from 1 to 5, to specify business rules for the Measurement Bulletin.

The confidence item was not included in the knowledge score.

## K1 Construction Monitoring Report instrument

The Construction Monitoring Report post-test evaluated whether participants could answer the following types of questions:

1. Explain the purpose of the Construction Monitoring Report.
2. Explain whether the report replaces the Measurement Bulletin and the Daily Construction Report.
3. Identify what the Construction Monitoring Report primarily represents.
4. Cite essential fields in a Construction Monitoring Report form.
5. Identify documents that can feed or support the report.
6. Explain why comparing planned and executed progress is important.
7. Cite business rules for identifying delay or risk.
8. Explain what it means to register pending issues in work monitoring.
9. Explain the role of evidence in the report.
10. Distinguish occurrence, pending issue, and risk.
11. Cite an ambiguity that would require validation by a domain specialist.

The confidence item asked participants how secure they felt, from 1 to 5, to specify business rules for the Construction Monitoring Report.

The confidence item was not included in the knowledge score.

## Corrected K1 results by document

| Document | Score | Percentage |
|---|---:|---:|
| Measurement Bulletin | 165/176 | 93.75% |
| Construction Monitoring Report | 164/176 | 93.18% |

## Corrected K1 results by condition

| Condition | Score | Percentage |
|---|---:|---:|
| Condition A: standard structured prompt | 164/176 | 93.18% |
| Condition B: personality-aware prompt | 165/176 | 93.75% |

Difference B - A:

- +1 point out of 176
- +0.57 percentage points

## Why raw answers are not included

The raw test files are not included because they contain:

- participant names;
- informal profile labels;
- open-ended participant responses;
- correction notes;
- potentially identifiable writing patterns;
- domain-specific details that are not necessary for reproducing the scoring structure.

For reproducibility, this repository provides the sanitized instrument structure, scoring rubric, maximum scores, and corrected aggregate results.