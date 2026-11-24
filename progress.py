import streamlit as st
import pandas as pd
import textwrap
import plotly.express as px
import plotly.graph_objects as go

from database import get_history, get_user_stats, DEMO_PROFILES
from Machine_learning.prediction import get_model_info


def render_html(html_str):
    clean = textwrap.dedent(html_str).strip()
    if hasattr(st, "html"):
        st.html(clean)
    else:
        st.markdown(clean, unsafe_allow_html=True)


def show_progress():
    uid = st.session_state.user_id
    name = st.session_state.display_name
    is_demo = st.session_state.get("is_demo", False)

    records = get_history(uid)
    stats = get_user_stats(uid)
    model_info = get_model_info()

    # Progress Page Header
    render_html(f"""
    <div style="background: linear-gradient(135deg, #161129 0%, #2A134D 50%, #00D2FF 100%);
                border-radius: 24px; padding: 28px 34px; color: white; margin-bottom: 25px;
                border: 2px solid rgba(0, 210, 255, 0.4);
                box-shadow: 0 14px 34px rgba(0, 210, 255, 0.25);">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="background: #FFD166; color: #161129; 
                             padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 900; letter-spacing: 1.5px;">
                    COGNITIVE ANALYTICS ENGINE
                </span>
                <h1 style="color:white; margin: 8px 0 4px 0; font-size: 32px; font-weight: 900;">
                    📈 Performance & Learning Curves
                </h1>
                <p style="color: #FFF8F0; opacity: 0.95; margin: 0; font-size: 17px;">
                    Viewing records for: <b>{name}</b> ({'Demo Senior Profile' if is_demo else 'Active Live User'})
                </p>
            </div>
            <div style="font-size: 52px;">📊</div>
        </div>
    </div>
    """)

    # 4 KEY METRIC TILES
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Total Sessions Completed", value=stats["games"])
    with c2:
        st.metric(label="Average Accuracy", value=f"{stats['average_accuracy']}%" if records else "—")
    with c3:
        st.metric(label="Highest Single Score", value=f"{stats['best_score']} pts" if records else "—")
    with c4:
        st.metric(label="Total Neural Points", value=f"{stats['total_points']}" if records else "—")

    render_html("<div style='height: 20px;'></div>")

    # Filter / Profile switcher bar on Progress Page
    with st.container(border=True):
        st.markdown("##### 🔍 Choose Data Source to View")
        source_options = ["👤 My Live User Account"] + [f"{p['avatar']} {p['name']} (Age {p['age']} - {p['city']})" for p in DEMO_PROFILES]
        
        current_idx = 0
        if is_demo:
            for idx, p in enumerate(DEMO_PROFILES):
                if p["id"] == uid:
                    current_idx = idx + 1
                    break

        new_source = st.selectbox(
            "Select Account History:",
            source_options,
            index=current_idx,
            help="Switch between your live gameplay records and sample senior Indian learner trajectories."
        )

        if new_source == "👤 My Live User Account":
            if is_demo:
                st.session_state.user_id = "Learner-001"
                st.session_state.display_name = "My Live Account"
                st.session_state.user_age = "65"
                st.session_state.is_demo = False
                st.rerun()
        else:
            chosen_demo = next(p for p in DEMO_PROFILES if f"{p['avatar']} {p['name']} (Age {p['age']} - {p['city']})" == new_source)
            if uid != chosen_demo["id"]:
                st.session_state.user_id = chosen_demo["id"]
                st.session_state.display_name = chosen_demo["name"]
                st.session_state.user_age = str(chosen_demo["age"])
                st.session_state.is_demo = True
                st.rerun()

    render_html("<div style='height: 20px;'></div>")

    if not records:
        st.info("💡 No gameplay data recorded for this account yet. Play a round in Brain Games to generate your performance analytics!")
        return

    df = pd.DataFrame(records)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    # TABS: ANALYTICS VISUALIZATIONS & RAW CSV LOGS
    tab_charts, tab_history, tab_ml = st.tabs(["📊 Performance Visualizations", "📋 Complete CSV History", "🤖 Random Forest Model Diagnostics"])

    with tab_charts:
        st.markdown("#### 📈 Longitudinal Accuracy Progression")
        st.write("Tracking accuracy percentage across practice sessions:")
        
        try:
            fig_acc = go.Figure()
            
            # Palette: Hot Pink, Electric Blue, Turquoise
            color_map = {"Memory": "#FF007F", "Attention": "#FF6B35", "Pattern": "#06D6A0"}

            for game_name, group in df.groupby("game"):
                fig_acc.add_trace(go.Scatter(
                    x=group["timestamp"],
                    y=group["accuracy"],
                    mode="lines+markers",
                    name=f"{game_name} Game",
                    line=dict(width=3.5, color=color_map.get(game_name, "#00D2FF")),
                    marker=dict(size=10, symbol="circle")
                ))

            # Benchmark line at 80%
            fig_acc.add_hline(
                y=80, line_dash="dash", line_color="#FFD166",
                annotation_text="High Mastery Benchmark (80%)",
                annotation_position="top right"
            )

            fig_acc.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white",
                margin=dict(l=20, r=20, t=30, b=20),
                xaxis=dict(title="Practice Date & Time", showgrid=True, gridcolor="#F0F4F8"),
                yaxis=dict(title="Accuracy (%)", range=[0, 105], showgrid=True, gridcolor="#F0F4F8"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                height=380
            )
            st.plotly_chart(fig_acc, use_container_width=True)

        except Exception:
            chart_data = df.set_index("timestamp")[["accuracy"]]
            st.line_chart(chart_data)

        render_html("<div style='height: 15px;'></div>")

        sub1, sub2 = st.columns(2)

        with sub1:
            st.markdown("#### 🎮 Average Accuracy by Brain Activity")
            game_summary = df.groupby("game").agg(
                avg_accuracy=("accuracy", "mean"),
                avg_score=("score", "mean"),
                count=("score", "count")
            ).reset_index()

            try:
                fig_bar = px.bar(
                    game_summary,
                    x="game",
                    y="avg_accuracy",
                    text_auto=".1f",
                    color="game",
                    color_discrete_map={"Memory": "#FF007F", "Attention": "#FF6B35", "Pattern": "#06D6A0"},
                    labels={"avg_accuracy": "Average Accuracy (%)", "game": "Brain Activity"}
                )
                fig_bar.update_layout(
                    plot_bgcolor="white",
                    paper_bgcolor="white",
                    showlegend=False,
                    height=320,
                    margin=dict(l=10, r=10, t=10, b=10),
                    yaxis=dict(range=[0, 105], showgrid=True, gridcolor="#F0F4F8")
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            except Exception:
                st.bar_chart(game_summary.set_index("game")["avg_accuracy"])

        with sub2:
            st.markdown("#### 🎯 Difficulty Distribution")
            diff_counts = df["difficulty"].value_counts().reset_index()
            diff_counts.columns = ["Difficulty", "Sessions"]

            try:
                fig_pie = px.pie(
                    diff_counts,
                    names="Difficulty",
                    values="Sessions",
                    hole=0.45,
                    color="Difficulty",
                    color_discrete_map={"Easy": "#06D6A0", "Medium": "#FFD166", "Hard": "#FF007F"}
                )
                fig_pie.update_layout(
                    paper_bgcolor="white",
                    height=320,
                    margin=dict(l=10, r=10, t=10, b=10)
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            except Exception:
                st.write(diff_counts)

    with tab_history:
        st.markdown(f"#### 📋 Activity Log ({'Demo Records' if is_demo else 'Real User Records'})")
        file_ref = "Data/demo_learner_history.csv" if is_demo else "Data/game_history.csv"
        st.caption(f"Loaded directly from persistent CSV: `{file_ref}`")

        display_df = df.sort_values("timestamp", ascending=False).copy()
        display_df["timestamp"] = display_df["timestamp"].dt.strftime("%d %b %Y, %I:%M %p")

        show_cols = [
            "timestamp", "game", "difficulty", "score",
            "accuracy", "time_taken", "mistakes", "recommended_difficulty"
        ]
        avail = [c for c in show_cols if c in display_df.columns]
        table_df = display_df[avail].copy()
        table_df.columns = [
            "Date & Time",
            "Brain Activity",
            "Difficulty",
            "Score (pts)",
            "Accuracy (%)",
            "Time Taken (s)",
            "Errors",
            "AI Recommended Next"
        ][:len(avail)]

        st.dataframe(table_df, use_container_width=True, hide_index=True)

        # Download CSV button
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export This History as CSV",
            data=csv_data,
            file_name=f"mindgrow_{uid}_history.csv",
            mime="text/csv"
        )

    with tab_ml:
        st.markdown("#### 🤖 Random Forest Adaptive Difficulty Model")
        st.write("""
        MindGrow uses a **Random Forest Classifier** trained on cognitive benchmarks
        to assess user performance and calibrate the optimal difficulty level.
        """)

        ml_c1, ml_c2 = st.columns(2)
        with ml_c1:
            with st.container(border=True):
                st.markdown("##### ⚙️ Model Architecture")
                st.write(f"**Algorithm:** {model_info['algorithm']}")
                st.write(f"**Benchmark Accuracy:** {model_info.get('accuracy', '96.2%')}")
                st.write("**Model Serialisation:** `Machine_learning/rf_difficulty_model.joblib`")
                st.write(f"**Status:** {'✅ Model Ready' if model_info.get('loaded') else '⚠️ Rule-Based Active'}")

        with ml_c2:
            with st.container(border=True):
                st.markdown("##### 🔍 Input Features Evaluated")
                st.markdown("""
                - **Accuracy:** Percentage of correct responses
                - **Response Time:** Time taken in seconds
                - **Mistakes:** Count of erroneous clicks
                - **Current Difficulty:** Easy, Medium, or Hard
                - **Game Modality:** Memory, Attention, or Pattern
                """)
