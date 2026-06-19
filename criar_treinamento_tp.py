"""
Cria o Template de Treinamento "Documentação como Código — Guia AltoQi"
no projeto AltoQi Treinamento (Id=75718) do TargetProcess.

Estrutura criada:
  1. Request (Template) — com Objetivo, Público alvo, Trilha, Detalhamento, Resultados
  2. 7 UserStories (um por módulo: 6 + módulo extra)
  3. Relations ligando cada UserStory ao Template (RelationType=Relation)

Uso:
  python criar_treinamento_tp.py
  python criar_treinamento_tp.py --dry-run   # apenas exibe o payload sem criar
"""

import urllib.request
import urllib.parse
import json
import os
import sys
import argparse
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

BASE_URL = os.environ.get("TARGETPROCESS_BASE_URL", "https://altoqi.tpondemand.com").rstrip("/")
TOKEN    = os.environ.get("TARGETPROCESS_TOKEN", "")
PROJECT_ID = 75718
SITE_URL = "https://andrebanki.github.io/github_para_docs"

# ---------------------------------------------------------------------------
# Dados dos módulos
# ---------------------------------------------------------------------------
MODULOS = [
    {
        "nome": "Módulo 01 — Git para Documentação",
        "url": f"{SITE_URL}/01-git-para-documentacao.html",
        "descricao": (
            "<p>Neste módulo você vai aprender a usar o Git como sistema de controle de versão "
            "para documentação técnica, sem precisar saber programar.</p>"
            "<ul>"
            "<li>O que é Git e por que usá-lo para documentação</li>"
            "<li>Conceitos de repositório, commit, clone, push e pull</li>"
            "<li>O fluxo de trabalho diário (simplificado e completo)</li>"
            "<li>Os comandos essenciais e quando usá-los</li>"
            "<li>Como resolver conflitos e desfazer erros</li>"
            "</ul>"
        ),
    },
    {
        "nome": "Módulo 02 — Markdown e MkDocs",
        "url": f"{SITE_URL}/02-markdown-e-mkdocs.html",
        "descricao": (
            "<p>Aprenda a escrever em Markdown e a publicar um site de documentação "
            "navegável com MkDocs.</p>"
            "<ul>"
            "<li>O que é Markdown e por que usá-lo em vez de Word/Google Docs</li>"
            "<li>Sintaxe essencial: títulos, listas, tabelas, imagens, código</li>"
            "<li>Como o MkDocs transforma arquivos <code>.md</code> em site HTML</li>"
            "<li>Configuração do <code>mkdocs.yml</code> e preview local</li>"
            "</ul>"
        ),
    },
    {
        "nome": "Módulo 03 — VS Code e Claude Code",
        "url": f"{SITE_URL}/02-vscode-e-claude-code.html",
        "descricao": (
            "<p>Configure o VS Code como ambiente de documentação e use o Claude Code "
            "para acelerar a escrita com IA.</p>"
            "<ul>"
            "<li>Por que usar o VS Code para documentação</li>"
            "<li>Extensões, preview de Markdown e terminal integrado</li>"
            "<li>Todos os comandos Git pelo VS Code (sem terminal)</li>"
            "<li>Os modos do Claude Code: Chat, Edição, Agente e CLI</li>"
            "<li>Boas práticas para IA generativa em documentação</li>"
            "</ul>"
        ),
    },
    {
        "nome": "Módulo 04 — Personalizando o Claude Code",
        "url": f"{SITE_URL}/06-claude-code-customizacao.html",
        "descricao": (
            "<p>Configure o Claude Code para trabalhar com as convenções e padrões do seu "
            "repositório de documentação.</p>"
            "<ul>"
            "<li>Os 4 mecanismos: CLAUDE.md, Comandos Personalizados, Agente e Skills</li>"
            "<li>Onde colocar cada arquivo e como configurá-lo</li>"
            "<li>Tabela de decisão: quando usar cada mecanismo</li>"
            "<li>Exemplo prático de sessão de trabalho com agente</li>"
            "</ul>"
        ),
    },
    {
        "nome": "Módulo 05 — Branches e Pull Requests",
        "url": f"{SITE_URL}/05-branches-e-pull-requests.html",
        "descricao": (
            "<p>Aprofunde o fluxo Git com branches isolados e revisão formal via Pull Request.</p>"
            "<ul>"
            "<li>O que é um branch e por que ele existe</li>"
            "<li>Como criar, navegar e trabalhar em branches</li>"
            "<li>O que é um Pull Request e como fazer revisão</li>"
            "<li>Como resolver conflitos de merge</li>"
            "<li>O fluxo completo passo a passo</li>"
            "</ul>"
        ),
    },
    {
        "nome": "Módulo 06 — Publicando para Acesso Externo",
        "url": f"{SITE_URL}/06-publicacao-externa.html",
        "descricao": (
            "<p>Publique a documentação gerada pelo MkDocs para acesso externo, "
            "escolhendo a opção certa para cada contexto.</p>"
            "<ul>"
            "<li>Opções disponíveis: GitHub Pages, servidores internos, plataformas pagas</li>"
            "<li>Como escolher entre conteúdo público e privado</li>"
            "<li>Como funciona a atualização automática via GitHub Actions</li>"
            "</ul>"
        ),
    },
    {
        "nome": "Módulo Extra — Instruções Específicas (Repositórios Reais)",
        "url": f"{SITE_URL}/modulo-extra.html",
        "descricao": (
            "<p>Padrões práticos encontrados nos repositórios reais da AltoQi: "
            "como documentar a partir do TargetProcess, espelhar épicos e organizar "
            "fontes com a pasta <code>raw/</code>.</p>"
            "<ul>"
            "<li>Dica 1 — Documentar features a partir do TargetProcess</li>"
            "<li>Dica 2 — Espelhar épicos do TargetProcess como páginas wiki</li>"
            "<li>Dica 3 — Pasta <code>raw/</code> como zona de entrada de fontes</li>"
            "</ul>"
        ),
    },
]

# ---------------------------------------------------------------------------
# Descrição HTML do Template principal
# ---------------------------------------------------------------------------
TEMPLATE_NAME = "Documentação como Código — Guia AltoQi"

TRILHA_ITEMS = "".join(
    f"<li><a href='{m['url']}'>{m['nome']}</a></li>"
    for m in MODULOS
)

DETALHAMENTO_ITEMS = "".join(
    f"<li><strong>{m['nome']}</strong> — <a href='{m['url']}'>acessar módulo</a>{m['descricao']}</li>"
    for m in MODULOS
)

TEMPLATE_DESC = f"""
<h3>1. Objetivo</h3>
<p>
Capacitar equipes de Produto e Engenharia a colaborar em documentação técnica
usando Git, Markdown, MkDocs e Claude Code — mesmo sem experiência prévia com
ferramentas de desenvolvimento. Ao final da trilha, o participante consegue criar,
revisar e publicar documentação como um profissional.
</p>

<h3>2. Público-alvo</h3>
<ul>
<li>Equipes de Produto (PMs, redatores técnicos)</li>
<li>Equipes de Engenharia que mantêm documentação</li>
<li>Qualquer colaborador que precise contribuir com repositórios de documentação</li>
</ul>
<p><strong>Pré-requisito:</strong> nenhum — o curso começa do zero.</p>

<h3>3. Trilha dos módulos</h3>
<ul>
{TRILHA_ITEMS}
</ul>
<p>
Site do treinamento: <a href="{SITE_URL}">{SITE_URL}</a>
</p>

<h3>4. Detalhamento de cada módulo</h3>
<ul>
{DETALHAMENTO_ITEMS}
</ul>

<h3>5. Resultados esperados</h3>
<p>
Ao final da trilha, os participantes serão capazes de:
</p>
<ul>
<li>Usar Git no dia a dia para documentação (commit, push, pull, branch, PR)</li>
<li>Escrever e formatar documentação em Markdown</li>
<li>Publicar e manter um site de documentação com MkDocs</li>
<li>Usar o Claude Code para acelerar e padronizar a escrita</li>
<li>Configurar agentes e prompts personalizados para o contexto da equipe</li>
<li>Aplicar padrões dos repositórios reais da AltoQi (TP, épicos, raw/)</li>
</ul>
""".strip()

# ---------------------------------------------------------------------------
# Helpers HTTP
# ---------------------------------------------------------------------------

def tp_get(path: str) -> dict:
    url = f"{BASE_URL}/api/v1/{path}?format=json&access_token={TOKEN}"
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read())


def tp_post(path: str, body: dict) -> dict:
    url = f"{BASE_URL}/api/v1/{path}?format=json&access_token={TOKEN}"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(dry_run: bool = False) -> None:
    if not TOKEN:
        sys.exit("❌  TARGETPROCESS_TOKEN não encontrado. Verifique o arquivo .env")

    print(f"🔗  Base URL : {BASE_URL}")
    print(f"📁  Projeto  : AltoQi Treinamento (Id={PROJECT_ID})")
    print(f"🧪  Dry-run  : {dry_run}\n")

    # ------------------------------------------------------------------
    # 1. Criar o Template (Request)
    # ------------------------------------------------------------------
    template_payload = {
        "Name": TEMPLATE_NAME,
        "Description": TEMPLATE_DESC,
        "Project": {"Id": PROJECT_ID},
    }

    print(f"📄  Criando Template: {TEMPLATE_NAME}")
    if dry_run:
        print("  [DRY-RUN] payload:")
        print(json.dumps(template_payload, indent=2, ensure_ascii=False)[:800])
        template_id = 0
    else:
        resp = tp_post("Requests", template_payload)
        template_id = resp["Id"]
        print(f"  ✅  Template criado — Id={template_id}")
        print(f"  🔗  https://altoqi.tpondemand.com/entity/{template_id}")

    print()

    # ------------------------------------------------------------------
    # 2. Criar as UserStories (módulos) e vincular ao Template
    # ------------------------------------------------------------------
    for i, mod in enumerate(MODULOS, 1):
        story_payload = {
            "Name": mod["nome"],
            "Description": (
                f"{mod['descricao']}"
                f"<p><strong>🔗 Link do módulo:</strong> "
                f"<a href='{mod['url']}'>{mod['url']}</a></p>"
            ),
            "Project": {"Id": PROJECT_ID},
        }

        print(f"  📝  [{i}/{len(MODULOS)}] Criando módulo: {mod['nome']}")

        if dry_run:
            story_id = i * 1000
            print(f"       [DRY-RUN] seria criada a UserStory e vinculada ao Template")
        else:
            story_resp = tp_post("UserStories", story_payload)
            story_id = story_resp["Id"]
            print(f"       ✅  UserStory Id={story_id}")

            # Vincular ao Template via Relation
            rel_payload = {
                "Master": {"Id": template_id},
                "Slave": {"Id": story_id},
                "RelationType": {"Id": 3},  # Relation
            }
            rel_resp = tp_post("Relations", rel_payload)
            print(f"       🔗  Relation criada — Id={rel_resp['Id']}")

    print()
    if not dry_run:
        print(f"🎉  Concluído! Template disponível em:")
        print(f"    https://altoqi.tpondemand.com/entity/{template_id}")
    else:
        print("🏁  Dry-run finalizado. Remova --dry-run para criar no TargetProcess.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cria o Template de Treinamento no TargetProcess")
    parser.add_argument("--dry-run", action="store_true", help="Exibe payloads sem criar nada")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
