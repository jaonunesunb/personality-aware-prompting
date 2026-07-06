# Execution and Contamination Control

The instructional materials were generated through scripted API calls rather than through an interactive chat interface.

This choice was made to reduce manual variation, improve traceability, and reduce the risk of cross-condition contamination.

## Independent calls

Each participant-task-condition combination was generated through an independent API call.

The script did not reuse:

- conversation history;
- previous model responses;
- participant answers;
- materials generated for other participants;
- materials generated under the other condition.

## Controlled inputs

Both conditions used the same:

- controlled technical domain base;
- task structure;
- mandatory output format;
- model configuration;
- temperature setting.

The difference between conditions was restricted to the explanatory strategy.

## Condition A

Condition A used a standard structured prompt.

It did not include participant profile information.

## Condition B

Condition B used the same domain base, task, and output format as Condition A.

The only additional input was an anonymized didactic strategy derived from OCEAN/IPIP-NEO.

The prompt instructed the model to adapt the form of explanation, not the technical content.

## Traceability

For each execution, the script saved:

- the exact prompt sent to the model;
- the generated response;
- participant code;
- condition;
- task;
- timestamp;
- model;
- temperature.

## Storage

The API call was configured with `store=false`.

## Cost-control run

A preliminary single-call execution was performed to estimate API cost before running the full generation round.

This preliminary call was not treated as a separate experimental condition.

## Remaining limitations

These controls reduce cross-condition and cross-participant contamination, but do not eliminate all threats.

The model provider, model updates, and internal training data remain outside researcher control.

The study also did not include a non-LLM instructional control group, so the learning gain should not be interpreted as proof that the LLM was superior to other well-structured instructional materials.