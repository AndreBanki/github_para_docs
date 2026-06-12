---
title: Início
---

<div class="course-hero" markdown="0">
  <span class="eyebrow">Curso AltoQi · Produto &amp; Engenharia</span>
  <h1>Documentação como <span class="hl">Código</span></h1>
  <p class="lead">Aprenda a colaborar em documentação de produto usando Git, Markdown, MkDocs e GitHub Copilot — mesmo que você nunca tenha usado Git na vida.</p>
  <div class="course-meta">
    <span>📚 <b>8</b> módulos</span>
    <span>🎯 Nível <b>iniciante</b></span>
    <span>⏱️ ~<b>4h</b> de estudo</span>
    <span>💻 Prática guiada no VS Code</span>
  </div>
  <div class="cta-row">
    <a class="cta-btn primary" href="01-git-para-documentacao.html">Começar o curso →</a>
    <a class="cta-btn ghost" href="#modulos">Ver módulos</a>
  </div>
</div>

!!! tip "Primeira vez aqui?"
    Este material foi feito para quem **nunca usou Git**. Siga os módulos em ordem — cada um constrói sobre o anterior. Ao final, você vai conseguir colaborar em documentação como um profissional.

<p class="home-section-title" id="modulos">Trilha do curso</p>

<div class="module-grid" markdown="0">
  <a class="module-card" href="01-git-para-documentacao.html">
    <span class="mod-icon">🔀</span>
    <span class="mod-num">Módulo 01</span>
    <span class="mod-title">Git para Documentação</span>
    <span class="mod-desc">Repositório, commit, push/pull e o fluxo de trabalho diário — simplificado e completo.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card" href="02-vscode-e-copilot.html">
    <span class="mod-icon">🧩</span>
    <span class="mod-num">Módulo 02</span>
    <span class="mod-title">VS Code e GitHub Copilot</span>
    <span class="mod-desc">Instalação do ambiente, extensões, Git visual e os modos de uso do Copilot no dia a dia.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card" href="03-markdown-e-mkdocs.html">
    <span class="mod-icon">📝</span>
    <span class="mod-num">Módulo 03</span>
    <span class="mod-title">Markdown e MkDocs</span>
    <span class="mod-desc">Sintaxe Markdown, preview local, build/serve do MkDocs, temas e o plugin awesome-pages.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card" href="04-branches-e-pull-requests.html">
    <span class="mod-icon">🌿</span>
    <span class="mod-num">Módulo 04</span>
    <span class="mod-title">Branches e Pull Requests</span>
    <span class="mod-desc">Aprofundamento do fluxo completo: branches isolados, revisão por PR e resolução de conflitos.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card" href="05-publicacao-externa.html">
    <span class="mod-icon">🌐</span>
    <span class="mod-num">Módulo 05</span>
    <span class="mod-title">Publicando para Acesso Externo</span>
    <span class="mod-desc">GitHub Pages, Render.com, Keycloak e CloudOps — como escolher e como atualizar o site.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card" href="06-copilot-customizacao.html">
    <span class="mod-icon">⚙️</span>
    <span class="mod-num">Módulo 06</span>
    <span class="mod-title">Personalizando o Copilot</span>
    <span class="mod-desc">Instructions, prompts reutilizáveis, agentes e skills para documentação.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card extra" href="07-instrucoes-especificas.html">
    <span class="mod-icon">⭐</span>
    <span class="mod-num">Módulo 07</span>
    <span class="mod-title">Instruções Específicas</span>
    <span class="mod-desc">Padrões de repositórios reais: Targetprocess, espelhamento de épicos e pasta <code>raw/</code>.</span>
    <span class="mod-go">Iniciar →</span>
  </a>
  <a class="module-card extra" href="08-exercicios-praticos.html">
    <span class="mod-icon">🧪</span>
    <span class="mod-num">Módulo 08</span>
    <span class="mod-title">Exercícios Práticos</span>
    <span class="mod-desc">Revisão final da trilha com exercícios organizados na mesma ordem dos módulos.</span>
    <span class="mod-go">Praticar →</span>
  </a>
</div>

<p class="home-section-title">Fluxo de trabalho que você vai dominar</p>

```mermaid
flowchart LR
    A["🔄 git pull\nAtualizar"] --> B["✏️ Editar\narquivos .md"] --> C["📦 git add + commit\nRegistrar"] --> D["🚀 git push\nPublicar"]
    style A fill:#0a2a1c,stroke:#1aa863,color:#d4ede0
    style B fill:#0c3322,stroke:#25CE7B,color:#dcfaea
    style C fill:#0e3d28,stroke:#3BE592,color:#e3fff1
    style D fill:#114e34,stroke:#25CE7B,color:#ffffff
```

<p class="home-section-title">Pré-requisitos</p>

<div class="prereq-grid" markdown="0">
  <div class="prereq-item">
    <span class="pi-icon">🟧</span>
    <div><a href="https://git-scm.com">Git</a><small>controle de versão</small></div>
  </div>
  <div class="prereq-item">
    <span class="pi-icon">🐍</span>
    <div><a href="https://www.python.org">Python 3.10+</a><small>roda o MkDocs</small></div>
  </div>
  <div class="prereq-item">
    <span class="pi-icon">🔷</span>
    <div><a href="https://code.visualstudio.com">VS Code</a><small>editor</small></div>
  </div>
  <div class="prereq-item">
    <span class="pi-icon">🤖</span>
    <div><a href="https://marketplace.visualstudio.com/items?itemName=GitHub.copilot">GitHub Copilot</a><small>extensão do VS Code</small></div>
  </div>
</div>
