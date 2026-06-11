# Módulo 1 — Git para Documentação

> **Para quem é este módulo:** equipes de Produto e Engenharia que mantêm documentação em repositórios Git — sem necessidade de saber programar.

!!! abstract "🎯 Objetivos de aprendizagem"
    Neste módulo você vai aprender:

    - O que é Git e por que usá-lo para documentação
    - Os conceitos de repositório, commit, clone, push e pull
    - O fluxo de trabalho diário (simplificado e completo)
    - Os comandos essenciais e quando usá-los
    - Como resolver situações comuns (conflitos, desfazer erros)

---

## 1. Por que usar Git para documentação?

Git é um sistema de **controle de versão**: ele registra cada mudança feita em arquivos ao longo do tempo, permitindo que múltiplas pessoas colaborem sem sobrescrever o trabalho umas das outras.

Para documentação, isso significa:

| Situação | Sem Git | Com Git |
|---|---|---|
| Duas pessoas editam o mesmo arquivo | Uma versão sobrescreve a outra | Cada mudança é rastreada e mesclada |
| Um texto errado é publicado | Difícil saber quem mudou o quê | É possível ver quem alterou, quando e por quê — e reverter |
| Nova funcionalidade precisa de doc em rascunho | Arquivo paralelo vira bagunça | Você cria um branch isolado |
| Revisão de conteúdo antes de publicar | E-mail ou comentário no doc | Pull Request com histórico de revisão |

---

## 2. Conceitos Fundamentais

### Repositório (repo)

É a **pasta raiz do projeto**, controlada pelo Git. No caso da documentação do Visus, o repositório é `visus_docs/`. Tudo dentro dele — arquivos Markdown, imagens, configurações — é rastreado.

Um repositório pode ser:
- **Local**: a cópia que existe na sua máquina
- **Remoto**: a cópia oficial que fica no GitHub (ou GitLab, Azure DevOps, etc.)

### Commit

Um commit é um **snapshot** — uma fotografia do estado dos arquivos em um momento específico. Cada commit tem:
- Uma **mensagem** descrevendo o que foi alterado (ex.: `docs: adiciona guia de acesso ao módulo Collab`)
- Um **autor** e **data/hora**
- Um **identificador único** (hash)

> **Analogia:** um commit é como salvar uma versão de um documento Word com um nome descritivo — mas automático, rastreável e reversível.

### Clone

**Clonar** um repositório significa baixar uma cópia completa dele (incluindo todo o histórico de commits) para a sua máquina. É a **primeira operação** que você faz — feita uma única vez por máquina.

#### O que acontece quando você clona

O Git cria uma **nova pasta** com o nome do repositório dentro do diretório onde você executou o comando. Por exemplo, se você estiver em `C:\Projetos\` e clonar o repositório `visus-docs`, a estrutura resultante será:

```
C:\Projetos\                  ← pasta onde você executou o clone
└── visus-docs\               ← pasta criada pelo Git (o repositório local)
    ├── .git\                 ← histórico e metadados do Git (não mexa aqui)
    ├── docs\
    ├── mkdocs.yml
    └── ...
```

O comando:

```bash
git clone https://github.com/altoqi/visus-docs.git
```

deve ser executado **dentro da pasta onde você quer que o repositório fique** — não dentro de outra pasta de repositório já existente.

#### Onde clonar — escolha uma pasta dedicada

Crie uma pasta simples para guardar seus repositórios, por exemplo:

```
C:\Repos\          (Windows)
C:\Dev\            (Windows)
~/repos/           (macOS/Linux)
```

Então navegue até ela antes de clonar:

```bash
cd C:\Repos
git clone https://github.com/altoqi/visus-docs.git
# resultado: C:\Repos\visus-docs\
```

??? warning "Nunca coloque um repositório dentro de outro"
    O Git rastreia tudo que está dentro da pasta do repositório. Se você clonar um projeto dentro da pasta de outro repositório existente, o Git pai vai começar a enxergar o repositório filho como arquivos não rastreados — causando confusão e erros difíceis de diagnosticar.

    ```
    ❌  C:\Repos\visus-docs\          ← repositório A
                  └── curso_github\   ← repositório B clonado aqui dentro → PROBLEMA

    ✅  C:\Repos\visus-docs\          ← repositório A
        C:\Repos\curso_github\        ← repositório B na mesma pasta pai → CORRETO
    ```

    **Exceção:** repositórios aninhados de forma intencional existem (chamados de *git submodules*), mas são uma configuração avançada que nunca acontece por acidente — exige um comando específico.

---

## 3. Fluxo de Trabalho Diário

Existem dois fluxos possíveis. Comece pelo simplificado e migre para o completo quando a equipe crescer ou quando a documentação precisar de revisão antes de publicar.

---

### Fluxo Simplificado — todos trabalham direto no `main`

**Quando usar:** equipe pequena (2–3 pessoas), confiança mútua no conteúdo, sem necessidade de revisão formal antes de publicar. É o ponto de partida natural para quem está aprendendo.

```mermaid
flowchart LR
    A["🔄 git pull\nAtualizar"] --> B["✏️ Editar\narquivos .md"] --> C["📦 git add .\nRegistrar"] --> D["💾 git commit\nCommitar"] --> E["🚀 git push\nPublicar"]
    style A fill:#0a2a1c,stroke:#1aa863,color:#d4ede0
    style B fill:#0c3322,stroke:#25CE7B,color:#dcfaea
    style C fill:#0e3d28,stroke:#3BE592,color:#e3fff1
    style D fill:#0e3d28,stroke:#3BE592,color:#e3fff1
    style E fill:#114e34,stroke:#25CE7B,color:#ffffff
```

!!! warning "Atenção"
    No fluxo simplificado, o que você faz `push` vai direto para produção. Revise bem antes de commitar.

---

### Fluxo Completo — branches e Pull Requests

**Quando usar:** equipe maior, conteúdo que precisa de revisão antes de publicar, trabalhos longos em paralelo (ex.: um redator documenta o módulo Planning enquanto outro atualiza o Collab), ou quando erros no main causariam problemas visíveis para usuários do site.

O fluxo completo adiciona duas etapas entre o commit e a publicação: um **branch isolado** e um **Pull Request** com revisão. Para entender em detalhe o que são e como funcionam, veja o documento complementar: [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md).

```mermaid
flowchart LR
    A["🔄 git pull\nAtualizar"] --> B["🌿 checkout -b\nCriar branch"] --> C["✏️ Editar\narquivos .md"] --> D["📦 git add .\nRegistrar"]
    D --> E["💾 git commit\nCommitar"] --> F["🚀 git push\nEnviar branch"]
    F --> G["🔍 Pull Request\nRevisar"] --> H["✅ Merge\nPublicar"]
    style A fill:#0a2a1c,stroke:#1aa863,color:#d4ede0
    style B fill:#0e3a30,stroke:#34d399,color:#dafff2
    style C fill:#0c3322,stroke:#25CE7B,color:#dcfaea
    style D fill:#0e3d28,stroke:#3BE592,color:#e3fff1
    style E fill:#0e3d28,stroke:#3BE592,color:#e3fff1
    style F fill:#114e34,stroke:#25CE7B,color:#ffffff
    style G fill:#3a3408,stroke:#facc15,color:#fff6cf
    style H fill:#155f3f,stroke:#3BE592,color:#ffffff
```

---

## 4. Comandos Essenciais

> **Não é preciso decorar os comandos.** O que importa é entender o *conceito* de cada operação — o que ela faz e quando usar. Na prática do dia a dia, você vai executar a maioria dessas ações pelos botões do VS Code, sem digitar nada no terminal. Veja a seção [4. Git integrado no VS Code](./03-vscode-e-copilot.md#4-git-integrado-no-vs-code) do Módulo 3 para conhecer a interface visual.

---

### `git pull` — Atualizar seu repositório local

```bash
git pull
```

> **Sempre faça isso antes de começar a trabalhar.** Garante que você está partindo da versão mais recente.

---

### `git status` — Ver o que foi alterado

```bash
git status
```

Mostra os arquivos modificados, novos ou deletados desde o último commit.

---

### `git add` — Preparar arquivos para o commit

```bash
git add docs/collab/introducao.md      # arquivo específico
git add docs/collab/                   # uma pasta inteira
git add .                              # tudo que foi alterado
```

---

### `git commit` — Registrar as alterações

```bash
git commit -m "docs: adiciona introdução ao módulo Collab"
```

**Convenção de mensagens de commit** (recomendada):

| Prefixo | Quando usar |
|---------|-------------|
| `docs:` | Criação ou atualização de conteúdo de documentação |
| `fix:` | Correção de erro (link quebrado, informação errada) |
| `refactor:` | Reorganização de estrutura sem mudar o conteúdo |
| `chore:` | Alterações de configuração (mkdocs.yml, requirements.txt) |

---

### `git push` — Enviar para o repositório remoto

No **fluxo simplificado** (direto no main):

```bash
git push
```

No **fluxo completo** (branch dedicado) — veja [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md):

```bash
git push origin docs/guia-collab
```

---

### `git log` — Ver o histórico de commits

```bash
git log --oneline --graph
```

---

## 5. Situações Comuns

!!! tip "Conflitos são raros"
    Se a equipe sempre faz `git pull` antes de começar a trabalhar, conflitos quase nunca acontecem. As situações abaixo são para quando eles ocorrem.

### "Alguém atualizou o arquivo que eu também editei"

Isso gera um **conflito de merge**. O Git marca as diferenças no arquivo:

```
<<<<<<< HEAD
Texto que está no seu branch
=======
Texto que está no main
>>>>>>> main
```

Você precisa editar o arquivo manualmente, escolhendo qual versão manter (ou combinando as duas), e depois fazer um novo commit. O VS Code tem uma interface visual para resolver conflitos.

#### Walkthrough passo a passo: resolvendo um conflito no VS Code

**Situação:** você e um colega editaram o mesmo parágrafo do arquivo `docs/visao-geral.md` e agora, ao fazer `git pull`, o Git informa conflito.

---

**Passo 1 — Identificar o conflito**

O painel **Source Control** (`Ctrl+Shift+G`) exibe o arquivo com o ícone **C** (Conflict). Clique nele para abri-lo.

```
SOURCE CONTROL
  Merge Changes
    C  docs/visao-geral.md
```

---

**Passo 2 — Entender as marcações no arquivo**

O arquivo aberto mostrará algo como:

```
<<<<<<< HEAD (Current Change)
O AltoQi Visus é uma plataforma de gestão de obras baseada em BIM.
=======
O AltoQi Visus é um ambiente colaborativo para gestão de projetos BIM.
>>>>>>> origin/main (Incoming Change)
```

| Marcação | O que significa |
|---|---|
| `<<<<<<< HEAD` | Início da sua versão (local) |
| `=======` | Separador entre as duas versões |
| `>>>>>>> origin/main` | Fim da versão que veio do repositório remoto |

---

**Passo 3 — Escolher a resolução usando os botões do VS Code**

O VS Code exibe quatro botões diretamente acima do bloco de conflito no editor:

| Botão | O que faz |
|---|---|
| **Accept Current Change** | Mantém sua versão, descarta a do colega |
| **Accept Incoming Change** | Mantém a versão do colega, descarta a sua |
| **Accept Both Changes** | Insere as duas versões, uma após a outra |
| **Compare Changes** | Abre diff lado a lado para decidir com mais cuidado |

!!! tip "Na dúvida, use Compare Changes"
    O diff lado a lado facilita entender o que cada pessoa mudou antes de decidir qual versão manter — ou como combinar as duas manualmente.

---

**Passo 4 — Editar manualmente se necessário**

Se nenhum dos botões atende (por exemplo, você quer combinar partes das duas versões), apague as marcações `<<<<<<<`, `=======` e `>>>>>>>` manualmente e deixe o texto como deve ficar. O resultado final deve ser um arquivo limpo, sem nenhum marcador do Git.

!!! warning "Nunca commite com marcadores de conflito"
    Se o arquivo ainda contiver `<<<<<<< HEAD` ou `=======`, o conteúdo publicado ficará corrompido. Revise o arquivo inteiro antes de fazer o commit.

---

**Passo 5 — Fazer stage e commit da resolução**

Após salvar o arquivo resolvido:

1. No painel **Source Control**, clique em ![Add](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/add.svg){: .vscode-icon} ao lado do arquivo para fazer stage
2. Clique em ![Check](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/check.svg){: .vscode-icon} **Commit** (a mensagem sugerida `Merge branch 'origin/main'` já está preenchida)
3. Clique em **Sync Changes** para enviar o commit de merge

O conflito está resolvido. O histórico registrará que houve um merge e quem o resolveu.

---

### "Cometi um erro e quero desfazer antes de commitar"

```bash
git checkout -- docs/arquivo-errado.md   # descarta mudanças não commitadas
```

---

### "Já commitei algo errado"

```bash
git revert HEAD    # cria um novo commit que desfaz o último
```

> Não use `git reset --hard` sem entender o impacto — ele pode apagar commits irreversivelmente.

---

??? note "Glossário Rápido"
    | Termo | Significado |
    |---|---|
    | **Repository (repo)** | Pasta do projeto gerenciada pelo Git |
    | **Clone** | Baixar uma cópia completa do repositório para sua máquina |
    | **Commit** | Snapshot dos arquivos com mensagem descritiva |
    | **Push** | Enviar commits locais para o repositório remoto |
    | **Pull** | Baixar e integrar commits do repositório remoto |
    | **main** | Branch principal (produção) |
    | **Branch / PR** | Conceitos do fluxo completo — ver [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md) |

---

## Exercícios práticos

??? example "Exercício 1 — Seu primeiro clone e commit"
    **Objetivo:** executar o fluxo completo `clone → editar → commit → push` pela primeira vez.

    **Pré-requisito:** ter o Git instalado e acesso ao repositório de exercícios do curso.

    1. Abra o terminal (ou use `Ctrl+Shift+P` → `Git: Clone` no VS Code)
    2. Clone o repositório de exercícios:
       ```bash
       git clone https://github.com/andrebanki/github_para_docs.git
       ```
    3. Navegue até a pasta `docs/` e crie um arquivo com seu nome: `seu-nome.md`
    4. Escreva uma linha de texto qualquer no arquivo
    5. Salve, faça stage (`git add docs/seu-nome.md`) e commite:
       ```bash
       git commit -m "docs: adiciona arquivo de seu-nome"
       ```
    6. Faça push:
       ```bash
       git push
       ```

    ✅ **Resultado esperado:** seu arquivo aparece no repositório remoto no GitHub.

??? example "Exercício 2 — Simular e resolver um conflito"
    **Objetivo:** vivenciar um conflito de merge controlado e resolvê-lo no VS Code.

    1. Abra o arquivo `docs/conflito-exercicio.md` (peça ao instrutor para criá-lo no repositório de exercícios com um parágrafo)
    2. Antes de fazer `git pull`, edite o mesmo parágrafo localmente e commite
    3. Agora faça `git pull` — o Git vai reportar um conflito
    4. Abra o painel **Source Control** e localize o arquivo marcado com **C**
    5. Use o botão **Accept Both Changes** e depois ajuste o texto manualmente
    6. Faça stage, commite e push

    ✅ **Resultado esperado:** o conflito é resolvido e o histórico mostra um commit de merge.

??? example "Exercício 3 — Desfazer um commit"
    **Objetivo:** usar `git revert` com segurança.

    1. Faça uma edição pequena num arquivo qualquer e commite com a mensagem `"teste: commit para reverter"`
    2. No terminal, execute:
       ```bash
       git log --oneline -5
       ```
       Anote o hash do commit que acabou de fazer.
    3. Reverta esse commit:
       ```bash
       git revert HEAD
       ```
    4. Confirme a mensagem de commit gerada pelo Git (pode aceitar o padrão)
    5. Execute `git log --oneline -5` novamente e observe o novo commit de reversão

    ✅ **Resultado esperado:** o arquivo voltou ao estado anterior e o histórico registra a reversão — sem apagar nenhum commit.

!!! success "✅ Resumo do módulo"
    Git versiona sua documentação e evita que o trabalho de uma pessoa sobrescreva o de outra. Você viu os conceitos de **repositório, commit, clone, push e pull**, o fluxo diário (`pull` → editar → `add` → `commit` → `push`) e como lidar com conflitos e desfazer erros. Na prática, a maior parte dessas ações é feita pelos botões do VS Code — o importante é entender *o que cada operação faz*.

---

> **Leitura complementar:** [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md) — aprofundamento do fluxo completo  
> **Próximo módulo:** [02 — Markdown e MkDocs](./02-markdown-e-mkdocs.md)
