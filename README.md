# Learning the Domain Before Writing Requirements

This repository contains the anonymized artifacts of a pilot study on
LLM-mediated domain learning in Requirements Engineering.

The study investigated whether LLM-generated instructional materials could
support initial domain learning in an unfamiliar requirements domain, and
whether personality-aware prompting based on OCEAN/IPIP-NEO didactic profiles
would provide additional benefits over a standard structured prompt.

## Study summary

The study was conducted in the context of a graduate-level course on
Intelligent Software Engineering.

Participants worked with a public works monitoring domain and received
LLM-generated instructional materials about two artifacts:

- Measurement Bulletin
- Construction Monitoring Report

Two experimental conditions were compared:

- **Condition A:** standard structured prompt.
- **Condition B:** structured prompt plus anonymized didactic strategy derived
  from OCEAN/IPIP-NEO profiles.

Both conditions used the same controlled technical domain base. The difference
was the explanatory strategy used in Condition B.

## Main results

The corrected descriptive results are:

| Measure | Result |
|---|---:|
| K0 average | 50.00% |
| K1 average | 93.47% |
| Condition A | 93.20% |
| Condition B | 93.74% |
| Difference B - A | +0.54 p.p. |

The results suggest that LLM-generated instructional materials supported
initial domain learning. However, the small numerical advantage of Condition B
is not sufficient to claim a conclusive benefit of personality-aware prompting.

## Repository structure

```text
EXPERIMENTO_ESI_LLM/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── .env.example
│
├── paper/
│   └── artigo.pdf
│
├── scripts/
│   └── generate_materials.py
│
├── docs/
│   ├── protocol_summary.md
│   ├── prompt_strategy.md
│   ├── scoring_summary.md
│   └── results_summary.md
│
└── outputs/
    ├── prompts_enviados/
    └── respostas_llm/
## Methodological documentation

Additional methodological details are available in:

- [`docs/protocol_summary.md`](docs/protocol_summary.md)
- [`docs/prompt_strategy.md`](docs/prompt_strategy.md)
- [`docs/scoring_summary.md`](docs/scoring_summary.md)
- [`docs/results_summary.md`](docs/results_summary.md)
- [`docs/execution_and_reproducibility.md`](docs/execution_and_reproducibility.md)
- [`docs/contamination_control.md`](docs/contamination_control.md)


## Methodological documentation

Additional methodological details are available in:

- [`docs/protocol_summary.md`](docs/protocol_summary.md)
- [`docs/prompt_strategy.md`](docs/prompt_strategy.md)
- [`docs/instruments_summary.md`](docs/instruments_summary.md)
- [`docs/results_summary.md`](docs/results_summary.md)
- [`docs/execution_and_contamination_control.md`](docs/execution_and_contamination_control.md)
