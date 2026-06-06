/* AltoQi Curso — tema escuro do Mermaid + ajustes da home */

if (window.mermaid) {
  window.mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
    theme: "base",
    fontFamily: "'Inter', 'Segoe UI', sans-serif",
    themeVariables: {
      background: "#0a0e1c",
      primaryColor: "#0f1626",
      primaryTextColor: "#F1F5F9",
      primaryBorderColor: "#25CE7B",
      lineColor: "#25CE7B",
      secondaryColor: "#114e34",
      tertiaryColor: "#0c1020",
      clusterBkg: "#0c1020",
      clusterBorder: "#25CE7B",
      edgeLabelBackground: "#0a0e1c",
      nodeTextColor: "#F1F5F9",
      titleColor: "#3BE592",

      /* ── gitGraph (Módulo 5) ── */
      git0: "#3BE592",
      git1: "#25CE7B",
      git2: "#34d399",
      git3: "#1aa863",
      git4: "#5eead4",
      git5: "#2dd4bf",
      git6: "#86efac",
      git7: "#4ade80",
      gitBranchLabel0: "#04130b",
      gitBranchLabel1: "#04130b",
      gitBranchLabel2: "#04130b",
      gitBranchLabel3: "#04130b",
      gitBranchLabel4: "#04130b",
      gitBranchLabel5: "#04130b",
      gitBranchLabel6: "#04130b",
      gitBranchLabel7: "#04130b",
      commitLabelColor: "#e3fff1",
      commitLabelBackground: "#0c1322",
      commitLabelFontSize: "12px",
      tagLabelColor: "#e3fff1",
      tagLabelBackground: "#114e34",
      tagLabelBorder: "#25CE7B",
      tagLabelFontSize: "12px"
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  if (window.mermaid && typeof window.mermaid.run === "function") {
    try {
      window.mermaid.run({ querySelector: ".mermaid" });
    } catch (e) {
      console.warn("Mermaid render:", e);
    }
  }

  var path = window.location.pathname;
  if (
    path.endsWith("/") ||
    path.endsWith("/index.html") ||
    path.endsWith("/curso_github/") ||
    /\/$/.test(path)
  ) {
    document.body.classList.add("course-home");
  }
});
