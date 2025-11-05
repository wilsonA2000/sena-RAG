# 🚀 Cómo Obtener tu API Key GRATUITA de Groq

## ✅ Ventajas de Groq

- **100% GRATIS** - Sin tarjeta de crédito
- **Muy rápido** - Respuestas en 1-2 segundos
- **Límites generosos** - Suficiente para demos y uso moderado
- **Fácil de usar** - Setup en 3 minutos

---

## 📝 Paso a Paso (5 minutos)

### 1. Crear Cuenta

1. Ve a: **https://console.groq.com/**
2. Click en "Sign Up" o "Get Started"
3. Regístrate con tu email (Gmail funciona perfecto)
4. Verifica tu email

### 2. Obtener API Key

1. Una vez dentro, busca la sección **"API Keys"** en el menú
2. Click en **"Create API Key"**
3. Dale un nombre como: `asistente-sena-demo`
4. Click en **"Create"**
5. **COPIA la API key** (se ve así: `gsk_...`)
   - ⚠️ IMPORTANTE: Solo la verás una vez, guárdala bien

### 3. Configurar en tu Aplicación

1. Abre el archivo `.env` en tu proyecto
2. Reemplaza `tu_api_key_aqui` con tu API key:
   ```
   GROQ_API_KEY=gsk_tu_key_aqui_pegala
   ```
3. Guarda el archivo

### 4. Ejecutar

```bash
cd "/mnt/c/Users/wilso/Desktop/APLICACION DEMO SENA/asistente-normativo-sena"
streamlit run app.py
```

---

## 🎯 Límites del Plan Gratuito

- **Llama 3.1 70B**: 30 requests/min, 6,000 tokens/min
- **Llama 3.1 8B**: 30 requests/min, 20,000 tokens/min

**Traducción:** Puedes hacer más de 1,000+ consultas al día sin problema.

---

## ❓ Problemas Comunes

### Error: "Invalid API Key"
- Verifica que copiaste la key completa (empieza con `gsk_`)
- No debe tener espacios al inicio o final

### Error: "Rate limit exceeded"
- Espera 1 minuto y vuelve a intentar
- En plan gratuito hay límites por minuto

### La app no carga
- Verifica que instalaste groq: `pip3 list | grep groq`
- Si no está: `pip3 install groq==0.4.1`

---

## 💡 Tips para tu Demo

1. **Antes de presentar:** Haz 2-3 consultas de prueba para calentar
2. **Consultas recomendadas:**
   - "¿Cómo registro cartera morosa en SIREC?"
   - "Explícame el proceso de certificados"
   - "¿Qué es Sofia Plus y cómo se usa?"

3. **Durante la demo:** Menciona que:
   - Es IA de código abierto (Llama de Meta)
   - Completamente gratuito
   - Puede escalar a producción fácilmente

---

**¡Listo para impresionar a tus directivos! 🎓**
