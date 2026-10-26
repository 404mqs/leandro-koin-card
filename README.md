# leandro-koin-card

Tarjeta de contacto digital para **Leandro Montedonico**, Sales Manager en Koin.

**URL pública:** https://404mqs.github.io/leandro-koin-card/
**Repo:** https://github.com/404mqs/leandro-koin-card

Réplica de [`leandro-card`](https://github.com/404mqs/leandro-card) (Torque and Taste) con la identidad de Koin.

---

## Qué es

Página estática de un archivo — `index.html` — deployada en GitHub Pages. Sin backend, dependencias npm ni build step. Para actualizar: editar el archivo y hacer push.

---

## Diseño

Identidad tomada de [koin.com.br](https://www.koin.com.br/) (colores, logo y tipografía extraídos del sitio):

- **Tipografía:** Plus Jakarta Sans (Google Fonts), la misma del sitio de Koin.
- **Verde Koin:** `#14DD3E` (la barra de la K del logo).
- **Paleta modo oscuro:** fondo `#0C1114`, card `#10181B`, texto `#F5F5F5`, acento `#14DD3E`.
- **Paleta modo claro:** fondo `#F4F5F4`, card `#FFFFFF`, texto `#10181B`, acento `#0C8525` (verde oscurecido para contraste sobre blanco).
- **Logo:** la K (favicon de Koin) arriba del nombre y el wordmark `koin` en el company tag. Ambos son SVG inline; el wordmark usa `currentColor` para pasar a blanco/negro según el tema.
- **Bordes redondeados** (card 20px, items 12px, CTA pill) en línea con el sitio de Koin.

### Modo claro / oscuro

Igual que la tarjeta original: detecta `prefers-color-scheme`, botón sol/luna, preferencia persistida en `localStorage` (key: `koin-theme`), script inline en `<head>` para evitar el flash.

---

## Agregar a Contactos

Mismo mecanismo que `leandro-card`:

| Plataforma | Mecanismo |
|---|---|
| **iOS Safari** | Navega a `data:text/vcard;charset=utf-8,...` → Contactos lo intercepta |
| **Android Chrome** | Navega a un Blob URL sin atributo `download` → el SO lo abre con Contactos |
| **Desktop** | Descarga `leandro-montedonico-koin.vcf` via `<a download>` |

`leandro.vcf` es una copia estática del mismo contacto (respaldo, no se usa en producción).

---

## Datos del contacto

```
Nombre:   Leandro Montedonico
Cargo:    Sales Manager
Empresa:  Koin
Tel:      +54 11 3008-4910
Email:    leandro.montedonico@koin.com.br
Web:      https://www.koin.com.br
```

---

## Archivos

```
leandro-koin-card/
├── index.html        # toda la app (HTML + CSS + JS inline)
├── favicon.svg       # K de Koin
├── leandro.vcf       # vCard estática de respaldo
├── qr.png            # QR verde sobre oscuro (versión de marca)
├── qr-light.png      # QR oscuro sobre blanco (máxima compatibilidad / impresión)
└── tools/make_qr.py  # genera ambos QR
```

---

## QR

Generado con `tools/make_qr.py` (`qrcode` + `Pillow`): módulos redondeados, corrección de errores H y la K de Koin al centro. Dos variantes:

- `qr.png` — verde `#14DD3E` sobre `#0C1114`. Es un QR invertido (claro sobre oscuro): lo leen la cámara de iPhone y Google Lens, pero algunos lectores viejos de Android no.
- `qr-light.png` — oscuro sobre blanco, lo lee cualquier lector. Usar este para imprimir.

Para regenerarlos:

```bash
pip install qrcode pillow
python tools/make_qr.py
```
