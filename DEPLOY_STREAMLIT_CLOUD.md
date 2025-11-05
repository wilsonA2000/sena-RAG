# 🚀 Desplegar en Streamlit Community Cloud (GRATIS)

## ¿Por qué Streamlit Cloud?

- ✅ **100% GRATIS** - Para apps públicas
- ✅ **Oficial de Streamlit** - Optimizado para tu app
- ✅ **Fácil** - Deploy en 5 minutos
- ✅ **URL compartible** - Acceso desde cualquier lugar
- ✅ **Actualizaciones automáticas** - Al hacer push a GitHub

---

## 📋 Paso a Paso (15 minutos total)

### PASO 1: Crear Cuenta en GitHub (5 min)

1. Ve a: **https://github.com/**
2. Click en **"Sign up"**
3. Crea cuenta con tu email
4. Verifica tu email

### PASO 2: Subir tu Proyecto a GitHub (10 min)

#### Opción A: Usando la Interfaz Web (MÁS FÁCIL)

1. En GitHub, click en **"New repository"** (botón verde)
2. Configuración:
   - **Repository name:** `asistente-normativo-sena`
   - **Description:** "Chatbot IA para consultas SENA"
   - **Public** (debe ser público para plan gratis)
   - ✅ NO marques "Add README"
3. Click **"Create repository"**

4. En la nueva página, click en **"uploading an existing file"**

5. Arrastra estos archivos desde tu carpeta:
   - `app.py`
   - `requirements.txt`
   - `.env.example` (NO subas `.env` con tu API key!)
   - `README.md`
   - `LEEME_PRIMERO.md`

6. Scroll abajo, escribe: "Initial commit"
7. Click **"Commit changes"**

#### Opción B: Usando Git (Terminal)

```bash
cd "/mnt/c/Users/wilso/Desktop/APLICACION DEMO SENA/asistente-normativo-sena"

# Inicializar repositorio
git init

# Crear .gitignore para NO subir secretos
echo ".env" > .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# Agregar archivos
git add .
git commit -m "Initial commit - Asistente Virtual SENA"

# Conectar con GitHub (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/asistente-normativo-sena.git
git branch -M main
git push -u origin main
```

### PASO 3: Crear Cuenta en Streamlit Cloud (2 min)

1. Ve a: **https://streamlit.io/cloud**
2. Click en **"Sign up"** o **"Get started"**
3. **Inicia sesión con GitHub** (botón azul)
4. Autoriza Streamlit a acceder a tus repos

### PASO 4: Desplegar tu App (3 min)

1. En Streamlit Cloud, click **"New app"**

2. Configuración:
   - **Repository:** `asistente-normativo-sena`
   - **Branch:** `main`
   - **Main file path:** `app.py`

3. Click en **"Advanced settings"**

4. En **"Secrets"**, pega esto (reemplaza con tu API key):
   ```toml
   GROQ_API_KEY = "gsk_tu_api_key_aqui"
   ```

5. Click **"Deploy!"**

6. **Espera 2-3 minutos** mientras se despliega

7. ¡LISTO! Tu app estará en:
   ```
   https://TU_USUARIO-asistente-normativo-sena.streamlit.app
   ```

---

## 🔐 IMPORTANTE: Seguridad

### ⚠️ NUNCA subas estos archivos a GitHub:
- ❌ `.env` (contiene tu API key)
- ❌ Archivos con contraseñas

### ✅ Archivo .gitignore (ya creado si usaste Opción B):
```
.env
venv/
__pycache__/
*.pyc
```

---

## 🎯 Después del Deploy

### Tu URL será algo como:
```
https://wilson-asistente-normativo-sena.streamlit.app
```

### Puedes:
- ✅ Compartirla con tus directivos
- ✅ Usarla en tu presentación del diplomado
- ✅ Acceder desde cualquier dispositivo
- ✅ Actualizar el código y se despliega automáticamente

---

## 🐛 Problemas Comunes

### Error: "No module named 'groq'"
- **Solución:** Verifica que `requirements.txt` tenga:
  ```
  streamlit==1.29.0
  groq==0.4.1
  python-dotenv==1.0.0
  ```

### Error: "GROQ_API_KEY not found"
- **Solución:** Agrega tu API key en **Settings → Secrets** en Streamlit Cloud

### La app se queda en "Running..."
- **Solución:** Revisa los logs en Streamlit Cloud
- Puede ser error de sintaxis en el código

---

## 🔄 Actualizar tu App

Cuando hagas cambios:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

Streamlit Cloud detectará el cambio y actualizará automáticamente (30-60 segundos).

---

## 💡 Tips para la Presentación

1. **Abre la URL antes** de presentar (para que esté "caliente")
2. **Ten 2-3 consultas preparadas** para demostrar
3. **Menciona que está en la nube** - accesible 24/7
4. **Destaca el costo:** $0 para la demo
5. **Muestra el código en GitHub** - transparencia y profesionalismo

---

## 📞 ¿Necesitas Ayuda?

Si tienes problemas:
1. Revisa los logs en Streamlit Cloud
2. Verifica que todos los archivos estén en GitHub
3. Confirma que la API key esté en Secrets
4. Asegúrate que el repo sea público

---

**¡Tu aplicación estará en línea y lista para impresionar! 🎓**
