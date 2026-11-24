import streamlit as st
import pandas as pd
import textwrap

from database import get_user_stats, get_history, DEMO_PROFILES
from Machine_learning.prediction import get_model_info


def render_html(html_str):
    clean = textwrap.dedent(html_str).strip()
    if hasattr(st, "html"):
        st.html(clean)
    else:
        st.markdown(clean, unsafe_allow_html=True)


def show_dashboard():
    uid = st.session_state.user_id
    name = st.session_state.display_name
    age = st.session_state.get("user_age", "65")
    is_demo = st.session_state.get("is_demo", False)

    stats = get_user_stats(uid)
    records = get_history(uid)
    model_info = get_model_info()

    # Profile editor drawer
    if st.session_state.get("edit_profile", False) and not is_demo:
        with st.container(border=True):
            st.subheader("👤 Edit Your Live Account")
            st.write("Update your learner profile details below:")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                new_name = st.text_input("Preferred Name / Nickname", value=name)
            with c2:
                new_age = st.text_input("Your Age", value=age)
            with c3:
                new_id = st.text_input("Learner ID", value=uid)

            sc1, sc2 = st.columns([1.2, 4])
            with sc1:
                if st.button("Save Profile Details", type="primary", use_container_width=True):
                    st.session_state.display_name = new_name.strip() or "Learner"
                    st.session_state.user_age = new_age.strip() or "65"
                    st.session_state.user_id = new_id.strip() or "Learner-001"
                    st.session_state.edit_profile = False
                    st.rerun()
            with sc2:
                if st.button("Cancel", use_container_width=False):
                    st.session_state.edit_profile = False
                    st.rerun()

    # VIBRANT ARCADE HERO SECTION
    profile_tag = "ACTIVE USER ACCOUNT" if not is_demo else "DEMO SENIOR LEARNER PROFILE"
    tag_bg = "#00D2FF" if not is_demo else "#FFD166"
    tag_text = "#1A102F"

    render_html(f"""
    <div style="background: linear-gradient(135deg, #161129 0%, #2A134D 45%, #7928CA 80%, #00D2FF 100%);
                border-radius: 28px; padding: 36px 40px; color: white; margin-bottom: 25px;
                border: 2px solid rgba(0, 210, 255, 0.4);
                box-shadow: 0 16px 40px rgba(121, 40, 202, 0.35); position: relative; overflow: hidden;">
        
        <!-- Ambient arcade neon halos -->
        <div style="position: absolute; right: -30px; top: -30px; width: 220px; height: 220px; 
                    background: radial-gradient(circle, rgba(255, 0, 127, 0.35) 0%, transparent 70%); border-radius: 50%;"></div>
        <div style="position: absolute; left: 35%; bottom: -50px; width: 250px; height: 250px; 
                    background: radial-gradient(circle, rgba(0, 210, 255, 0.25) 0%, transparent 70%); border-radius: 50%;"></div>

        <div style="display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 2; flex-wrap: wrap; gap: 24px;">
            <div style="max-width: 660px;">
                <div style="display: inline-flex; align-items: center; gap: 8px; background: {tag_bg}; 
                            border-radius: 30px; padding: 6px 18px; margin-bottom: 16px;">
                    <span style="font-size: 14px;">⚡</span>
                    <span style="color: {tag_text}; font-size: 12px; font-weight: 900; letter-spacing: 1.5px;">
                        {profile_tag}
                    </span>
                </div>
                
                <h1 style="color: #FFF8F0; font-size: 38px; font-weight: 900; line-height: 1.2; margin: 0 0 12px 0;">
                    Welcome, <span style="color: #FFD166;">{name}</span>! 🎮
                </h1>
                
                <p style="color: #FFF8F0; opacity: 0.95; font-size: 18px; line-height: 1.6; margin: 0 0 22px 0;">
                    Welcome to the <b>MindGrow Neural Arcade</b>. Exercise your memory, sharpen visual observation,
                    and decode logical puzzles in a vibrant, friendly environment. Start easy and enjoy learning at your own pace!
                </p>
                
                <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
                    <span style="background: rgba(0,0,0,0.4); border: 1.5px solid #FFD166; padding: 8px 16px; border-radius: 14px; font-size: 14px; font-weight: 800; color: #FFD166;">
                        🏆 Rank: {stats['mastery_level']}
                    </span>
                    <span style="background: rgba(0,0,0,0.4); border: 1.5px solid #00D2FF; padding: 8px 16px; border-radius: 14px; font-size: 14px; font-weight: 800; color: #00D2FF;">
                        🤖 AI Difficulty Model: {model_info['algorithm']}
                    </span>
                </div>
            </div>

            <!-- Arcade Badge Mascot Vector -->
            <div style="text-align: center; padding: 10px;">
                <svg width="210" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <polygon points="100,6 170,30 194,100 170,170 100,194 30,170 6,100 30,30" fill="#1A102F" stroke="#00D2FF" stroke-width="8"/>
                    <polygon points="100,20 158,40 178,100 158,160 100,180 42,160 22,100 42,40" fill="#251644" stroke="#FF007F" stroke-width="3" opacity="0.7"/>
                    <!-- Brain Hemispheres -->
                    <path d="M 94 52 C 65 52, 48 72, 48 100 C 48 120, 60 134, 65 144 C 55 155, 66 166, 88 166 C 94 166, 94 160, 94 154 Z" fill="#FF007F"/>
                    <path d="M 106 52 C 135 52, 152 72, 152 100 C 152 120, 140 134, 135 144 C 145 155, 134 166, 112 166 C 106 166, 106 160, 106 154 Z" fill="#00D2FF"/>
                    <!-- Synapse Lightning -->
                    <polygon points="104,40 92,95 108,95 96,160 114,90 98,90" fill="#FFD166"/>
                    <circle cx="72" cy="85" r="5" fill="#FFF275"/>
                    <circle cx="128" cy="85" r="5" fill="#06D6A0"/>
                    <!-- Star sparks -->
                    <polygon points="26,26 29,20 32,26 38,29 32,32 29,38 26,32 20,29" fill="#FFD166"/>
                    <polygon points="172,172 174,166 177,172 183,174 177,176 174,182 172,176 166,174" fill="#00D2FF"/>
                </svg>
            </div>
        </div>
    </div>
    """)

    # START PLAYING BUTTON
    sc1, sc2 = st.columns([1.5, 3])
    with sc1:
        if st.button("🚀 Jump Into Brain Games", type="primary", use_container_width=True):
            st.session_state.page = "Brain Games"
            st.rerun()

    render_html("<div style='height: 20px;'></div>")

    # 4 KEY PERFORMANCE INDICATORS
    st.markdown("### 📊 Performance & High Scores")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            label="Total Sessions Completed",
            value=stats["games"]
        )
    with kpi2:
        st.metric(
            label="Average Accuracy",
            value=f"{stats['average_accuracy']}%" if records else "—"
        )
    with kpi3:
        st.metric(
            label="Highest Score",
            value=f"{stats['best_score']} pts" if records else "—"
        )
    with kpi4:
        st.metric(
            label="Total Neural Points",
            value=f"{stats['total_points']}" if records else "—"
        )

    render_html("<div style='height: 25px;'></div>")

    # 3 LARGE & ATTRACTIVE ARCADE GAME CARDS
    st.markdown("### 🎮 Select an Arcade Activity")
    st.write("All three games feature gentle, senior-friendly controls and start on **Easy** by default:")

    game_scores = {"Memory": 0, "Attention": 0, "Pattern": 0}
    for r in records:
        g = r.get("game")
        if g in game_scores:
            game_scores[g] = max(game_scores[g], int(r.get("score", 0)))

    c_mem, c_att, c_pat = st.columns(3)

    # CARD 1: MEMORY MATRIX
    with c_mem:
        with st.container(border=True):
            render_html(f"""
            <div style="padding: 10px 4px 14px 4px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px;">
                    <span style="background: rgba(255, 0, 127, 0.15); color: #FF007F; 
                                 padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 900; letter-spacing: 0.5px;">
                        WORKING MEMORY
                    </span>
                    <span style="font-size: 14px; font-weight: 800; color: #7928CA;">
                        Best: {game_scores['Memory']} pts
                    </span>
                </div>
                <div style="font-size: 52px; margin: 8px 0;">🧠</div>
                <h3 style="color: #1A102F; margin: 0 0 8px 0; font-size: 24px; font-weight: 900;">
                    Memory Matrix
                </h3>
                <p style="color: #4A5568; font-size: 16px; line-height: 1.6; min-height: 72px;">
                    Memorize and repeat friendly symbol chains. Reconstruct the sequence in order at your own pace.
                </p>
            </div>
            """)
            if st.button("Play Memory Matrix →", key="dash_play_mem", type="primary", use_container_width=True):
                st.session_state.selected_game = "Memory"
                st.session_state.page = "Brain Games"
                st.rerun()

    # CARD 2: FOCUS FINDER
    with c_att:
        with st.container(border=True):
            render_html(f"""
            <div style="padding: 10px 4px 14px 4px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px;">
                    <span style="background: rgba(255, 107, 53, 0.15); color: #FF6B35; 
                                 padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 900; letter-spacing: 0.5px;">
                        SELECTIVE FOCUS
                    </span>
                    <span style="font-size: 14px; font-weight: 800; color: #FF6B35;">
                        Best: {game_scores['Attention']} pts
                    </span>
                </div>
                <div style="font-size: 52px; margin: 8px 0;">🎯</div>
                <h3 style="color: #1A102F; margin: 0 0 8px 0; font-size: 24px; font-weight: 900;">
                    Focus Finder
                </h3>
                <p style="color: #4A5568; font-size: 16px; line-height: 1.6; min-height: 72px;">
                    Scan the distractor grid and spot the unique symbol. Relaxing, high-contrast, and fun for all ages.
                </p>
            </div>
            """)
            if st.button("Play Focus Finder →", key="dash_play_att", type="primary", use_container_width=True):
                st.session_state.selected_game = "Attention"
                st.session_state.page = "Brain Games"
                st.rerun()

    # CARD 3: PATTERN PATH
    with c_pat:
        with st.container(border=True):
            render_html(f"""
            <div style="padding: 10px 4px 14px 4px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px;">
                    <span style="background: rgba(6, 214, 160, 0.15); color: #06D6A0; 
                                 padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 900; letter-spacing: 0.5px;">
                        INDUCTIVE LOGIC
                    </span>
                    <span style="font-size: 14px; font-weight: 800; color: #00D2FF;">
                        Best: {game_scores['Pattern']} pts
                    </span>
                </div>
                <div style="font-size: 52px; margin: 8px 0;">🔷</div>
                <h3 style="color: #1A102F; margin: 0 0 8px 0; font-size: 24px; font-weight: 900;">
                    Pattern Path
                </h3>
                <p style="color: #4A5568; font-size: 16px; line-height: 1.6; min-height: 72px;">
                    Uncover numeric sequences and shape patterns with immediate educational explanations after each puzzle.
                </p>
            </div>
            """)
            if st.button("Play Pattern Path →", key="dash_play_pat", type="primary", use_container_width=True):
                st.session_state.selected_game = "Pattern"
                st.session_state.page = "Brain Games"
                st.rerun()

    render_html("<div style='height: 30px;'></div>")

    # SENIOR DEMO PROFILES SHOWCASE SECTION
    st.markdown("### 🇮🇳 Senior Learner Spotlights (Ages 60–75)")
    st.write("MindGrow is proudly engineered for older adults. Meet our fictional demo learners:")

    demo_cols = st.columns(4)
    for idx, p in enumerate(DEMO_PROFILES):
        with demo_cols[idx]:
            with st.container(border=True):
                render_html(f"""
                <div style="text-align: center; padding: 4px;">
                    <div style="font-size: 44px; margin-bottom: 6px;">{p['avatar']}</div>
                    <div style="font-weight: 900; font-size: 17px; color: #1A102F;">{p['name']}</div>
                    <div style="font-size: 13px; font-weight: 700; color: #7928CA; margin-bottom: 4px;">
                        Age: {p['age']} • {p['city']}
                    </div>
                    <div style="font-size: 12px; color: #718096; margin-bottom: 10px;">
                        {p['occupation']}
                    </div>
                    <div style="background: #F8F9FE; border-radius: 10px; padding: 6px 10px; font-size: 12px; font-style: italic; color: #4A5568; min-height: 52px; margin-bottom: 10px;">
                        "{p['quote']}"
                    </div>
                </div>
                """)
                btn_label = "Active Now" if uid == p["id"] else f"View {p['name'].split()[0]}"
                btn_type = "primary" if uid == p["id"] else "secondary"
                if st.button(btn_label, key=f"view_demo_{p['id']}", type=btn_type, use_container_width=True):
                    st.session_state.user_id = p["id"]
                    st.session_state.display_name = p["name"]
                    st.session_state.user_age = str(p["age"])
                    st.session_state.is_demo = True
                    st.rerun()

    render_html("<div style='height: 30px;'></div>")

    # RECENT ACTIVITY SECTION
    st.markdown(f"### 📋 Activity History ({'Demo: ' + name if is_demo else 'My Live Account'})")
    if not records:
        st.info("💡 No gameplay records found for this profile yet. Pick any game above to begin recording!")
    else:
        df = pd.DataFrame(records).sort_values("timestamp", ascending=False).head(5)
        
        display_df = df.copy()
        try:
            display_df["timestamp"] = pd.to_datetime(display_df["timestamp"]).dt.strftime("%d %b %Y, %I:%M %p")
        except Exception:
            pass

        show_cols = ["timestamp", "game", "difficulty", "score", "accuracy", "time_taken", "recommended_difficulty"]
        avail_cols = [c for c in show_cols if c in display_df.columns]
        display_df = display_df[avail_cols]
        display_df.columns = [
            "Date & Time",
            "Game",
            "Level Played",
            "Score (pts)",
            "Accuracy (%)",
            "Time Taken (s)",
            "AI Recommended Next"
        ][:len(avail_cols)]

        st.dataframe(display_df, use_container_width=True, hide_index=True)
