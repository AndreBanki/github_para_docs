"""
Atualiza o Template 290058 e suas UserStories no TargetProcess.

Mapeamento (IDs existentes → nova estrutura):
  290059  Atividade 1  →  Etapa 1 — Fundação: Ambiente e Git
  290061  Atividade 2  →  Etapa 2 — Conteúdo: Markdown, MkDocs e Publicação
  290062  Atividade 3  →  Etapa 3 — IA: Claude Code do Básico ao Avançado
  290064  Atividade 4  →  Etapa 4 — Colaboração e Padrões Reais
  (nova)               →  Etapa 5 — Consolidação Prática  + nova Relation
  290322  Gabarito     →  Gabarito atualizado (25 perguntas)
  290058  Template     →  Descrição atualizada

Uso:
  python atualizar_treinamento_tp.py
  python atualizar_treinamento_tp.py --dry-run
"""

import urllib.request
import json
import os
import sys
import argparse
import io
from dotenv import load_dotenv

# Força UTF-8 no stdout para evitar erro de encoding em emojis no Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

load_dotenv()

BASE_URL   = os.environ.get("TARGETPROCESS_BASE_URL", "https://altoqi.tpondemand.com").rstrip("/")
TOKEN      = os.environ.get("TARGETPROCESS_TOKEN", "")
PROJECT_ID = 75718
SITE_URL   = "https://andrebanki.github.io/github_para_docs"

TEMPLATE_ID   = 290058
ETAPA1_ID     = 290059
ETAPA2_ID     = 290061
ETAPA3_ID     = 290062
ETAPA4_ID     = 290064
GABARITO_ID   = 290322

# ---------------------------------------------------------------------------
# Conteúdo das etapas (importado inline para script autônomo)
# ---------------------------------------------------------------------------
from criar_treinamento_tp import (
    ETAPAS,
    GABARITO_NAME,
    GABARITO_DESC,
    TEMPLATE_DESC,
    TEMPLATE_NAME,
)

# Mapeamento ID existente → índice em ETAPAS
ID_PARA_ETAPA = {
    ETAPA1_ID: 0,
    ETAPA2_ID: 1,
    ETAPA3_ID: 2,
    ETAPA4_ID: 3,
}

# ---------------------------------------------------------------------------
# Helpers HTTP
# ---------------------------------------------------------------------------

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
    print(f"🎯  Template : Id={TEMPLATE_ID}")
    print(f"🧪  Dry-run  : {dry_run}\n")

    # ------------------------------------------------------------------
    # 1. Atualizar o Template (Request 290058)
    # ------------------------------------------------------------------
    print(f"📄  Atualizando Template Id={TEMPLATE_ID}: {TEMPLATE_NAME}")
    payload = {"Id": TEMPLATE_ID, "Name": TEMPLATE_NAME, "Description": TEMPLATE_DESC}
    if dry_run:
        print("  [DRY-RUN] payload (truncado):")
        print(json.dumps(payload, indent=2, ensure_ascii=False)[:600])
    else:
        tp_post("Requests", payload)
        print(f"  ✅  Template atualizado")
    print()

    # ------------------------------------------------------------------
    # 2. Atualizar Etapas 1–4 (UserStories existentes)
    # ------------------------------------------------------------------
    print("📝  Atualizando Etapas 1–4 (UserStories existentes)...")
    for us_id, idx in ID_PARA_ETAPA.items():
        etapa = ETAPAS[idx]
        payload = {"Id": us_id, "Name": etapa["nome"], "Description": etapa["descricao"]}
        print(f"  [{idx+1}/4] Id={us_id}  →  {etapa['nome']}")
        if dry_run:
            print(f"       [DRY-RUN] seria atualizada a UserStory {us_id}")
        else:
            tp_post("UserStories", payload)
            print(f"       ✅  Atualizada")
    print()

    # ------------------------------------------------------------------
    # 3. Criar Etapa 5 (nova UserStory) e vincular ao Template
    # ------------------------------------------------------------------
    etapa5 = ETAPAS[4]
    print(f"🆕  Criando Etapa 5: {etapa5['nome']}")
    if dry_run:
        etapa5_id = 99999
        print(f"  [DRY-RUN] seria criada a UserStory da Etapa 5 e vinculada ao Template")
    else:
        resp = tp_post("UserStories", {
            "Name": etapa5["nome"],
            "Description": etapa5["descricao"],
            "Project": {"Id": PROJECT_ID},
        })
        etapa5_id = resp["Id"]
        print(f"  ✅  UserStory criada — Id={etapa5_id}")

        rel_resp = tp_post("Relations", {
            "Master": {"Id": TEMPLATE_ID},
            "Slave":  {"Id": etapa5_id},
            "RelationType": {"Id": 3},
        })
        print(f"  🔗  Relation criada — Id={rel_resp['Id']}")
    print()

    # ------------------------------------------------------------------
    # 4. Atualizar Gabarito (UserStory 290322)
    # ------------------------------------------------------------------
    print(f"🔒  Atualizando Gabarito Id={GABARITO_ID}: {GABARITO_NAME}")
    payload = {"Id": GABARITO_ID, "Name": GABARITO_NAME, "Description": GABARITO_DESC}
    if dry_run:
        print("  [DRY-RUN] seria atualizada a UserStory do Gabarito")
    else:
        tp_post("UserStories", payload)
        print(f"  ✅  Gabarito atualizado")
    print()

    # ------------------------------------------------------------------
    # Resumo
    # ------------------------------------------------------------------
    if not dry_run:
        print("🎉  Concluído! Links:")
        print(f"    Template  → https://altoqi.tpondemand.com/entity/{TEMPLATE_ID}")
        print(f"    Etapa 5   → https://altoqi.tpondemand.com/entity/{etapa5_id}")
        print(f"    Gabarito  → https://altoqi.tpondemand.com/entity/{GABARITO_ID}")
    else:
        print("🏁  Dry-run finalizado. Remova --dry-run para atualizar no TargetProcess.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Atualiza o Template de Treinamento no TargetProcess")
    parser.add_argument("--dry-run", action="store_true", help="Exibe payloads sem modificar nada")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
