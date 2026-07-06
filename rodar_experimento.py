from openai import OpenAI
from pathlib import Path
from datetime import datetime
import os
import json
import time
import argparse

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.2"))

OUT_PROMPTS = Path("outputs/prompts_enviados")
OUT_RESPONSES = Path("outputs/respostas_llm")
LOGS = Path("logs")

OUT_PROMPTS.mkdir(parents=True, exist_ok=True)
OUT_RESPONSES.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)

client = OpenAI()

BASE_CONTEXT = """
O sistema apoia o acompanhamento de obras públicas executadas de forma indireta.
Nesse contexto, uma empresa contratada executa a obra, enquanto o órgão público acompanha,
registra, valida e consolida informações sobre planejamento, execução, evidências, medições
e andamento.

Documentos importantes:

Contrato:
define objeto, prazo, valor e condições gerais da obra.

Planilha Orçamentária Analítica:
detalha itens, quantidades, custos e composição orçamentária.

Cronograma Físico-Financeiro:
representa o planejamento físico e financeiro da obra ao longo do tempo.

Boletim de Medição:
registra serviços executados/medidos em determinado período e apoia conferência,
validação e pagamento.

Relatório Diário de Obras:
registra atividades, ocorrências, evidências e condições cotidianas da obra.

Relatório de Acompanhamento de Obra:
consolida informações sobre andamento, pendências, riscos, atrasos e situação geral da obra.
"""

TASKS = {
    "boletim": "Criar regras de negócio para um formulário de Boletim de Medição.",
    "relatorio": "Criar regras de negócio para um formulário de Relatório de Acompanhamento de Obra."
}

PROFILES = {
    "P01": """
Perfil didático:
Alta conscienciosidade. Baixo neuroticismo. Baixa extroversão. Abertura média-alta.

Estratégia:
Use explicação objetiva, estruturada e criteriosa. Evite floreio.
Destaque regras, validações e ordem lógica.
""",
    "P02": """
Perfil didático:
Alto neuroticismo. Alta abertura. Alta extroversão. Conscienciosidade baixa-média.

Estratégia:
Use explicação acolhedora, organizada em passos curtos.
Reduza sobrecarga. Dê exemplos antes de pedir abstração.
Use checkpoints de entendimento.
""",
    "P03": """
Perfil didático:
Alta abertura. Alta conscienciosidade. Baixa amabilidade. Baixa extroversão.

Estratégia:
Use linguagem técnica, direta e lógica. Evite tom motivacional.
Foque em estrutura, precisão, dependências e exceções.
""",
    "P04": """
Perfil didático:
Alta extroversão. Abertura média-alta. Conscienciosidade baixa. Neuroticismo médio-alto.

Estratégia:
Use explicação orientada a decisão e gestão.
Destaque impacto prático. Organize em blocos curtos.
""",
    "P05": """
Perfil didático:
Alta conscienciosidade. Baixa abertura. Baixa extroversão. Baixo neuroticismo.

Estratégia:
Use explicação prática, estável e operacional.
Evite excesso de abstração. Dê exemplos concretos de campos, regras e validações.
""",
    "P06": """
Perfil didático:
Alta abertura. Alta extroversão. Baixa conscienciosidade. Baixo neuroticismo.

Estratégia:
Use explicação dinâmica, com exemplos e checkpoints.
Quebre a tarefa em passos pequenos. Evite muitas opções abertas ao mesmo tempo.
""",
    "P07": """
Perfil didático:
Altíssima conscienciosidade. Alta abertura. Baixa extroversão. Neuroticismo baixo-médio.

Estratégia:
Use explicação formal, lógica e bem delimitada.
Destaque regras, consistência e critérios. Evite analogias vagas.
""",
    "P08": """
Perfil didático:
Alta extroversão. Alta amabilidade. Alta conscienciosidade. Neuroticismo médio.

Estratégia:
Use explicação colaborativa, estruturada e orientada a requisitos.
Destaque consenso, responsáveis, validação e rastreabilidade.
"""
}

RUNS = [
    {"p": "P01", "cond": "A", "task": "boletim"},
    {"p": "P01", "cond": "B", "task": "relatorio"},

    {"p": "P02", "cond": "A", "task": "relatorio"},
    {"p": "P02", "cond": "B", "task": "boletim"},

    {"p": "P03", "cond": "A", "task": "boletim"},
    {"p": "P03", "cond": "B", "task": "relatorio"},

    {"p": "P04", "cond": "A", "task": "relatorio"},
    {"p": "P04", "cond": "B", "task": "boletim"},

    {"p": "P05", "cond": "A", "task": "boletim"},
    {"p": "P05", "cond": "B", "task": "relatorio"},

    {"p": "P06", "cond": "A", "task": "relatorio"},
    {"p": "P06", "cond": "B", "task": "boletim"},

    {"p": "P07", "cond": "A", "task": "boletim"},
    {"p": "P07", "cond": "B", "task": "relatorio"},

    {"p": "P08", "cond": "A", "task": "relatorio"},
    {"p": "P08", "cond": "B", "task": "boletim"},
]

FORMAT = """
Produza um artefato com esta estrutura obrigatória:

1. Objetivo do formulário
2. Entidades principais
3. Campos necessários
4. Regras de negócio
5. Validações
6. Exceções e alertas
7. Relações com outros documentos
8. Ambiguidades ou dúvidas
9. Observações finais
"""

RULES_A = """
Regras para sua resposta:

- separe conceitos, regras e requisitos;
- explique termos técnicos do domínio;
- evite respostas genéricas;
- não invente legislação específica;
- indique incertezas quando necessário;
- destaque o que precisaria ser validado com especialista;
- use linguagem objetiva;
- organize a resposta em tópicos.
"""

RULES_B = """
Regras para sua resposta:

- separe conceitos, regras e requisitos;
- explique termos técnicos do domínio;
- evite respostas genéricas;
- não invente legislação específica;
- indique incertezas quando necessário;
- destaque o que precisaria ser validado com especialista;
- adapte a forma, não o conteúdo técnico;
- não mencione que está usando perfil psicológico;
- não elogie, julgue ou rotule o participante;
- use o perfil apenas como estratégia didática;
- organize a resposta em tópicos.
"""

def build_prompt(run):
    participant = run["p"]
    condition = run["cond"]
    task = TASKS[run["task"]]

    if condition == "A":
        return f"""
Você é um assistente especializado em Engenharia de Requisitos.

Sua tarefa é ajudar um desenvolvedor a compreender um domínio desconhecido
e produzir regras de negócio para um formulário de sistema.

Contexto do domínio:
{BASE_CONTEXT}

Tarefa do participante:
{task}

{FORMAT}

{RULES_A}
""".strip()

    return f"""
Você é um assistente especializado em Engenharia de Requisitos.

Sua tarefa é ajudar um desenvolvedor a compreender um domínio desconhecido
e produzir regras de negócio para um formulário de sistema.

Além do domínio, você receberá um perfil OCEAN/IPIP-NEO do participante.
Use esse perfil apenas para adaptar a forma da explicação, não para alterar o conteúdo técnico.

Contexto do domínio:
{BASE_CONTEXT}

Perfil do participante:
{PROFILES[participant]}

Tarefa do participante:
{task}

{FORMAT}

{RULES_B}
""".strip()

def run_one(run):
    participant = run["p"]
    condition = run["cond"]
    task = run["task"]
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    name = f"{participant}_{condition}_{task}_{stamp}"
    prompt = build_prompt(run)

    prompt_path = OUT_PROMPTS / f"{name}_prompt.txt"
    response_path = OUT_RESPONSES / f"{name}_resposta.txt"

    prompt_path.write_text(prompt, encoding="utf-8")

    response = client.responses.create(
        model=MODEL,
        input=prompt,
        temperature=TEMPERATURE,
        store=False,
        max_output_tokens=2200
    )

    output_text = response.output_text
    response_path.write_text(output_text, encoding="utf-8")

    usage = None
    if getattr(response, "usage", None):
        try:
            usage = response.usage.model_dump()
        except Exception:
            usage = str(response.usage)

    log = {
        "timestamp": stamp,
        "participant": participant,
        "condition": condition,
        "task": task,
        "model": MODEL,
        "temperature": TEMPERATURE,
        "response_id": getattr(response, "id", None),
        "prompt_file": str(prompt_path),
        "response_file": str(response_path),
        "usage": usage
    }

    with open(LOGS / "execucoes.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")

    print(f"OK: {name}")
    return log

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="Roda só N chamadas para teste.")
    args = parser.parse_args()

    selected = RUNS[:args.limit] if args.limit else RUNS

    print(f"Modelo: {MODEL}")
    print(f"Temperatura: {TEMPERATURE}")
    print(f"Total de chamadas: {len(selected)}")

    for run in selected:
        run_one(run)
        time.sleep(1)

    print("Fim. Veja as pastas outputs/ e logs/.")

if __name__ == "__main__":
    main()
