"""
Cria o Template de Treinamento "Documentação como Código — Guia AltoQi"
no projeto AltoQi Treinamento (Id=75718) do TargetProcess.

Estrutura criada:
  1. Request (Template) — com Objetivo, Público-alvo, Trilha, Detalhamento, Resultados
  2. 5 UserStories (uma por etapa da trilha, com perguntas teóricas para o colaborador)
  3. 1 UserStory exclusiva do instrutor com o gabarito das 25 perguntas
  4. Relations ligando cada UserStory ao Template (RelationType=Relation)

Etapas:
  Etapa 1 — Fundação: Ambiente e Git         (Módulos 01 + 02)
  Etapa 2 — Conteúdo: Markdown e Publicação  (Módulos 03 + 06)
  Etapa 3 — IA: Claude Code                  (Módulos 04 + 07)
  Etapa 4 — Colaboração e Padrões Reais      (Módulos 05 + 08)
  Etapa 5 — Consolidação Prática             (Módulo 09)

Uso:
  python criar_treinamento_tp.py
  python criar_treinamento_tp.py --dry-run   # apenas exibe o payload sem criar
"""

import urllib.request
import urllib.parse
import json
import os
import sys
import argparse
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

BASE_URL   = os.environ.get("TARGETPROCESS_BASE_URL", "https://altoqi.tpondemand.com").rstrip("/")
TOKEN      = os.environ.get("TARGETPROCESS_TOKEN", "")
PROJECT_ID = 75718
SITE_URL   = "https://andrebanki.github.io/github_para_docs"

# ---------------------------------------------------------------------------
# Dados das etapas
# Cada etapa agrupa módulos relacionados e encerra com 5 perguntas teóricas
# que o colaborador deverá responder por comentário na tarefa do TargetProcess.
# ---------------------------------------------------------------------------
ETAPAS = [
    {
        "nome": "Etapa 1 — Fundação: Ambiente e Git",
        "descricao": (
            "<h3>Objetivo da etapa</h3>"
            "<p>Preparar o ambiente de trabalho e dominar o vocabulário e o fluxo "
            "básico do Git — pré-requisitos para todas as etapas seguintes.</p>"

            "<h3>Módulos desta etapa</h3>"

            "<h4>"
            "<a href='{site}/01-setup-ambiente.html'>Módulo 01 — VS Code e Configuração do Ambiente</a>"
            "</h4>"
            "<p>Instale as ferramentas, abra o repositório e aprenda a operar o Git "
            "pela interface visual do VS Code.</p>"
            "<ul>"
            "<li>Quais programas instalar primeiro (Git, Python, VS Code e extensões)</li>"
            "<li>Por que usar o VS Code como editor de documentação</li>"
            "<li>Todas as operações de Git pela interface visual — sem terminal</li>"
            "<li>Preview de Markdown e terminal integrado</li>"
            "</ul>"

            "<h4>"
            "<a href='{site}/02-git-para-documentacao.html'>Módulo 02 — Git para Documentação</a>"
            "</h4>"
            "<p>Entenda o raciocínio do trabalho com documentação versionada e o "
            "vocabulário do Git, sem precisar saber programar.</p>"
            "<ul>"
            "<li>O que é repositório, commit, branch e Pull Request</li>"
            "<li>O fluxo de trabalho diário (simplificado e completo)</li>"
            "<li>Os comandos essenciais e quando usá-los</li>"
            "<li>Como resolver conflitos e desfazer erros</li>"
            "</ul>"

            "<h3>Perguntas teóricas</h3>"
            "<p>Responda as perguntas abaixo por <strong>comentário nesta tarefa</strong> "
            "após concluir a leitura dos dois módulos.</p>"
            "<ol>"
            "<li>Quais são os 4 programas essenciais para começar a trabalhar com "
            "documentação como código e qual a ordem recomendada de instalação?</li>"
            "<li>Explique com suas palavras o que é um repositório Git e como ele se "
            "diferencia de uma pasta comum no computador.</li>"
            "<li>O que é um commit e por que é importante escrever mensagens descritivas?</li>"
            "<li>Qual a diferença entre <code>git pull</code> e <code>git push</code>, "
            "e em qual momento do fluxo diário cada um é usado?</li>"
            "<li>Por que o VS Code é preferido como editor de documentação nesse fluxo "
            "de trabalho?</li>"
            "</ol>"
        ).format(site=SITE_URL),
    },
    {
        "nome": "Etapa 2 — Conteúdo: Markdown, MkDocs e Publicação",
        "descricao": (
            "<h3>Objetivo da etapa</h3>"
            "<p>Dominar a escrita em Markdown, a geração do site com MkDocs e a "
            "publicação para acesso externo — o ciclo completo do conteúdo, da criação "
            "à disponibilização.</p>"

            "<h3>Módulos desta etapa</h3>"

            "<h4>"
            "<a href='{site}/03-markdown-e-mkdocs.html'>Módulo 03 — Markdown e MkDocs</a>"
            "</h4>"
            "<p>Aprenda a escrever em Markdown e a publicar um site de documentação "
            "navegável com MkDocs.</p>"
            "<ul>"
            "<li>O que é Markdown e por que usá-lo em vez de Word/Google Docs</li>"
            "<li>Sintaxe essencial: títulos, listas, tabelas, imagens, código</li>"
            "<li>Como o MkDocs transforma arquivos <code>.md</code> em site HTML</li>"
            "<li>Configuração do <code>mkdocs.yml</code> e preview local</li>"
            "</ul>"

            "<h4>"
            "<a href='{site}/06-publicacao-externa.html'>Módulo 06 — Publicando para Acesso Externo</a>"
            "</h4>"
            "<p>Publique a documentação gerada pelo MkDocs para acesso externo, "
            "escolhendo a opção certa para cada contexto.</p>"
            "<ul>"
            "<li>Opções disponíveis: GitHub Pages, Render.com, Keycloak e CloudOps</li>"
            "<li>Como escolher entre conteúdo público e privado</li>"
            "<li>Como funciona a atualização automática via GitHub Actions</li>"
            "</ul>"

            "<h3>Perguntas teóricas</h3>"
            "<p>Responda as perguntas abaixo por <strong>comentário nesta tarefa</strong> "
            "após concluir a leitura dos dois módulos.</p>"
            "<ol>"
            "<li>Cite 3 situações em que o Markdown seria mais vantajoso do que Word ou "
            "Google Docs para documentação técnica.</li>"
            "<li>Como o arquivo <code>mkdocs.yml</code> controla a estrutura de navegação "
            "do site? Descreva pelo menos 2 configurações importantes.</li>"
            "<li>Qual é o papel do GitHub Actions na publicação automática e como ele "
            "é acionado?</li>"
            "<li>Descreva a diferença entre publicar no GitHub Pages versus Render.com "
            "com autenticação Keycloak — em qual contexto você usaria cada opção?</li>"
            "<li>Qual comando visualiza o site localmente durante a edição, e o que "
            "acontece ao salvar um <code>.md</code> enquanto esse servidor está "
            "rodando?</li>"
            "</ol>"
        ).format(site=SITE_URL),
    },
    {
        "nome": "Etapa 3 — IA: Claude Code do Básico ao Avançado",
        "descricao": (
            "<h3>Objetivo da etapa</h3>"
            "<p>Usar o Claude Code como redator técnico assistente e configurá-lo para "
            "seguir automaticamente as convenções do repositório — do uso básico à "
            "personalização avançada.</p>"

            "<h3>Módulos desta etapa</h3>"

            "<h4>"
            "<a href='{site}/04-claude-code.html'>Módulo 04 — Claude Code</a>"
            "</h4>"
            "<p>Use o Claude Code como redator técnico assistente dentro do VS Code "
            "para acelerar a escrita e a revisão com IA.</p>"
            "<ul>"
            "<li>O que é o Claude Code e o que ele pode fazer</li>"
            "<li>Os modos de uso: Chat, Edição pelo Chat, Modo Agente e CLI</li>"
            "<li>Quando usar cada modo no fluxo diário</li>"
            "<li>Boas práticas para IA generativa em documentação</li>"
            "</ul>"

            "<h4>"
            "<a href='{site}/07-claude-code-customizacao.html'>Módulo 07 — Personalizando o Claude Code</a>"
            "</h4>"
            "<p>Configure o Claude Code para trabalhar com as convenções e padrões do "
            "seu repositório de documentação.</p>"
            "<ul>"
            "<li>Os 4 mecanismos: CLAUDE.md, Comandos Personalizados, Agente e Skills</li>"
            "<li>Onde colocar cada arquivo e como configurá-lo</li>"
            "<li>Tabela de decisão: quando usar cada mecanismo</li>"
            "<li>Exemplo prático de sessão de trabalho com agente</li>"
            "</ul>"

            "<h3>Perguntas teóricas</h3>"
            "<p>Responda as perguntas abaixo por <strong>comentário nesta tarefa</strong> "
            "após concluir a leitura dos dois módulos.</p>"
            "<ol>"
            "<li>Quais são os 4 modos de uso do Claude Code (Chat, Edição pelo Chat, "
            "Modo Agente e CLI)? Descreva brevemente quando cada um é adequado no "
            "fluxo diário.</li>"
            "<li>O que é o arquivo <code>CLAUDE.md</code> e qual a diferença entre "
            "colocá-lo na raiz do repositório versus em uma subpasta?</li>"
            "<li>Cite 2 boas práticas para usar IA generativa na criação de documentação "
            "técnica, justificando cada uma.</li>"
            "<li>Qual é a diferença entre um Comando Personalizado "
            "(<code>/meu-comando</code>) e uma Skill no Claude Code? Quando você "
            "escolheria um em vez do outro?</li>"
            "<li>Como você configuraria o Claude Code para que ele sempre siga as "
            "convenções do seu repositório sem precisar repetir as instruções a cada "
            "sessão?</li>"
            "</ol>"
        ).format(site=SITE_URL),
    },
    {
        "nome": "Etapa 4 — Colaboração e Padrões Reais",
        "descricao": (
            "<h3>Objetivo da etapa</h3>"
            "<p>Aprofundar o fluxo colaborativo com branches e Pull Requests e aplicar "
            "os padrões encontrados nos repositórios reais da AltoQi, incluindo a "
            "integração com o TargetProcess.</p>"

            "<h3>Módulos desta etapa</h3>"

            "<h4>"
            "<a href='{site}/05-branches-e-pull-requests.html'>Módulo 05 — Branches e Pull Requests</a>"
            "</h4>"
            "<p>Aprofunde o fluxo Git com branches isolados e revisão formal via "
            "Pull Request.</p>"
            "<ul>"
            "<li>O que é um branch e por que ele existe</li>"
            "<li>Como criar, navegar e trabalhar em branches</li>"
            "<li>O que é um Pull Request e como fazer revisão</li>"
            "<li>Como resolver conflitos de merge</li>"
            "<li>O fluxo completo passo a passo</li>"
            "</ul>"

            "<h4>"
            "<a href='{site}/08-instrucoes-especificas.html'>Módulo 08 — Instruções Específicas (Repositórios Reais)</a>"
            "</h4>"
            "<p>Padrões práticos encontrados nos repositórios reais da AltoQi: como "
            "documentar a partir do TargetProcess, espelhar épicos e organizar fontes "
            "com a pasta <code>raw/</code>.</p>"
            "<ul>"
            "<li>Dica 1 — Documentar features a partir do TargetProcess</li>"
            "<li>Dica 2 — Espelhar épicos do TargetProcess como páginas wiki</li>"
            "<li>Dica 3 — Pasta <code>raw/</code> como zona de entrada de fontes</li>"
            "</ul>"

            "<h3>Perguntas teóricas</h3>"
            "<p>Responda as perguntas abaixo por <strong>comentário nesta tarefa</strong> "
            "após concluir a leitura dos dois módulos.</p>"
            "<ol>"
            "<li>Por que criar um branch separado para cada feature ou correção, em vez "
            "de trabalhar diretamente na branch <code>main</code>?</li>"
            "<li>Descreva o processo completo de um Pull Request — da criação do branch "
            "ao merge — incluindo as etapas de revisão.</li>"
            "<li>O que é um conflito de merge e como o VS Code auxilia na resolução? "
            "Cite os tipos de escolha disponíveis durante a resolução.</li>"
            "<li>Como o fluxo do Módulo 08 integra o TargetProcess como fonte de "
            "documentação? O que seria documentado a partir de uma feature do TP?</li>"
            "<li>Qual é o propósito da pasta <code>raw/</code> nos repositórios reais "
            "da AltoQi e como ela se encaixa no fluxo de entrada de novos "
            "conteúdos?</li>"
            "</ol>"
        ).format(site=SITE_URL),
    },
    {
        "nome": "Etapa 5 — Consolidação Prática",
        "descricao": (
            "<h3>Objetivo da etapa</h3>"
            "<p>Aplicar e consolidar todo o conhecimento da trilha por meio de exercícios "
            "práticos que percorrem o fluxo de trabalho completo, do setup à publicação "
            "a partir do TargetProcess.</p>"

            "<h3>Módulos desta etapa</h3>"

            "<h4>"
            "<a href='{site}/09-exercicios-praticos.html'>Módulo 09 — Exercícios Práticos</a>"
            "</h4>"
            "<p>Revisão final da trilha com 10 exercícios focados, na ordem natural do "
            "fluxo de trabalho.</p>"
            "<ul>"
            "<li>Exercícios práticos com foco no uso do Claude Code</li>"
            "<li>O ciclo Git completo: do commit à publicação</li>"
            "<li>Cada exercício indica o módulo que reforça e o resultado esperado</li>"
            "</ul>"

            "<h3>Perguntas teóricas</h3>"
            "<p>Responda as perguntas abaixo por <strong>comentário nesta tarefa</strong> "
            "após concluir todos os exercícios.</p>"
            "<ol>"
            "<li>Descreva o ciclo completo para documentar uma nova feature: da abertura "
            "no TargetProcess até a publicação no site.</li>"
            "<li>Qual dos exercícios práticos foi mais desafiador para você e o que ele "
            "revelou sobre seu entendimento do fluxo de trabalho?</li>"
            "<li>Um colega que nunca usou Git precisa começar a contribuir com "
            "documentação — quais seriam os 3 primeiros passos que você "
            "recomendaria?</li>"
            "<li>Como você usaria o Claude Code para documentar um épico do "
            "TargetProcess com múltiplas user stories? Descreva o prompt ou comando "
            "que utilizaria.</li>"
            "<li>Quais são os 3 hábitos ou práticas que você pretende incorporar no "
            "seu trabalho diário com documentação após concluir a trilha?</li>"
            "</ol>"
        ).format(site=SITE_URL),
    },
]

# ---------------------------------------------------------------------------
# Descrição HTML do Template principal
# ---------------------------------------------------------------------------
TEMPLATE_NAME = "Documentação como Código — Guia AltoQi"

TRILHA_ITEMS = "".join(
    f"<li><a href='{SITE_URL}/{['01-setup-ambiente','03-markdown-e-mkdocs','04-claude-code','05-branches-e-pull-requests','09-exercicios-praticos'][i]}.html'>{e['nome']}</a></li>"
    for i, e in enumerate(ETAPAS)
)

ETAPAS_RESUMO = "".join(
    f"<li><strong>{e['nome']}</strong></li>"
    for e in ETAPAS
)

TEMPLATE_DESC = f"""
<h3>1. Objetivo</h3>
<p>
Capacitar equipes de Produto e Engenharia a colaborar em documentação técnica
usando Git, Markdown, MkDocs e Claude Code — mesmo sem experiência prévia com
ferramentas de desenvolvimento. Ao final da trilha, o participante consegue criar,
revisar e publicar documentação como um profissional.
</p>

<h3>2. Público-alvo</h3>
<ul>
<li>Equipes de Produto (PMs, redatores técnicos)</li>
<li>Equipes de Engenharia que mantêm documentação</li>
<li>Qualquer colaborador que precise contribuir com repositórios de documentação</li>
</ul>
<p><strong>Pré-requisito:</strong> nenhum — o curso começa do zero.</p>

<h3>3. Trilha das etapas</h3>
<ul>
{ETAPAS_RESUMO}
</ul>
<p>
Site do treinamento: <a href="{SITE_URL}">{SITE_URL}</a>
</p>

<h3>4. Como funciona</h3>
<p>
Cada etapa é uma tarefa separada neste projeto. Ao concluir a leitura dos módulos
de uma etapa, o colaborador responde as <strong>5 perguntas teóricas</strong>
por comentário na respectiva tarefa antes de avançar para a próxima.
</p>

<h3>5. Resultados esperados</h3>
<p>Ao final da trilha, os participantes serão capazes de:</p>
<ul>
<li>Usar Git no dia a dia para documentação (commit, push, pull, branch, PR)</li>
<li>Escrever e formatar documentação em Markdown</li>
<li>Publicar e manter um site de documentação com MkDocs</li>
<li>Usar o Claude Code para acelerar e padronizar a escrita</li>
<li>Configurar agentes e prompts personalizados para o contexto da equipe</li>
<li>Aplicar padrões dos repositórios reais da AltoQi (TP, épicos, raw/)</li>
</ul>
""".strip()

# ---------------------------------------------------------------------------
# Gabarito — tarefa exclusiva do instrutor
# Contém as respostas modelo das 25 perguntas teóricas (5 por etapa).
# ---------------------------------------------------------------------------
GABARITO_NAME = "[INSTRUTOR] Gabarito — Respostas Modelo das Perguntas Teóricas"

GABARITO_DESC = """
<p><strong>⚠️ Esta tarefa é exclusiva do instrutor. Não compartilhar com os participantes.</strong></p>
<p>
Contém as respostas modelo para as 5 perguntas teóricas de cada etapa do treinamento
<em>Documentação como Código — Guia AltoQi</em>. Use como referência ao avaliar os
comentários postados pelos colaboradores nas tarefas de cada etapa.
</p>
<p>
Perguntas abertas (marcadas com ★) não têm resposta única — avalie pela coerência,
reflexão e relação com o conteúdo da trilha. O critério de avaliação está indicado
junto à resposta modelo.
</p>

<hr/>

<h2>Etapa 1 — Fundação: Ambiente e Git</h2>

<h4>Pergunta 1</h4>
<p><em>Quais são os 4 programas essenciais para começar a trabalhar com documentação
como código e qual a ordem recomendada de instalação?</em></p>
<p><strong>Resposta modelo:</strong> Git → Python → VS Code → Extensões do VS Code
(Python, GitLens, Markdown Preview Enhanced). Git primeiro porque é a base de controle
de versão; Python porque o MkDocs é instalado via pip; VS Code depois de ambos para já
detectar as ferramentas automaticamente; extensões por último pois dependem do VS Code
instalado.</p>

<h4>Pergunta 2</h4>
<p><em>Explique com suas palavras o que é um repositório Git e como ele se diferencia
de uma pasta comum no computador.</em></p>
<p><strong>Resposta modelo:</strong> Um repositório Git é uma pasta que contém, além dos
arquivos, um histórico completo de todas as alterações feitas neles ao longo do tempo.
A diferença principal é que uma pasta comum só guarda o estado atual dos arquivos,
enquanto o repositório Git permite voltar a qualquer versão anterior, comparar mudanças,
trabalhar em paralelo em branches e colaborar com outras pessoas sem sobrescrever o
trabalho alheio.</p>

<h4>Pergunta 3</h4>
<p><em>O que é um commit e por que é importante escrever mensagens descritivas?</em></p>
<p><strong>Resposta modelo:</strong> Um commit é um "snapshot" do estado dos arquivos em
um determinado momento, acompanhado de uma mensagem explicativa. Mensagens descritivas
são importantes porque permitem entender, sem abrir os arquivos, o que foi alterado e
por quê — facilitando revisão histórica, identificação de erros e colaboração em
equipe.</p>

<h4>Pergunta 4</h4>
<p><em>Qual a diferença entre <code>git pull</code> e <code>git push</code>, e em qual
momento do fluxo diário cada um é usado?</em></p>
<p><strong>Resposta modelo:</strong> <code>git pull</code> baixa as alterações do
repositório remoto (GitHub) para o computador local — usado no início do trabalho para
garantir a versão mais recente. <code>git push</code> envia as alterações locais para o
remoto — usado após os commits para compartilhar o trabalho e atualizar o site.</p>

<h4>Pergunta 5</h4>
<p><em>Por que o VS Code é preferido como editor de documentação nesse fluxo de
trabalho?</em></p>
<p><strong>Resposta modelo:</strong> O VS Code reúne em uma única ferramenta: editor
com highlight de Markdown, interface visual do Git (Source Control), terminal integrado,
preview de Markdown e suporte à extensão do Claude Code — eliminando a necessidade de
alternar entre múltiplos programas e reduzindo o atrito para quem não tem experiência
com linha de comando.</p>

<hr/>

<h2>Etapa 2 — Conteúdo: Markdown, MkDocs e Publicação</h2>

<h4>Pergunta 1</h4>
<p><em>Cite 3 situações em que o Markdown seria mais vantajoso do que Word ou Google
Docs para documentação técnica.</em></p>
<p><strong>Resposta modelo:</strong> (1) Documentação versionada com Git — arquivos
<code>.md</code> são texto puro, permitindo diff linha a linha e histórico completo,
impossível com <code>.docx</code>. (2) Inclusão de blocos de código — o Markdown tem
sintaxe nativa para código com highlight, enquanto o Word exige formatação manual.
(3) Geração automática de site — o MkDocs converte <code>.md</code> em HTML navegável
sem trabalho extra; o Word exige exportação manual a cada atualização.</p>

<h4>Pergunta 2</h4>
<p><em>Como o arquivo <code>mkdocs.yml</code> controla a estrutura de navegação do
site? Descreva pelo menos 2 configurações importantes.</em></p>
<p><strong>Resposta modelo:</strong> O <code>mkdocs.yml</code> é o arquivo central de
configuração. Duas configurações importantes: (1) <code>nav</code> — define a hierarquia
de páginas e o menu lateral, mapeando títulos visíveis para arquivos <code>.md</code>;
(2) <code>theme</code> — define o visual do site (ex.: material), com paleta de cores,
logo e busca. Outras válidas: <code>site_name</code> e <code>repo_url</code>.</p>

<h4>Pergunta 3</h4>
<p><em>Qual é o papel do GitHub Actions na publicação automática e como ele é
acionado?</em></p>
<p><strong>Resposta modelo:</strong> O GitHub Actions executa workflows automaticamente
em resposta a eventos no repositório. No contexto do MkDocs, é configurado para rodar
<code>mkdocs gh-deploy</code> toda vez que um push ocorre na branch <code>main</code>
— qualquer commit aprovado que chegue à main dispara a reconstrução e publicação do site
sem intervenção manual.</p>

<h4>Pergunta 4</h4>
<p><em>Descreva a diferença entre publicar no GitHub Pages versus Render.com com
autenticação Keycloak. Em qual contexto você usaria cada opção?</em></p>
<p><strong>Resposta modelo:</strong> GitHub Pages publica o site publicamente, acessível
por qualquer pessoa sem login — ideal para documentação aberta ou pública. Render.com com
Keycloak adiciona autenticação, exigindo login — usado quando a documentação é interna
ou restrita a colaboradores autorizados, como manuais de produto ou documentação
confidencial.</p>

<h4>Pergunta 5</h4>
<p><em>Qual comando visualiza o site localmente durante a edição, e o que acontece ao
salvar um <code>.md</code> enquanto esse servidor está rodando?</em></p>
<p><strong>Resposta modelo:</strong> O comando é <code>mkdocs serve</code>. Ao salvar
qualquer arquivo <code>.md</code> (ou o próprio <code>mkdocs.yml</code>), o servidor
detecta a alteração automaticamente, reconstrói o site e recarrega o browser (live
reload) — sem precisar rodar o comando novamente.</p>

<hr/>

<h2>Etapa 3 — IA: Claude Code do Básico ao Avançado</h2>

<h4>Pergunta 1</h4>
<p><em>Quais são os 4 modos de uso do Claude Code? Descreva brevemente quando cada
um é adequado no fluxo diário.</em></p>
<p><strong>Resposta modelo:</strong> (1) <strong>Chat</strong> — conversação sem edição
de arquivos; para tirar dúvidas e explorar ideias. (2) <strong>Edição pelo Chat</strong>
— o Claude propõe alterações que o usuário aceita ou rejeita; para revisões pontuais.
(3) <strong>Modo Agente</strong> — o Claude age autonomamente: lê, edita e cria
arquivos; para tarefas maiores como criar um módulo inteiro. (4) <strong>CLI</strong>
— execução via terminal; para automações e scripts repetitivos.</p>

<h4>Pergunta 2</h4>
<p><em>O que é o arquivo <code>CLAUDE.md</code> e qual a diferença entre colocá-lo
na raiz do repositório versus em uma subpasta?</em></p>
<p><strong>Resposta modelo:</strong> O <code>CLAUDE.md</code> contém instruções
permanentes que o Claude Code lê automaticamente ao iniciar uma sessão. Na raiz, as
instruções se aplicam a todo o projeto. Em uma subpasta, aplicam-se apenas quando o
Claude trabalha com arquivos daquela pasta — útil para repositórios com seções de
convenções distintas.</p>

<h4>Pergunta 3</h4>
<p><em>Cite 2 boas práticas para usar IA generativa na criação de documentação técnica,
justificando cada uma.</em></p>
<p><strong>Resposta modelo:</strong> (1) <strong>Sempre revisar o conteúdo gerado antes
de publicar</strong> — a IA pode produzir informações plausíveis mas incorretas
(alucinações); o autor é responsável pela precisão técnica. (2) <strong>Fornecer
contexto específico nos prompts</strong> — quanto mais detalhado o prompt
(público-alvo, tom, estrutura esperada), mais alinhado ao padrão do repositório será
o resultado.</p>

<h4>Pergunta 4</h4>
<p><em>Qual é a diferença entre um Comando Personalizado (<code>/meu-comando</code>) e
uma Skill no Claude Code? Quando você escolheria um em vez do outro?</em></p>
<p><strong>Resposta modelo:</strong> Um Comando Personalizado é um atalho de prompt
(arquivo <code>.md</code> em <code>.claude/commands/</code>) — ao digitá-lo, o Claude
recebe aquele texto de instrução. Uma Skill é um conjunto mais sofisticado de instruções
com lógica estruturada, podendo orquestrar múltiplos passos. O Comando é melhor para
tarefas simples e repetitivas; a Skill para fluxos complexos com múltiplas etapas
condicionais.</p>

<h4>Pergunta 5</h4>
<p><em>Como você configuraria o Claude Code para que ele sempre siga as convenções
do repositório sem repetir as instruções a cada sessão?</em></p>
<p><strong>Resposta modelo:</strong> Criando um arquivo <code>CLAUDE.md</code> na raiz
do repositório com as convenções do projeto (tom, estrutura de seções, padrões de
nomenclatura, exemplos). O Claude lê esse arquivo automaticamente a cada sessão. Para
regras mais específicas por contexto, criar <code>CLAUDE.md</code> adicionais nas
subpastas relevantes.</p>

<hr/>

<h2>Etapa 4 — Colaboração e Padrões Reais</h2>

<h4>Pergunta 1</h4>
<p><em>Por que criar um branch separado para cada feature em vez de trabalhar
diretamente na <code>main</code>?</em></p>
<p><strong>Resposta modelo:</strong> Trabalhar na <code>main</code> diretamente expõe
qualquer erro à versão publicada imediatamente (via GitHub Actions). Um branch isolado
permite desenvolver, revisar e testar antes de integrar — protegendo a <code>main</code>
de conteúdo incompleto. Além disso, múltiplas pessoas podem trabalhar em paralelo em
branches diferentes sem interferir umas nas outras.</p>

<h4>Pergunta 2</h4>
<p><em>Descreva o processo completo de um Pull Request — da criação do branch ao merge
— incluindo as etapas de revisão.</em></p>
<p><strong>Resposta modelo:</strong> (1) Criar branch com nome descritivo a partir da
<code>main</code>; (2) fazer commits com as alterações no branch; (3) fazer push para o
GitHub; (4) abrir o PR descrevendo as mudanças; (5) revisores leem o diff, comentam e
aprovam ou pedem ajustes; (6) o autor responde e faz novos commits se necessário;
(7) após aprovação, o PR é mergeado na <code>main</code> e o branch pode ser
deletado.</p>

<h4>Pergunta 3</h4>
<p><em>O que é um conflito de merge e como o VS Code auxilia na resolução? Cite os
tipos de escolha disponíveis.</em></p>
<p><strong>Resposta modelo:</strong> Um conflito de merge ocorre quando dois branches
modificaram a mesma parte do mesmo arquivo e o Git não consegue decidir qual versão
manter. O VS Code exibe o arquivo com as duas versões marcadas e oferece 3 opções:
<strong>Accept Current Change</strong> (versão do branch atual),
<strong>Accept Incoming Change</strong> (versão do branch que está sendo mergeado) e
<strong>Accept Both Changes</strong> (ambas as versões, uma após a outra).</p>

<h4>Pergunta 4</h4>
<p><em>Como o fluxo do Módulo 08 integra o TargetProcess como fonte de documentação?
O que seria documentado a partir de uma feature do TP?</em></p>
<p><strong>Resposta modelo:</strong> O fluxo consiste em usar a descrição de uma feature
ou user story do TargetProcess como insumo para o Claude Code gerar o rascunho da
documentação correspondente. O autor copia o conteúdo do TP (objetivo, critérios de
aceite, contexto), fornece ao Claude com um prompt direcionado, revisa o resultado e
commita o arquivo <code>.md</code>. O site é atualizado automaticamente via GitHub
Actions.</p>

<h4>Pergunta 5</h4>
<p><em>Qual é o propósito da pasta <code>raw/</code> nos repositórios reais da AltoQi
e como ela se encaixa no fluxo de entrada de novos conteúdos?</em></p>
<p><strong>Resposta modelo:</strong> A pasta <code>raw/</code> funciona como zona de
entrada para fontes brutas — textos não formatados, exports de ferramentas, notas
avulsas. Fluxo: (1) depositar o arquivo bruto na <code>raw/</code>; (2) usar o Claude
Code para transformá-lo em Markdown formatado; (3) mover o resultado para a pasta de
destino correta; (4) commitar e publicar. Isso separa claramente o insumo bruto do
conteúdo publicável.</p>

<hr/>

<h2>Etapa 5 — Consolidação Prática</h2>

<h4>Pergunta 1</h4>
<p><em>Descreva o ciclo completo para documentar uma nova feature: da abertura no
TargetProcess até a publicação no site.</em></p>
<p><strong>Resposta modelo:</strong> (1) Consultar a feature no TargetProcess para
entender objetivo e critérios de aceite; (2) criar um branch com nome relacionado à
feature; (3) depositar na <code>raw/</code> qualquer insumo bruto disponível; (4) usar
o Claude Code para gerar o rascunho em Markdown a partir do conteúdo do TP; (5) revisar
e ajustar; (6) adicionar a página ao <code>mkdocs.yml</code>; (7) rodar
<code>mkdocs serve</code> para validar localmente; (8) commitar e fazer push; (9) abrir
PR, revisar e mergear na <code>main</code>; (10) GitHub Actions publica
automaticamente.</p>

<h4>Pergunta 2 ★ (resposta aberta)</h4>
<p><em>Qual dos exercícios práticos foi mais desafiador para você e o que ele revelou
sobre seu entendimento do fluxo de trabalho?</em></p>
<p><strong>Critério de avaliação:</strong> Avaliar se o colaborador identifica o
exercício com clareza e explica o que dificultou (ex.: resolução de conflito, uso do
Claude Code, configuração do <code>mkdocs.yml</code>) e se demonstra aprendizado a
partir da dificuldade. Respostas vagas como "todos foram fáceis" ou sem justificativa
merecem aprofundamento no feedback individual.</p>

<h4>Pergunta 3</h4>
<p><em>Um colega que nunca usou Git precisa começar a contribuir com documentação —
quais seriam os 3 primeiros passos que você recomendaria?</em></p>
<p><strong>Resposta modelo:</strong> (1) Instalar Git e VS Code (Módulo 01); (2) clonar
o repositório via VS Code (Módulo 01); (3) fazer a primeira edição, commit e push usando
apenas a interface visual do VS Code, sem terminal (Módulos 01 e 02). Avaliar se o
colaborador recomenda entrada suave pela interface visual — não jogar o colega direto
no terminal.</p>

<h4>Pergunta 4</h4>
<p><em>Como você usaria o Claude Code para documentar um épico do TargetProcess com
múltiplas user stories? Descreva o prompt ou comando que utilizaria.</em></p>
<p><strong>Resposta modelo:</strong> Usar o Modo Agente do Claude Code, com as
convenções do repositório no <code>CLAUDE.md</code>; copiar as descrições das user
stories do TP e pedir ao Claude que gere uma página por story dentro da estrutura do
épico; revisar cada página gerada; atualizar o <code>mkdocs.yml</code> com as novas
entradas; commitar o conjunto. Avaliar se o colaborador menciona revisão humana e
integração com o <code>mkdocs.yml</code>.</p>

<h4>Pergunta 5 ★ (resposta aberta)</h4>
<p><em>Quais são os 3 hábitos ou práticas que você pretende incorporar no seu trabalho
diário com documentação após concluir a trilha?</em></p>
<p><strong>Critério de avaliação:</strong> Avaliar se os hábitos citados são concretos e
relacionados ao fluxo aprendido (ex.: "fazer commit ao final de cada sessão", "criar
branch para cada nova seção", "usar Claude Code para revisar antes de abrir PR",
"depositar fontes na <code>raw/</code> antes de formatar"). Respostas genéricas sem
relação direta com a trilha indicam absorção superficial — considerar conversa de
acompanhamento.</p>
""".strip()

# ---------------------------------------------------------------------------
# Helpers HTTP
# ---------------------------------------------------------------------------

def tp_get(path: str) -> dict:
    url = f"{BASE_URL}/api/v1/{path}?format=json&access_token={TOKEN}"
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.loads(r.read())


def tp_post(path: str, body: dict) -> dict:
    url = f"{BASE_URL}/api/v1/{path}?format=json&access_token={TOKEN}"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(dry_run: bool = False) -> None:
    if not TOKEN:
        sys.exit("❌  TARGETPROCESS_TOKEN não encontrado. Verifique o arquivo .env")

    print(f"🔗  Base URL : {BASE_URL}")
    print(f"📁  Projeto  : AltoQi Treinamento (Id={PROJECT_ID})")
    print(f"🧪  Dry-run  : {dry_run}\n")

    # ------------------------------------------------------------------
    # 1. Criar o Template (Request)
    # ------------------------------------------------------------------
    template_payload = {
        "Name": TEMPLATE_NAME,
        "Description": TEMPLATE_DESC,
        "Project": {"Id": PROJECT_ID},
    }

    print(f"📄  Criando Template: {TEMPLATE_NAME}")
    if dry_run:
        print("  [DRY-RUN] payload:")
        print(json.dumps(template_payload, indent=2, ensure_ascii=False)[:800])
        template_id = 0
    else:
        resp = tp_post("Requests", template_payload)
        template_id = resp["Id"]
        print(f"  ✅  Template criado — Id={template_id}")
        print(f"  🔗  https://altoqi.tpondemand.com/entity/{template_id}")

    print()

    # ------------------------------------------------------------------
    # 2. Criar as UserStories (etapas) e vincular ao Template
    # ------------------------------------------------------------------
    for i, etapa in enumerate(ETAPAS, 1):
        story_payload = {
            "Name": etapa["nome"],
            "Description": etapa["descricao"],
            "Project": {"Id": PROJECT_ID},
        }

        print(f"  📝  [{i}/{len(ETAPAS)}] Criando etapa: {etapa['nome']}")

        if dry_run:
            story_id = i * 1000
            print(f"       [DRY-RUN] seria criada a UserStory e vinculada ao Template")
        else:
            story_resp = tp_post("UserStories", story_payload)
            story_id = story_resp["Id"]
            print(f"       ✅  UserStory Id={story_id}")

            rel_payload = {
                "Master": {"Id": template_id},
                "Slave": {"Id": story_id},
                "RelationType": {"Id": 3},  # Relation
            }
            rel_resp = tp_post("Relations", rel_payload)
            print(f"       🔗  Relation criada — Id={rel_resp['Id']}")

    # ------------------------------------------------------------------
    # 3. Criar a UserStory exclusiva do instrutor (gabarito)
    # ------------------------------------------------------------------
    gabarito_payload = {
        "Name": GABARITO_NAME,
        "Description": GABARITO_DESC,
        "Project": {"Id": PROJECT_ID},
    }

    print(f"  🔒  Criando tarefa do instrutor: {GABARITO_NAME}")

    if dry_run:
        print(f"       [DRY-RUN] seria criada a UserStory do gabarito e vinculada ao Template")
    else:
        gabarito_resp = tp_post("UserStories", gabarito_payload)
        gabarito_id = gabarito_resp["Id"]
        print(f"       ✅  UserStory Id={gabarito_id}")

        rel_payload = {
            "Master": {"Id": template_id},
            "Slave": {"Id": gabarito_id},
            "RelationType": {"Id": 3},  # Relation
        }
        rel_resp = tp_post("Relations", rel_payload)
        print(f"       🔗  Relation criada — Id={rel_resp['Id']}")

    print()
    if not dry_run:
        print(f"🎉  Concluído! Template disponível em:")
        print(f"    https://altoqi.tpondemand.com/entity/{template_id}")
    else:
        print("🏁  Dry-run finalizado. Remova --dry-run para criar no TargetProcess.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cria o Template de Treinamento no TargetProcess")
    parser.add_argument("--dry-run", action="store_true", help="Exibe payloads sem criar nada")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
