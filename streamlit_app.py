from ultralytics import YOLO
import streamlit as st
from PIL import Image

# Logo and title section
with st.container():
    col = st.columns([0.2, 0.8])
    col[0].image('logo.png')
    col[1].title('Wheat Disease Detection')

# About the app section
with st.container():
    st.header('About the App')
    st.write('''
        This Wheat Disease Detection App aims to identify diseases affecting wheat crops and provides 
        recommendations for treatment. Wheat suffers from numerous diseases caused by various pathogens and pests, 
        resulting in annual losses equivalent to 21.5% of global wheat production, totaling 209 million tonnes valued at $31 billion.
    ''')
    
    # Display disease images with captions
    col = st.columns(5)
    with col[0]:
        st.image('black_rust_1.jpeg', caption='Black Rust')
    with col[1]:
        st.image('blast_1.jpeg', caption='Blast')
    with col[2]:
        st.image('smut_test_0.png', caption='Smut')
    with col[3]:
        st.image('fusarium_head_blight_test_0.png', caption='Fusarium Head Blight')
    with col[4]:
        st.image('tan_spot_24.jpeg', caption='Tan Spot')
        
    col1 = st.columns(5)
    with col1[0]:
        st.image('black_rust_1.jpeg', caption='Black Rust')
    with col1[1]:
        st.image('blast_1.jpeg', caption='Blast')
    with col1[2]:
        st.image('smut_test_0.png', caption='Smut')
    with col1[3]:
        st.image('fusarium_head_blight_test_0.png', caption='Fusarium Head Blight')
    with col1[4]:
        st.image('tan_spot_24.jpeg', caption='Tan Spot')
        
    col2 = st.columns(5)
    with col2[0]:
        st.image('black_rust_1.jpeg', caption='Black Rust')
    with col2[1]:
        st.image('blast_1.jpeg', caption='Blast')
    with col2[2]:
        st.image('smut_test_0.png', caption='Smut')
    with col2[3]:
        st.image('fusarium_head_blight_test_0.png', caption='Fusarium Head Blight')
    with col2[4]:
        st.image('tan_spot_24.jpeg', caption='Tan Spot')
        
    st.write('''
        It imports ultralytics and uses the YOLOv8 model to train and test data. 
        YOLOv8 is an evolution in the YOLO (You Only Look Once) series of real-time detection models. 
        Its core functionality revolves around a single-stage detector that processes images in one pass through the network, making it highly efficient for real-time applications.
    ''')
    st.subheader('Steps to use the app')
    st.markdown('''
        - Take a clear image
        - Upload the image
        - Analyze the image and the name of the disease will be displayed in the result panel below
    ''')

# Load the model
@st.cache_resource
def models():
    mod = YOLO('best.pt')
    return mod

# Image upload and analysis section
with st.container():
    img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
    analyse = st.button('Analyze')
    
if analyse:
    if img is not None:
        img = Image.open(img)
        st.markdown('Image Visualization')
        st.image(img)
        st.subheader('This wheat crop has been affected by:')
        model = models()
        res = model.predict(img)
        label = res[0].probs.top5
        conf = res[0].probs.top5conf
        conf = conf.tolist()
        st.write('Disease: ' + str(res[0].names[label[0]].title()))
        st.write('Confidence level: ' + str(conf[0]))
        
        if str(res[0].names[label[0]].title()) == 'Aphid':
            st.write('''Aphids are a group of sap-sucking, soft-bodied insects that are about the size of a pinhead.''')
            st.markdown('''Causes:
            - Aphids infest wheat plants by sucking sap, leading to reduced yield.''')
            st.markdown('''Preventions:
            - Plant resistant wheat varieties.
            - Use insecticidal soaps or neem oil.
            - Encourage natural predators like ladybugs.''')
            st.markdown('''Remedies:
            - Apply insecticides if infestations are severe.
            - Use cultural practices like crop rotation to disrupt aphid life cycles.''')


