
import streamlit as st


def show_about():

    st.markdown("""
    <style>
    .about-hero {
        background: linear-gradient(115deg, #21113F, #54209A, #7928CA);
        border: 2px solid #00CFFF;
        border-radius: 25px;
        padding: 42px 38px;
        color: white;
        margin-bottom: 32px;
        box-shadow: 0 12px 30px rgba(65, 25, 120, 0.18);
    }

    .about-tag {
        display: inline-block;
        background: #FFD166;
        color: #24133F;
        padding: 7px 15px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }

    .about-hero h1 {
        color: white !important;
        font-size: 38px;
        font-weight: 900;
        margin: 5px 0 12px 0;
    }

    .about-hero p {
        color: #F2EAFE !important;
        font-size: 18px;
        line-height: 1.7;
        max-width: 850px;
    }

    .about-section-title {
        color: #281344;
        font-size: 25px;
        font-weight: 900;
        margin: 30px 0 18px 0;
    }

    .about-intro {
        color: #35264B;
        font-size: 17px;
        line-height: 1.8;
        margin-bottom: 25px;
    }

    .feature-card {
        background: #FFFFFF;
        border: 2px solid #E2D5F5;
        border-radius: 19px;
        padding: 22px;
        min-height: 175px;
        box-shadow: 0 7px 20px rgba(45, 20, 75, 0.07);
        transition: 0.2s ease;
        margin-bottom: 15px;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        border-color: #7928CA;
        box-shadow: 0 10px 25px rgba(121, 40, 202, 0.16);
    }

    .feature-icon {
        font-size: 30px;
        margin-bottom: 10px;
    }

    .feature-card h3 {
        color: #35145E !important;
        font-size: 19px;
        margin: 5px 0 9px 0;
        font-weight: 900;
    }

    .feature-card p {
        color: #514360 !important;
        font-size: 15px;
        line-height: 1.6;
        margin: 0;
    }

    .step-card {
        background: #25163F;
        border-radius: 17px;
        padding: 20px;
        color: white;
        min-height: 145px;
        margin-bottom: 12px;
        border-bottom: 5px solid #00D2FF;
    }

    .step-card h3 {
        color: #FFD166 !important;
        font-size: 19px;
        margin-bottom: 8px;
    }

    .step-card p {
        color: #F1EAFB !important;
        font-size: 14px;
        line-height: 1.6;
    }

    .about-footer {
        background: linear-gradient(110deg, #421778, #7928CA);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-top: 28px;
    }

    .about-footer h2 {
        color: white !important;
        font-size: 25px;
    }

    .about-footer p {
        color: #F4EAFE !important;
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION
    st.markdown("""
    <div class="about-hero">
        <div class="about-tag">WELCOME TO MINDGROW</div>
        <h1>Train Your Brain. Grow Every Day. 🧠</h1>
        <p>
            Discover a fun and engaging way to challenge your mind.
            MindGrow brings together interactive brain games,
            adaptive difficulty and personal progress tracking
            to make cognitive practice enjoyable.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # INTRODUCTION
    st.markdown("""
    <div class="about-section-title">
        ✨ Discover MindGrow
    </div>

    <div class="about-intro">
        MindGrow is an AI-based adaptive cognitive learning platform
        designed to make brain training simple, enjoyable and accessible.
        Through interactive activities, users can practise memory,
        attention and pattern recognition while tracking their
        performance over time.
    </div>
    """, unsafe_allow_html=True)

    # FEATURE CARDS
    st.markdown("""
    <div class="about-section-title">
        🚀 What You Can Explore
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎮</div>
            <h3>Interactive Brain Games</h3>
            <p>Explore Memory, Attention and Pattern games
            through fun and engaging challenges.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Progress Tracking</h3>
            <p>View your completed sessions, accuracy,
            scores and overall playing history.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3>Adaptive Difficulty</h3>
            <p>The learning system uses gameplay performance
            to help select suitable challenge levels.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">⭐</div>
            <h3>Personalised Experience</h3>
            <p>Individual learner profiles help keep
            game history and progress organised.</p>
        </div>
        """, unsafe_allow_html=True)

    # HOW IT WORKS
    st.markdown("""
    <div class="about-section-title">
        🎯 How MindGrow Works
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="step-card">
            <h3>01. Choose</h3>
            <p>Select a brain-training activity
            that you would like to play.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="step-card">
            <h3>02. Play</h3>
            <p>Complete challenges and let the
            system record your performance.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="step-card">
            <h3>03. Improve</h3>
            <p>Review your results and experience
            challenges suited to your performance.</p>
        </div>
        """, unsafe_allow_html=True)

    # FOOTER
    st.markdown("""
    <div class="about-footer">
        <h2>Ready to Challenge Your Mind? 🎮</h2>
        <p>
            Explore the games, track your progress
            and make every session count!
        </p>
    </div>
    """, unsafe_allow_html=True)
