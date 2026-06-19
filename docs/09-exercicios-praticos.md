# Módulo 9 — Exercícios Práticos

> Este módulo reúne os exercícios práticos do curso, organizados na ordem natural do fluxo de trabalho. Use-o como revisão ao final da trilha ou faça cada exercício logo após o módulo correspondente.
>
> **Por que este módulo vem por último:** o fechamento consolida a trilha inteira em prática guiada, sem interromper o fluxo de aprendizagem dos módulos principais. A ideia é praticar depois que o caminho completo já fez sentido.

!!! abstract "🎯 Como usar este módulo"
    São **10 exercícios** focados no que você realmente vai fazer no dia a dia. Como na prática a escrita de Markdown é feita **com a ajuda do Claude Code**, não há exercícios de sintaxe — o foco está no fluxo Git, no uso da IA e na publicação. Cada exercício indica o módulo que reforça e o resultado esperado, para você saber se está no caminho certo.

!!! note "Pré-requisitos"
    A maioria dos exercícios depende do ambiente configurado no **Módulo 1** e de **acesso ao repositório de exercícios** do curso. Se ainda não instalou Git, Python e VS Code, comece pelo Exercício 1.

    Repositório de exercícios: `https://github.com/andrebanki/github_para_docs.git`

---

## Mapa dos exercícios

| # | Exercício | Reforça |
|---|---|---|
| 1 | Preparar o ambiente e rodar o site localmente | [Módulo 1](./01-setup-ambiente.md) |
| 2 | O ciclo diário no VS Code (sem terminal) | [Módulo 2](./02-git-para-documentacao.md) |
| 3 | Deixe a IA escrever o Markdown | [Módulos 3](./03-markdown-e-mkdocs.md) e [4](./04-claude-code.md) |
| 4 | Revisar e reescrever uma página com o Claude Code | [Módulo 4](./04-claude-code.md) |
| 5 | Tarefa autônoma no Modo Agente | [Módulo 4](./04-claude-code.md) |
| 6 | Branch e Pull Request de ponta a ponta | [Módulo 5](./05-branches-e-pull-requests.md) |
| 7 | Resolver um conflito de merge no VS Code | [Módulo 5](./05-branches-e-pull-requests.md) |
| 8 | Publicar no GitHub Pages e acompanhar o deploy | [Módulo 6](./06-publicacao-externa.md) |
| 9 | Personalizar o Claude Code com um comando | [Módulo 7](./07-claude-code-customizacao.md) |
| 10 | Documentar uma feature do TargetProcess | [Módulo 8](./08-instrucoes-especificas.md) |

---

## Exercício 1 — Preparar o ambiente e rodar o site localmente

> Reforça o **[Módulo 1 — VS Code e Configuração do Ambiente](./01-setup-ambiente.md)**

??? example "Abrir exercício"
    **Objetivo:** ter o ambiente completo funcionando e ver a documentação rodando no navegador.

    1. Instale **Git**, **Python 3.10+** e **VS Code** (links no Módulo 1)
    2. No VS Code, pressione `Ctrl+Shift+P` → **Git: Clone**, cole a URL do repositório de exercícios, escolha uma pasta e clique em **Open**
    3. Instale as extensões recomendadas (`Ctrl+Shift+X`): **Claude Code**, **Markdown All in One**, **markdownlint**, **Code Spell Checker** (+ dicionário PT-BR) e **Git Graph**
    4. Abra o terminal integrado (`Ctrl+\``) e execute:
        ```bash
        pip install -r requirements.txt
        ```
    5. Ainda no terminal, rode o site localmente:
        ```bash
        mkdocs serve
        ```
    6. Abra `http://localhost:8000` no navegador e navegue pelo material

    ✅ **Resultado esperado:** `git --version` e `python --version` (ou `py --version`) funcionam, o repositório está aberto no VS Code e o site carrega localmente.

---

## Exercício 2 — O ciclo diário no VS Code, sem terminal

> Reforça o **[Módulo 2 — Git para Documentação](./02-git-para-documentacao.md)**

??? example "Abrir exercício"
    **Objetivo:** executar o ciclo `pull → editar → commit → push` pela interface visual e saber desfazer com segurança.

    1. Abra o painel **Source Control** (`Ctrl+Shift+G`) e faça **Pull** (menu **...** → **Pull**, ou **Sync Changes**)
    2. Crie o arquivo `docs/seu-nome.md` com um título e uma linha de texto
    3. Clique em **+** ao lado do arquivo para fazer **stage**, escreva a mensagem `docs: adiciona pagina de seu-nome` e clique em **Commit** (✓)
    4. Clique em **Sync Changes** para enviar ao remoto
    5. No GitHub, confirme que o arquivo e a **mensagem do commit** aparecem na pasta `docs/`
    6. **Desfazer mudanças não commitadas:** edite o arquivo, salve e, no Source Control, clique com o botão direito → **Discard Changes**
    7. **Desfazer um commit já feito:** faça um commit qualquer e reverta com a extensão **Git Graph** → botão direito no commit → **Revert** (equivale a `git revert HEAD`)

    ✅ **Resultado esperado:** seu arquivo aparece no repositório remoto e você consegue desfazer alterações tanto antes quanto depois de commitar — sem usar o terminal.

---

## Exercício 3 — Deixe a IA escrever o Markdown

> Reforça os **[Módulos 3](./03-markdown-e-mkdocs.md) e [4](./04-claude-code.md)**

??? example "Abrir exercício"
    **Objetivo:** gerar uma página completa com o Claude Code e conferir o resultado no preview — sem digitar sintaxe Markdown na mão.

    1. Abra o **Claude Code** (ícone na Barra de Atividades)
    2. Peça, dando contexto claro:
        ```
        Crie a página docs/exemplo-funcionalidade.md documentando uma
        funcionalidade fictícia de relatórios do AltoQi Visus, para um público
        de engenheiros civis que usam BIM. Inclua: frontmatter YAML (title, type,
        created, updated), títulos H2/H3, uma tabela, uma lista e uma admonition
        !!! tip.
        ```
    3. Revise o **diff** proposto e aceite a criação do arquivo
    4. Abra o **preview** (`Ctrl+K V`) e confira se títulos, tabela e admonition renderizam corretamente
    5. Veja também a página no `mkdocs serve` (`http://localhost:8000`)

    ✅ **Resultado esperado:** uma página bem formatada, gerada pela IA, renderizando corretamente — sem que você precise lembrar a sintaxe de tabelas, admonitions ou frontmatter.

---

## Exercício 4 — Revisar e reescrever uma página com o Claude Code

> Reforça o **[Módulo 4 — Claude Code](./04-claude-code.md)**

??? example "Abrir exercício"
    **Objetivo:** usar a **Edição pelo Chat**, referenciando um arquivo com `#`, e aprovar mudança a mudança.

    1. No painel de chat, digite `#` e selecione a página criada no exercício anterior:
        ```
        #exemplo-funcionalidade.md Reescreva a introdução em um tom mais direto e
        técnico e padronize a terminologia BIM ao longo da página.
        ```
    2. Revise o **diff** e aceite ou rejeite **cada trecho** — nada é alterado sem sua confirmação
    3. Em seguida, peça uma verificação de qualidade:
        ```
        Verifique se há links internos quebrados, seções vazias ou termos
        inconsistentes nesta página.
        ```
    4. Aplique as correções sugeridas que fizerem sentido

    ✅ **Resultado esperado:** a página foi melhorada com a sua aprovação explícita, e você consegue distinguir entre "pedir uma análise" e "pedir uma edição".

---

## Exercício 5 — Tarefa autônoma no Modo Agente

> Reforça o **[Módulo 4 — Claude Code](./04-claude-code.md)**

??? example "Abrir exercício"
    **Objetivo:** executar uma tarefa de **múltiplos passos** no Modo Agente (aba **CLAUDE CODE**).

    1. Abra a aba **CLAUDE CODE** (não a aba CHAT) no topo do painel — esse é o modo agente
    2. Peça uma tarefa que exija ler e escrever vários arquivos:
        ```
        Leia todas as páginas .md de docs/ e crie docs/indice-exercicios.md
        listando cada página com seu título e uma linha de resumo.
        ```
    3. Acompanhe as ferramentas sendo chamadas em tempo real (leitura, escrita) e **confirme** as edições quando solicitado
    4. Abra `docs/indice-exercicios.md` no preview e confira o resultado

    ✅ **Resultado esperado:** o agente leu múltiplas páginas e produziu um índice coerente em sequência, com a sua confirmação a cada passo sensível.

---

## Exercício 6 — Branch e Pull Request de ponta a ponta

> Reforça o **[Módulo 5 — Branches e Pull Requests](./05-branches-e-pull-requests.md)**

??? example "Abrir exercício"
    **Objetivo:** isolar o trabalho em um branch e publicá-lo via Pull Request revisado.

    1. Crie um branch: clique no nome do branch na barra de status → **Create new branch...** → `docs/exercicio-pr-seu-nome`
    2. Peça ao Claude Code para criar ou ajustar uma página; faça **commit** no branch e **Sync Changes** (o VS Code pergunta se deve publicar o branch — confirme)
    3. No GitHub, clique na faixa **Compare & pull request**, escreva título e descrição e atribua um **revisor**
    4. O revisor abre **Files changed**, adiciona um comentário em uma linha; você responde e ajusta com um **novo commit** no mesmo branch
    5. Após **Approve**, clique em **Merge pull request** e **delete o branch**

    ✅ **Resultado esperado:** o conteúdo chega ao `main` via PR revisado, com histórico de comentários, e o site é atualizado automaticamente após o merge.

---

## Exercício 7 — Resolver um conflito de merge no VS Code

> Reforça o **[Módulo 5 — Branches e Pull Requests](./05-branches-e-pull-requests.md)**

??? example "Abrir exercício"
    **Objetivo:** reproduzir um conflito real entre dois branches e resolvê-lo visualmente.

    1. No `main`, crie `docs/conflito.md` com o texto `Versão original` e commite
    2. Crie dois branches que editam **a mesma linha**:
        ```bash
        git checkout -b docs/branch-a
        # edite docs/conflito.md → "Versão do branch A"
        git add . ; git commit -m "docs: versão A"

        git checkout main
        git checkout -b docs/branch-b
        # edite docs/conflito.md → "Versão do branch B"
        git add . ; git commit -m "docs: versão B"
        ```
    3. Faça merge do `branch-a` no `main`; depois tente o merge do `branch-b` → o Git reporta **conflito**
    4. No **Source Control**, abra o arquivo marcado com **C**; use **Compare Changes** e **Accept Both Changes** (ou edite à mão), removendo **todos** os marcadores `<<<<<<<`, `=======` e `>>>>>>>`
    5. Faça **stage** e **commit** da resolução

    ✅ **Resultado esperado:** o conflito é resolvido, o arquivo final fica limpo (sem marcadores) e o histórico registra o commit de merge.

---

## Exercício 8 — Publicar no GitHub Pages e acompanhar o deploy

> Reforça o **[Módulo 6 — Publicando para Acesso Externo](./06-publicacao-externa.md)**

??? example "Abrir exercício"
    **Objetivo:** ativar a publicação automática e saber ler o pipeline quando algo falha.

    1. (Feito pelo dono do repositório) **Settings → Pages** → **Deploy from a branch** → branch `gh-pages`; confirme que existe `.github/workflows/deploy.yml`
    2. Faça uma alteração pequena em qualquer `.md` e dê **push** no `main` (ou faça merge de um PR)
    3. Na aba **Actions** do GitHub, acompanhe a execução do workflow `deploy.yml` — observe a etapa que instala dependências e a que roda `mkdocs gh-deploy`
    4. Acesse a URL pública e confirme que a alteração apareceu
    5. **(Opcional)** Introduza um erro de sintaxe no `mkdocs.yml`, dê push e veja a etapa que falha no log; depois corrija e publique novamente

    ✅ **Resultado esperado:** a alteração entra no ar em poucos minutos e você sabe onde acompanhar e diagnosticar um deploy.

---

## Exercício 9 — Personalizar o Claude Code com um comando

> Reforça o **[Módulo 7 — Personalizando o Claude Code](./07-claude-code-customizacao.md)**

??? example "Abrir exercício"
    **Objetivo:** criar um comando reutilizável e fazer o agente seguir o padrão do projeto.

    1. Crie o arquivo `.claude/commands/nova-pagina.md` com o frontmatter e as instruções (use o exemplo do Módulo 7):
        ```markdown
        ---
        description: Cria uma nova página seguindo o padrão do projeto
        allowed-tools: Read, Write, Edit
        ---
        Crie uma nova página de documentação em $ARGUMENTS, com o frontmatter YAML
        padrão (title, type, created, updated, sources, tags) e a estrutura:
        resumo de uma linha → corpo com H2/H3 → links relacionados.
        ```
    2. **(Opcional)** Crie ou ajuste o `CLAUDE.md` na raiz com o papel do agente, a estrutura de pastas e a regra de ouro "nunca inventar conteúdo"
    3. No chat, invoque o comando: `/nova-pagina docs/teste-comando.md`
    4. Confira se o rascunho gerado segue exatamente o template definido

    ✅ **Resultado esperado:** o comando aparece na lista `/` e gera páginas consistentes com o padrão, sem você repetir o prompt longo toda vez.

---

## Exercício 10 — Documentar uma feature do TargetProcess

> Reforça o **[Módulo 8 — Instruções Específicas](./08-instrucoes-especificas.md)**

??? example "Abrir exercício"
    **Objetivo:** praticar a **Dica 1** — transformar um card técnico em documentação orientada ao usuário final.

    1. No **Modo Agente**, cole um card simulado do TargetProcess:
        ```
        Feature 999001 — Exportação de relatório em PDF
        Descrição: o usuário pode exportar o relatório de progresso do projeto em
        PDF, com opção de incluir ou excluir gráficos.
        Critérios de aceite:
        - Botão "Exportar PDF" na tela de relatórios
        - Opções: incluir gráficos (sim/não), orientação (retrato/paisagem)
        - PDF gerado com o logo da empresa no cabeçalho
        ```
    2. Peça:
        ```
        Crie uma página de documentação para o usuário final com base nesta feature.
        Exclua detalhes de implementação e foque no comportamento visível. Use o
        frontmatter padrão do projeto.
        ```
    3. Verifique se o agente: **excluiu** os critérios técnicos, **focou** na interface e nas opções visíveis, e **criou** o frontmatter correto

    ✅ **Resultado esperado:** uma página orientada ao usuário, sem jargão de desenvolvimento — uma interpretação do card, não uma cópia.

---

> **Módulo anterior:** [08 — Instruções Específicas](./08-instrucoes-especificas.md)  
> **Índice:** [Início](./index.md)
