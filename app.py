import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Imaginador IA 🧠💪✝️", page_icon="🧠")

st.title("Imaginador IA 🧠💪✝️")
st.markdown("""
<div style="text-align: center; margin-bottom: 2.5rem;">
    <b>
    <span style='font-size:1.3em; color:#2b7de9;'>Generador de Imágenes Educativas por IA</span><br><br>
    Escribe una descripción detallada y genera imágenes impactantes, coloridas y únicas para tus proyectos académicos.<br><br>
    Powered by DeepAI | Desarrollado por Pedro Tovar.
    </b>
</div>
""", unsafe_allow_html=True)

st.header("Crea tu imagen educativa")

prompt_img = st.text_area("Describe la imagen que quieres generar (sé específico, usa detalles, colores, estilo, etc.):", height=80)

if st.button("Generar imagen IA"):
    if prompt_img.strip():
        with st.spinner("Generando imagen..."):
            url = "https://api.deepai.org/api/text2img"
            api_key = "a066da1d-287b-49f3-ab6c-411dfd39d24b"  # Tu API Key de DeepAI
            try:
                response = requests.post(
                    url,
                    data={'text': prompt_img},
                    headers={'api-key': api_key}
                )
                img_url = response.json().get("output_url")
                if img_url:
                    img_data = requests.get(img_url).content
                    image = Image.open(BytesIO(img_data))
                    st.image(image, caption="Imagen generada por IA", use_column_width=True)
                else:
                    st.warning("No se pudo generar la imagen. Intenta con otra descripción o sé más específico.")
            except Exception as e:
                st.error(f"Error al generar imagen: {e}")
    else:
        st.warning("Por favor, escribe una descripción para la imagen.")

st.markdown("""
---
**© 2025 Pedro Tovar. Todos los derechos reservados.**  
Esta aplicación fue desarrollada por Pedro Tovar para fines académicos. Prohibida su reproducción total o parcial sin autorización.
""")
