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
st.write("Gender")
gender = st.selectbox("Gender: ",['Male', 'Female'])
st.write("Polyuria")
polyuria = st.selectbox("Polyuria: ",['Yes', 'No'])
st.write("Polydipsia")
polydipsia = st.selectbox("Polydipsia: ",['Yes', 'No'])
st.write("sudden weight loss")
weight = st.selectbox("sudden weight loss: ",['Yes', 'No'])
st.write("weakness")
weakness = st.selectbox("weakness: ",['Yes', 'No'])
st.write("Polyphagia")
polyphagia = st.selectbox("Polyphagia: ",['Yes', 'No'])
st.write("Genital thrush")
thrush = st.selectbox("Genital thrush: ",['Yes', 'No'])
st.write("visual blurring")
visual = st.selectbox("visual blurring: ",['Yes', 'No'])
st.write("Itching")
itching = st.selectbox("Itching: ",['Yes', 'No'])
st.write("Irritability")
irritability = st.selectbox("Irritability: ",['Yes', 'No'])
st.write("delayed healing")
healing = st.selectbox("delayed healing: ",['Yes', 'No'])
st.write("partial paresis")
paresis = st.selectbox("partial paresis: ",['Yes', 'No'])
st.write("muscle stiffness")
muscle = st.selectbox("muscle stiffness: ",['Yes', 'No'])
st.write("Alopecia")
alopecia = st.selectbox("Alopecia: ",['Yes', 'No'])
st.write("Obesity")
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
        'Obecity': [obesity]
    })

    # Realiza la predicción
    prediction = best_svc_model.predict(input_data)
    
    # Muestra la predicción al usuario
    st.subheader("Resultado de la Predicción")
    st.write(f"Usted dio: {prediction[0]} para Diabetes")
