import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo SVC desde el archivo pkl
best_svc_model = joblib.load('SVC_best_model.pkl')

# Titulo de la aplicación
st.title("Early Diabetes risk")

# Sección de entrada de características
st.header("Ingrese las características")

# Crea una entrada de texto para cada característica (asegúrate de que coincidan con las columnas de tus datos)
age = st.number_input("Age",  min_value=1.0)
gender = st.selectbox("Gender: ",['Male', 'Female'])
polyuria = st.selectbox("Polyuria: ",['Yes', 'No'])
polydipsia = st.selectbox("Polydipsia: ",['Yes', 'No'])
weight = st.selectbox("sudden weight loss: ",['Yes', 'No'])
weakness = st.selectbox("weakness: ",['Yes', 'No'])
polyphagia = st.selectbox("Polyphagia: ",['Yes', 'No'])
thrush = st.selectbox("Genital thrush: ",['Yes', 'No'])
visual = st.selectbox("visual blurring: ",['Yes', 'No'])
itching = st.selectbox("Itching: ",['Yes', 'No'])
irritability = st.selectbox("Irritability: ",['Yes', 'No'])
healing = st.selectbox("delayed healing: ",['Yes', 'No'])
paresis = st.selectbox("partial paresis: ",['Yes', 'No'])
muscle = st.selectbox("muscle stiffness: ",['Yes', 'No'])
alopecia = st.selectbox("Alopecia: ",['Yes', 'No'])
obesity = st.selectbox("Obesity: ",['Yes', 'No'])


# Botón de predicción
if st.button("Prediction"):
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Polyuria': [polyuria],
        'Polydipsia': [polydipsia],
        'sudden weight loss': [weight],
        'weakness': [weakness],
        'Polyphagia': [polyphagia],
        'Genital thrush': [thrush],
        'visual blurring': [visual],
        'Itching': [itching],
        'Irritability': [irritability],
        'delayed healing': [healing],
        'partial paresis': [paresis],
        'muscle stiffness': [muscle],
        'Alopecia': [alopecia],
        'Obesity': [obesity]
    })

    # Realiza la predicción
    prediction = best_svc_model.predict(input_data)
    
    # Muestra la predicción al usuario
    st.subheader("Resultado de la Predicción")
    st.write(f"Usted dio: {prediction[0]} para Diabetes")
