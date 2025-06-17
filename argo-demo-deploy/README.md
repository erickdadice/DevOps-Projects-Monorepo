# ArgoCD Demo Deploy 🚀

Este proyecto simula el despliegue GitOps de una aplicación Python (FastAPI) utilizando **Kustomize** y **ArgoCD**, siguiendo las mejores prácticas para entornos separados (`dev`, `qa`, `main`).

---

## 📦 Contenido

- `app/`: Código fuente Python (FastAPI)
- `Dockerfile`: Contenedor para la aplicación
- `kustomize/base`: Configuración base (deployment, service, ingress)
- `kustomize/overlays/`: Parches específicos por entorno
- `docs/`: Carpeta para imágenes y guía visual

---

## ▶️ Cómo probar localmente

```bash
# Construir imagen
docker build -t argocd-demo-app .

# Ejecutar localmente
docker run -p 8080:80 argocd-demo-app

# Probar en navegador o curl
curl http://localhost:8080/
```

---

## ⚙️ Estructura Kustomize

```
kustomize/
├── base/
│   ├── deployment.yml
│   ├── ingress.yml
│   ├── service.yml
│   └── kustomization.yml
└── overlays/
    ├── dev/
    ├── qa/
    └── main/
```

Puedes copiar `base/` a cada overlay y modificar:
- Imagen (`deployment_overlay.yml`)
- Namespace
- Ingress path

---

## 📸 Despliegue simulado en ArgoCD

### Requisitos

- ArgoCD instalado en tu clúster AKS o K8s
- Repositorio Git accesible con estos archivos

### Pasos

1. **Crear aplicación en ArgoCD UI**
   - Name: `argocd-demo-dev`
   - Repo URL: tu repositorio
   - Revision: `main`
   - Path: `kustomize/overlays/dev`
   - Project: `default`
   - Enable Auto-Sync ✅

2. **Sincronizar cambios**
   - Al hacer `git push` sobre los manifiestos, ArgoCD aplicará el cambio.

3. **Rollback**
   - Desde la pestaña *History* puedes hacer rollback a un estado anterior.

4. **Monitoreo**
   - Verifica eventos y estado de recursos desde la UI

---

## 🖼️ Documentación visual

Guarda tus capturas de pantalla en la carpeta `docs/` para ilustrar:

- Acceso a ArgoCD UI
- Configuración de la App
- Resultado del despliegue

---

## 💡 Próximos pasos

- Agregar CI/CD para build + push a DockerHub/ACR
- Actualizar manifiestos automáticamente
- Conectar con GitHub Actions para flujo completo

