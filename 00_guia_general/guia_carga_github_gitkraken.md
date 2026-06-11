# Cómo cargar este paquete en GitHub con GitKraken

Repositorio objetivo:

`https://github.com/ESPOCH-Electricidad/power-systems-planning-operation`

## Opción recomendada: GitKraken

1. Abre GitKraken Desktop.
2. Selecciona **Clone a repo**.
3. Usa la URL del repositorio.
4. Elige una carpeta local, por ejemplo:

```text
D:\GitHub\power-systems-planning-operation
```

5. Copia todo el contenido de este paquete dentro de esa carpeta local.
6. En GitKraken aparecerán los archivos como cambios pendientes.
7. Revisa que no se hayan añadido archivos `.mod` ni `.run`.
8. Escribe un mensaje de commit, por ejemplo:

```text
Estructura inicial del repositorio docente por bloques
```

9. Haz **Stage all changes**.
10. Haz **Commit**.
11. Haz **Push** hacia `origin/main`.

## Configurar GitHub Pages

1. En GitHub, entra al repositorio.
2. Ve a **Settings**.
3. En el menú lateral, entra a **Pages**.
4. En **Build and deployment**, selecciona **Deploy from a branch**.
5. Selecciona rama `main` y carpeta `/docs`.
6. Guarda los cambios.
7. Espera a que GitHub genere el sitio.

## Verificación antes de publicar

Ejecuta este checklist:

- [ ] No hay `.mod`.
- [ ] No hay `.run`.
- [ ] No hay datos sensibles de estudiantes.
- [ ] Cada caso tiene `README.md`.
- [ ] Cada caso tiene `metadata.yaml`.
- [ ] El sitio en `/docs` tiene `index.md`.
- [ ] Los enlaces del README funcionan.
