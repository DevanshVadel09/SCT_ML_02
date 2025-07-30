import streamlit as st
import numpy as np
import joblib
import os

# Page configuration
st.set_page_config(page_title="🧠 Customer Segmentation", layout="centered", page_icon="🧠")

# ---------- CSS Styling ----------
custom_css = """
<style>
body {
    background-color: #111827;
    color: white;
}
h1, h2, h3, h4 {
    color: #FACC15;
}
.stSlider > div > div {
    background: #1F2937 !important;
}
.stSelectbox > div > div {
    background-color: #1F2937 !important;
}
.stButton > button {
    background-color: #FACC15;
    color: #000;
    font-weight: bold;
    border-radius: 8px;
    padding: 8px 16px;
}
.stButton > button:hover {
    background-color: #FFD60A;
    color: #000;
}
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------- Load Model ----------
@st.cache_resource
def load_model():
    model_path = "customer_segmentation_model.pkl"
    try:
        if not os.path.exists(model_path):
            st.error("❌ Model file not found. Please train and save your model first.")
            return None
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None

model_data = load_model()

# ---------- App Title ----------
st.markdown("<h1 style='text-align:center;'>🧠 Customer Segmentation Predictor</h1>", unsafe_allow_html=True)

if model_data:
    try:
        model = model_data.get('model')
        scaler = model_data.get('scaler')
        feature_names = model_data.get('feature_names', [])
        optimal_k = model_data.get('optimal_k', 0)

        if model is None or scaler is None:
            st.error("⚠️ Model or scaler object is missing inside the pickle file.")
            st.stop()

        # ---------- User Inputs ----------
        st.markdown("### 👤 Enter Customer Details Below:")

        gender = st.selectbox("Select Gender", ["Male", "Female"])
        age = st.slider("Age", min_value=18, max_value=80, value=30)
        annual_income = st.slider("Annual Income (in k$)", min_value=10, max_value=150, value=60)
        spending_score = st.slider("Spending Score (1 to 100)", min_value=1, max_value=100, value=50)

        gender_num = 1 if gender == "Male" else 0
        input_data = np.array([gender_num, age, annual_income, spending_score])

        # ---------- Prediction ----------
        if st.button("🔍 Predict Customer Segment"):
            try:
                input_scaled = scaler.transform([input_data])
                cluster = model.predict(input_scaled)[0]
                distances = model.transform(input_scaled)[0]
                confidence = max(distances) / sum(distances)

                # ---------- Output ----------
                st.success(f"🎯 Predicted Segment: Cluster {cluster}")
                st.info(f"📈 Confidence Score: {confidence:.2%}")
                st.markdown("### 🔬 Distance to Cluster Centers:")
                for i, dist in enumerate(distances):
                    st.markdown(f"- 🌀 Cluster {i}: `{dist:.4f}`")

            except Exception as e:
                st.error(f"❌ Prediction Error: {e}")

    except Exception as e:
        st.error(f"❌ Unexpected Error: {e}")
else:
    st.stop()
