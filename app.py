import streamlit as st
import textwrap
from pathlib import Path

from ui_pages.dashboard import show_dashboard
from ui_pages.games import show_games
from ui_pages.progress import show_progress
from ui_pages.about import show_about

from database import ensure_history_file, get_user_stats, DEMO_PROFILES

# Page configuration
st.set_page_config(
    page_title="MindGrow | Neural Arcade Cognitive Training",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

ensure_history_file()

BASE_DIR = Path(__file__).resolve().parent
LOGO_FILE = BASE_DIR / "Assets" / "logo.png"   # put your uploaded logo here (optional)

NAV_PAGES = ["Home", "Brain Games", "My Progress", "About MindGrow"]
NAV_LABELS = {
    "Home": "🏠  Home",
    "Brain Games": "🎮  Brain Games",
    "My Progress": "📈  My Progress",
    "About MindGrow": "ℹ️  About MindGrow",
}


def render_html(html_str):
    clean = textwrap.dedent(html_str).strip()
    if hasattr(st, "html"):
        st.html(clean)
    else:
        st.markdown(clean, unsafe_allow_html=True)


# ----------------- SESSION STATE DEFAULTS -----------------
if "user_id" not in st.session_state:
    st.session_state.user_id = "Learner-001"
if "display_name" not in st.session_state:
    st.session_state.display_name = "My Live Account"
if "user_age" not in st.session_state:
    st.session_state.user_age = "65"
if "is_demo" not in st.session_state:
    st.session_state.is_demo = False
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "selected_game" not in st.session_state:
    st.session_state.selected_game = "Memory"

# Keep the sidebar radio in sync when a button elsewhere changes st.session_state.page
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = st.session_state.page
if st.session_state.page != st.session_state.get("_last_page"):
    st.session_state.nav_choice = st.session_state.page

# ----------------- ARCADE NEURAL STYLING -----------------
render_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Nunito:wght@400;600;700;800;900&display=swap');

:root {
    --electric-blue: #00D2FF;
    --vibrant-purple: #7928CA;
    --neon-pink: #FF007F;
    --sunshine-yellow: #FFD166;
    --deep-arcade: #161129;
    --text-primary: #1A102F;
}

html, body, [class*="css"], .stMarkdown, .stText, p, span, label {
    font-family: 'Outfit', 'Nunito', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: 16px;
}

.stApp {
    background-color: #F8F9FE !important;
    background-image:
        radial-gradient(at 0% 0%, rgba(121, 40, 202, 0.08) 0px, transparent 55%),
        radial-gradient(at 100% 0%, rgba(0, 210, 255, 0.09) 0px, transparent 55%),
        radial-gradient(at 50% 100%, rgba(255, 0, 127, 0.05) 0px, transparent 55%) !important;
    color: var(--text-primary) !important;
}

[data-testid="stHeader"] { background: transparent !important; }

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"] {
    background-color: #161129 !important;
    background-image: linear-gradient(180deg, #161129 0%, #20133D 50%, #2A134D 100%) !important;
    border-right: 2px solid rgba(0, 210, 255, 0.25) !important;
    box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3) !important;
}
[data-testid="stSidebar"] * { color: #FFF8F0 !important; }

/* Sidebar navigation (radio styled as menu buttons) */
[data-testid="stSidebar"] div[role="radiogroup"] { gap: 8px !important; }
[data-testid="stSidebar"] div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.07) !important;
    border: 2px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
    padding: 12px 14px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    border-color: #00D2FF !important;
    background: rgba(0,210,255,0.12) !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked) {
    background: linear-gradient(135deg, #7928CA, #00BDEB) !important;
    border-color: #FFFFFF !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] > label > div:first-child { display: none !important; }
[data-testid="stSidebar"] div[role="radiogroup"] p { font-weight: 800 !important; font-size: 17px !important; }

/* Sidebar dropdown: white box with dark text (fixes black box) */
[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 2px solid #A98ACF !important;
    border-radius: 14px !important;
}
[data-testid="stSidebar"] div[data-baseweb="select"] * { color: #25113F !important; }
[data-testid="stSidebar"] div[data-baseweb="select"] svg { fill: #25113F !important; }

/* Dropdown popup list (rendered outside sidebar) */
div[data-baseweb="popover"], div[data-baseweb="popover"] ul,
div[data-baseweb="popover"] li, div[data-baseweb="menu"] {
    background: #FFFFFF !important;
}
div[data-baseweb="popover"] li, div[data-baseweb="popover"] li * { color: #25113F !important; }
div[data-baseweb="popover"] li:hover { background: #EFE4FF !important; }

/* Sidebar buttons */
[data-testid="stSidebar"] div.stButton > button {
    background: #FFFFFF !important;
    border: 2px solid #A98ACF !important;
    box-shadow: 0 4px 0 #7928CA !important;
}
[data-testid="stSidebar"] div.stButton > button * { color: #35145E !important; }

.block-container {
    max-width: 1350px !important;
    padding: 1.8rem 2.2rem 3.5rem !important;
}

/* ---------- BUTTONS ---------- */
div.stButton > button {
    border-radius: 16px !important;
    font-weight: 800 !important;
    font-size: 17px !important;
    font-family: 'Outfit', sans-serif !important;
    letter-spacing: 0.5px !important;
    padding: 0.7rem 1.6rem !important;
    min-height: 52px !important;
    cursor: pointer !important;
    transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7928CA, #00BDEB) !important;
    border: 2px solid #54209A !important;
    box-shadow: 0 5px 0 #4C168A, 0 10px 20px rgba(0, 210, 255, 0.3) !important;
}
div.stButton > button[kind="primary"],
div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }
div.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 7px 0 #4C168A, 0 14px 26px rgba(0, 210, 255, 0.45) !important;
}
div.stButton > button[kind="primary"]:active {
    transform: translateY(3px) !important;
    box-shadow: 0 2px 0 #4C168A !important;
}

div.stButton > button[kind="secondary"] {
    background: #FFFFFF !important;
    border: 2px solid #A98ACF !important;
    box-shadow: 0 4px 0 #CBB8E6, 0 6px 14px rgba(0,0,0,0.06) !important;
}
div.stButton > button[kind="secondary"],
div.stButton > button[kind="secondary"] * { color: #35145E !important; }
div.stButton > button[kind="secondary"]:hover {
    transform: translateY(-2px) !important;
    border-color: #00D2FF !important;
    background: #F3EAFF !important;
    box-shadow: 0 6px 0 #00D2FF, 0 10px 20px rgba(0,210,255,0.18) !important;
}
div.stButton > button[kind="secondary"]:active {
    transform: translateY(2px) !important;
    box-shadow: 0 1px 0 #00D2FF !important;
}

/* Disabled buttons: light, never black */
div.stButton > button:disabled {
    background: #EFE8FA !important;
    border: 2px solid #D6C8EE !important;
    box-shadow: none !important;
    opacity: 0.8 !important;
    cursor: not-allowed !important;
}
div.stButton > button:disabled, div.stButton > button:disabled * { color: #8A7AA5 !important; }

/* Download button */
div.stDownloadButton > button {
    background: #FFFFFF !important;
    border: 2px solid #7928CA !important;
    border-radius: 14px !important;
}
div.stDownloadButton > button * { color: #35145E !important; font-weight: 800 !important; }

/* ---------- CARDS / METRICS ---------- */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: white !important;
    border-radius: 22px !important;
    border: 2px solid #EAE6F8 !important;
    box-shadow: 0 10px 28px rgba(22, 17, 41, 0.06) !important;
    transition: all 0.25s ease !important;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #00D2FF !important;
    box-shadow: 0 14px 36px rgba(0, 210, 255, 0.15) !important;
}

div[data-testid="stMetric"] {
    background: white !important;
    padding: 20px 22px !important;
    border-radius: 20px !important;
    border: 2px solid #EAE6F8 !important;
    box-shadow: 0 8px 20px rgba(22, 17, 41, 0.05) !important;
    position: relative !important;
    overflow: hidden !important;
}
div[data-testid="stMetric"]::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important; left: 0 !important; right: 0 !important;
    height: 6px !important;
    background: linear-gradient(90deg, #FF007F, #FFD166, #00D2FF) !important;
}
div[data-testid="stMetricLabel"], div[data-testid="stMetricLabel"] * {
    color: #38204F !important; font-weight: 900 !important; font-size: 14px !important;
    text-transform: uppercase !important; letter-spacing: 0.8px !important; opacity: 1 !important;
}
div[data-testid="stMetricValue"], div[data-testid="stMetricValue"] * {
    color: #24113D !important; font-size: 34px !important; font-weight: 900 !important; opacity: 1 !important;
}
div[data-testid="stMetricDelta"] { color: #176B45 !important; font-weight: 800 !important; }

/* ---------- INPUTS ---------- */
.stTextInput input, .stNumberInput input {
    border-radius: 14px !important;
    border: 2px solid #A98ACF !important;
    padding: 12px 16px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #25113F !important;
    background: #FFFFFF !important;
}
.stTextInput input:focus {
    border-color: #00D2FF !important;
    box-shadow: 0 0 0 3px rgba(0, 210, 255, 0.2) !important;
}

/* Main-area selectboxes */
.stApp [data-testid="stMain"] div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 2px solid #A98ACF !important;
    border-radius: 14px !important;
}
.stApp [data-testid="stMain"] div[data-baseweb="select"] * { color: #25113F !important; }

[data-testid="stDataFrame"] {
    border-radius: 18px !important;
    overflow: hidden !important;
    border: 2px solid #EAE6F8 !important;
}

[data-testid="stMain"] p, [data-testid="stMain"] label, [data-testid="stMain"] .stMarkdown {
    color: #28183F;
}
</style>
""")

# ----------------- SIDEBAR -----------------
with st.sidebar:

    # Brand: uses your own logo if Assets/logo.png exists, else the built-in SVG
    if LOGO_FILE.exists():
        st.image(str(LOGO_FILE), use_container_width=True)
    else:
        render_html("""
        <div style="text-align: center; padding: 10px 0 4px 0;">
            <svg width="68" height="68" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
                <polygon points="100,6 170,30 194,100 170,170 100,194 30,170 6,100 30,30" fill="#1A102F" stroke="#00D2FF" stroke-width="8"/>
                <polygon points="100,20 158,40 178,100 158,160 100,180 42,160 22,100 42,40" fill="#251644" stroke="#FF007F" stroke-width="3" opacity="0.7"/>
                <path d="M 94 52 C 65 52, 48 72, 48 100 C 48 120, 60 134, 65 144 C 55 155, 66 166, 88 166 C 94 166, 94 160, 94 154 Z" fill="#FF007F"/>
                <path d="M 106 52 C 135 52, 152 72, 152 100 C 152 120, 140 134, 135 144 C 145 155, 134 166, 112 166 C 106 166, 106 160, 106 154 Z" fill="#00D2FF"/>
                <polygon points="104,40 92,95 108,95 96,160 114,90 98,90" fill="#FFD166"/>
                <circle cx="72" cy="85" r="5" fill="#FFF275"/>
                <circle cx="128" cy="85" r="5" fill="#06D6A0"/>
            </svg>
        </div>
        """)

    render_html("""
    <div style="text-align: center; padding-bottom: 8px;">
        <h2 style="margin: 0; color: #FFF8F0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px;">
            MIND<span style="color: #FFD166;">GROW</span>
        </h2>
        <span style="background: linear-gradient(90deg, #FF007F, #00D2FF); color: white;
                     padding: 3px 12px; border-radius: 12px; font-size: 10px; font-weight: 900; letter-spacing: 2px;">
            NEURAL ARCADE
        </span>
    </div>
    <hr style='border: none; height: 1px; background: rgba(255,255,255,0.12); margin: 12px 0;'>
    """)

    # ---------- NAVIGATION ----------
    st.markdown("##### 🧭 Navigation")
    nav_selected = st.radio(
        "Go to page",
        NAV_PAGES,
        key="nav_choice",
        format_func=lambda p: NAV_LABELS[p],
        label_visibility="collapsed",
    )
    st.session_state.page = nav_selected
    st.session_state._last_page = nav_selected

    render_html("<hr style='border: none; height: 1px; background: rgba(255,255,255,0.12); margin: 15px 0;'>")

    # ---------- PROFILE SELECTOR ----------
    st.markdown("##### 👥 Active Learner Profile")

    profile_options = ["👤 My Live Account"] + [
        f"{p['avatar']} {p['name']} (Age {p['age']})" for p in DEMO_PROFILES
    ]

    current_idx = 0
    if st.session_state.is_demo:
        for idx, p in enumerate(DEMO_PROFILES):
            if p["id"] == st.session_state.user_id:
                current_idx = idx + 1
                break

    selected_profile_str = st.selectbox(
        "Switch Profile (Demo or Live):",
        profile_options,
        index=current_idx,
        help="Select a fictional Indian senior profile to view sample trajectories or switch to your live account."
    )

    if selected_profile_str == "👤 My Live Account":
        if st.session_state.is_demo:
            st.session_state.user_id = "Learner-001"
            st.session_state.display_name = "My Live Account"
            st.session_state.user_age = "65"
            st.session_state.is_demo = False
            st.rerun()
    else:
        chosen_demo = next(
            p for p in DEMO_PROFILES
            if f"{p['avatar']} {p['name']} (Age {p['age']})" == selected_profile_str
        )
        if st.session_state.user_id != chosen_demo["id"]:
            st.session_state.user_id = chosen_demo["id"]
            st.session_state.display_name = chosen_demo["name"]
            st.session_state.user_age = str(chosen_demo["age"])
            st.session_state.is_demo = True
            st.rerun()

    # ---------- PROFILE BADGE ----------
    stats = get_user_stats(st.session_state.user_id)
    badge_label = "ACTIVE USER" if not st.session_state.is_demo else "DEMO SENIOR PROFILE"

    render_html(f"""
    <div style="background: linear-gradient(135deg, #382052, #4B286E); border: 2px solid #9360D5;
                border-radius: 20px; padding: 16px; margin: 12px 0; box-shadow: 0 6px 18px rgba(0,0,0,0.2);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <span style="background:#087D70; color:#FFFFFF !important; padding:5px 10px; border-radius:12px;
                         font-size:11px; font-weight:900;">{badge_label}</span>
            <span style="color:#FFE08A !important; font-size:13px; font-weight:900;">Age: {st.session_state.user_age}</span>
        </div>
        <div style="color:#FFFFFF !important; font-size:18px; font-weight:900; margin-bottom:5px;">
            {st.session_state.display_name}
        </div>
        <div style="color:#DCC9F5 !important; font-size:12px; font-weight:700; margin-bottom:12px;">
            ID: {st.session_state.user_id}
        </div>
        <div style="background:#241432; border:1px solid #63417F; border-radius:13px; padding:11px;">
            <div style="color:#DCC9F5 !important; font-size:11px; font-weight:900; margin-bottom:5px;">CURRENT RANK</div>
            <div style="color:#FFD166 !important; font-size:15px; font-weight:900;">⚡ {stats['mastery_level']}</div>
        </div>
    </div>
    """)

    if not st.session_state.is_demo:
        if st.button("✏️ Edit My Account Details", use_container_width=True):
            st.session_state.edit_profile = True
            st.session_state.page = "Home"
            st.rerun()

    render_html("""
    <div style="font-size: 12px; margin-top: 10px; line-height: 1.5; opacity: 0.8;">
        🔒 <b>Data Separation:</b> Live user records and demo profile records are kept strictly separate.
    </div>
    """)

# ----------------- PAGE ROUTING -----------------
selected = st.session_state.page

if selected == "Home":
    show_dashboard()
elif selected == "Brain Games":
    show_games()
elif selected == "My Progress":
    show_progress()
elif selected == "About MindGrow":
    show_about()