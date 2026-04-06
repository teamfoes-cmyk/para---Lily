import streamlit as st
import random
from datetime import datetime
import time

# Configuración
st.set_page_config(page_title="Para mi Lily ❤️", page_icon="❤️")

# --- ESTILO CSS (Números Rosas + Etiquetas Blancas) ---
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: #ffffff; }
    
    /* Los números mantienen su estilo rosado que te gustó */
    [data-testid="stMetricValue"] {
        color: #ffb3c1 !important;
        font-size: 50px !important;
        text-shadow: 0px 0px 15px #ff4d6d;
    }
    
    /* El texto 'Días, Horas...' ahora en blanco puro para que no sea opaco */
    [data-testid="stMetricLabel"] { 
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 14px !important;
        letter-spacing: 1px;
    }

    .mensaje-card {
        padding: 30px; border-radius: 20px;
        background: linear-gradient(135deg, #2d0a0a 0%, #4a0e0e 100%);
        border: 2px solid #ff4d6d;
        text-align: center; font-size: 1.3rem;
        margin-top: 20px; box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    .stButton>button {
        width: 100%; border-radius: 15px; background-color: #2d0a0a;
        color: #ffb3c1; border: 1px solid #ff4d6d; height: 3.5em;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #ff4d6d; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TIEMPO ---
fecha_inicio = datetime(2026, 4, 6, 14, 0, 0)
ahora = datetime.now() 

diff = ahora - fecha_inicio
meses_juntos = (ahora.year - fecha_inicio.year) * 12 + (ahora.month - fecha_inicio.month)
if ahora.day < fecha_inicio.day:
    meses_juntos -= 1

st.title("❤️ Nuestro Rincón Eterno❤️")

# Contador
# --- CONTADOR COMPACTO PARA MÓVIL ---
st.write("---")
html_contador = f"""
<div style="display: flex; justify-content: space-around; text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; border: 1px solid #ff4d6d;">
    <div><div style="color: white; font-size: 10px;">DÍAS</div><div style="color: #ffb3c1; font-size: 25px; font-weight: bold; text-shadow: 0 0 10px #ff4d6d;">{abs(diff.days)}</div></div>
    <div><div style="color: white; font-size: 10px;">HORAS</div><div style="color: #ffb3c1; font-size: 25px; font-weight: bold; text-shadow: 0 0 10px #ff4d6d;">{diff.seconds // 3600}</div></div>
    <div><div style="color: white; font-size: 10px;">MINS</div><div style="color: #ffb3c1; font-size: 25px; font-weight: bold; text-shadow: 0 0 10px #ff4d6d;">{(diff.seconds % 3600) // 60}</div></div>
    <div><div style="color: white; font-size: 10px;">SEGS</div><div style="color: #ffb3c1; font-size: 25px; font-weight: bold; text-shadow: 0 0 10px #ff4d6d;">{diff.seconds % 60}</div></div>
</div>
"""
st.markdown(html_contador, unsafe_allow_html=True)
st.write("---")

st.write("---")

# --- MENSAJE ESPECIAL DEL 15 ---
if ahora.day == 15:
    if 'efectos_lanzados' not in st.session_state:
        st.balloons(); st.snow()
        st.session_state.efectos_lanzados = True
    
    texto_mes = f"{meses_juntos} meses" if meses_juntos != 1 else "nuestro primer mes"
    st.markdown(f"""
    <div class="mensaje-card">
        <h2 style='color: #ff4d6d;'>🎊 ¡Feliz día 15, mi Lily! 🎊</h2>
        <p>Hoy cumplimos <b>{texto_mes}</b> de este nuevo camino.</p>
        <p style='font-size: 1.1rem; font-style: italic;'>
            "No hay nada que me haga más feliz que saber que eres mi novia. 
            Gracias por dejarme quererte y por ser esa luz en mis días. Te amo tal cual eres."
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- BANCO DE FRASES EMOTIVAS ---
if 'last_msg' not in st.session_state:
    st.session_state.last_msg = "Elige cómo te sientes para decirte algo..."

st.subheader("¿Cómo está tu corazón ahora?")
c1, c2 = st.columns(2)

with c1:
    if st.button("❤️ Te extraño"):
        st.session_state.last_msg = random.choice([
            "Yo te extraño mucho más... cada minuto cuento para estar cerquita de ti. ✨",
            "Cierra los ojos un momento, siente mi abrazo. No importa la distancia, estoy ahí. ❤️",
            "Me haces falta en cada silencio de mi día. Eres mi pensamiento favorito. 🌙",
            "Contando las horas para poder darte ese cariño que tanto nos hace falta. Te amo. 🧸",
            "Te extraño tanto que a veces siento que me falta algo si no te hablo. 🌹"
        ])
    if st.button("🥺 Mal día"):
        st.session_state.last_msg = random.choice([
            "Respira mi niña, aquí estoy. Deja que yo cuide tu corazón un ratito hoy. ❤️",
            "Todo va a estar bien, lo prometo. Eres la mujer más fuerte que conozco. 💪",
            "Siente mi mano en la tuya. Mañana será un mejor día y yo estaré ahí para verlo. ✨",
            "No dejes que nada te apague esa luz tan linda que tienes. Yo te protejo. 🛡️❤️",
            "Ven a descansar aquí conmigo. Suelta todo lo malo, yo te sostengo. 🕊️"
        ])

with c2:
    if st.button("🔥 Un beso"):
        st.balloons()
        st.session_state.last_msg = random.choice([
            "💋 *Un beso dulce y largo, de esos que te hacen olvidar todo el mundo.* 💋",
            "💋 *Te envío el beso más tierno justo en tu frente, para que sepas que te cuido.* 💋",
            "💋 *Un beso de esos que nos dábamos y que pronto volveremos a darnos.* 💋",
            "💋 *Siente mi cariño cruzando la pantalla... te amo infinito.* 💋",
            "💋 *Beso robado (y enviado con mucho amor) para mi novia favorita.* 💋"
        ])
    if st.button("✨ El futuro"):
        st.session_state.last_msg = random.choice([
            "Nos veo cumpliendo cada cosa que soñamos. No nos va a faltar nada. 🏡💍",
            "Te prometo un futuro donde lo que más sobre sea el cariño y la paz. ❤️",
            "Tú y yo contra el mundo, siempre de la mano, sin soltarnos nunca más. 🤝",
            "Veo una vida llena de risas contigo. Ese es mi único plan. 🌎✨",
            "Sé que lo que viene es hermoso, porque lo vamos a construir juntos. 🔑❤️"
        ])

st.markdown(f'<div class="mensaje-card" style="background: rgba(255,255,255,0.05);">{st.session_state.last_msg}</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"📍 Hecho con amor para Lily. Sincronizado: {abs(diff.days)} días.")

time.sleep(1)
st.rerun()
