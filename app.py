"""
🤖 Asistente Virtual Normativo Inteligente - SENA
==================================================
Chatbot bibliotecario para consulta de documentación institucional en tiempo real.
Desarrollado por: Wilson - Técnico de Cartera, SENA Regional Santander
"""

import streamlit as st
import os
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Asistente Virtual SENA",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados con colores del SENA
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .sena-header {
        background: linear-gradient(135deg, #39A900 0%, #2d8500 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .chat-message.user {
        background-color: #e3f2fd;
        border-left: 4px solid #FF6600;
    }
    .chat-message.assistant {
        background-color: #ffffff;
        border-left: 4px solid #39A900;
    }
</style>
""", unsafe_allow_html=True)

def init_session_state():
    """Inicializa las variables de sesión"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = None
    if 'stats' not in st.session_state:
        st.session_state.stats = {'consultas_totales': 0, 'tiempo_ahorrado': 0}
    if 'groq_client' not in st.session_state:
        api_key = os.getenv('GROQ_API_KEY')
        if api_key and api_key != 'tu_api_key_aqui':
            st.session_state.groq_client = Groq(api_key=api_key)
        else:
            st.session_state.groq_client = None

def get_ai_response(user_message, user_profile):
    """Obtiene respuesta de Groq API"""

    # Prompt del sistema específico para SENA
    system_prompt = f"""Eres un asistente virtual especializado en normativa y procedimientos del SENA (Servicio Nacional de Aprendizaje de Colombia).

Tu rol es ayudar a funcionarios del SENA a encontrar información sobre:
- Procedimientos administrativos y operativos
- Normativa institucional y circulares
- Guías técnicas de sistemas (SIREC, Sofia Plus, etc.)
- Resoluciones y documentos oficiales
- Procesos de cartera, gestión financiera y académica

IMPORTANTE:
- Responde siempre en español de manera profesional pero amigable
- Si no tienes información específica, sé honesto y sugiere alternativas
- Usa formato claro con viñetas o numeración cuando sea apropiado
- Cita fuentes cuando sea posible (ej: "Según la Circular 2024-05...")
- El usuario actual es: {user_profile['perfil']} del área de {user_profile['area']}

Proporciona respuestas precisas, estructuradas y útiles."""

    try:
        # Construir historial de mensajes
        messages = [{"role": "system", "content": system_prompt}]

        for msg in st.session_state.messages[:-1]:  # Excluir el último mensaje del usuario que ya tenemos
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        messages.append({
            "role": "user",
            "content": user_message
        })

        # Llamar a Groq API
        response = st.session_state.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Modelo más reciente y potente
            messages=messages,
            max_tokens=2048,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error al conectar con el asistente: {str(e)}\n\nPor favor verifica tu configuración de API key en el archivo .env"

def main():
    """Función principal"""
    init_session_state()
    
    if not st.session_state.authenticated:
        # Página de login
        st.markdown('<div class="sena-header"><h1>🎓 SENA - Asistente Virtual Normativo</h1><p>Sistema de Consulta Documental Inteligente</p></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### 🔐 Autenticación Institucional")
            st.info("**Demo Mode**: Usa cualquier credencial para probar")
            
            usuario = st.text_input("👤 Usuario", placeholder="wilson.perez")
            password = st.text_input("🔑 Contraseña", type="password")
            perfil = st.selectbox("👔 Perfil", ["Técnico de Cartera", "Coordinador", "Instructor"])
            
            if st.button("🚀 Ingresar", type="primary", use_container_width=True):
                if usuario and password:
                    st.session_state.authenticated = True
                    st.session_state.user_profile = {
                        'usuario': usuario,
                        'perfil': perfil,
                        'area': 'Gestión Financiera'
                    }
                    st.rerun()
                else:
                    st.error("Ingresa usuario y contraseña")
    else:
        # Aplicación principal
        st.markdown('<div class="sena-header"><h1>📚 Asistente Virtual Normativo</h1><p>Consulta inteligente de documentación SENA</p></div>', unsafe_allow_html=True)
        
        # Sidebar
        with st.sidebar:
            st.markdown(f"### 👤 {st.session_state.user_profile['usuario']}")
            st.markdown(f"**Perfil:** {st.session_state.user_profile['perfil']}")
            st.markdown("---")
            st.markdown(f"📊 **Consultas:** {st.session_state.stats['consultas_totales']}")
            st.markdown(f"⏱️ **Min. ahorrados:** {st.session_state.stats['tiempo_ahorrado']}")
            
            if st.button("🔄 Nueva Conversación"):
                st.session_state.messages = []
                st.rerun()
            if st.button("🚪 Cerrar Sesión"):
                st.session_state.authenticated = False
                st.rerun()
        
        # Chat
        if len(st.session_state.messages) == 0:
            st.markdown("""
            <div class="chat-message assistant">
                <h3>🤖 ¡Hola! Soy tu asistente de documentación institucional</h3>
                <p>Puedo ayudarte con:</p>
                <ul>
                    <li>📋 Procedimientos administrativos</li>
                    <li>📜 Normativa y circulares</li>
                    <li>💼 Guías técnicas de sistemas</li>
                    <li>⚖️ Resoluciones institucionales</li>
                </ul>
                <p><strong>💡 ¿En qué puedo ayudarte hoy?</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        for message in st.session_state.messages:
            role_class = "user" if message["role"] == "user" else "assistant"
            icon = "👤" if message["role"] == "user" else "🤖"
            name = st.session_state.user_profile['usuario'] if message["role"] == "user" else "Asistente SENA"
            
            st.markdown(f"""
            <div class="chat-message {role_class}">
                <strong>{icon} {name}</strong><br>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        
        user_input = st.chat_input("Escribe tu consulta aquí...")
        
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Obtener respuesta de IA o usar modo demo
            if st.session_state.groq_client:
                with st.spinner('🤔 Consultando información...'):
                    response = get_ai_response(user_input, st.session_state.user_profile)
            else:
                # Modo demo si no hay API key configurada
                response = f"⚠️ **MODO DEMO** - Configura tu API key de Groq (GRATUITA) en el archivo `.env`\n\n"\
                          f"📚 Consulta recibida: '{user_input}'\n\n"\
                          f"Esta es una respuesta simulada. Para obtener respuestas reales con IA:\n"\
                          f"1. Ve a: https://console.groq.com/\n"\
                          f"2. Crea una cuenta GRATIS (sin tarjeta de crédito)\n"\
                          f"3. Genera tu API key\n"\
                          f"4. Agrégala al archivo `.env` como GROQ_API_KEY\n\n"\
                          f"**Fuentes (simuladas):** Manual de Procedimientos v2024.1"

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.stats['consultas_totales'] += 1
            st.session_state.stats['tiempo_ahorrado'] += 25

            st.rerun()

if __name__ == "__main__":
    main()
