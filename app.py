import pickle
import streamlit as st


# Load saved model
model = pickle.load(open('heart_model.sav', 'rb'))

# Title of the web app
st.title('Prediksi Penyakit Jantung')

# Options 
restecg_options = {
    0: "Normal",
    1: "Memiliki kelainan gelombang ST-T (inversi gelombang T dan/atau elevasi atau depresi ST > 0.05 mV)",
    2: "Menunjukkan hipertrofi ventrikel kiri yang mungkin atau pasti menurut kriteria Estes"

}


sex_options = {
    0: "Laki-laki",
    1: "Perempuan"
}


cp_options = {
    0: "typical angina",
    1: "atypical angina",
    2: "non-anginal pain",
    3: "asymptomatic"
}


fbs_options = {
    0: "<120",
    1: "120+"
}


exang_options = {
    0: "Tidak",
    1: "Ya"
}


slope_options = {
    0: "Upsloping",
    1: "flat",
    2: "Down Sloping"
}


thal_options = {
    0: "normal blood flow",
    1: "fixed defect",
    2: "reversible defect"
}


# Create columns for layout

col1, col2 = st.columns(2)


# Input fields

with col1:
    age = st.number_input('Umur', step=1, min_value=1)

with col2:
    sex = st.selectbox("Jenis Kelamin", list(sex_options.values()), format_func=lambda x: x)

with col1:
    cp = st.selectbox("Jenis Nyeri Dada", list(cp_options.values()), format_func=lambda x: x)

with col2:
    trestbps = st.number_input('Tekanan Darah (mm/HG)', step=1, min_value=0)

with col1:
    chol = st.number_input('Nilai Kolesterol (mg/dl)', step=1, min_value=1)

with col2:
    fbs = st.selectbox("Gula Darah", list(fbs_options.values()), format_func=lambda x: x)

with col1:
    restecg = st.selectbox('Hasil Elektrokardiografi', list(restecg_options.values()), format_func=lambda x: x)

with col2:
    thalach = st.number_input('Detak Jantung Maksimum', step=1, min_value=0)

with col1:
    exang = st.selectbox('Induksi Angina', list(exang_options.values()), format_func=lambda x: x)

with col2:
    oldpeak = st.number_input('ST Depression', format="%0.1f", step=0.1)

with col1:
    slope = st.selectbox('Slope', list(slope_options.values()), format_func=lambda x: x)

with col2:
    ca = st.number_input('Nilai CA', step=1, min_value=0, max_value=3)

with col1:
    thal = st.selectbox('Nilai Thal', list(thal_options.values()), format_func=lambda x: x)


# Code for prediction

heart_diagnosis = ''

# Create prediction button
if st.button('Prediksi Penyakit Jantung'):
    # Prepare input for the model
    heart_prediction = model.predict([[
        age,
        list(sex_options.keys())[list(sex_options.values()).index(sex)],  # Convert to numerical directly
        list(cp_options.keys())[list(cp_options.values()).index(cp)],  # Get numerical key for cp
        trestbps,
        chol,
        list(fbs_options.keys())[list(fbs_options.values()).index(fbs)],  # Get numerical key for fbs
        list(restecg_options.keys())[list(restecg_options.values()).index(restecg)],  # Get numerical key for restecg
        thalach,
        list(exang_options.keys())[list(exang_options.values()).index(exang)],  # Convert to numerical directly
        oldpeak,
        list(slope_options.keys())[list(slope_options.values()).index(slope)],  # Get numerical key for slope
        ca,
        list(thal_options.keys())[list(thal_options.values()).index(thal)]  # Get numerical key for thal
    ]])

    if (heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
        st.success(heart_diagnosis)
    else:
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        st.success(heart_diagnosis)


