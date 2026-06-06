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

> **Módulo anterior:** [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md)  
> **Índice:** [Início](./index.md)
