# Módulo 3 — VS Code e GitHub Copilot para Documentação

> **Para quem é este módulo:** toda a equipe que vai escrever documentação no VS Code com apoio de IA.

!!! abstract "🎯 Objetivos de aprendizagem"
    Neste módulo você vai aprender:

    - Por que usar o VS Code como editor de documentação
    - Como configurar o ambiente (extensões, preview, terminal)
    - Todos os comandos Git pelo VS Code (sem terminal)
    - Os 4 modos do GitHub Copilot e quando usar cada um
    - Boas práticas para IA generativa em documentação

---

## 1. Por que VS Code para documentação?

O VS Code (Visual Studio Code) é um editor de código gratuito da Microsoft, mas funciona igualmente bem para escrever documentação em Markdown. As vantagens para equipes de documentação:

- **Preview de Markdown em tempo real** — você vê o resultado enquanto escreve
- **Integração nativa com Git** — commit, push, pull, resolução de conflitos sem usar terminal
- **GitHub Copilot integrado** — IA que sugere, revisa e gera conteúdo
- **Extensões úteis** — spell check, formatação automática, preview do MkDocs
- **Terminal embutido** — para rodar `mkdocs serve` sem sair do editor

---

## 2. Configuração inicial do ambiente

### 2.1 Instalar o VS Code

Baixe em [https://code.visualstudio.com](https://code.visualstudio.com) e instale normalmente.

### 2.2 Abrir o repositório

No VS Code: `File → Open Folder` → selecione a pasta do repositório clonado (ex.: `visus_docs/`).

### 2.3 Extensões recomendadas

Instale pelo painel de extensões (clique em ![Extensions](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/extensions.svg){: .vscode-icon} na Barra de Atividades, ou `Ctrl+Shift+X`):

| Extensão | ID | Para que serve |
|---|---|---|
| **GitHub Copilot** | `GitHub.copilot` | Sugestões inline de IA |
| **GitHub Copilot Chat** | `GitHub.copilot-chat` | Chat de IA (painel lateral e agente) |
| **Markdown All in One** | `yzhang.markdown-all-in-one` | Atalhos, preview, sumário automático |
| **markdownlint** | `DavidAnson.vscode-markdownlint` | Valida a formatação do Markdown |
| **Code Spell Checker** | `streetsidesoftware.code-spell-checker` | Verificação ortográfica |
| **Brazilian Portuguese** | `streetsidesoftware.code-spell-checker-portuguese-brazilian` | Dicionário PT-BR |
| **Git Graph** | `mhutchie.git-graph` | Visualização do histórico de branches |

---

## 3. Preview de Markdown

Clique no ícone ![Open Preview](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/open-preview.svg){: .vscode-icon} no canto superior direito do editor para abrir o preview ao lado, ou pressione `Ctrl+Shift+V`.

**Dica:** use `Ctrl+K V` para abrir o preview em coluna separada, editando e visualizando ao mesmo tempo.

---

## 4. Git integrado no VS Code

O VS Code tem uma interface visual completa para Git — sem precisar do terminal para operações do dia a dia. Esta seção explica cada comando Git apresentado no [Módulo 1](./01-git-para-documentacao.md), mostrando tanto o comando de terminal quanto o equivalente visual no VS Code.

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

**No VS Code:** clique em ![Git Branch](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-branch.svg){: .vscode-icon} **nome do branch** na barra de status inferior (canto esquerdo) → selecione **Create new branch...** → digite o nome.

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
| `git checkout -b` | Cria branch | ![Git Branch](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-branch.svg){: .vscode-icon} barra de status | — |
| `git log` | Histórico de commits | ![Git Commit](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-commit.svg){: .vscode-icon} Git Graph | barra de status |
| `git checkout -- arquivo` | Descarta mudanças | — | Discard Changes (botão direito) |
| `git revert HEAD` | Desfaz último commit | — | Git Graph → Revert |

---

## 5. O que é o GitHub Copilot?

!!! warning "Licença necessária"
    O GitHub Copilot requer licença paga (individual ou via organização). Consulte seu gestor para verificar se sua conta já tem acesso.

O GitHub Copilot é um **assistente de IA integrado ao editor**. Ele foi treinado em bilhões de linhas de código e documentação e pode:

- **Completar frases e parágrafos** enquanto você digita (sugestões inline)
- **Responder perguntas** sobre o conteúdo do repositório
- **Gerar rascunhos** de páginas de documentação a partir de uma instrução
- **Revisar e melhorar** textos existentes
- **Responder dúvidas** sobre Git, MkDocs, Markdown

O Copilot lê o contexto dos arquivos abertos e do repositório inteiro para gerar respostas relevantes ao seu projeto específico.

---

## 6. Modos de uso do Copilot

Use o diagrama abaixo para decidir qual modo usar:

```mermaid
flowchart TD
    A{"O que você quer fazer?"} -->|Completar uma frase\nenquanto digita| B["Sugestões Inline\nTab para aceitar"]
    A -->|Inserir ou editar\num trecho específico| C["Chat Inline\nCtrl+I"]
    A -->|Fazer uma pergunta\nou pedir análise| D["Painel de Chat\nCtrl+Alt+I"]
    A -->|Tarefa de múltiplos passos\ncom leitura/escrita de arquivos| E["Modo Agente\nChat → Agent"]
    style B fill:#0a2a1c,stroke:#1aa863,color:#d4ede0
    style C fill:#0c3322,stroke:#25CE7B,color:#dcfaea
    style D fill:#0e3d28,stroke:#3BE592,color:#e3fff1
    style E fill:#0e3a30,stroke:#34d399,color:#dafff2
```

### 6.1 Sugestões inline (Completions)

Enquanto você digita, o Copilot sugere o texto seguinte em cinza. Pressione `Tab` para aceitar ou `Esc` para ignorar.

**Exemplo:** você digita:
```
## Acessando o módulo Collab pela primeira vez
```
O Copilot pode sugerir automaticamente o próximo parágrafo com base no contexto do arquivo.

---

### 6.2 Chat Inline (`Ctrl+I`)

Posicione o cursor onde quer inserir conteúdo e pressione `Ctrl+I` — ou clique com o botão direito → **Copilot → Start Inline Chat**. Um campo de input aparece diretamente no editor:

```
/doc Escreva uma introdução para esta seção sobre o módulo de Cotações
```

O Copilot gera o conteúdo e insere diretamente no arquivo. Você aceita ou rejeita.

---

### 6.3 Painel de Chat (`Ctrl+Alt+I`)

Clique em ![Copilot Chat](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/comment-discussion.svg){: .vscode-icon} na Barra de Atividades (ou pressione `Ctrl+Alt+I`) para abrir o painel de conversação ao lado do editor. Ideal para:
- Fazer perguntas sobre o conteúdo do repositório
- Pedir análises de estrutura
- Trabalhar em tarefas mais longas com múltiplos arquivos

**Exemplos de uso:**

```
Analise a página docs/collab/introducao.md e sugira melhorias de clareza
e estrutura para um público de engenheiros civis.
```

```
Quais páginas da documentação ainda não têm uma seção de "Pré-requisitos"?
```

```
Crie o rascunho de uma nova página para docs/bid/fornecedores.md com
frontmatter YAML seguindo o padrão do projeto.
```

---

### 6.4 Modo Agente

O **Modo Agente** (Agent Mode) é a forma mais poderosa do Copilot: ele executa tarefas de múltiplos passos de forma autônoma, lendo e escrevendo arquivos, rodando comandos no terminal e tomando decisões.

Para ativar: no painel de Chat, troque o modo de `Ask` para `Agent` no seletor.

**Exemplo de tarefa para o Agente:**

```
Leia todos os arquivos em docs/cost_management/ e crie um índice
em docs/cost_management/index.md listando todas as páginas com
seus títulos e uma linha de resumo de cada uma.
```

O agente vai ler cada arquivo, extrair o título e resumo, e criar o `index.md` automaticamente.

---

## 7. Boas práticas ao usar Copilot para documentação

### Dê contexto suficiente

O Copilot responde muito melhor quando você fornece contexto claro:

❌ Ruim:
```
Escreva sobre o módulo.
```

✅ Bom:
```
Escreva uma página de documentação para o módulo de Planejamento 4D do
AltoQi Visus. O público é de engenheiros civis que usam BIM. Siga o
frontmatter YAML do projeto (title, type, created, updated, sources, tags).
```

---

### Não publique sem revisar

O Copilot pode gerar informações incorretas (chamado de "alucinação"). **Toda saída gerada por IA deve ser revisada** antes de entrar em um commit.

Regra de ouro do projeto Visus:
> **Nunca invente conteúdo — toda informação deve ter origem em uma fonte fornecida pelo usuário.**

---

### Use o Copilot para consistência

Peça ao Copilot para:
- Verificar se a terminologia está consistente com outras páginas do repositório
- Garantir que o tom e estilo seguem o padrão estabelecido
- Identificar links internos quebrados ou páginas referenciadas que não existem

---

## 8. Atalhos Essenciais no VS Code

| Ação | Ícone / Onde Clicar | Atalho |
|---|---|---|
| Abrir painel de Chat do Copilot | ![Copilot Chat](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/comment-discussion.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Alt+I` |
| Inline Chat | Botão direito → Copilot → Start Inline Chat | `Ctrl+I` |
| Aceitar sugestão inline | Sugestão em cinza → aceitar | `Tab` |
| Rejeitar sugestão inline | Sugestão em cinza → ignorar | `Esc` |
| Preview de Markdown | ![Open Preview](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/open-preview.svg){: .vscode-icon} canto superior direito do editor | `Ctrl+Shift+V` |
| Preview ao lado | ![Open Preview](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/open-preview.svg){: .vscode-icon} (abre em coluna separada) | `Ctrl+K V` |
| Source Control (Git) | ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Shift+G` |
| Extensões | ![Extensions](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/extensions.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Shift+X` |
| Terminal integrado | ![Terminal](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/terminal.svg){: .vscode-icon} menu View → Terminal | Ctrl+` |
| Paleta de comandos | — | `Ctrl+Shift+P` |
| Buscar em todos os arquivos | ![Search](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/search.svg){: .vscode-icon} Barra de Atividades | `Ctrl+Shift+F` |

---

!!! info "Exercícios práticos"
    Os exercícios deste módulo foram reunidos no [Módulo Extra — Exercícios Práticos](./exercicios-praticos.md).

!!! success "✅ Resumo do módulo"
    O **VS Code** concentra edição, preview e Git em um só lugar. Você configurou o ambiente (extensões, preview e terminal), aprendeu a executar todas as operações Git pela interface visual — sem digitar comandos — e conheceu os **4 modos do GitHub Copilot** e quando usar cada um na documentação.

---

> **Módulo anterior:** [02 — Markdown e MkDocs](./02-markdown-e-mkdocs.md)  
> **Próximo módulo:** [04 — Personalizando o Copilot](./04-copilot-customizacao.md)
