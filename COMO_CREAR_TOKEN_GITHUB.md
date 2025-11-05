# 🔑 GUÍA VISUAL: Crear Token de GitHub

## ✨ MÉTODO RÁPIDO - USA ESTE LINK

**Copia y pega esto en tu navegador:**
```
https://github.com/settings/tokens/new
```

Luego salta al PASO 3 abajo ⬇️

---

## 📸 MÉTODO PASO A PASO CON CAPTURAS

### PASO 1: Ve a tu perfil de GitHub

1. Abre tu navegador
2. Ve a: **https://github.com**
3. Inicia sesión si no lo has hecho
4. En la **esquina superior derecha**, verás tu **foto de perfil** (un círculo)
5. **Click en tu foto**

### PASO 2: Ir a Settings (Configuración)

Después de hacer click en tu foto, se abre un menú. Busca:

```
┌─────────────────────────────┐
│  Signed in as wilsonA2000   │
├─────────────────────────────┤
│  Your profile               │
│  Your repositories          │
│  Your projects              │
│  Your stars                 │
├─────────────────────────────┤
│  ⚙️  Settings  ← CLICK AQUÍ │
├─────────────────────────────┤
│  Sign out                   │
└─────────────────────────────┘
```

**Click en "Settings"** (tiene un ícono de engranaje ⚙️)

### PASO 3: Buscar Developer Settings

En la página de Settings, verás un **menú lateral IZQUIERDO** largo.

**Haz SCROLL HASTA ABAJO** del menú izquierdo hasta encontrar:

```
Settings (Menú lateral izquierdo)
┌────────────────────────────┐
│  Profile                   │
│  Account                   │
│  Appearance                │
│  ...                       │
│  (scroll más abajo)        │
│  ...                       │
│  Repositories              │
│  Packages                  │
│  Copilot                   │
│  ...                       │
│  (casi al final)           │
│  ...                       │
│  🔧 Developer settings     │ ← AQUÍ! (Es la ÚLTIMA opción)
└────────────────────────────┘
```

**Click en "Developer settings"** (🔧 Developer settings)

### PASO 4: Personal Access Tokens

Ahora verás un nuevo menú lateral. Busca:

```
Developer settings (Menú lateral)
┌────────────────────────────────────┐
│  GitHub Apps                       │
│  OAuth Apps                        │
│  Personal access tokens ▼          │ ← CLICK en la flechita
│    ├─ Fine-grained tokens          │
│    └─ Tokens (classic)             │ ← CLICK AQUÍ
└────────────────────────────────────┘
```

**Click en "Tokens (classic)"**

### PASO 5: Generate New Token

Ahora verás una página que dice "Personal access tokens (classic)"

En la parte superior derecha hay un botón:

```
┌──────────────────────────────┐
│  Generate new token ▼        │ ← CLICK en la flechita
├──────────────────────────────┤
│  Generate new token (classic)│ ← CLICK AQUÍ
│  Fine-grained token          │
└──────────────────────────────┘
```

**Click en "Generate new token (classic)"**

### PASO 6: Llenar el Formulario

Te pedirá tu **contraseña de GitHub** → Ingrésala

Luego verás un formulario. Llénalo así:

```
┌─────────────────────────────────────────────┐
│  New personal access token (classic)        │
├─────────────────────────────────────────────┤
│                                             │
│  Note (nombre del token)                    │
│  ┌────────────────────────────────────┐    │
│  │ sena-rag-token                     │    │ ← Escribe esto
│  └────────────────────────────────────┘    │
│                                             │
│  Expiration (cuánto dura)                   │
│  ┌────────────────────────────────────┐    │
│  │ 90 days                       ▼    │    │ ← Selecciona 90 days
│  └────────────────────────────────────┘    │
│                                             │
│  Select scopes (permisos)                   │
│  ☑️ repo (Full control of private repos)   │ ← MARCA ESTA
│      ☑️ repo:status                         │   (se marcan solas)
│      ☑️ repo_deployment                     │
│      ☑️ public_repo                         │
│      ☑️ repo:invite                         │
│      ☑️ security_events                     │
│                                             │
│  ☐ workflow                                 │ ← NO marques estas
│  ☐ write:packages                           │
│  ☐ delete:packages                          │
│  ☐ admin:org                                │
│  ...                                        │
│                                             │
│  (scroll abajo hasta el final)              │
│                                             │
│  ┌──────────────────────────┐              │
│  │ Generate token           │              │ ← CLICK AQUÍ
│  └──────────────────────────┘              │
└─────────────────────────────────────────────┘
```

**Click en el botón verde "Generate token"**

### PASO 7: COPIAR EL TOKEN

Verás una pantalla con un **recuadro verde** que dice:

```
┌─────────────────────────────────────────────────┐
│  ✅ Make sure to copy your personal access      │
│     token now. You won't be able to see it      │
│     again!                                      │
├─────────────────────────────────────────────────┤
│  ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  📋   │ ← ESTE ES TU TOKEN
└─────────────────────────────────────────────────┘
```

**IMPORTANTE:**
1. **Click en el ícono 📋** (copiar) al lado derecho del token
2. El token se copiará automáticamente
3. **PÉGALO en un Notepad** o archivo de texto temporal
4. ⚠️ **Solo lo verás UNA VEZ** - si cierras la página se pierde

---

## ✅ Ya tienes el Token - Siguiente Paso

El token se ve así:
```
ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8
```

**Pégamelo aquí** (en el chat) y yo haré el push automáticamente a tu repositorio.

---

## ❓ Si Aún No Funciona

**Alternativa - Usa SSH en lugar de Token:**

Dime y te explico cómo configurar SSH (es un poco más largo pero más seguro).

O también puedes:
1. Subir los archivos manualmente a GitHub (arrastra y suelta en la web)
2. Luego conectar Streamlit Cloud directo al repo

---

**¿En qué paso estás atorado exactamente?**
- ¿No encuentras "Settings"?
- ¿No ves "Developer settings"?
- ¿Otra cosa?

Dime y te ayudo específicamente.
