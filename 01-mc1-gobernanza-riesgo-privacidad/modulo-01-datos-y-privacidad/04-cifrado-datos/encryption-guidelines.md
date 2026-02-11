# Directrices de Cifrado (Encryption Guidelines) – Módulo 1

## 1. Objetivo
Establecer criterios para cifrar datos sensibles, especialmente PII, reduciendo el impacto de una brecha de seguridad.

## 2. Cifrado en tránsito (Data in Transit)
- Usar **TLS (HTTPS)** para comunicaciones entre:
  - Usuario ↔ Aplicación
  - Aplicación ↔ API
  - Aplicación ↔ Base de datos (cuando aplique)
- Rechazar protocolos inseguros (HTTP sin TLS).
- Recomendación: mantener configuraciones modernas y certificados vigentes.

## 3. Cifrado en reposo (Data at Rest)
Aplicar cifrado en:
- Bases de datos que contengan PII (cifrado a nivel de disco/BD).
- Backups (siempre cifrados).
- Discos/volúmenes de servidores con información sensible.
- Ficheros exportados (CSV, informes) si contienen PII.

## 4. Gestión de claves (Key Management) – Enfoque profesional
- Las claves deben:
  - Almacenarse de forma segura (no en repositorios, no en texto plano).
  - Rotarse periódicamente (política de rotación).
  - Tener control de acceso (solo roles autorizados).
- Separación recomendada:
  - Datos cifrados (en sistemas)
  - Claves (en un gestor de claves / vault, concepto)

## 5. Buenas prácticas complementarias
- **No confundir hashing con cifrado**:
  - Hashing (irreversible): contraseñas
  - Cifrado (reversible): datos que se deben recuperar
- Evitar exponer PII en logs; usar enmascaramiento o pseudonimización.

## 6. Resultado esperado
Incluso si un atacante accede a almacenamiento o backups, los datos permanecen protegidos sin la clave correspondiente.
