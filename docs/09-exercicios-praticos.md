# Módulo 9 — Exercícios Práticos

> Este módulo reúne todos os exercícios práticos do curso, organizados na mesma ordem da trilha principal. Use-o como revisão ao final do curso ou volte ao exercício correspondente após cada módulo.
>
> **Por que este módulo vem por último:** este fechamento existe para consolidar a trilha inteira em prática guiada, sem interromper o fluxo de aprendizagem dos módulos principais. A ideia é praticar depois que o caminho completo já fez sentido.

!!! abstract "🎯 Como usar este módulo"
    Os exercícios são independentes entre si — você pode fazê-los em ordem ou voltar a qualquer um quando precisar praticar um conceito específico. Cada exercício indica o resultado esperado para que você saiba se está no caminho certo.

---

## Módulo 1 — Git para Documentação

> [← Voltar ao módulo](./02-git-para-documentacao.md)

!!! note "Quando fazer estes exercícios"
     Embora estejam agrupados no Módulo 1 por assunto, estes exercícios dependem do ambiente configurado no Módulo 2. Se ainda não instalou Git, Python e VS Code, faça primeiro o exercício inicial do Módulo 2.

??? example "Exercício 1 — Seu primeiro clone e commit"
    **Objetivo:** executar o fluxo completo `clone → editar → commit → push` pela primeira vez.

     **Pré-requisito:** ter concluído o setup do Módulo 2 e ter acesso ao repositório de exercícios do curso.

     1. Abra o **VS Code** e use `Ctrl+Shift+P` → **Git: Clone**
     2. Cole a URL do repositório de exercícios: `https://github.com/andrebanki/github_para_docs.git`
     3. Escolha uma pasta local, aguarde o clone terminar e clique em **Open**
     4. Na pasta `docs/`, crie um arquivo com seu nome: `seu-nome.md`
     5. Escreva uma linha de texto qualquer no arquivo
     6. Salve, faça stage (`git add docs/seu-nome.md`) e commite:
         ```bash
         git commit -m "docs: adiciona arquivo de seu-nome"
         ```
     7. Faça push:
         ```bash
         git push
         ```
     8. Verifique o resultado no GitHub:
       - Acesse **[github.com/andrebanki/github_para_docs](https://github.com/andrebanki/github_para_docs)**
       - Clique na pasta **`docs/`**
       - Confirme que o arquivo `seu-nome.md` aparece na listagem
       - Clique no arquivo para ver o conteúdo — e confira a mensagem do seu commit ao lado do nome do arquivo

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

---

## Módulo 2 — VS Code e GitHub Copilot

> [← Voltar ao módulo](./02-vscode-e-copilot.md)

??? example "Exercício 1 — Configurar o ambiente"
    **Objetivo:** verificar que o ambiente está funcionando corretamente.

    1. Confirme no terminal que `git --version` funciona
    2. Confirme no terminal que `python --version` ou `py --version` funciona
    3. Instale as extensões recomendadas listadas na seção 2.4 (use `Ctrl+Shift+X` para abrir o painel)
    4. Abra o repositório do curso no VS Code (`File → Open Folder`)
    5. Abra o terminal integrado (Ctrl+`) e execute `pip install -r requirements.txt`, se ainda não tiver feito isso
    6. Abra o arquivo `docs/02-git-para-documentacao.md` e pressione `Ctrl+K V` para o preview ao lado
    7. Execute `mkdocs serve`
    8. Acesse `http://localhost:8000` e confirme que o site carrega

    ✅ **Resultado esperado:** Git, Python, VS Code e o site local estão funcionando no mesmo ambiente.

??? example "Exercício 2 — Commit via interface visual do VS Code"
    **Objetivo:** executar o fluxo completo `pull → editar → commit → push` sem usar o terminal.

    1. Clique em ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} na Barra de Atividades e verifique se há alterações pendentes
    2. Clique no ícone **↓ Pull** (ou no ícone de sincronização) para atualizar o repositório
    3. Crie o arquivo `docs/anotacoes-vscode.md` com um título H1 e um parágrafo curto
    4. No painel Source Control, clique em **+** ao lado do arquivo para fazer stage
    5. Digite a mensagem de commit: `docs: adiciona anotacoes-vscode`
    6. Clique em **✓ Commit** e depois em **Sync Changes**

    ✅ **Resultado esperado:** o commit aparece no histórico remoto no GitHub sem precisar de terminal.

??? example "Exercício 3 — Usar o Copilot no modo chat para documentação"
    **Objetivo:** experimentar o modo Ask e o modo Edit do Copilot num arquivo de documentação real.

    1. Abra o Copilot Chat com `Ctrl+Alt+I`
    2. No **modo Ask**, pergunte: `"Quais são as boas práticas para escrever documentação técnica em Markdown para desenvolvedores?"`
    3. Abra o arquivo `docs/anotacoes-vscode.md`
    4. Selecione um parágrafo do arquivo e pressione `Ctrl+I` para abrir o **Inline Chat**
    5. Digite: `"Reescreva este parágrafo em tom mais direto e técnico"`
    6. Revise a sugestão — aceite com `Tab` ou rejeite com `Esc`

    ✅ **Resultado esperado:** você usou dois modos diferentes do Copilot e entendeu quando cada um é mais adequado.

---

## Módulo 3 — Markdown e MkDocs

> [← Voltar ao módulo](./03-markdown-e-mkdocs.md)

??? example "Exercício 1 — Criar uma página Markdown completa"
    **Objetivo:** escrever uma página usando todos os elementos essenciais de Markdown.

    1. Crie o arquivo `docs/pagina-teste.md` no repositório
    2. Escreva uma página que contenha:
       - Um título H1 e pelo menos dois H2
       - Um parágrafo com texto em **negrito** e *itálico*
       - Uma lista não-ordenada com 3 itens
       - Uma tabela com 2 colunas e 3 linhas
       - Um bloco de código com a linguagem especificada (ex.: ` ```bash `)
       - Uma admonition `!!! tip` com pelo menos duas linhas de conteúdo
    3. Abra o preview no VS Code (`Ctrl+K V`) e verifique a renderização
    4. Faça commit e push do arquivo

    ✅ **Resultado esperado:** a página renderiza corretamente no preview e no site local.

??? example "Exercício 2 — Rodar o MkDocs localmente"
    **Objetivo:** gerar o site e visualizá-lo no navegador.

    1. Abra o terminal integrado do VS Code (Ctrl+`)
    2. Certifique-se de estar na raiz do repositório
    3. Execute:
       ```bash
       mkdocs serve
       ```
    4. Abra `http://localhost:8000` no navegador
    5. Enquanto o servidor roda, edite o arquivo `docs/pagina-teste.md` criado no exercício anterior — observe que o navegador atualiza automaticamente ao salvar
    6. Pare o servidor com `Ctrl+C` no terminal

    ✅ **Resultado esperado:** o site carrega com a página de teste aparecendo na navegação.

??? example "Exercício 3 — Usar admonitions colapsáveis"
    **Objetivo:** praticar os tipos `!!!` e `???` de admonitions.

    1. No arquivo `docs/pagina-teste.md`, adicione:
       - Uma admonition `!!! warning` com uma lista de 3 itens
       - Uma admonition colapsável `??? note` com um parágrafo de texto
       - Uma admonition `???+` (começa aberta) com código dentro
    2. Visualize no preview e confirme que a versão `???` começa fechada
    3. Tente intencionalmente colocar 2 espaços de indentação em uma delas — observe o resultado quebrado no preview
    4. Corrija para 4 espaços

    ✅ **Resultado esperado:** as três admonitions rendeizam corretamente, com a `???` colapsando ao clicar.

---

## Módulo 4 — Branches e Pull Requests

> [← Voltar ao módulo](./05-branches-e-pull-requests.md)

??? example "Exercício 1 — Criar um branch e trabalhar isolado"
    **Objetivo:** praticar o fluxo de branch sem afetar o main.

    1. Certifique-se de estar no `main` e atualizado (`git pull`)
    2. Crie um branch com seu nome:
       ```bash
       git checkout -b docs/pagina-seu-nome
       ```
    3. Crie o arquivo `docs/seu-nome-branch.md` com um título H1 e um parágrafo
    4. Faça commit:
       ```bash
       git add docs/seu-nome-branch.md
       git commit -m "docs: adiciona página de exercício de branch"
       ```
    5. Envie o branch para o GitHub:
       ```bash
       git push origin docs/pagina-seu-nome
       ```
    6. Verifique no GitHub que o branch existe mas o `main` ainda não tem o arquivo

    ✅ **Resultado esperado:** o arquivo existe apenas no branch — o main está intacto.

??? example "Exercício 2 — Abrir e revisar um Pull Request"
    **Objetivo:** criar um PR e simular o fluxo de revisão.

    1. Acesse o repositório no GitHub
    2. Clique em **Compare & pull request** (o GitHub detecta o branch recém-enviado)
    3. Preencha:
       - **Título:** `docs: adiciona página de exercício – [seu nome]`
       - **Descrição:** escreva em 2-3 linhas o que foi alterado
    4. Solicite revisão de um colega (campo **Reviewers**)
    5. O colega deve abrir o PR, ir em **Files changed** e adicionar um comentário inline em uma linha do arquivo
    6. Responda ao comentário e faça a correção sugerida com um novo commit no mesmo branch
    7. Após aprovação, clique em **Merge pull request** → **Confirm merge**
    8. Delete o branch após o merge

    ✅ **Resultado esperado:** a página chega ao main via PR revisado, com histórico de comentários.

??? example "Exercício 3 — Resolver um conflito de merge entre branches"
    **Objetivo:** reproduzir um conflito real entre dois branches e resolvê-lo.

    1. No `main`, crie o arquivo `docs/conflito-branches.md` com o texto: `"Versão original"`
    2. Crie dois branches a partir do main:
       ```bash
       git checkout -b docs/branch-a
       # edite docs/conflito-branches.md → "Versão do branch A"
       git add . ; git commit -m "docs: versão do branch A"

       git checkout main
       git checkout -b docs/branch-b
       # edite docs/conflito-branches.md → "Versão do branch B"
       git add . ; git commit -m "docs: versão do branch B"
       ```
    3. Faça merge do `branch-a` no `main` primeiro
    4. Tente fazer merge do `branch-b` — o Git vai reportar conflito
    5. Abra o VS Code, localize o arquivo conflitante no painel Source Control e resolva usando **Accept Both Changes**
    6. Ajuste o texto final manualmente, faça stage e commit

    ✅ **Resultado esperado:** o conflito é resolvido e o arquivo final contém o conteúdo correto.

---

## Módulo 5 — Publicando para Acesso Externo

> [← Voltar ao módulo](./06-publicacao-externa.md)

??? example "Exercício 1 — Publicar no GitHub Pages"
    **Objetivo:** ativar o GitHub Pages e verificar o deploy automático.

    1. Acesse o repositório do curso no GitHub
    2. Vá em **Settings → Pages** (menu lateral)
    3. Em **Source**, selecione **Deploy from a branch** e escolha o branch `gh-pages`
    4. Salve as configurações
    5. No repositório local, faça uma alteração pequena em qualquer arquivo `.md` (ex.: adicione uma linha em branco)
    6. Commite e faça `git push` para o `main`
    7. Acesse a aba **Actions** no GitHub e acompanhe a execução do workflow `deploy.yml`
    8. Após o deploy concluir, acesse a URL pública do site

    ✅ **Resultado esperado:** a alteração aparece na URL pública em menos de 2 minutos.

??? example "Exercício 2 — Ler e interpretar os logs do GitHub Actions"
    **Objetivo:** saber onde olhar quando um deploy falha.

    1. Acesse a aba **Actions** no repositório do curso no GitHub
    2. Clique no workflow mais recente
    3. Expanda cada etapa e leia o log:
       - Qual etapa instala as dependências?
       - Qual etapa executa o `mkdocs gh-deploy`?
       - Quanto tempo cada etapa levou?
    4. Para simular uma falha, edite o `mkdocs.yml` e introduza um erro de sintaxe YAML (ex.: remova um `:`)
    5. Faça push e observe a aba Actions — qual etapa falhou? Qual é a mensagem de erro?
    6. Corrija o `mkdocs.yml` e faça push novamente

    ✅ **Resultado esperado:** você consegue identificar onde um deploy falhou lendo os logs, sem ajuda externa.

??? example "Exercício 3 — Decidir a opção de publicação para cenários reais"
    **Objetivo:** aplicar a tabela de decisão a situações concretas.

    Para cada cenário abaixo, escolha a opção de publicação mais adequada e justifique:

    | Cenário | Opção recomendada | Por quê? |
    |---|---|---|
    | Manual de uso público de um produto AltoQi | ? | ? |
    | Wiki interna de processos da equipe de Produto | ? | ? |
    | Documentação técnica sensível para clientes enterprise | ? | ? |
    | Guia de onboarding para novos colaboradores | ? | ? |

    Compare suas respostas com o diagrama de decisão no início do módulo.

    ✅ **Resultado esperado:** você consegue justificar cada escolha sem consultar o diagrama.

---

## Módulo 6 — Personalizando o GitHub Copilot

> [← Voltar ao módulo](./06-copilot-customizacao.md)

??? example "Exercício 1 — Criar um copilot-instructions.md básico"
    **Objetivo:** escrever o arquivo de instruções para um repositório fictício.

    1. No repositório do curso, crie o arquivo `.github/copilot-instructions.md`
    2. Escreva as seguintes seções:
       - **Papel**: descreva o papel do agente (ex.: redator técnico do repositório X)
       - **Estrutura de diretórios**: liste as pastas de `docs/` com uma linha explicando o que vai em cada uma
       - **Estilo de escrita**: defina o tom (formal, direto, voz ativa) e 2 regras de terminologia
       - **Restrições**: liste os arquivos que nunca devem ser modificados
    3. Abra o Copilot Chat em **modo agente** e peça: `"Crie um arquivo index.md para a pasta docs/intro/"`
    4. Observe se o agente seguiu as instruções que você escreveu

    ✅ **Resultado esperado:** o agente cria o arquivo respeitando o estilo e a estrutura que você definiu.

??? example "Exercício 2 — Criar um prompt reutilizável"
    **Objetivo:** criar um arquivo `.prompt.md` para uma tarefa recorrente.

    1. Crie o arquivo `.github/prompts/nova-pagina.prompt.md`
    2. O prompt deve instruir o Copilot a criar uma nova página com:
       - Frontmatter YAML com `title`, `created` e `updated`
       - Um título H1 igual ao valor de `title`
       - Uma seção `## Visão Geral` vazia
       - Uma admonition `!!! abstract` com os objetivos da página (placeholder)
    3. No Copilot Chat, invoque o prompt com `/nova-pagina` e peça para criar uma página sobre "Gestão de Permissões"
    4. Verifique se o rascunho gerado segue o template do prompt

    ✅ **Resultado esperado:** o Copilot gera uma página com a estrutura exata definida no prompt.

??? example "Exercício 3 — Tabela de decisão na prática"
    **Objetivo:** escolher o mecanismo correto para três cenários reais.

    Para cada cenário abaixo, identifique qual mecanismo usar (Instructions, Prompt, Agente ou Skill) e justifique em uma frase:

    | Cenário | Mecanismo | Por quê? |
    |---|---|---|
    | Toda página deve sempre ter frontmatter YAML | ? | ? |
    | Criar uma nova página de tutorial quando solicitado | ? | ? |
    | Ingerir um épico do TargetProcess, criar páginas e atualizar o índice | ? | ? |

    Compare suas respostas com a tabela de decisão da seção 5 do módulo.

    ✅ **Resultado esperado:** você consegue escolher o mecanismo certo sem consultar a tabela.

---

## Módulo 7 — Instruções Específicas

> [← Voltar ao módulo](./08-instrucoes-especificas.md)

??? example "Exercício 1 — Simular a ingestão de uma feature do TargetProcess"
    **Objetivo:** praticar o fluxo da Dica 1 com um card fictício.

    1. Abra o Copilot Chat no **modo agente** no VS Code
    2. Simule um card do TargetProcess colando o texto abaixo na conversa:

       ```
       Feature 999001 — Exportação de relatório em PDF
       Descrição: o usuário pode exportar o relatório de progresso do projeto
       em formato PDF, com opção de incluir ou excluir gráficos.
       Critérios de aceite:
       - Botão "Exportar PDF" disponível na tela de relatórios
       - Opções: incluir gráficos (sim/não), orientação (retrato/paisagem)
       - PDF gerado com logo da empresa no cabeçalho
       ```

    3. Peça ao agente: `"Crie uma página de documentação para o usuário final com base nessa feature"`
    4. Verifique se o agente:
       - Excluiu os critérios de aceite (detalhes de implementação)
       - Focou no comportamento visível para o usuário
       - Criou frontmatter YAML correto

    ✅ **Resultado esperado:** uma página de documentação orientada ao usuário, sem jargão técnico de desenvolvimento.

??? example "Exercício 2 — Estruturar um repositório com pasta raw/"
    **Objetivo:** criar a estrutura `raw/` + `wiki/` em um repositório de exercício.

    1. No repositório do curso, crie a seguinte estrutura de pastas:
       ```
       raw/
         produto_exemplo/
           spec-funcionalidade-x.md
       wiki/
       ```
    2. No arquivo `raw/produto_exemplo/spec-funcionalidade-x.md`, cole uma especificação simples (pode inventar — ex.: um formulário de cadastro)
    3. Peça ao agente: `"Ingira o arquivo raw/produto_exemplo/spec-funcionalidade-x.md e crie a página correspondente em wiki/"`
    4. Observe se o agente:
       - Leu o arquivo `raw/` sem modificá-lo
       - Criou uma página nova em `wiki/`
       - A página em `wiki/` é orientada ao usuário (não copia a spec literalmente)

    ✅ **Resultado esperado:** o arquivo `raw/` permanece intacto e `wiki/` tem uma nova página com conteúdo processado.

??? example "Exercício 3 — Comparar os três padrões de ingestão"
    **Objetivo:** consolidar a diferença entre as três dicas do módulo.

    Preencha a tabela abaixo com base no que você aprendeu:

    | | Dica 1 — Documentar feature | Dica 2 — Espelhar épico | Dica 3 — Pasta raw/ |
    |---|---|---|---|
    | **Repositório** | ? | ? | ? |
    | **O agente filtra o conteúdo?** | ? | ? | ? |
    | **Imagens são baixadas?** | ? | ? | ? |
    | **Fonte principal** | ? | ? | ? |
    | **Resultado** | ? | ? | ? |

    Confira suas respostas relendo as três dicas do módulo.

    ✅ **Resultado esperado:** você consegue explicar para um colega quando usar cada padrão, sem consultar o material.

---

> **Módulo anterior:** [08 — Instruções Específicas](./08-instrucoes-especificas.md)  
> **Índice:** [Início](./index.md)
