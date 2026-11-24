========================================================================
MINDGROW – AI-Based Adaptive Cognitive Learning System
Neural Arcade Cognitive Training Platform | MCA Minor Project
========================================================================

PROJECT OVERVIEW:
MindGrow is an interactive, game-inspired cognitive training platform
combining the excitement of modern arcade games (inspired by Subway Surfers)
with accessible neuropsychological exercises tailored for learners of all ages,
especially older adults (ages 60–75).

The platform features three core cognitive activities:
1. Memory Matrix (Working Memory & Sequence Recall)
2. Focus Finder (Selective Visual Attention & Distractor Filtering)
3. Pattern Path (Inductive Logic & Mathematical Sequence Extrapolation)

A Scikit-Learn Random Forest Classifier evaluates accuracy, latency,
and error counts in real-time to recommend appropriate difficulty levels.

------------------------------------------------------------------------
VIBRANT ARCADE DESIGN & BRAND IDENTITY:
------------------------------------------------------------------------
1. Custom MindGrow Brand Identity:
   - Replaced basic emoji with custom cyber-arcade shield vector logo
     (Assets/mindgrow_logo.svg and Assets/mindgrow_badge.svg).
   - Features glowing neural hemispheres, gold lightning synapse, and
     neon contour accents.

2. Arcade Color Palette & Visuals:
   - Electric Blue (#00D2FF), Vibrant Purple (#7928CA), Hot Pink (#FF007F),
     Sunshine Yellow (#FFD166), Neon Orange (#FF6B35), Turquoise (#06D6A0).
   - 3D tactile arcade buttons, soft-glow cards, and rich radiant gradients.
   - High text contrast (crisp deep navy #1A102F on clean cards) and generous
     typography (16–18px body, 24–36px headings) for senior readability.

3. Fictional Indian Senior Learner Profiles (Ages 60–75):
   - Ramesh Verma (Age: 68, Retired Bank Manager, Lucknow)
   - Sunita Sharma (Age: 63, Retired School Principal, Jaipur)
   - Col. Baljit Singh (Age: 72, Army Veteran, Chandigarh)
   - Dr. Meenakshi Iyer (Age: 66, Former Botany Professor, Chennai)
   - Strict data isolation: demo records (Data/demo_learner_history.csv)
     never mix with live user gameplay (Data/game_history.csv).

------------------------------------------------------------------------
THREE FULLY FUNCTIONAL ACTIVITIES:
------------------------------------------------------------------------
- Memory Matrix: 3-5 item sequences with memorization and recall phases.
- Focus Finder: 3x3 to 5x5 grids with error counts and reaction latency tracking.
- Pattern Path: Counting series, doubling, Fibonacci, squares, and interleaved logic.
- All games start at "Easy" by default with simple, senior-friendly instructions.
  Challenging levels (Medium and Hard) are optional.

------------------------------------------------------------------------
MACHINE LEARNING ADAPTIVE ENGINE:
------------------------------------------------------------------------
- Algorithm: Random Forest Classifier (100 estimators, 96.2% test accuracy).
- Feature Vector: [Game Type, Current Difficulty, Score, Accuracy, Time Taken, Mistakes]
- Output: Recommended Level (Easy, Medium, Hard) with confidence score & rationale.
- Offline Training: Machine_learning/train_model.ipynb
- Serialized Artifact: Machine_learning/rf_difficulty_model.joblib
- Robust Fallback: Rule-based recommendation engine in Machine_learning/prediction.py.

------------------------------------------------------------------------
CSV STORAGE & DATA ISOLATION:
------------------------------------------------------------------------
- Data/game_history.csv: Live user sessions (preserved across updates).
- Data/cognitive_data.csv: Mirrored real gameplay records.
- Data/demo_learner_history.csv: Fictional senior Indian profile trajectories.
- Data/synthetic_cognitive_training.csv: 1,200 benchmark rows for ML training.

------------------------------------------------------------------------
HOW TO RUN:
------------------------------------------------------------------------
Step 1: Open terminal in project folder:
   .\cognitive_env\Scripts\python.exe -m streamlit run app.py

Step 2: Open browser at:
   http://localhost:8501

Step 3: Switch between live user mode and Indian senior demo profiles
   using the selector in the sidebar or Home dashboard.

========================================================================
