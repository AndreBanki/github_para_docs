# Módulo 6 — Publicando para Acesso Externo

> **Para quem é este módulo:** quem precisa entender como a documentação sai do repositório e chega a um ambiente acessível para outras pessoas.
>
> **Por que este módulo vem agora:** depois de escrever, revisar e consolidar o conteúdo, o próximo passo natural é entender como ele vai para o ar. Este módulo fecha a trilha operacional principal mostrando as opções de publicação e atualização do site.

!!! abstract "🎯 Objetivos de aprendizagem"
    Neste módulo você vai aprender:

    - Quais são as opções para publicar a documentação
    - Como escolher a opção certa para o seu caso
    - Como funciona a atualização automática do conteúdo online

---

## Há mais de uma forma de publicar

Publicar a documentação gerada pelo MkDocs não tem uma resposta única — a melhor opção depende de **duas perguntas**:

1. O conteúdo é **público** ou **privado**?
2. Qual é o **nível de controle de acesso** necessário?

O diagrama abaixo resume as opções disponíveis:

```mermaid
flowchart TD
    A[Publicar documentação] --> B{O conteúdo é público?}
    B -- Sim --> C[GitHub Pages\n✅ Opção mais simples]
    B -- Não --> D{Qual nível de controle?}
    D -- Básico\nsenha compartilhada --> E[Render.com\ncom autenticação simples]
    D -- Intermediário\nlogin individual --> F[Render.com\n+ integração Keycloak]
    D -- Corporativo\nambiente oficial --> G[Solicitar ao\nCloudOps da AltoQi]
```

---

## Opção 1 — GitHub Pages (conteúdo público)

O **GitHub Pages** é a solução mais simples para conteúdo que pode ser acessado por qualquer pessoa — como este curso.

O GitHub constrói o site automaticamente a partir do repositório e disponibiliza em uma URL pública do tipo `https://seu-usuario.github.io/nome-do-repositorio/`.

### Como configurar

A configuração é feita pelo **dono da conta** do repositório no GitHub:

1. Acesse o repositório no GitHub
2. Vá em **Settings** → **Pages** (menu lateral)
3. Em **Source**, selecione **Deploy from a branch**
4. Selecione o branch **`gh-pages`** como origem
5. Certifique-se de que o arquivo `.github/workflows/deploy.yml` existe no repositório

### Como publicar

O deploy é **automático** — basta fazer `push` para o `main`. O GitHub Actions executa o build e publica o site sem nenhuma ação manual.

```mermaid
flowchart LR
    A[git push\npara o main] --> B[GitHub Actions\nexecuta deploy.yml]
    B --> C[pip install\nrequisitos]
    C --> D[mkdocs gh-deploy]
    D --> E[Site publicado\natualizado]
```

!!! tip "Deploy automático configurado"
    Este repositório já possui o arquivo `.github/workflows/deploy.yml`. Qualquer `push` para o `main` — inclusive via merge de Pull Request — atualiza o site automaticamente.

---

## Opção 2 — Render.com com senha compartilhada (conteúdo privado, baixa criticidade)

Para documentação que não deve ser pública, mas sem necessidade de controle de acesso individual, o **[Render.com](https://render.com)** é uma boa opção. Ele oferece uma conta gratuita suficiente para hospedar o site estático.

Nesse cenário, o arquivo `serve.py` (ou similar) pode ser ajustado para exigir **login e senha** antes de exibir o conteúdo. Todos os usuários compartilham a mesma credencial.

```
Usuário: equipe
Senha: (senha definida pelo responsável pelo repositório)
```

!!! warning "Limitações desta abordagem"
    - A senha é única para todos — se vazar, é necessário trocá-la e comunicar todos os usuários
    - Não há como revogar o acesso de uma pessoa específica sem trocar a senha para todos
    - Adequada para materiais internos de baixa criticidade (manuais operacionais, guias internos etc.)

### Como configurar no Render.com

1. Crie uma conta em [render.com](https://render.com)
2. Conecte o repositório GitHub ao Render
3. Configure o serviço como **Web Service** apontando para o `serve.py`
4. Defina as variáveis de ambiente com o usuário e senha

---

## Opção 3 — Render.com com Keycloak (login individual)

Para eliminar a senha compartilhada e ter controle de acesso por usuário, é possível integrar o ambiente do Render.com com o **Keycloak** — o servidor de identidade utilizado pela AltoQi.

Com essa integração, cada pessoa usa suas próprias credenciais corporativas para acessar a documentação, e o acesso pode ser gerenciado de forma centralizada.

!!! info "Referência de implementação"
    As instruções para essa integração estão disponíveis em:
    [https://github.com/AltoQiTec/qilabs_ai_agents.git](https://github.com/AltoQiTec/qilabs_ai_agents.git)

    Essa configuração está fora do escopo deste curso básico, mas é o caminho recomendado para documentação sensível que precisa de controle de acesso individual.

---

## Opção 4 — Ambiente corporativo via CloudOps (produção oficial)

Para materiais que precisam de um ambiente oficial, com SLA, domínio próprio da AltoQi e suporte de infraestrutura, a publicação pode ser feita por meio de uma **solicitação ao time de CloudOps da AltoQi**.

Esse é o caminho adequado para:

- Documentação de produto para clientes externos
- Manuais técnicos que fazem parte do entregável oficial
- Qualquer conteúdo que precise de infraestrutura gerenciada e monitorada

Entre em contato com o CloudOps descrevendo o repositório, o tipo de conteúdo e o nível de acesso necessário.

---

## Como o conteúdo é atualizado em todos os casos

Independentemente da opção escolhida, a lógica de atualização é a mesma quando há CI/CD configurado:

!!! success "Regra universal de atualização"
    **O site online é atualizado sempre que ocorre um `push` para o branch `main`** — seja por commit direto ou por merge de Pull Request.

Para o **GitHub Pages**, isso é feito via GitHub Actions (arquivo `.github/workflows/deploy.yml`). Para **Render.com** e **CloudOps**, o pipeline equivalente é configurado na respectiva plataforma.

Você nunca precisa publicar manualmente — basta que o conteúdo esteja no `main`.

---

## Resumo comparativo

| Opção | Conteúdo | Controle de acesso | Complexidade | Custo |
|---|---|---|---|---|
| GitHub Pages | Público | Nenhum (aberto a todos) | Baixa | Gratuito |
| Render.com + senha | Privado | Senha única compartilhada | Baixa | Gratuito (plano free) |
| Render.com + Keycloak | Privado | Login individual corporativo | Média | Depende do uso |
| CloudOps AltoQi | Privado/Público | Gerenciado pela infraestrutura | Alta (gerenciada) | Interno |

---

---

> **Módulo anterior:** [05 — Branches e Pull Requests](./05-branches-e-pull-requests.md)  
> **Próximo módulo:** [07 — Personalizando o Claude Code](./07-claude-code-customizacao.md)
