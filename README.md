# Documentação como Código — Guia para Equipes de Produto e Engenharia

> Material de estudo para trabalhar com documentação de produto usando Git, Markdown, MkDocs e Claude Code — da forma que a equipe técnica já trabalha com código.

---

## Por que este material?

Equipes de desenvolvimento de software trabalham com código-fonte em repositórios Git: fazem **clone**, **pull**, **commit**, **push** e **Pull Requests** para colaborar sem conflitos.

A documentação de produto do AltoQi Visus segue o mesmo modelo — chamado de **"Docs as Code"** (documentação como código). Isso significa:

- A documentação vive em um repositório Git, versionada como qualquer software
- Você escreve em **Markdown** (texto simples), não em Word ou Notion
- O site de documentação é **gerado automaticamente** a partir dos arquivos `.md` usando MkDocs
- O **Claude Code** atua como redator técnico assistente dentro do VS Code

Este guia prepara você para trabalhar com este fluxo, mesmo sem experiência prévia com desenvolvimento de software.

---

## Estrutura do Material

```
curso_github/
├── README.md
└── docs/
  ├── index.md
  ├── 01-setup-ambiente.md           ← ambiente, extensões, preview e Git visual
  ├── 02-git-para-documentacao.md     ← fundamentos de Git aplicados a docs
  ├── 03-markdown-e-mkdocs.md         ← escrita em Markdown e preview/build local
  ├── 04-claude-code.md               ← modos de uso do Claude Code e boas práticas de IA
  ├── 05-branches-e-pull-requests.md  ← colaboração avançada com revisão
  ├── 06-publicacao-externa.md        ← publicação e atualização do site
  ├── 07-claude-code-customizacao.md  ← CLAUDE.md, comandos, agente e skills
  ├── 08-instrucoes-especificas.md    ← padrões específicos de repositórios reais
  └── 09-exercicios-praticos.md       ← revisão prática ao final da trilha
```

---

## Módulos

### [Módulo 1 — VS Code e Configuração do Ambiente](./docs/01-setup-ambiente.md)

O que você vai aprender:
- Quais programas instalar primeiro (Git, Python, VS Code e extensões)
- Por que usar o VS Code como editor de documentação
- Como executar todas as operações de Git pela interface visual — sem terminal
- Como usar o preview de Markdown e o terminal integrado

---

### [Módulo 2 — Git para Documentação](./docs/02-git-para-documentacao.md)

O que você vai aprender:
- O que é um repositório, commit, branch e Pull Request
- O fluxo de trabalho diário: `pull → branch → editar → commit → push → PR`
- Comandos essenciais do Git com exemplos práticos
- Como resolver conflitos de merge
- Convenções de nomenclatura de branches e mensagens de commit

---

### [Módulo 3 — Markdown e MkDocs](./docs/03-markdown-e-mkdocs.md)

O que você vai aprender:
- O que é Markdown e por que ele é superior ao Word para documentação técnica
- Toda a sintaxe necessária: títulos, listas, tabelas, links, imagens, código
- Admonitions (`!!! note`, `!!! warning`) e frontmatter YAML
- Como o MkDocs transforma arquivos `.md` em um site HTML navegável
- Como rodar o site localmente com `mkdocs serve`
- Como publicar automaticamente com GitHub Actions

---

### [Módulo 4 — Claude Code](./docs/04-claude-code.md)

O que você vai aprender:
- O que é o Claude Code e o que ele pode fazer
- Os modos de uso: Chat, Edição pelo Chat, Modo Agente e CLI
- Quando usar cada modo no fluxo diário de escrita e revisão
- Boas práticas para IA generativa em documentação

---

### [Módulo 5 — Branches e Pull Requests](./docs/05-branches-e-pull-requests.md)

O que você vai aprender:
- Como isolar trabalho em branches antes de publicar
- Como abrir, revisar e aprovar Pull Requests no GitHub
- Como resolver conflitos de merge no fluxo completo

---

### [Módulo 6 — Publicando para Acesso Externo](./docs/06-publicacao-externa.md)

O que você vai aprender:
- Como escolher a melhor opção de publicação para conteúdo público ou privado
- Como o GitHub Pages se encaixa na trilha básica
- Como funciona a atualização automática do site após `push` no `main`

---

### [Módulo 7 — Personalizando o Claude Code](./docs/07-claude-code-customizacao.md)

O que você vai aprender:
- O que é o `CLAUDE.md` e por que ele é o "manual do agente"
- Como criar instruções contextuais por seção com `CLAUDE.md` em subpastas
- Como salvar comandos reutilizáveis em `.claude/commands/`
- Como usar o modo agente com perfis especializados
- O que são Skills e quando usá-las
- Como todos esses mecanismos se encaixam num fluxo de trabalho real

---

### [Módulo 8 — Instruções Específicas](./docs/08-instrucoes-especificas.md)

O que você vai aprender:
- Padrões usados em repositórios reais além da trilha básica
- Como lidar com TargetProcess, espelhamento de épicos e pasta `raw/`
- Quando aplicar esses padrões no dia a dia

---

### [Módulo 9 — Exercícios Práticos](./docs/09-exercicios-praticos.md)

O que você vai aprender:
- Como revisar a trilha inteira com exercícios na mesma ordem do curso
- Como praticar desde setup até publicação em um módulo final único

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
  VS Code + Claude Code              ← escrever em Markdown
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
| Extensão Claude Code | — | Marketplace VS Code |

---

## Repositório de Referência

O repositório `visus_docs` é o exemplo real que este curso usa como referência. Sua estrutura implementa todas as práticas descritas neste material:

```
visus_docs/
├── .github/
├── CLAUDE.md                     ← manual do agente de IA
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
