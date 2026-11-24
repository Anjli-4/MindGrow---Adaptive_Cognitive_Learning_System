# MindGrow – Adaptive Cognitive Learning System 🧠

## About MindGrow

MindGrow is a cognitive learning web application developed to make brain-training activities more interactive and engaging. It provides different games that allow users to practice and improve skills such as memory, attention and pattern recognition.

The project also includes a Machine Learning component that uses a Random Forest model to analyze game performance and recommend suitable difficulty levels. This makes the experience adaptive, as the difficulty recommendation is based on how the user performs.

## What does MindGrow offer?

- **Memory Game:** Practice memory and recall through interactive activities.
- **Attention Game:** Activities designed to practice focus and attention.
- **Pattern Game:** Improve pattern recognition through different challenges.
- **Performance Tracking:** Keep track of game scores and previous performance.
- **Difficulty Recommendation:** Uses a Random Forest model to suggest difficulty levels based on performance.
- **Dashboard:** Provides an overview of game activity and progress.

## Technologies Used

- Python
- Streamlit
- Machine Learning
- Random Forest Algorithm
- Pandas
- Scikit-learn
- CSV for data storage
- Jupyter Notebook for model development

## How the Machine Learning Part Works

MindGrow uses a Random Forest model to analyze game-related performance data. Based on the available performance information, the model predicts a suitable difficulty level for the user.

The model was developed and trained using Python in Jupyter Notebook and integrated into the main application using a saved model file.

## Project Structure

```text
MindGrow/
│
├── app.py
├── about.py
├── dashboard.py
├── games.py
├── progress.py
├── prediction.py
├── __init__.py
│
├── train_model.ipynb
├── rf_difficulty_model.joblib
│
├── data/
├── requirements.txt
└── README.md
```

## How to Run the Project

Follow these steps to run MindGrow on your system.

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd MindGrow
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

## Project Objective

The main aim of MindGrow is to provide a simple and interactive platform where users can play cognitive games, track their performance and receive difficulty recommendations through Machine Learning.

## Future Improvements

Some features that can be added in the future include:

- Adding more cognitive games and activities.
- Improving the accuracy of difficulty recommendations.
- Adding more detailed performance reports.
- Introducing additional personalization features.

---

**MindGrow – Play, Learn, Improve!** 🧠
