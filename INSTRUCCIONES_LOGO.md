# Instrucciones para Agregar el Logo del SENA

## Estado Actual

La aplicación está **completamente funcional sin logo**. El código incluye soporte automático para mostrar el logo si está disponible.

---

## Opción 1: Con Logo Oficial (Recomendado)

### Paso 1: Obtener el Logo
- Descarga el logo oficial del SENA desde la intranet institucional
- Solicítalo al área de comunicaciones de tu regional
- Usa el logo en formato PNG con fondo transparente

### Paso 2: Preparar la Imagen
Especificaciones recomendadas:
```
Formato:      PNG
Fondo:        Transparente
Tamaño:       200x200px (mínimo 150x150px)
Peso:         < 100KB (optimizado)
Nombre:       logo_sena.png
```

### Paso 3: Ubicar el Archivo
```
asistente-normativo-sena/
└── assets/
    └── logos/
        └── logo_sena.png  ← Coloca aquí
```

### Paso 4: Verificar
- Reinicia la aplicación: `streamlit run app.py`
- El logo aparecerá automáticamente en el header
- Tendrá animación flotante (sube y baja suavemente)

---

## Opción 2: Sin Logo (Actual)

### Estado Actual:
- La aplicación funciona perfectamente sin logo
- Muestra el título institucional completo
- No requiere ningún cambio
- Listo para usar inmediatamente

### Ventajas:
- Más rápido para demos iniciales
- No depende de archivos externos
- Funciona en cualquier entorno
- Deploy más simple en Streamlit Cloud

---

## Opción 3: Crear Logo Temporal (Para Demos)

Si necesitas un logo temporal para la demo y no tienes el oficial:

### Herramientas Online Gratuitas:

#### 1. Canva (Recomendado)
```
URL: https://www.canva.com
- Crea diseño personalizado 200x200px
- Usa colores SENA: #39A900 (verde)
- Agrega texto "SENA" con fuente moderna
- Descarga como PNG transparente
```

#### 2. Remove.bg + Editor
```
1. Busca imagen del logo SENA en Google
2. Usa remove.bg para quitar fondo
3. Redimensiona a 200x200px
4. Guarda como PNG
```

#### 3. GIMP (Software Libre)
```
1. Abre GIMP
2. Nuevo archivo 200x200px
3. Diseña logo simple con colores SENA
4. Exporta como PNG con transparencia
```

---

## Especificaciones Técnicas del Logo

### Para Diseñadores:

```css
Dimensiones visuales en la app:
- Desktop: 80px de altura
- Móvil: 60px de altura
- Proporción: Mantener aspecto original

Efectos aplicados automáticamente:
- Animación flotante: 3s infinite
- Sombra: drop-shadow(0 4px 8px rgba(0,0,0,0.2))
- Margen: 1.5rem entre logo y título
- Display: flex center

Colores institucionales para referencia:
- Verde primario: #39A900
- Verde oscuro: #2d8500
- Naranja acento: #FF6600
- Blanco: #FFFFFF
```

---

## Cómo Funciona el Código

### Detección Automática:
```python
# El código verifica si existe el archivo
logo_path = "assets/logos/logo_sena.png"
logo_exists = os.path.exists(logo_path)

# Si existe: Muestra logo + título
if show_logo and logo_exists:
    # Convierte imagen a base64
    # Incrusta en HTML
    # Aplica animaciones CSS

# Si NO existe: Muestra solo título
else:
    # Header sin logo
    # Funciona perfectamente igual
```

---

## Troubleshooting

### El logo no aparece:

**Verificar:**
1. Ruta correcta: `assets/logos/logo_sena.png`
2. Nombre exacto: `logo_sena.png` (minúsculas)
3. Formato: PNG (no JPG, no SVG)
4. Permisos de lectura del archivo
5. Reiniciar la aplicación

**Logs de debug:**
```python
# Agregar temporalmente en render_header():
print(f"Logo path: {logo_path}")
print(f"Logo exists: {logo_exists}")
```

---

## Alternativas Avanzadas

### Usar Logo SVG (Requiere modificación):
```python
# Cambiar en render_header():
# De PNG a SVG
logo_path = "assets/logos/logo_sena.svg"

# Leer SVG como texto
with open(logo_path, 'r') as f:
    svg_content = f.read()

# Incrustar directamente
st.markdown(svg_content, unsafe_allow_html=True)
```

### Usar URL Externa:
```python
# Si el logo está en servidor SENA:
logo_url = "https://sena.edu.co/logo-oficial.png"

# En HTML:
<img src="{logo_url}" alt="Logo SENA">
```

---

## Recomendaciones Oficiales

### Para Deploy en Streamlit Cloud:

**Con logo:**
```
1. Asegúrate que assets/logos/ esté en Git
2. No incluir logos muy pesados (máx 100KB)
3. Usar PNG optimizado
4. Verificar en .gitignore que assets/ NO esté excluido
```

**Sin logo:**
```
1. Funciona perfectamente sin cambios
2. Más rápido de cargar
3. Menos dependencias
4. Listo para deploy inmediato
```

---

## FAQ

### ¿Es obligatorio tener logo?
**No.** La aplicación funciona perfectamente sin él.

### ¿Puedo usar el logo oficial del SENA?
**Sí**, si tienes autorización institucional. Es un demo interno.

### ¿Qué pasa si el logo es muy grande?
Se redimensiona automáticamente a 80px (desktop) o 60px (móvil).

### ¿Puedo cambiar la animación del logo?
**Sí**, editando el CSS de `.logo-container img`:
```css
/* Quitar animación: */
animation: none;

/* Cambiar velocidad: */
animation: logoFloat 5s ease-in-out infinite;
```

### ¿Funciona con logo rectangular?
**Sí**, se mantiene la proporción automáticamente.

---

## Checklist de Deploy

### Antes de Presentar:

**Con logo:**
- [ ] Logo colocado en `assets/logos/logo_sena.png`
- [ ] Tamaño optimizado (< 100KB)
- [ ] PNG con fondo transparente
- [ ] Probado en localhost
- [ ] Probado en Streamlit Cloud (si aplica)
- [ ] Logo visible y con animación

**Sin logo:**
- [ ] Header muestra título correctamente
- [ ] Sin errores en consola
- [ ] Listo para demo

---

## Contacto para Logo Oficial

### Áreas a Consultar:
```
1. Comunicaciones Regional
   - Logos oficiales
   - Manual de marca
   - Colores institucionales

2. TIC/Sistemas
   - Repositorio de assets
   - Servidor de imágenes
   - URLs institucionales

3. Subdirección
   - Autorización de uso
   - Validación institucional
```

---

## Ejemplo Visual

### Con Logo:
```
┌─────────────────────────────┐
│   [LOGO FLOTANTE] 🎓         │
│   SENA - Asistente Virtual  │
│   Sistema de Consulta...     │
└─────────────────────────────┘
```

### Sin Logo (Actual):
```
┌─────────────────────────────┐
│   🎓 SENA - Asistente       │
│   Sistema de Consulta...     │
└─────────────────────────────┘
```

Ambas opciones se ven profesionales.

---

## Comandos Útiles

### Optimizar PNG:
```bash
# Con ImageMagick
convert logo_original.png -resize 200x200 -quality 85 logo_sena.png

# Con OptiPNG
optipng -o7 logo_sena.png
```

### Verificar Dimensiones:
```bash
file logo_sena.png
identify logo_sena.png
```

---

## Resumen

1. **Sin logo:** Funciona perfectamente (estado actual)
2. **Con logo:** Agrega archivo PNG en `assets/logos/`
3. **Automático:** El código detecta y aplica
4. **Animado:** Flotación suave incluida
5. **Responsive:** Se adapta a móvil/desktop

---

**Recomendación:** Comienza sin logo para demos rápidos, agrega logo oficial después para presentaciones formales.

La aplicación está lista para usar en ambos casos.
