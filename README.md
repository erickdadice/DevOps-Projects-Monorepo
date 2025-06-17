# 🧱 DevOps Monorepo: Multi-Proyecto con Filtros GitHub Actions

Este repositorio contiene múltiples proyectos DevOps organizados como subcarpetas independientes. Cada uno tiene su propio flujo de CI/CD que se activa **solo cuando se modifica su carpeta** usando `paths:` en los workflows.

## 🗂️ Estructura

```
.
├── .github/workflows/   # Flujos filtrados
├── pokedex/             # App Node.js + Deploy Vercel
├── skills-test/         # Laboratorio de Actions
├── skills-azure/        # Azure Deploy con Docker
├── python-basic/        # Python Lint + Test
├── python-vercel/       # Python Deploy a Vercel
├── argo-gitops-app/     # App Python GitOps
└── argo-gitops-ops/     # Manifiestos GitOps
```

## 🚀 Workflows

Cada flujo tiene esta configuración:

```yaml
on:
  push:
    paths:
      - "nombre-subcarpeta/**"
```

Esto asegura que solo el flujo de `pokedex/` se dispare si cambias archivos en `pokedex/`.

## 🛠️ Requisitos

- Configura los secretos de Vercel (`VERCEL_TOKEN`, `VERCEL_PROJECT_ID`, etc.) donde aplique
- Usa `OPS_REPO_TOKEN` para el flujo GitOps automático

