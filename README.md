# EP2 - DevOps Microservicios

Proyecto de dos microservicios desarrollados con Python y FastAPI: **Catalog**, para consultar productos, y **Orders**, para gestionar pedidos.

## Pipeline CI/CD

El pipeline se ejecuta al subir cambios a `main`, crear un pull request o iniciarlo manualmente. Incluye cinco etapas:

1. **Pruebas:** pytest verifica el código y exige un 80 % de cobertura.
2. **Seguridad:** Snyk revisa las dependencias en busca de vulnerabilidades.
3. **Calidad:** SonarCloud analiza el código. Si falla la Quality Gate, el despliegue puede continuar.
4. **Construcción:** Docker genera las imágenes de ambos microservicios.
5. **Despliegue:** Docker Compose levanta los servicios y ejecuta pruebas de integración.

## Trazabilidad y calidad

Los commits permiten identificar cada cambio y GitHub Actions guarda el resultado de cada ejecución. Los reportes de pytest, Snyk y SonarCloud ayudan a detectar errores y revisar la calidad del código.

El despliegue es simulado y los contenedores se detienen al terminar las pruebas.
