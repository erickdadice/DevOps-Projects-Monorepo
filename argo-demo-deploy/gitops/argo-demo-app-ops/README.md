# argo-demo-app-ops

Repositorio de operaciones (infraestructura) para el despliegue GitOps con ArgoCD.

Este repositorio contiene los manifiestos Kustomize de la aplicación `argo-demo-app`, separados por entorno (`dev`, `qa`, `main`).

## Estructura

```
argo-demo-app-ops/
├── base/
│   ├── deployment.yml
│   ├── service.yml
│   ├── ingress.yml
│   └── kustomization.yml
└── overlays/
    ├── dev/
    │   ├── deployment_overlay.yml
    │   └── kustomization.yml
    ├── qa/
    └── main/
```

## Uso con ArgoCD

En la creación de una App en ArgoCD:

- **Repo URL**: este repositorio
- **Path**: `overlays/dev`
- **Revision**: `main`
- **Sync Policy**: automática (opcional)

