"""
🤖 Asistente Virtual Normativo Inteligente - SENA
==================================================
Chatbot bibliotecario para consulta de documentación institucional en tiempo real.
Desarrollado por: Wilson - Técnico de Cartera, SENA Regional Santander
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
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados con colores del SENA - Diseño Ultra Moderno
st.markdown("""
<style>
    /* ========== CONFIGURACIÓN GLOBAL ========== */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    * {
        font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        animation: gradientShift 15s ease infinite;
    }

    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    /* Ocultar elementos de Streamlit por defecto */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ========== HEADER PRINCIPAL CON LOGO ========== */
    .sena-header {
        background: linear-gradient(135deg, #39A900 0%, #2d8500 50%, #1f6600 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 10px 40px rgba(57, 169, 0, 0.3),
                    0 0 0 1px rgba(255,255,255,0.1) inset;
        position: relative;
        overflow: hidden;
        animation: fadeInDown 0.8s ease-out;
    }

    .sena-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }

    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .sena-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
        letter-spacing: -0.5px;
    }

    .sena-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }

    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 1rem;
    }

    .logo-container img {
        height: 80px;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
        animation: logoFloat 3s ease-in-out infinite;
    }

    @keyframes logoFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* ========== LOGIN MODERNO ========== */
    .login-container {
        background: white;
        border-radius: 24px;
        padding: 3rem 2.5rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.08),
                    0 0 0 1px rgba(0,0,0,0.02);
        animation: fadeInUp 0.6s ease-out;
        position: relative;
        overflow: hidden;
    }

    .login-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, #39A900, #FF6600);
        border-radius: 24px 24px 0 0;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .login-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2d8500;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    .login-subtitle {
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 0.95rem;
    }

    /* Mejorar inputs de Streamlit */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 2px solid #e9ecef;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: white;
    }

    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #39A900;
        box-shadow: 0 0 0 3px rgba(57, 169, 0, 0.1);
    }

    /* Botones mejorados */
    .stButton > button {
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(57, 169, 0, 0.2);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(57, 169, 0, 0.3);
    }

    .stButton > button:active {
        transform: translateY(0px);
    }

    /* ========== MENSAJES DE CHAT MODERNOS ========== */
    .chat-message {
        padding: 1.5rem;
        border-radius: 18px;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        animation: messageSlideIn 0.4s ease-out;
        position: relative;
        backdrop-filter: blur(10px);
    }

    @keyframes messageSlideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .chat-message.user {
        background: linear-gradient(135deg, #fff5f0 0%, #ffe8dc 100%);
        border-left: 5px solid #FF6600;
        margin-left: 10%;
        border-radius: 18px 18px 4px 18px;
    }

    .chat-message.assistant {
        background: linear-gradient(135deg, #ffffff 0%, #f8fff5 100%);
        border-left: 5px solid #39A900;
        margin-right: 10%;
        border-radius: 18px 18px 18px 4px;
    }

    .chat-message strong {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        color: #495057;
    }

    .chat-message.user strong {
        color: #FF6600;
        justify-content: flex-end;
    }

    .chat-message.assistant strong {
        color: #39A900;
    }

    .chat-avatar {
        display: inline-flex;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .chat-avatar.user {
        background: linear-gradient(135deg, #FF6600, #ff8533);
    }

    .chat-avatar.assistant {
        background: linear-gradient(135deg, #39A900, #4dd419);
    }

    /* Mensaje de bienvenida especial */
    .welcome-message {
        background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
        border: 2px solid #e3f2fd;
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        animation: fadeInScale 0.6s ease-out;
    }

    @keyframes fadeInScale {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    .welcome-message h3 {
        color: #2d8500;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .welcome-message ul {
        list-style: none;
        padding: 0;
        margin: 1.5rem 0;
    }

    .welcome-message li {
        padding: 0.75rem 0;
        color: #495057;
        font-size: 1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        transition: transform 0.2s ease;
    }

    .welcome-message li:hover {
        transform: translateX(5px);
    }

    /* ========== SIDEBAR MEJORADO ========== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
        border-right: 1px solid rgba(0,0,0,0.05);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    .sidebar-stat {
        background: linear-gradient(135deg, #f8fff5 0%, #e8f5e3 100%);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #39A900;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    /* ========== INPUT DE CHAT MEJORADO ========== */
    .stChatInput {
        border-radius: 16px;
        border: 2px solid #e9ecef;
        transition: all 0.3s ease;
    }

    .stChatInput:focus-within {
        border-color: #39A900;
        box-shadow: 0 4px 16px rgba(57, 169, 0, 0.15);
    }

    /* ========== SPINNER PERSONALIZADO ========== */
    .stSpinner > div {
        border-top-color: #39A900 !important;
    }

    /* ========== INFO/WARNING/ERROR MEJORADOS ========== */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* ========== EFECTOS HOVER PROFESIONALES ========== */
    .hover-lift {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .hover-lift:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.1);
    }

    /* ========== RESPONSIVE DESIGN ========== */
    @media (max-width: 768px) {
        .sena-header h1 {
            font-size: 1.75rem;
        }

        .sena-header p {
            font-size: 0.95rem;
        }

        .logo-container img {
            height: 60px;
        }

        .chat-message.user {
            margin-left: 0;
        }

        .chat-message.assistant {
            margin-right: 0;
        }

        .login-container {
            padding: 2rem 1.5rem;
        }
    }

    /* ========== ANIMACIONES DE CARGA ========== */
    .loading-dots {
        display: inline-flex;
        gap: 0.25rem;
    }

    .loading-dots span {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #39A900;
        animation: loadingDots 1.4s infinite ease-in-out;
    }

    .loading-dots span:nth-child(1) {
        animation-delay: -0.32s;
    }

    .loading-dots span:nth-child(2) {
        animation-delay: -0.16s;
    }

    @keyframes loadingDots {
        0%, 80%, 100% {
            transform: scale(0);
            opacity: 0.5;
        }
        40% {
            transform: scale(1);
            opacity: 1;
        }
    }

    /* ========== BADGE/PILLS ========== */
    .badge {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        background: linear-gradient(135deg, #39A900, #4dd419);
        color: white;
        box-shadow: 0 2px 8px rgba(57, 169, 0, 0.2);
    }

    .badge-orange {
        background: linear-gradient(135deg, #FF6600, #ff8533);
    }

    /* ========== SCROLL SUAVE ========== */
    html {
        scroll-behavior: smooth;
    }

    /* ========== SCROLLBAR PERSONALIZADO ========== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #39A900, #2d8500);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #2d8500, #1f6600);
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

def render_header(title, subtitle, show_logo=True):
    """Renderiza el header moderno con logo opcional"""
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
            </div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Header sin logo (fallback)
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
        # Página de login moderna
        render_header("🎓 SENA - Asistente Virtual Normativo", "Sistema de Consulta Documental Inteligente", show_logo=True)

        # Espaciado
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2.5, 1])
        with col2:
            st.markdown("""
            <div class="login-container">
                <div class="login-title">🔐 Autenticación Institucional</div>
                <div class="login-subtitle">Ingresa con tus credenciales del SENA</div>
            </div>
            """, unsafe_allow_html=True)

            # Espaciado
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

            # Mostrar badge de demo
            st.markdown("""
            <div style='text-align: center; margin-bottom: 1.5rem;'>
                <span class="badge-orange badge">MODO DEMO - Usa cualquier credencial</span>
            </div>
            """, unsafe_allow_html=True)

            usuario = st.text_input("👤 Usuario", placeholder="wilson.perez", key="login_user")
            password = st.text_input("🔑 Contraseña", type="password", placeholder="••••••••", key="login_pass")
            perfil = st.selectbox(
                "👔 Perfil",
                ["Técnico de Cartera", "Coordinador Académico", "Instructor", "Subdirector", "Administrativo"],
                key="login_profile"
            )

            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

            if st.button("🚀 INGRESAR AL SISTEMA", type="primary", use_container_width=True):
                if usuario and password:
                    # Animación de carga
                    with st.spinner('Autenticando...'):
                        time.sleep(0.8)  # Simular autenticación

                    st.session_state.authenticated = True
                    st.session_state.user_profile = {
                        'usuario': usuario,
                        'perfil': perfil,
                        'area': 'Gestión Financiera' if perfil == "Técnico de Cartera" else 'Académica'
                    }
                    st.success("✅ Autenticación exitosa. Redirigiendo...")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("⚠️ Por favor ingresa usuario y contraseña")

            # Footer del login
            st.markdown("""
            <div style='text-align: center; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #e9ecef;'>
                <p style='color: #6c757d; font-size: 0.85rem; margin: 0;'>
                    🔒 Conexión segura | 🛡️ Datos protegidos
                </p>
                <p style='color: #adb5bd; font-size: 0.75rem; margin-top: 0.5rem;'>
                    Desarrollado para SENA Regional Santander
                </p>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Aplicación principal
        render_header("📚 Asistente Virtual Normativo", "Consulta inteligente de documentación SENA", show_logo=True)

        # Sidebar moderno
        with st.sidebar:
            # Perfil de usuario
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #f8fff5 0%, #e8f5e3 100%);
                        border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem;
                        border-left: 5px solid #39A900; box-shadow: 0 4px 12px rgba(0,0,0,0.05);'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem;'>
                    <div style='width: 50px; height: 50px; border-radius: 50%;
                                background: linear-gradient(135deg, #39A900, #4dd419);
                                display: flex; align-items: center; justify-content: center;
                                font-size: 1.5rem; box-shadow: 0 4px 12px rgba(57, 169, 0, 0.3);'>
                        👤
                    </div>
                    <div>
                        <div style='font-weight: 600; font-size: 1.1rem; color: #2d8500;'>
                            {st.session_state.user_profile['usuario']}
                        </div>
                        <div style='font-size: 0.85rem; color: #6c757d;'>
                            {st.session_state.user_profile['perfil']}
                        </div>
                    </div>
                </div>
                <div style='font-size: 0.8rem; color: #6c757d; padding-top: 0.75rem;
                            border-top: 1px solid rgba(0,0,0,0.05);'>
                    📍 {st.session_state.user_profile['area']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Estadísticas
            st.markdown("### 📊 Estadísticas")
            st.markdown(f"""
            <div class='sidebar-stat'>
                <div style='font-size: 2rem; font-weight: 700; color: #39A900;'>
                    {st.session_state.stats['consultas_totales']}
                </div>
                <div style='font-size: 0.85rem; color: #6c757d;'>
                    Consultas realizadas
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='sidebar-stat'>
                <div style='font-size: 2rem; font-weight: 700; color: #FF6600;'>
                    {st.session_state.stats['tiempo_ahorrado']}
                </div>
                <div style='font-size: 0.85rem; color: #6c757d;'>
                    Minutos ahorrados
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("---")

            # Botones de acción
            if st.button("🔄 Nueva Conversación", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

            if st.button("🚪 Cerrar Sesión", use_container_width=True):
                st.session_state.authenticated = False
                st.rerun()

            # Footer del sidebar
            st.markdown("""
            <div style='margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);
                        text-align: center;'>
                <p style='color: #adb5bd; font-size: 0.75rem; margin: 0;'>
                    v1.0.0 | SENA 2025
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Chat - Mensaje de bienvenida
        if len(st.session_state.messages) == 0:
            st.markdown("""
            <div class="welcome-message">
                <h3>🤖 ¡Bienvenido al Asistente Virtual SENA!</h3>
                <p style='color: #6c757d; font-size: 1rem; margin-bottom: 1rem;'>
                    Soy tu asistente especializado en documentación institucional. Puedo ayudarte con:
                </p>
                <ul>
                    <li>📋 <strong>Procedimientos administrativos</strong> - Guías paso a paso</li>
                    <li>📜 <strong>Normativa y circulares</strong> - Documentos oficiales vigentes</li>
                    <li>💼 <strong>Guías técnicas de sistemas</strong> - SIREC, Sofia Plus y más</li>
                    <li>⚖️ <strong>Resoluciones institucionales</strong> - Normativas y políticas</li>
                </ul>
                <div style='background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
                            border-radius: 12px; padding: 1rem; margin-top: 1.5rem;
                            border-left: 4px solid #0ea5e9;'>
                    <strong style='color: #0369a1;'>💡 Consejo:</strong>
                    <span style='color: #6c757d;'>
                        Sé específico en tu consulta para obtener mejores resultados
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Renderizar mensajes del chat
        for message in st.session_state.messages:
            role_class = "user" if message["role"] == "user" else "assistant"
            icon = "👤" if message["role"] == "user" else "🤖"
            avatar_class = "user" if message["role"] == "user" else "assistant"
            name = st.session_state.user_profile['usuario'] if message["role"] == "user" else "Asistente SENA"

            # Convertir saltos de línea a <br> para mejor renderizado
            content_html = message["content"].replace("\n", "<br>")

            st.markdown(f"""
            <div class="chat-message {role_class}">
                <strong>
                    <span class="chat-avatar {avatar_class}">{icon}</span>
                    {name}
                </strong>
                <div style='line-height: 1.6; color: #212529;'>
                    {content_html}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Input de chat con placeholder personalizado
        user_input = st.chat_input(f"💬 Escribe tu consulta aquí, {st.session_state.user_profile['usuario']}...")

        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Obtener respuesta de IA o usar modo demo
            if st.session_state.groq_client:
                with st.spinner('🔍 Consultando información...'):
                    response = get_ai_response(user_input, st.session_state.user_profile)
            else:
                # Modo demo si no hay API key configurada
                response = f"""⚠️ **MODO DEMOSTRACIÓN ACTIVO**

📚 **Tu consulta:** {user_input}

---

Esta es una respuesta simulada. Para activar respuestas reales con IA:

**Pasos para configurar Groq API (GRATIS):**

1. 🌐 Visita: https://console.groq.com/
2. ✅ Crea una cuenta gratuita (sin tarjeta de crédito)
3. 🔑 Genera tu API key
4. 📝 Agrégala al archivo `.env` como `GROQ_API_KEY`
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
