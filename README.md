# Documentação como Código — Guia para Equipes de Produto e Engenharia

> Material de estudo para trabalhar com documentação de produto usando Git, Markdown, MkDocs e GitHub Copilot — da forma que a equipe técnica já trabalha com código.

---

## Por que este material?

Equipes de desenvolvimento de software trabalham com código-fonte em repositórios Git: fazem **clone**, **pull**, **commit**, **push** e **Pull Requests** para colaborar sem conflitos.

A documentação de produto do AltoQi Visus segue o mesmo modelo — chamado de **"Docs as Code"** (documentação como código). Isso significa:

- A documentação vive em um repositório Git, versionada como qualquer software
- Você escreve em **Markdown** (texto simples), não em Word ou Notion
- O site de documentação é **gerado automaticamente** a partir dos arquivos `.md` usando MkDocs
- O **GitHub Copilot** atua como redator técnico assistente dentro do VS Code

Este guia prepara você para trabalhar com este fluxo, mesmo sem experiência prévia com desenvolvimento de software.

---

## Estrutura do Material

```
curso_github/
├── README.md                    ← você está aqui
├── 01-git-para-documentacao.md  ← fundamentos de Git aplicados a docs
├── 02-markdown-e-mkdocs.md      ← escrita em Markdown e publicação com MkDocs
├── 03-vscode-e-copilot.md       ← ambiente de trabalho e uso de IA
└── 04-copilot-customizacao.md   ← instructions, prompts, agentes e skills
```

---

## Módulos

### [Módulo 1 — Git para Documentação](./01-git-para-documentacao.md)

O que você vai aprender:
- O que é um repositório, commit, branch e Pull Request
- O fluxo de trabalho diário: `pull → branch → editar → commit → push → PR`
- Comandos essenciais do Git com exemplos práticos
- Como resolver conflitos de merge
- Convenções de nomenclatura de branches e mensagens de commit

---

### [Módulo 2 — Markdown e MkDocs](./02-markdown-e-mkdocs.md)

O que você vai aprender:
- O que é Markdown e por que ele é superior ao Word para documentação técnica
- Toda a sintaxe necessária: títulos, listas, tabelas, links, imagens, código
- Admonitions (`!!! note`, `!!! warning`) e frontmatter YAML
- Como o MkDocs transforma arquivos `.md` em um site HTML navegável
- Como rodar o site localmente com `mkdocs serve`
- Como publicar automaticamente com GitHub Actions

---

### [Módulo 3 — VS Code e GitHub Copilot](./03-vscode-e-copilot.md)

O que você vai aprender:
- Por que usar VS Code para escrever documentação
- Extensões essenciais para a equipe instalar
- Como usar o Git diretamente pelo painel visual do VS Code (sem terminal)
- O que é o GitHub Copilot e como ele se integra ao repositório
- Os quatro modos de uso: sugestões inline, Inline Chat, painel de Chat e Modo Agente
- Boas práticas para obter resultados de qualidade com IA

---

### [Módulo 4 — Personalizando o GitHub Copilot](./04-copilot-customizacao.md)

O que você vai aprender:
- O que é o `copilot-instructions.md` e por que ele é o "manual do agente"
- Como criar instruções contextuais por seção com `.instructions.md`
- Como salvar prompts reutilizáveis em arquivos `.prompt.md`
- Como definir agentes especializados com `.agent.md`
- O que são Skills e quando usá-las
- Como todos esses mecanismos se encaixam num fluxo de trabalho real

---

## Referência Rápida: Fluxo Completo

```
┌─────────────────────────────────────────────────────────────────┐
│           FLUXO DOCS AS CODE — DO RASCUNHO À PUBLICAÇÃO         │
└─────────────────────────────────────────────────────────────────┘

SETUP (uma vez)
  git clone <url-do-repositorio>
  pip install -r requirements.txt

INÍCIO DE CADA SESSÃO
  git pull                           ← pegar últimas mudanças
  git checkout -b docs/nome-tarefa   ← criar branch isolado

ESCREVER/EDITAR
  VS Code + GitHub Copilot           ← escrever em Markdown
  mkdocs serve                       ← visualizar em http://localhost:8000

SALVAR PROGRESSO
  git add .
  git commit -m "docs: descreve o que foi feito"

ENVIAR PARA REVISÃO
  git push origin docs/nome-tarefa
  → Abrir Pull Request no GitHub
  → Colega revisa e aprova

PUBLICAR
  → Merge do PR no main
  → GitHub Actions reconstrói e publica o site automaticamente
```

---

## Pré-requisitos para o Ambiente

| Ferramenta | Versão mínima | Link |
|---|---|---|
| Git | 2.x | https://git-scm.com |
| Python | 3.10 | https://www.python.org |
| VS Code | mais recente | https://code.visualstudio.com |
| Extensão GitHub Copilot | — | Marketplace VS Code |
| Extensão GitHub Copilot Chat | — | Marketplace VS Code |

---

## Repositório de Referência

O repositório `visus_docs` é o exemplo real que este curso usa como referência. Sua estrutura implementa todas as práticas descritas neste material:

```
visus_docs/
├── .github/
│   └── copilot-instructions.md   ← manual do agente de IA
├── .vscode/
│   └── settings.json             ← configurações do workspace
├── docs/                         ← todo o conteúdo em Markdown
│   ├── index.md
│   ├── plataforma/
│   ├── workflow/
│   ├── collab/
│   ├── cost_management/
│   ├── planning/
│   ├── bid/
│   ├── tracking/
│   └── control_tower/
├── source/                       ← fontes originais (leitura apenas)
├── instructions.md               ← mapa de localização de conteúdo
├── mkdocs.yml                    ← configuração do MkDocs
└── requirements.txt              ← dependências Python
```

---

*Material preparado para as equipes de Produto e Engenharia da AltoQi — Junho 2025.*
