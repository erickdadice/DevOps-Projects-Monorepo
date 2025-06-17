# Skills Deploy to Azure

Este proyecto demuestra cómo desplegar una aplicación web a Azure App Service utilizando GitHub Actions.

## 🧱 Tecnologías

- Node.js (App base)
- Azure App Service
- GitHub Actions

## ⚙️ Flujo de trabajo

El pipeline realiza:
- Instalación y build
- Login en Azure con secretos
- Deploy a App Service

## 🪪 Secrets necesarios

- `AZURE_WEBAPP_NAME`
- `AZURE_PUBLISH_PROFILE`
