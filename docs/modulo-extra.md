# Módulo Extra — Instruções Específicas

> Este módulo reúne dicas práticas que se aplicam a diferentes tipos de repositórios de documentação. Cada dica apresenta um padrão de instrução pronto para adaptar ao seu contexto.

---

## Dica 1 — Documentar uma feature a partir do Targetprocess

### Contexto

Equipes de Produto que usam o **Targetprocess** como ferramenta de gestão podem configurar o Copilot para buscar especificações diretamente do backlog e transformá-las em documentação orientada ao usuário. Isso elimina a etapa de "traduzir o card para o redator" — o próprio agente faz a leitura e a filtragem.

Essa dica é aplicável a qualquer repositório de documentação cujas fontes de especificação vivam no Targetprocess.

---

### O princípio fundamental: filtragem técnica → usuário

O conteúdo de uma Feature ou User Story no Targetprocess é **especificação técnica de implementação**. O redator técnico — humano ou IA — precisa extrair apenas o que é **visível e relevante para o usuário final**.

**Incluir na documentação:**

- Comportamento da interface (telas, botões, campos, fluxos)
- Regras de negócio visíveis ao usuário
- Mensagens de validação, notificações, alertas
- Novos menus, opções de configuração, permissões
- Mudanças em relatórios, exportações, visualizações

**Excluir da documentação:**

- Detalhes de implementação (banco de dados, APIs, migrations, código)
- Decisões arquiteturais internas
- Estimativas de esforço, assignments, sprints
- Comentários de revisão de código ou deploy

---

### Hierarquia de conteúdo: Feature × User Story

| Entidade | Papel na documentação | Contém |
|---|---|---|
| **Feature** | Contextualização — o "por quê" e "o quê" | Objetivo da implementação, requisito do usuário |
| **User Story** | Fonte primária — o "como funciona" | Comportamento implementado, solução detalhada pelos analistas |

A Feature define o requisito; as Stories filhas descrevem a solução. A documentação final deve refletir a solução **conforme experimentada pelo usuário**, usando a Feature apenas como contexto.

---

### Como configurar o agente

Crie um arquivo `.github/ingest-targetprocess.md` no repositório. Esse arquivo é referenciado pelo `copilot-instructions.md` e ativado sempre que o usuário pedir para documentar um item do Targetprocess.

#### Estrutura recomendada do arquivo

```markdown
# Ingest de Features e User Stories do Targetprocess

## Quando ativar
Quando o usuário pedir para **documentar** uma feature ou story por ID numérico:
- "documentar feature 272753"
- "documentar stories 282522, 282530"

## Princípio geral
O conteúdo no Targetprocess é especificação técnica. Extrair apenas o que
é visível ao usuário final (interface, regras de negócio, fluxos).

## Hierarquia
- **Feature** → contextualização (requisito, objetivo)
- **User Story** → fonte primária (comportamento implementado)

## Modo 1 — Documentar User Stories
1. Buscar cada story por ID para obter Name, Description e Comments
2. Se houver lista de stories, ler todas antes de processar
3. Extrair apenas comportamento visível ao usuário
4. Seguir o fluxo de ingest padrão do repositório

## Modo 2 — Documentar Features
1. Buscar a Feature por ID (Name, Description)
2. Listar as User Stories filhas
3. Buscar cada story filha (Description e Comments)
4. Combinar: Feature como contexto + Stories como fonte primária
5. Se houver lista de features, ler todas (com stories) antes de processar

## Quando há múltiplos IDs
Ler tudo primeiro, depois sintetizar uma visão unificada.
Os itens podem ser etapas sequenciais ou aspectos complementares
de uma mesma funcionalidade.

## Registro
- Registrar cada item em `docs/sources.md` com tipo `targetprocess-feature`
  ou `targetprocess-story`
- URL de referência: `https://suainstancia.tpondemand.com/entity/{Id}`
```

---

### Como o agente acessa o Targetprocess

Existem dois padrões conforme a configuração do ambiente:

#### Padrão A — Via MCP Targetprocess

Se o repositório tem o servidor MCP `targetprocess` configurado, o agente chama as ferramentas diretamente:

```markdown
## Ferramentas disponíveis
- `mcp_targetprocess_get_feature` → busca Feature por ID
- `mcp_targetprocess_get_user_story` → busca Story por ID
- `mcp_targetprocess_list_user_stories` → lista stories com filtro
  (ex.: `where_clause="Feature.Id eq 272753"`)
```

#### Padrão B — Via script Python (skill local)

Se o repositório usa um skill local para leitura da API:

```markdown
## Ferramentas disponíveis
Executar o script do skill para cada ID:
```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = "utf-8"
python .github/skills/tp-read-description/scripts/read_description.py <ID>
```
O script retorna Name, Description e — para Features — a lista de stories
filhas com ID, Nome e Estado.
```

Em ambos os casos, o **fluxo de ingest é o mesmo**; só muda o mecanismo de leitura.

---

### Referência no `copilot-instructions.md`

Adicione ao seu `copilot-instructions.md` uma linha apontando para o arquivo de ingest:

```markdown
## Fontes externas

### Targetprocess
Quando o usuário solicitar a documentação de uma feature ou story por ID,
seguir as instruções em `.github/ingest-targetprocess.md`.
```

---

### Exemplo de uso

Com o agente ativo no repositório:

```
Usuário: documentar feature 272753

Agente:
1. Busca Feature 272753 → lê Name e Description
2. Lista stories filhas → encontra stories 282522, 282530, 282535
3. Lê cada story (Description + Comments)
4. Filtra: mantém comportamento de interface, descarta detalhes técnicos
5. Cria o rascunho da página de documentação
6. Registra a feature em docs/sources.md
7. Apresenta o resultado para revisão
```

---

## Dica 2 — Espelhar épicos do Targetprocess como páginas wiki

### Contexto

Algumas wikis internas de produto funcionam como um **espelho fiel** do Targetprocess: cada épico vira uma página com o mesmo texto que o PM escreveu, incluindo as figuras anexadas ao card. Não há interpretação nem filtragem — o objetivo é ter o conteúdo de especificação acessível na wiki, exatamente como está.

Esse padrão é diferente da Dica 1:

| | Dica 1 — Documentar (usuário) | Dica 2 — Espelhar (wiki interna) |
|---|---|---|
| **Conteúdo gerado** | Documentação orientada ao usuário final | Cópia fiel da especificação interna |
| **Figuras** | Não se aplicam (texto narrativo) | Baixadas e referenciadas na página |
| **Filtragem** | Sim — detalhes técnicos são removidos | Não — tudo é importado |
| **Destino** | Estrutura decidida pelo agente | Pasta fixa por produto (`epicos/`) |
| **Entidade TP** | Feature + User Stories filhas | Épicos (por produto e ano) |

---

### O fluxo de espelhamento

O processo tem três etapas:

```
1. Listar épicos do produto no TP
        ↓
2. Importar cada épico (HTML → Markdown + download de imagens)
        ↓
3. Atualizar navegação (.pages e index.md)
```

#### Etapa 1 — Listar épicos

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $env:PYTHONIOENCODING="utf-8"
python .github/skills/tp-read-description/scripts/list_epics.py --project <PRODUTO> --ano <ANO>
```

Retorna uma tabela Markdown com `ID`, `Nome`, `Estado`, `Projeto` e `AnoFechamento`.

#### Etapa 2 — Importar épico

```powershell
python .github/skills/tp-read-description/scripts/ingest_epic.py <ID> --produto <PRODUTO>
```

O script:

1. Busca o épico na API do Targetprocess
2. Converte a `Description` de HTML para Markdown (via `markdownify`)
3. Baixa as imagens dos attachments do TP para `<pasta_epicos>/img/`
4. Grava `<pasta_epicos>/<ID>.md` com frontmatter completo

```yaml
# Frontmatter gerado automaticamente
title: <Nome do épico>
type: feature
created: YYYY-MM-DD
tp_id: 139911
tp_state: In Testing
tp_project: Eberick
tp_url: https://altoqi.tpondemand.com/entity/139911
```

Para subprodutos do Visus (collab, workflow, hub, cost_planning), passar o destino explicitamente:

```powershell
python .github/skills/tp-read-description/scripts/ingest_epic.py <ID> \
  --produto workflow --outdir wiki/produto_visus/produto_workflow/epicos
```

Em lote:

```powershell
@(139911, 140022, 140150) | ForEach-Object {
    python .github/skills/tp-read-description/scripts/ingest_epic.py $_ --produto eberick
}
```

#### Etapa 3 — Atualizar navegação

Após importar, atualizar dois arquivos na pasta de épicos:

**`.pages`** — adicionar entrada para cada épico novo:
```yaml
- "(ID) Título curto": <ID>.md
```
> Use aspas duplas ao redor do label para evitar que `:` no título quebre o YAML.

**`index.md`** — adicionar linha na tabela de épicos:
```markdown
| [139911](139911.md) | Nome completo do épico | In Testing |
```

---

### Como configurar o prompt

Crie `.github/prompts/atualizar-epicos.prompt.md` para que o agente saiba o mapeamento produto → pasta:

```markdown
---
mode: "agent"
description: "Importa épicos do Targetprocess para a wiki."
---

# Atualizar Épicos

## Mapeamento produto → pasta wiki

| Produto   | `--project` (TP) | `--produto` | Pasta wiki                      |
|-----------|------------------|-------------|---------------------------------|
| eberick   | Eberick          | eberick     | wiki/produto_eberick/epicos/    |
| builder   | Builder          | builder     | wiki/produto_builder/epicos/    |
| collab    | Collab           | collab      | wiki/produto_visus/produto_collab/epicos/ |
| ...       | ...              | ...         | ...                             |

## Procedimento

1. Listar épicos: `list_epics.py --project <PROJETO> --ano <ANO>`
2. Comparar com arquivos existentes na pasta de destino
3. Importar novos: `ingest_epic.py <ID> --produto <PRODUTO>`
4. Atualizar `.pages` e `index.md` da pasta
```

---

### O que muda na `copilot-instructions.md`

```markdown
## Wiki interna

Esta wiki espelha o conteúdo de épicos do Targetprocess sem modificações.
Quando o usuário pedir para "atualizar épicos" ou "importar épico <ID>",
seguir o prompt `/atualizar-epicos`.

Regras:
- Nunca reescrever ou resumir o conteúdo dos épicos
- Imagens são parte do conteúdo — sempre baixar junto com o texto
- Re-importar um épico existente é seguro (o arquivo é sobrescrito)
```

---

> **Módulo anterior:** [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md)  
> **Índice:** [Início](./index.md)
