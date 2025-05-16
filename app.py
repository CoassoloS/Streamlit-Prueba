import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="App Streamlit Sencilla", page_icon="🎨")

# Título
st.title("¡Mi App Interactiva! 🌟")

# Widgets
nombre = st.text_input("Dime tu nombre:", "Anónimo")
color = st.color_picker("Elige tu color favorito", "#FF0000")

# Mensaje dinámico
if nombre:
    st.markdown(
        f"<h2 style='color:{color}'>¡Hola, {nombre}!</h2>", 
        unsafe_allow_html=True
    )
    st.success("¡Funciona correctamente! ✅")
else:
    st.warning("Por favor, ingresa tu nombre.")

# Botón con efecto
if st.button("¡Celebrar!"):
    st.balloons()
    st.snow()  # Efecto adicional de nieve ❄️