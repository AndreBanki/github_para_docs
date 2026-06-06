# Módulo 5 — Branches e Pull Requests

> **Pré-requisito:** leia o [Módulo 1 — Git para Documentação](./01-git-para-documentacao.md) antes de continuar. Este documento aprofunda o **Fluxo Completo** — branches isolados e revisão via Pull Request.

!!! abstract "🎯 Objetivos de aprendizagem"
    Neste módulo você vai aprender:

    - O que é um branch e por que ele existe
    - Como criar, navegar e trabalhar em branches
    - O que é um Pull Request e como fazer revisão
    - Como resolver conflitos de merge
    - O fluxo completo passo a passo

!!! tip "Não se preocupe se parecer complexo"
    90% do seu dia a dia é o fluxo simplificado (Módulo 1). Branches e PRs são para quando a equipe crescer ou o conteúdo precisar de revisão formal.

---

## Por que isso existe?

No fluxo simplificado, tudo que você commita e faz `push` vai direto para o `main` — e, consequentemente, para o site publicado. Isso funciona bem enquanto a equipe é pequena e os conteúdos são independentes.

À medida que a equipe cresce ou o conteúdo se torna mais crítico, surgem situações que o fluxo simplificado não cobre:

- Dois redatores editam arquivos próximos ao mesmo tempo e sobrescrevem o trabalho um do outro
- Um rascunho incompleto vai parar no site antes de estar pronto
- Não há como pedir revisão de conteúdo antes de publicar
- É difícil trabalhar num conjunto grande de mudanças sem atrapalhar quem está editando outras seções

A solução são dois conceitos: **branch** e **Pull Request**.

---

## 1. O que é um Branch?

Um branch é uma **linha do tempo paralela** do repositório. Enquanto o `main` continua estável e publicado, você trabalha numa cópia isolada — sem afetar ninguém.

```mermaid
gitGraph
    commit id: "página existente"
    commit id: "correção anterior"
    branch docs/guia-collab
    commit id: "commit A"
    commit id: "commit B"
    commit id: "commit C"
    checkout main
    commit id: "outro trabalho"
    merge docs/guia-collab id: "merge do PR"
    commit id: "site atualizado"
```

Só quando você decidir (e alguém aprovar) é que esse trabalho é incorporado ao `main`.

### Criar um branch

```bash
git checkout -b docs/nome-da-tarefa
```

Esse comando cria o branch a partir do estado atual do `main` e já muda para ele.

**No VS Code:** clique em ![Git Branch](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-branch.svg){: .vscode-icon} **nome do branch** na barra de status inferior → **Create new branch...** → digite o nome.

**Convenção de nomes:**

| Prefixo | Quando usar | Exemplo |
|---|---|---|
| `docs/` | Criação ou expansão de conteúdo | `docs/tutorial-planning` |
| `fix/` | Correção pontual de erro | `fix/link-quebrado-collab` |
| `refactor/` | Reorganização de estrutura | `refactor/renomear-secoes-bid` |

---

### Navegar entre branches

```bash
git checkout main              # voltar para o main
git checkout docs/guia-collab  # ir para um branch existente
```

**No VS Code:** clique em ![Git Branch](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/git-branch.svg){: .vscode-icon} **nome do branch** na barra de status inferior → selecione o branch desejado na lista.

---

### Ver todos os branches

```bash
git branch -a    # local e remoto
```

---

## 2. Trabalhando no Branch

O fluxo dentro do branch é idêntico ao fluxo simplificado — você edita, faz `add`, `commit` e `push`. A diferença é que o `push` envia para o seu branch, não para o `main`:

```bash
git add .
git commit -m "docs: adiciona introdução ao módulo Collab"
git push origin docs/guia-collab
```

**No VS Code:** Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control → clique em ![Add](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/add.svg){: .vscode-icon} para fazer stage → escreva a mensagem → ![Check](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/check.svg){: .vscode-icon} **Commit** → ![Sync](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/sync.svg){: .vscode-icon} **Sync Changes** (ou ![Ellipsis](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/ellipsis.svg){: .vscode-icon} → **Push**).

Você pode fazer quantos commits quiser no branch. Enquanto não abrir o PR e ele não for mesclado, o `main` não é afetado.

---

## 3. O que é um Pull Request (PR)?

Um Pull Request é uma **proposta formal de mesclar um branch no `main`**. Ele é aberto no GitHub (não no terminal) e permite:

- **Revisão de conteúdo:** um colega lê o que você escreveu antes de publicar
- **Comentários linha a linha:** é possível comentar em trechos específicos
- **Histórico permanente:** toda a discussão fica registrada no repositório
- **Aprovação explícita:** o merge só acontece quando alguém aprova

### Abrir um PR

1. Após fazer `push` do branch, acesse o repositório no GitHub
2. Uma faixa amarela aparece: "Compare & pull request" — clique nela
3. Escreva um título descritivo e uma descrição do que foi adicionado/alterado
4. Atribua um revisor (campo "Reviewers")
5. Clique em **Create Pull Request**

### Revisar um PR

1. Acesse a aba **Pull requests** no repositório
2. Abra o PR designado para você
3. Vá em **Files changed** para ver exatamente o que mudou
4. Clique em qualquer linha para adicionar um comentário
5. Quando estiver satisfeito, clique em **Review changes → Approve**

### Mesclar (merge) o PR

Após aprovação, o próprio autor (ou o revisor) clica em **Merge pull request**. O conteúdo entra no `main` e o branch pode ser deletado.

---

## 4. Conflitos de Merge no Fluxo Completo

Quando dois branches alteram o mesmo trecho de um arquivo, o Git não consegue decidir sozinho qual versão manter. Isso é um **conflito de merge**.

O Git marca as diferenças no arquivo:

```
<<<<<<< HEAD
Texto que está no seu branch
=======
Texto que está no main
>>>>>>> main
```

### Resolver no VS Code

O VS Code detecta o conflito e exibe botões acima do trecho no Painel ![Source Control](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/source-control.svg){: .vscode-icon} Source Control:

- **Accept Current Change** — mantém o que está no seu branch
- **Accept Incoming Change** — mantém o que veio do main
- **Accept Both Changes** — mantém os dois trechos
- **Compare Changes** — mostra o diff lado a lado

Após resolver, salve o arquivo, clique em ![Add](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/add.svg){: .vscode-icon} para fazer stage e depois em ![Check](https://cdn.jsdelivr.net/npm/@vscode/codicons@0.0.35/src/icons/check.svg){: .vscode-icon} **Commit**.

---

## 5. Estrutura de Branches do Repositório

```
main
  └── Branch de produção. Nunca recebe push direto no fluxo completo.
      Todo conteúdo chega via Pull Request revisado.

docs/<nome>
  └── Trabalho em andamento. Aberto por um redator para uma tarefa específica.
      Exemplo: docs/tutorial-planning, docs/visao-geral-bid

fix/<nome>
  └── Correção pontual de erro de conteúdo.
      Exemplo: fix/link-quebrado-collab, fix/terminologia-incorreta
```

> Branches devem ser de vida curta. Crie, trabalhe, abra o PR, mescle e delete. Branches que ficam abertos por semanas tendem a acumular conflitos.

---

## 6. Fluxo Completo — Referência Rápida

```
git pull                                  # atualizar main
git checkout -b docs/nome-da-tarefa       # criar branch
# ... editar arquivos ...
git add .
git commit -m "docs: descreve o que foi feito"
git push origin docs/nome-da-tarefa       # enviar branch para o GitHub

→ Abrir Pull Request no GitHub
→ Revisor aprova
→ Merge no main → site atualizado automaticamente
→ Deletar o branch
```

!!! success "✅ Resumo do módulo"
    **Branches** isolam um trabalho em andamento sem afetar o `main`, e o **Pull Request** permite revisar o conteúdo antes de publicar. Você viu como criar e navegar em branches, abrir e revisar um PR, resolver conflitos de merge e executar o fluxo completo passo a passo.

---

> **Módulo anterior:** [01 — Git para Documentação](./01-git-para-documentacao.md)  
> **Índice:** [Início](./index.md)
