import streamlit as st
import textwrap

from Games.memory import show_memory_game
from Games.attention import show_attention_game
from Games.pattern import show_pattern_game


def render_html(html_str):
    clean = textwrap.dedent(html_str).strip()
    if hasattr(st, "html"):
        st.html(clean)
    else:
        st.markdown(clean, unsafe_allow_html=True)


def show_games():
    user_id = st.session_state.user_id
    games = ["Memory", "Attention", "Pattern"]
    game_names = {
        "Memory": "🧠 Memory Matrix (Recall Sequences)",
        "Attention": "🎯 Focus Finder (Spot Differences)",
        "Pattern": "🔷 Pattern Path (Find Next Item)"
    }

    current = st.session_state.get("selected_game", "Memory")
    if current not in games:
        current = "Memory"

    render_html("""
    <div style="background: linear-gradient(135deg, #161129 0%, #2A134D 50%, #7928CA 100%);
                border-radius: 24px; padding: 26px 34px; color: white; margin-bottom: 20px;
                border: 2px solid rgba(0, 210, 255, 0.35);
                box-shadow: 0 12px 30px rgba(121, 40, 202, 0.25);">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="background: #00D2FF; color: #161129; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 900; letter-spacing: 1.5px;">
                    NEURAL ARENA
                </span>
                <h1 style="color: white; margin: 8px 0 4px 0; font-size: 32px; font-weight: 900;">
                    🎮 Brain Training Activities
                </h1>
                <p style="color: #FFF8F0; opacity: 0.95; font-size: 17px; margin: 0;">
                    Pick an exercise below. Each activity starts at an <b>Easy</b> pace with gentle controls.
                </p>
            </div>
            <div style="font-size: 48px;">⚡</div>
        </div>
    </div>
    """)

    # Accessible horizontal radio selector with clear labels
    selected_name = st.radio(
        "Select your activity:",
        [game_names[g] for g in games],
        index=games.index(current),
        horizontal=True
    )

    for g, name in game_names.items():
        if name == selected_name:
            st.session_state.selected_game = g
            current = g
            break

    render_html("<hr style='border: none; height: 1px; background: #E2E8F0; margin: 20px 0;'>")

    # Render selected game
    if current == "Memory":
        show_memory_game(user_id)
    elif current == "Attention":
        show_attention_game(user_id)
    elif current == "Pattern":
        show_pattern_game(user_id)
