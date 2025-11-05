"""
Asistente Virtual Normativo Inteligente - SENA
==================================================
Chatbot bibliotecario para consulta de documentación institucional en tiempo real.

Desarrollado por: Wilson Andrés Arguello
Técnico de Cartera - SENA Regional Santander
Abogado 437.480 del C.S. de la Judicatura
"""

import streamlit as st
import os
import time
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Asistente Virtual SENA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS - Diseño Institucional Profesional
st.markdown("""
<style>
    /* ========== CONFIGURACIÓN GLOBAL - ESTILO CORPORATIVO ========== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    }

    .main {
        background-color: #F5F7FA;
        padding: 2rem 1rem;
    }

    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ========== HEADER INSTITUCIONAL ========== */
    .sena-header {
        background: #FFFFFF;
        border-bottom: 3px solid #39A900;
        padding: 2rem 3rem;
        margin-bottom: 3rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }

    .logo-container {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        margin-bottom: 0.75rem;
    }

    .logo-container img {
        height: 60px;
    }

    .sena-header h1 {
        margin: 0;
        font-size: 1.875rem;
        font-weight: 600;
        color: #1F2937;
        letter-spacing: -0.025em;
    }

    .sena-header p {
        margin: 0.5rem 0 0 0;
        font-size: 0.9375rem;
        color: #6B7280;
        font-weight: 400;
    }

    /* ========== CONTENEDOR DE LOGIN ========== */
    .login-container {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 3rem 2.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        max-width: 480px;
        margin: 0 auto;
    }

    .login-header {
        border-bottom: 1px solid #E5E7EB;
        padding-bottom: 1.5rem;
        margin-bottom: 2rem;
    }

    .login-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 0.5rem;
    }

    .login-subtitle {
        color: #6B7280;
        font-size: 0.875rem;
        font-weight: 400;
    }

    .demo-badge {
        display: inline-block;
        padding: 0.375rem 0.75rem;
        background-color: #FEF3C7;
        border: 1px solid #FDE68A;
        color: #92400E;
        font-size: 0.8125rem;
        font-weight: 500;
        border-radius: 4px;
        margin-bottom: 1.5rem;
    }

    /* ========== INPUTS PROFESIONALES ========== */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 1px solid #D1D5DB;
        border-radius: 6px;
        padding: 0.625rem 0.875rem;
        font-size: 0.9375rem;
        transition: all 0.15s ease;
        background: #FFFFFF;
        color: #1F2937;
    }

    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #39A900;
        box-shadow: 0 0 0 3px rgba(57, 169, 0, 0.08);
        outline: none;
    }

    .stTextInput label,
    .stSelectbox label {
        font-size: 0.875rem;
        font-weight: 500;
        color: #374151;
        margin-bottom: 0.5rem;
    }

    /* ========== BOTONES CORPORATIVOS ========== */
    .stButton > button {
        border-radius: 6px;
        padding: 0.625rem 1.25rem;
        font-weight: 500;
        font-size: 0.9375rem;
        border: none;
        transition: all 0.15s ease;
        background-color: #39A900;
        color: white;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    .stButton > button:hover {
        background-color: #2d8500;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }

    .stButton > button:active {
        background-color: #1f6600;
    }

    /* ========== MENSAJES DE CHAT ESTILO ENTERPRISE ========== */
    .chat-message {
        padding: 1.25rem;
        border-radius: 6px;
        margin-bottom: 1rem;
        border: 1px solid #E5E7EB;
        background: #FFFFFF;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }

    .chat-message.user {
        background: #F9FAFB;
        border-left: 3px solid #FF6600;
    }

    .chat-message.assistant {
        background: #FFFFFF;
        border-left: 3px solid #39A900;
    }

    .chat-message-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid #F3F4F6;
    }

    .chat-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 600;
        color: white;
        flex-shrink: 0;
    }

    .chat-avatar.user {
        background-color: #FF6600;
    }

    .chat-avatar.assistant {
        background-color: #39A900;
    }

    .chat-message-name {
        font-size: 0.875rem;
        font-weight: 600;
        color: #374151;
    }

    .chat-message-time {
        font-size: 0.75rem;
        color: #9CA3AF;
        margin-left: auto;
    }

    .chat-message-content {
        line-height: 1.6;
        color: #1F2937;
        font-size: 0.9375rem;
    }

    /* ========== MENSAJE DE BIENVENIDA ========== */
    .welcome-message {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }

    .welcome-message h3 {
        color: #1F2937;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .welcome-message p {
        color: #6B7280;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }

    .welcome-message ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .welcome-message li {
        padding: 0.75rem 0;
        color: #374151;
        font-size: 0.9375rem;
        border-bottom: 1px solid #F3F4F6;
    }

    .welcome-message li:last-child {
        border-bottom: none;
    }

    .welcome-message li strong {
        color: #1F2937;
        font-weight: 600;
    }

    .info-box {
        background: #EFF6FF;
        border: 1px solid #DBEAFE;
        border-radius: 6px;
        padding: 1rem;
        margin-top: 1.5rem;
    }

    .info-box-title {
        font-weight: 600;
        color: #1E40AF;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }

    .info-box-content {
        color: #1E3A8A;
        font-size: 0.875rem;
        line-height: 1.5;
    }

    /* ========== SIDEBAR PROFESIONAL ========== */
    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    section[data-testid="stSidebar"] > div {
        padding: 1.5rem 1rem;
    }

    .sidebar-section {
        background: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 6px;
        padding: 1.25rem;
        margin-bottom: 1.25rem;
    }

    .sidebar-section-title {
        font-size: 0.75rem;
        font-weight: 600;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem;
    }

    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1F2937;
        line-height: 1;
        margin-bottom: 0.25rem;
    }

    .stat-label {
        font-size: 0.8125rem;
        color: #6B7280;
        font-weight: 400;
    }

    .stat-divider {
        height: 1px;
        background: #E5E7EB;
        margin: 1rem 0;
    }

    /* ========== INPUT DE CHAT ========== */
    .stChatInput {
        border: 1px solid #D1D5DB;
        border-radius: 6px;
        transition: all 0.15s ease;
    }

    .stChatInput:focus-within {
        border-color: #39A900;
        box-shadow: 0 0 0 3px rgba(57, 169, 0, 0.08);
    }

    /* ========== ALERTS ========== */
    .stAlert {
        border-radius: 6px;
        border: 1px solid;
        padding: 1rem;
        font-size: 0.875rem;
    }

    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #F3F4F6;
    }

    ::-webkit-scrollbar-thumb {
        background: #D1D5DB;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #9CA3AF;
    }

    /* ========== UTILIDADES ========== */
    .text-muted {
        color: #6B7280;
        font-size: 0.875rem;
    }

    .divider {
        height: 1px;
        background: #E5E7EB;
        margin: 1.5rem 0;
    }

    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {
        .sena-header {
            padding: 1.5rem 1.5rem;
        }

        .sena-header h1 {
            font-size: 1.5rem;
        }

        .logo-container img {
            height: 48px;
        }

        .login-container {
            padding: 2rem 1.5rem;
        }

        .welcome-message {
            padding: 1.5rem;
        }
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
        # Intentar obtener API key de Streamlit secrets (Cloud) o .env (Local)
        api_key = None

        # Prioridad 1: Streamlit secrets (para Cloud)
        if hasattr(st, 'secrets') and "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
        # Prioridad 2: Variable de entorno (para local)
        elif os.getenv('GROQ_API_KEY'):
            api_key = os.getenv('GROQ_API_KEY')

        if api_key and api_key != 'tu_api_key_aqui':
            try:
                st.session_state.groq_client = Groq(api_key=api_key)
            except Exception as e:
                st.error(f"Error al inicializar Groq: {str(e)}")
                st.session_state.groq_client = None
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

        for msg in st.session_state.messages[:-1]:
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
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=2048,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error al conectar con el asistente: {str(e)}\n\nPor favor verifica tu configuración de API key."

def render_header(title, subtitle, show_logo=True):
    """Renderiza el header profesional con logo opcional"""
    import os

    # Usar ruta relativa para compatibilidad con Streamlit Cloud
    logo_path = os.path.join("assets", "logos", "logo_sena.png")
    logo_exists = os.path.exists(logo_path)

    if show_logo and logo_exists:
        # Header con logo
        st.markdown(f"""
        <div class="sena-header">
            <div class="logo-container">
                <img src="data:image/png;base64,{get_base64_image(logo_path)}" alt="Logo SENA">
                <div>
                    <h1>{title}</h1>
                    <p>{subtitle}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Header sin logo
        st.markdown(f"""
        <div class="sena-header">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)

def get_base64_image(image_path):
    """Convierte imagen a base64 para incrustarla en HTML"""
    import base64
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

def main():
    """Función principal"""
    init_session_state()

    if not st.session_state.authenticated:
        # Página de login profesional
        render_header("🎓 Asistente Virtual Normativo SENA", "Sistema de Consulta Documental Inteligente", show_logo=True)

        # Espaciado
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div class="login-container">
                <div class="login-header">
                    <div class="login-title">🔐 Autenticación Institucional</div>
                    <div class="login-subtitle">Ingresa con tus credenciales del SENA</div>
                </div>
                <div style="text-align: center;">
                    <div class="demo-badge">MODO DEMO - Usa cualquier credencial para probar</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

            usuario = st.text_input("👤 Usuario", placeholder="wilson.perez", key="login_user", label_visibility="visible")
            password = st.text_input("🔑 Contraseña", type="password", placeholder="••••••••", key="login_pass", label_visibility="visible")
            perfil = st.selectbox(
                "👔 Perfil",
                ["Técnico de Cartera", "Coordinador Académico", "Instructor", "Subdirector", "Administrativo"],
                key="login_profile",
                label_visibility="visible"
            )

            st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

            if st.button("🚀 Ingresar al Sistema", type="primary", use_container_width=True):
                if usuario and password:
                    with st.spinner('Autenticando...'):
                        time.sleep(0.8)

                    st.session_state.authenticated = True
                    st.session_state.user_profile = {
                        'usuario': usuario,
                        'perfil': perfil,
                        'area': 'Gestión Financiera' if perfil == "Técnico de Cartera" else 'Académica'
                    }
                    st.success("Autenticación exitosa")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Por favor ingresa usuario y contraseña")

            # Footer del login
            st.markdown("""
            <div style='text-align: center; margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid #E5E7EB;'>
                <p class='text-muted' style='margin: 0;'>
                    🔒 Conexión segura | 🛡️ Datos protegidos
                </p>
                <p class='text-muted' style='margin-top: 0.75rem; font-size: 0.75rem; line-height: 1.5;'>
                    SENA Regional Santander<br>
                    Desarrollado por Wilson Andrés Arguello<br>
                    Técnico de Cartera | Abogado 437.480 C.S. Judicatura
                </p>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Aplicación principal
        render_header("📚 Asistente Virtual Normativo", "Consulta inteligente de documentación SENA", show_logo=True)

        # Sidebar profesional
        with st.sidebar:
            # Perfil de usuario
            st.markdown(f"""
            <div class='sidebar-section'>
                <div style='display: flex; align-items: center; gap: 1rem;'>
                    <div class='chat-avatar user' style='width: 40px; height: 40px; font-size: 1rem;'>
                        {st.session_state.user_profile['usuario'][0].upper()}
                    </div>
                    <div style='flex: 1;'>
                        <div style='font-weight: 600; color: #1F2937; margin-bottom: 0.25rem;'>
                            {st.session_state.user_profile['usuario']}
                        </div>
                        <div style='font-size: 0.8125rem; color: #6B7280;'>
                            {st.session_state.user_profile['perfil']}
                        </div>
                    </div>
                </div>
                <div class='stat-divider'></div>
                <div style='font-size: 0.8125rem; color: #6B7280;'>
                    Área: {st.session_state.user_profile['area']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Estadísticas
            st.markdown("""<div class='sidebar-section-title'>📊 Estadísticas de Uso</div>""", unsafe_allow_html=True)

            st.markdown(f"""
            <div class='sidebar-section'>
                <div class='stat-value' style='color: #39A900;'>
                    {st.session_state.stats['consultas_totales']}
                </div>
                <div class='stat-label'>Consultas realizadas</div>
                <div class='stat-divider'></div>
                <div class='stat-value' style='color: #FF6600; font-size: 1.5rem;'>
                    {st.session_state.stats['tiempo_ahorrado']} min
                </div>
                <div class='stat-label'>Tiempo ahorrado</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

            # Botones de acción
            if st.button("🔄 Nueva Conversación", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

            if st.button("🚪 Cerrar Sesión", use_container_width=True):
                st.session_state.authenticated = False
                st.rerun()

            # Footer del sidebar
            st.markdown("""
            <div style='margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #E5E7EB; text-align: center;'>
                <p style='color: #9CA3AF; font-size: 0.75rem; margin: 0; line-height: 1.6;'>
                    Versión 1.0.0 | SENA 2025<br>
                    <span style='font-size: 0.7rem;'>Wilson Andrés Arguello<br>Abogado 437.480 C.S. Judicatura</span>
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Chat - Mensaje de bienvenida
        if len(st.session_state.messages) == 0:
            st.markdown("""
            <div class="welcome-message">
                <h3>🤖 Bienvenido al Asistente Virtual SENA</h3>
                <p>Soy tu asistente especializado en documentación institucional. Puedo ayudarte con:</p>
                <ul>
                    <li>📋 <strong>Procedimientos administrativos</strong> - Guías paso a paso</li>
                    <li>📜 <strong>Normativa y circulares</strong> - Documentos oficiales vigentes</li>
                    <li>💼 <strong>Guías técnicas de sistemas</strong> - SIREC, Sofia Plus y más</li>
                    <li>⚖️ <strong>Resoluciones institucionales</strong> - Normativas y políticas</li>
                </ul>
                <div class='info-box'>
                    <div class='info-box-title'>💡 Consejo profesional</div>
                    <div class='info-box-content'>
                        Sé específico en tu consulta para obtener resultados más precisos y relevantes
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Renderizar mensajes del chat
        for idx, message in enumerate(st.session_state.messages):
            role_class = "user" if message["role"] == "user" else "assistant"
            avatar_class = "user" if message["role"] == "user" else "assistant"

            if message["role"] == "user":
                name = st.session_state.user_profile['usuario']
                icon = "👤"
            else:
                name = "Asistente SENA"
                icon = "🤖"

            # Convertir saltos de línea a <br>
            content_html = message["content"].replace("\n", "<br>")

            # Timestamp simplificado
            time_str = "Ahora"

            st.markdown(f"""
            <div class="chat-message {role_class}">
                <div class="chat-message-header">
                    <div class="chat-avatar {avatar_class}">{icon}</div>
                    <div class="chat-message-name">{name}</div>
                    <div class="chat-message-time">{time_str}</div>
                </div>
                <div class="chat-message-content">
                    {content_html}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Input de chat
        user_input = st.chat_input(f"💬 Escribe tu consulta, {st.session_state.user_profile['usuario']}...")

        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Obtener respuesta de IA o usar modo demo
            if st.session_state.groq_client:
                with st.spinner('🔍 Consultando información...'):
                    response = get_ai_response(user_input, st.session_state.user_profile)
            else:
                # Modo demo
                response = f"""⚠️ MODO DEMOSTRACIÓN ACTIVO

📚 Tu consulta: {user_input}

---

Esta es una respuesta simulada. Para activar respuestas reales con IA:

**Pasos para configurar Groq API (GRATIS):**

1. 🌐 Visita: https://console.groq.com/
2. ✅ Crea una cuenta gratuita (sin tarjeta de crédito)
3. 🔑 Genera tu API key
4. 📝 Agrégala al archivo .env como GROQ_API_KEY
5. 🔄 Reinicia la aplicación

---

**Fuentes simuladas:**
- Manual de Procedimientos SENA v2024.1
- Circular 2024-003 Gestión Documental
- Resolución 0123 de 2024

💡 Una vez configurado, obtendrás respuestas reales con IA potenciada por Llama 3.3 70B."""

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.stats['consultas_totales'] += 1
            st.session_state.stats['tiempo_ahorrado'] += 25

            st.rerun()

if __name__ == "__main__":
    main()
