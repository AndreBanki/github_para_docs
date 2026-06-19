# Módulo 1 — VS Code e Configuração do Ambiente

> **Para quem é este módulo:** toda a equipe que vai escrever documentação no VS Code.
>
> **Por que este módulo vem primeiro:** antes de entender o fluxo de versionamento e escrever conteúdo, você precisa ter o ambiente pronto — ferramentas instaladas, repositório aberto e o site rodando localmente. Este módulo prepara a base prática usada em toda a trilha.

!!! abstract "🎯 Objetivos de aprendizagem"
    Neste módulo você vai aprender:

    - Quais programas instalar primeiro para começar a trabalhar
    - Por que usar o VS Code como editor de documentação
    - Como configurar o ambiente (Git, Python, VS Code, extensões, preview e terminal)
    - Todos os comandos Git pelo VS Code (sem terminal)

---

## 1. Por que VS Code para documentação?

O VS Code (Visual Studio Code) é um editor de código gratuito da Microsoft, mas funciona igualmente bem para escrever documentação em Markdown. As vantagens para equipes de documentação:

- **Preview de Markdown em tempo real** — você vê o resultado enquanto escreve
- **Integração nativa com Git** — commit, push, pull, resolução de conflitos sem usar terminal
- **Claude Code integrado** — IA que sugere, revisa e gera conteúdo (ver [Módulo 4](./04-claude-code.md))
- **Extensões úteis** — spell check, formatação automática, preview do MkDocs
- **Terminal embutido** — para rodar `mkdocs serve` sem sair do editor

---

## 2. Configuração inicial do ambiente

Este é o módulo de **setup** da trilha. Ao final desta seção, você deve ter tudo instalado e funcionando para conseguir clonar o repositório, abrir a documentação e visualizar o site localmente.

### 2.1 Instalar o Git

Baixe em [https://git-scm.com](https://git-scm.com) e instale com as opções padrão.

Depois da instalação, abra um terminal e verifique:

```bash
git --version
```

Se um número de versão aparecer, o Git está pronto para uso.

### 2.2 Instalar o Python

Baixe em [https://www.python.org](https://www.python.org) a versão 3.10 ou superior.

Durante a instalação no Windows, marque a opção para adicionar o Python ao `PATH`. Depois confirme no terminal:

```bash
python --version
```

Se sua máquina usar o Python Launcher, o comando também pode ser:

```bash
py --version
```

### 2.3 Instalar o VS Code

Baixe em [https://code.visualstudio.com](https://code.visualstudio.com) e instale normalmente.

### 2.4 Instalar as extensões recomendadas

Instale pelo painel de extensões (clique em ![Extensions](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/extensions.svg){: .vscode-icon} na Barra de Atividades, ou `Ctrl+Shift+X`):

| Extensão | ID | Para que serve |
|---|---|---|
| **Claude Code** | `Anthropic.claude-code` | Chat de IA, edição guiada e modo agente |
| **Markdown All in One** | `yzhang.markdown-all-in-one` | Atalhos, preview, sumário automático |
| **markdownlint** | `DavidAnson.vscode-markdownlint` | Valida a formatação do Markdown |
| **Code Spell Checker** | `streetsidesoftware.code-spell-checker` | Verificação ortográfica |
| **Brazilian Portuguese** | `streetsidesoftware.code-spell-checker-portuguese-brazilian` | Dicionário PT-BR |
| **Git Graph** | `mhutchie.git-graph` | Visualização do histórico de branches |

### 2.5 Clonar e abrir o repositório

Se o repositório ainda não estiver na sua máquina, use `Ctrl+Shift+P` → **Git: Clone**, cole a URL do repositório, escolha a pasta de destino e aguarde o download.

No VS Code: `File → Open Folder` → selecione a pasta do repositório clonado (ex.: `visus_docs/`).

### 2.6 Instalar as dependências do projeto

Com o repositório já aberto no VS Code, abra o terminal integrado e execute:

```bash
pip install -r requirements.txt
```

Isso instala o MkDocs e os plugins usados pelo projeto.

!!! tip "Checklist rápido de setup"
    Antes de seguir para os próximos tópicos, confirme:

    - `git --version` funciona
    - `python --version` ou `py --version` funciona
    - o repositório está aberto no VS Code
    - as extensões principais foram instaladas
    - `pip install -r requirements.txt` terminou sem erro

---

## 3. Preview de Markdown

Clique no ícone ![Open Preview](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/open-preview.svg){: .vscode-icon} no canto superior direito do editor para abrir o preview ao lado, ou pressione `Ctrl+Shift+V`.

**Dica:** use `Ctrl+K V` para abrir o preview em coluna separada, editando e visualizando ao mesmo tempo.

---

## 4. Git integrado no VS Code

O VS Code tem uma interface visual completa para Git — sem precisar do terminal para operações do dia a dia. Esta seção explica cada comando Git apresentado no [Módulo 2](./02-git-para-documentacao.md), mostrando tanto o comando de terminal quanto o equivalente visual no VS Code.

---

### `git clone` — Baixar o repositório pela primeira vez

```bash
git clone https://github.com/altoqi/visus-docs.git
```

Cria uma cópia local completa do repositório remoto, incluindo todo o histórico de commits. É feito **uma única vez por máquina**.

**No VS Code:** `Ctrl+Shift+P` → `Git: Clone` → cole a URL do repositório → escolha a pasta de destino.

---

### `git pull` — Atualizar seu repositório local

```bash
git pull
```

Baixa os commits mais recentes do repositório remoto e integra ao seu branch local. **Sempre execute antes de começar a trabalhar** para evitar conflitos desnecessários.

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control (`Ctrl+Shift+G`) → menu ![Ellipsis](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/ellipsis.svg){: .vscode-icon} → **Pull**.  
Ou clique em ![Sync](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/sync.svg){: .vscode-icon} **Sync Changes** na barra de status inferior (sincroniza pull + push).

---

### `git status` — Ver o que foi alterado

```bash
git status
```

Lista os arquivos modificados, adicionados ou deletados desde o último commit, indicando o que está preparado para commit e o que ainda não está.

**No VS Code:** o Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control (`Ctrl+Shift+G`) exibe isso continuamente e de forma visual — arquivos com `M` (modified), `U` (untracked), `D` (deleted) ao lado de cada nome.

---

### `git add` — Preparar arquivos para o commit

```bash
git add docs/collab/introducao.md      # arquivo específico
git add docs/collab/                   # uma pasta inteira
git add .                              # tudo que foi alterado
```

Move os arquivos para a **staging area**: uma área intermediária onde você decide exatamente o que vai entrar no próximo commit. Um commit só inclui o que foi adicionado com `git add`.

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control → clique em ![Add](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/add.svg){: .vscode-icon} ao lado de cada arquivo em "Changes" para fazer stage. Para adicionar tudo de uma vez, clique em ![Add](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/add.svg){: .vscode-icon} ao lado do título "Changes".

---

### `git commit` — Registrar as alterações

```bash
git commit -m "docs: adiciona introdução ao módulo Collab"
```

Cria um snapshot permanente dos arquivos que estão na staging area, com uma mensagem descritiva. O commit existe apenas no repositório **local** até que você faça `git push`.

**Convenção de mensagens:**

| Prefixo | Quando usar |
|---|---|
| `docs:` | Criação ou atualização de conteúdo |
| `fix:` | Correção de erro (link quebrado, informação errada) |
| `refactor:` | Reorganização sem mudar conteúdo |
| `chore:` | Alterações de configuração (mkdocs.yml, etc.) |

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control → escreva a mensagem no campo de texto → pressione `Ctrl+Enter` ou clique em ![Check](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/check.svg){: .vscode-icon} **Commit**.

---

### `git push` — Enviar para o repositório remoto

No **fluxo simplificado** (direto no `main`):
```bash
git push
```

No **fluxo completo** (branch dedicado):
```bash
git push origin docs/guia-collab
```

Envia seus commits locais para o repositório remoto. No fluxo simplificado, isso publica diretamente. No fluxo completo, apenas sobe o branch — a publicação acontece só após o merge do Pull Request.

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control → clique em ![Sync](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/sync.svg){: .vscode-icon} **Sync Changes** (faz pull + push) ou menu ![Ellipsis](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/ellipsis.svg){: .vscode-icon} → **Push**.

---

### `git checkout -b` — Criar e entrar em um novo branch

```bash
git checkout -b docs/nome-da-tarefa
```

Cria um novo branch a partir do estado atual e já muda para ele. Usado no início do **fluxo completo** para isolar o trabalho do `main`. O nome deve descrever a tarefa (ex.: `docs/modulo-bid`, `fix/link-quebrado-collab`).

**No VS Code:** clique em ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} **nome do branch** na barra de status inferior (canto esquerdo) → selecione **Create new branch...** → digite o nome.

---

### `git log` — Ver o histórico de commits

```bash
git log --oneline --graph
```

Exibe o histórico de commits em formato compacto (uma linha por commit) com um grafo ASCII mostrando a estrutura de branches. Útil para entender o que foi feito e por quem.

**No VS Code:** com a extensão **Git Graph** instalada, clique em ![Git Commit](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-commit.svg){: .vscode-icon} **Git Graph** na barra de status inferior para ver o histórico de forma visual, com branches coloridos e detalhes de cada commit ao clicar.

---

### `git checkout -- arquivo` — Descartar mudanças não commitadas

```bash
git checkout -- docs/arquivo-errado.md
```

Descarta todas as alterações feitas no arquivo desde o último commit, restaurando-o para o estado salvo. **Atenção: irreversível** — o que foi alterado e não commitado é perdido.

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control → clique com o botão direito no arquivo → **Discard Changes**.

---

### `git revert` — Desfazer um commit já registrado

```bash
git revert HEAD
```

Cria um **novo commit** que desfaz as mudanças do commit anterior. É a forma segura de reverter algo que já foi commitado, porque preserva o histórico.

> Prefira `git revert` a `git reset --hard`, que apaga commits de forma irreversível e pode causar problemas para outros colaboradores.

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control → extensão **Git Graph** → clique com o botão direito no commit que quer desfazer → **Revert**.

---

### Resolver conflitos visualmente

Quando dois colaboradores editam o mesmo trecho de um arquivo, o Git gera um **conflito de merge**. O VS Code exibe os dois lados com botões de resolução:

- **Accept Current Change** — mantém o que está no seu branch
- **Accept Incoming Change** — mantém o que veio do remoto
- **Accept Both Changes** — mantém os dois trechos
- **Compare Changes** — mostra o diff lado a lado

Após resolver todos os conflitos, faça `git add` nos arquivos resolvidos e depois `git commit` para finalizar o merge.

---

### Resumo: comandos × VS Code

| Comando | O que faz | Ícone / Botão no VS Code | Atalho / Ação |
|---|---|---|---|
| `git clone` | Baixa o repositório | — | `Ctrl+Shift+P` → Git: Clone |
| `git pull` | Atualiza do remoto | ![Sync](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/sync.svg){: .vscode-icon} Sync Changes | ![Ellipsis](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/ellipsis.svg){: .vscode-icon} → Pull |
| `git status` | Lista arquivos alterados | ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control | `Ctrl+Shift+G` |
| `git add` | Prepara para commit | ![Add](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/add.svg){: .vscode-icon} ao lado do arquivo | — |
| `git commit -m` | Salva o snapshot | ![Check](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/check.svg){: .vscode-icon} Commit | `Ctrl+Enter` |
| `git push` | Envia ao remoto | ![Sync](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/sync.svg){: .vscode-icon} Sync Changes | ![Ellipsis](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/ellipsis.svg){: .vscode-icon} → Push |
| `git checkout -b` | Cria branch | ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} barra de status | — |
| `git log` | Histórico de commits | ![Git Commit](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-commit.svg){: .vscode-icon} Git Graph | barra de status |
| `git checkout -- arquivo` | Descarta mudanças | — | Discard Changes (botão direito) |
| `git revert HEAD` | Desfaz último commit | — | Git Graph → Revert |

---

## 5. Atalhos Essenciais no VS Code

| Ação | Ícone / Onde Clicar | Atalho |
|---|---|---|
| Abrir Claude Code (chat) | Ícone Claude na Barra de Atividades | — |
| Terminal integrado (para `claude` CLI) | ![Terminal](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/terminal.svg){: .vscode-icon} menu View → Terminal | Ctrl+` |
| Preview de Markdown | ![Open Preview](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/open-preview.svg){: .vscode-icon} canto superior direito do editor | `Ctrl+Shift+V` |
| Preview ao lado | ![Open Preview](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/open-preview.svg){: .vscode-icon} (abre em coluna separada) | `Ctrl+K V` |
| Source Control (Git) | ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Shift+G` |
| Extensões | ![Extensions](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/extensions.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Shift+X` |
| Paleta de comandos | — | `Ctrl+Shift+P` |
| Buscar em todos os arquivos | ![Search](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/search.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Shift+F` |

---

!!! success "✅ Resumo do módulo"
    O **VS Code** concentra edição, preview e Git em um só lugar. Você configurou o ambiente completo (**Git, Python, VS Code, extensões e dependências do projeto**) e aprendeu a executar todas as operações Git pela interface visual — sem digitar comandos no terminal. Com a base pronta, a trilha segue para o raciocínio de versionamento e a produção de conteúdo.

---

> **Próximo módulo:** [02 — Git para Documentação](./02-git-para-documentacao.md)
