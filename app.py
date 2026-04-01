# import streamlit as st
# st.title("My App")
# st.write("Hello, World!")

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Student Score Predictor", layout="wide")

# -------------------------------
# Load dataset
# -------------------------------
data = pd.read_csv("student_scores.csv")

X = data[['Hours']].values
y = data['Scores'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# HEADER
# -------------------------------
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🎓 Student Score Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Predict student performance using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------------
# LAYOUT (2 COLUMNS)
# -------------------------------
col1, col2 = st.columns([1, 2])

# -------------------------------
# LEFT PANEL (INPUT)
# -------------------------------
with col1:
    st.subheader(" Input")

    hours = st.slider("Study Hours", 0.0, 10.0, 2.0)

    predict_btn = st.button(" Predict Score")

    st.divider()

    if st.checkbox(" Show Dataset"):
        st.dataframe(data)

    if st.checkbox(" Show Model Accuracy"):
        score = model.score(X_test, y_test)
        st.metric("R² Score", f"{score:.2f}")

# -------------------------------
# RIGHT PANEL (OUTPUT)
# -------------------------------
with col2:
    st.subheader(" Output")

    if predict_btn:
        prediction = model.predict([[hours]])
        
        st.success(f" Predicted Score: {prediction[0]:.2f}")
        
        st.progress(min(int(prediction[0]), 100))
	
        if prediction[0] > 80:
        	st.balloons()
        	st.success("Excellent performance!")
        elif prediction[0] > 50:
        	st.info("Good job! 👍")
        else:
        	st.warning("Needs improvement")

    st.divider()

    st.subheader(" Model Visualization")

    fig, ax = plt.subplots(figsize=(6,3))

    # Plot training & test data
    ax.scatter(X_train, y_train, label="Training Data")
    ax.scatter(X_test, y_test, label="Test Data")

    # Plot regression line
    ax.plot(X, model.predict(X), label="Regression Line")

    # -------------------------------
    # Highlight user input
    # -------------------------------
    if predict_btn:
        user_pred = model.predict([[hours]])
    
        ax.scatter(hours, user_pred, 
               s=120, 
               marker='o', 
               label="Your Input",
               edgecolors='black')
    
        ax.annotate(f"({hours}, {user_pred[0]:.1f})",
                (hours, user_pred),
                textcoords="offset points",
                xytext=(10,10))

    # Labels
    ax.set_xlabel("Hours Studied")
    ax.set_ylabel("Scores")
    ax.legend()

    st.pyplot(fig)