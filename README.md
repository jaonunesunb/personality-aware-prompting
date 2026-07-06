# Learning the Domain Before Writing Requirements

This repository contains the anonymized artifacts of a pilot study on LLM-mediated domain learning in Requirements Engineering.

The study investigated whether LLM-generated instructional materials could support initial domain learning in an unfamiliar requirements domain, and whether personality-aware prompting based on OCEAN/IPIP-NEO didactic strategies would provide additional benefits over a standard structured prompt.

## Study summary

The study was conducted in the context of a graduate-level course on Intelligent Software Engineering.

Participants worked with a public works monitoring domain and received LLM-generated instructional materials about two artifacts:

- Measurement Bulletin
- Construction Monitoring Report

Two experimental conditions were compared:

- **Condition A:** standard structured prompt.
- **Condition B:** structured prompt plus anonymized didactic strategy derived from OCEAN/IPIP-NEO profiles.

Both conditions used the same controlled technical domain base. The difference between conditions was the explanatory strategy used in Condition B.

## Main results

The corrected descriptive results are:

| Measure | Result |
|---|---:|
| K0 average | 31.82% |
| K1 average | 93.47% |
| Learning gain | +61.65 p.p. |
| Condition A | 93.18% |
| Condition B | 93.75% |
| Difference B - A | +0.57 p.p. |

The results suggest that LLM-generated instructional materials supported initial domain learning.

However, the small numerical advantage of Condition B is not sufficient to claim a conclusive benefit of personality-aware prompting. The study should therefore be interpreted as a pilot focused on domain learning and protocol validation, not as a definitive validation of personality-aware prompting.

## Repository structure

```text
personality-aware-prompting/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── .env.example
│
├── paper/
│   └── Learning the Domain Before Writing Requirements.pdf
│
├── slides/
│   └── ESI___perfis Slides.pdf
│
├── scripts/
│   └── generate_materials.py
│
├── docs/
│   ├── protocol_summary.md
│   ├── prompt_strategy.md
│   ├── instruments_summary.md
│   ├── scoring_summary.md
│   ├── results_summary.md
│   └── execution_and_contamination_control.md
│
└── outputs/
    ├── prompts_enviados/
    └── respostas_llm/
```

## Artifacts

The repository includes:

- the final article PDF;
- the final presentation slides;
- the Python script used to generate LLM materials;
- the generated prompts;
- the generated LLM responses;
- methodological documentation about protocol, instruments, scoring, results, and contamination control.

## Methodological documentation

Additional methodological details are available in:

- [`docs/protocol_summary.md`](docs/protocol_summary.md)
- [`docs/prompt_strategy.md`](docs/prompt_strategy.md)
- [`docs/instruments_summary.md`](docs/instruments_summary.md)
- [`docs/scoring_summary.md`](docs/scoring_summary.md)
- [`docs/results_summary.md`](docs/results_summary.md)
- [`docs/execution_and_contamination_control.md`](docs/execution_and_contamination_control.md)

## Experimental design

The study used a balanced pilot design with eight anonymized participants, identified as P01 to P08.

Each participant received two LLM-generated instructional materials, one for each domain artifact. Across the full design, both experimental conditions were applied to both artifacts.

The two conditions were:

- **Condition A:** standard structured prompting.
- **Condition B:** structured prompting plus anonymized didactic strategy derived from OCEAN/IPIP-NEO profiles.

The technical domain base, task structure, and mandatory output format were kept constant across both conditions.

## Instruments

The study used:

- one pre-test, referred to as K0;
- two task-specific post-tests, referred to as K1;
- one self-confidence item after each K1 test.

K0 measured initial familiarity with the public works monitoring domain.

K1 measured task-specific understanding after exposure to the LLM-generated instructional materials.

The self-confidence item was analyzed separately and was not included in the knowledge score.

## Execution and contamination control

The instructional materials were generated through scripted API calls rather than through an interactive chat interface.

Each participant-task-condition combination was generated through an independent API call. The script did not reuse conversation history, previous model responses, participant answers, or materials generated for other participants.

For each execution, the script saved:

- the exact prompt sent to the model;
- the generated response;
- participant code;
- condition;
- task;
- timestamp;
- model configuration;
- temperature setting.

The API call was configured with `store=false`.

## Running the material generation script

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Then edit `.env` with the API key and model configuration.

Run a limited test:

```bash
python scripts/generate_materials.py --limit 1
```

Run the full generation round:

```bash
python scripts/generate_materials.py
```

## Privacy and anonymization

The repository should not contain:

- real participant names;
- raw IPIP-NEO answers;
- complete psychological profiles;
- API keys;
- `.env`;
- execution logs with sensitive metadata.

Only anonymized participant codes, didactic strategy summaries, prompts, generated materials, and methodological documentation are included.

## Scope and limitations

This is a pilot study.

The results support claims about initial domain learning measured by K0 and K1.

The results do not support claims about improved requirements artifact quality, because the participant-produced artifact stage and blind expert review were not executed.

The small advantage observed for Condition B should be interpreted only as a descriptive result. It is not sufficient to claim that personality-aware prompting conclusively outperformed the standard structured prompt.
