# Módulo Extra — Instruções Específicas

> Este módulo reúne dicas práticas encontradas em repositórios reais da AltoQi. Cada dica descreve um padrão de instrução e como ele é usado no dia a dia.

!!! abstract "🎯 O que você vai encontrar aqui"
    Padrões reais de instrução usados nos repositórios da AltoQi: como documentar
    a partir do Targetprocess, espelhar épicos e organizar a pasta `raw/` de fontes.

---

## Dica 1 — Documentar uma feature a partir do Targetprocess

**Repositórios:** `visus_docs`, `eberick_docs`, `builder_docs`

O agente recebe um ID de Feature ou User Story do Targetprocess e produz documentação orientada ao usuário final. Não é uma cópia do card — é uma interpretação: o agente lê o conteúdo, descarta detalhes técnicos e extrai apenas o que se reflete no funcionamento visível da aplicação.

### Como usar

Basta informar o ID ao agente no modo agente:

```
documentar feature 272753
documentar stories 282522, 282530, 282535
```

O agente busca o conteúdo no Targetprocess, lê as stories filhas quando necessário, e produz o rascunho da página. Quando são fornecidos múltiplos IDs, o agente lê tudo antes de escrever — os itens podem ser etapas de uma mesma funcionalidade.

### O que o agente inclui e exclui

**Inclui:** comportamento de interface, regras de negócio visíveis, mensagens de validação, novos menus e permissões, mudanças em relatórios e exportações.

**Exclui:** implementação interna (banco, API, código), decisões arquiteturais, estimativas de esforço, comentários de deploy.

### Hierarquia Feature × User Story

| Entidade | Papel |
|---|---|
| **Feature** | Contextualização — o "por quê" e "o quê" |
| **User Story** | Fonte primária — o "como funciona" |

A Feature fornece o contexto do requisito; as Stories descrevem a solução. A documentação final reflete a solução conforme experimentada pelo usuário.

### O papel do `instructions.md`

Para que o agente saiba **onde** criar ou atualizar páginas após ler o conteúdo do Targetprocess, os três repositórios mantêm um arquivo `instructions.md` na raiz do projeto. Ele é um mapa de conteúdo: descreve cada seção de `docs/`, os critérios do que pertence a ela e o que deve ser explicitamente excluído.

| Repositório | Título do arquivo | O que documenta |
|---|---|---|
| `visus_docs` | Mapa de Conteúdo da Documentação | Plataforma, Workflow, Collab, Cost Management, Planning, Bid, Tracking, Control Tower |
| `eberick_docs` | Mapa do Repositório — AltoQi Eberick | Apresentação, Atualizações, Conceitos CAD, Comandos, Janelas, Dimensionamento, Critérios de Projeto |
| `builder_docs` | Instruções de Estrutura — AltoQi Builder | 11 seções: Apresentação, Notas de versão, Conceitos CAD, Conceitos da edificação, Critérios, Cadastro, Configurações, Janelas, Elementos, Comandos, Propriedades |

O agente lê o `instructions.md` antes de decidir o destino do conteúdo — sem ele, corre o risco de criar páginas no lugar errado ou de ignorar seções já existentes.

### Onde as instruções vivem

O comportamento do agente é definido em `.github/ingest-targetprocess.md`, referenciado pelo `copilot-instructions.md` do repositório.

---

## Dica 2 — Espelhar épicos do Targetprocess como páginas wiki

**Repositório:** `produto_docs`

O agente importa épicos do Targetprocess como páginas wiki, preservando o conteúdo **exatamente como está** — incluindo as figuras anexadas ao card. Não há interpretação nem filtragem. O objetivo é ter a especificação interna acessível na wiki, no mesmo formato em que o PM a escreveu.

Esse padrão é diferente da Dica 1:

| | Dica 1 — Documentar (`visus_docs`, `eberick_docs`) | Dica 2 — Espelhar (`produto_docs`) |
|---|---|---|
| **Conteúdo gerado** | Documentação orientada ao usuário final | Cópia fiel da especificação interna |
| **Figuras** | Não se aplicam | Baixadas e referenciadas na página |
| **Filtragem** | Sim — detalhes técnicos são removidos | Não — tudo é importado |
| **Entidade TP** | Feature + User Stories filhas | Épicos (por produto e ano) |

### Como usar

O agente é acionado pelo prompt `/atualizar-epicos`. O usuário informa o produto e, opcionalmente, o ano:

```
/atualizar-epicos  →  "Qual produto?"  →  eberick
```

O agente lista os épicos do produto no Targetprocess, identifica quais ainda não existem na wiki, importa cada um (convertendo o HTML para Markdown e baixando as imagens) e atualiza a navegação da seção.

### Onde a instrução vive

O comportamento do agente é definido em `.github/prompts/atualizar-epicos.prompt.md`. A regra de nunca reescrever ou resumir o conteúdo — e de sempre baixar as imagens junto — está no `copilot-instructions.md` do repositório.

---

## Dica 3 — Pasta `raw/` como zona de entrada de fontes

**Repositórios:** `produto_docs`, `cloudops_docs`

Inspirada no conceito de **LLM Wiki** de Andrej Karpathy, essa abordagem divide o repositório em duas zonas com papéis bem distintos:

| Zona | Pasta | Papel | Quem escreve |
|---|---|---|---|
| **Fontes** | `raw/` | Documentos originais, imutáveis | Humano |
| **Conhecimento** | `wiki/` ou `documentation/` | Páginas estruturadas e publicáveis | Agente |

A ideia central é que o LLM não gera conhecimento do zero — ele **processa fontes reais** e produz conhecimento estruturado. O `raw/` é o arquivo permanente de tudo que alimentou a wiki; a wiki é o destilado consultável desse material.

### Como usar

O fluxo é simples:

1. Um documento novo chega — PDF, DOCX, transcrição de reunião, spec doc, export do Targetprocess
2. O arquivo é colocado em `raw/` na subpasta correspondente ao tema
3. O agente é acionado para ingerir: `"ingerir raw/produto_visus/documento.md"`
4. O agente lê a fonte, extrai o conteúdo relevante e cria ou atualiza páginas na wiki
5. O `raw/` nunca é modificado pelo agente — serve como rastreabilidade de todas as fontes

### Por que a separação importa

Sem a divisão `raw/wiki`, é comum que o repositório misture fontes e conteúdo publicável, dificultando saber o que já foi processado e o que ainda está pendente. Com a separação:

- É possível reprocessar uma fonte a qualquer momento (o original está intacto)
- O agente nunca "inventa" — toda página da wiki tem um arquivo em `raw/` como origem
- A wiki pode ser consultada pelo próprio agente para responder perguntas, sem precisar reler as fontes brutas

### Variações nos repositórios

Em `produto_docs`, o `raw/` está organizado por produto (`produto_eberick/`, `produto_visus/`, etc.) e o conteúdo processado vai para `wiki/`. Em `cloudops_docs`, o `raw/` usa subpastas `conteudo_a_organizar/` e `conteudo_ja_importado/` para rastrear o status de cada fonte, e o conteúdo processado vai para `documentation/`.

---

> **Módulo anterior:** [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md)  
> **Índice:** [Início](./index.md)
