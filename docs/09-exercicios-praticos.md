# Módulo 9 — Exercícios Práticos

> Este módulo reúne os exercícios práticos do curso, organizados na ordem natural do fluxo de trabalho. Use-o como revisão ao final da trilha ou faça cada exercício logo após o módulo correspondente.
>
> **Por que este módulo vem por último:** o fechamento consolida a trilha inteira em prática guiada, sem interromper o fluxo de aprendizagem dos módulos principais. A ideia é praticar depois que o caminho completo já fez sentido.

!!! abstract "🎯 Como usar este módulo"
    São **5 exercícios** focados no que você realmente vai fazer no dia a dia. Como na prática a escrita de Markdown é feita **com a ajuda do Claude Code**, não há exercícios de sintaxe — o foco está no fluxo Git e no uso da IA. Cada exercício indica o módulo que reforça e o resultado esperado, para você saber se está no caminho certo.

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

> **Módulo anterior:** [08 — Instruções Específicas](./08-instrucoes-especificas.md)  
> **Índice:** [Início](./index.md)
