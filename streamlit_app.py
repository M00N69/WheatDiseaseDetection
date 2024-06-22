from ultralytics import YOLO
import streamlit as st

from PIL import Image

with st.container():
	col = st.columns([0.2,0.8])
	col[0].image('logo.png')
	col[1].title('Wheat Disease Detection')
	
with st.container(border=True):
        st.header('About the App')
        st.write('''This Wheat Disease Detection App identifies the disease in a wheat crop and suggests a cure.
        Wheat is attacked by many different diseases caused by various pathogens and pests.
        Around 21.5% of wheat production is lost to these diseases annually, totalling losses of 209 million tonnes worth $31 billion.''')
        col = st.columns(5)
        with col[0]:
                st.image('black_rust_1.jpeg')
                st.write('Black Rust')
        with col[1]:
                st.image('blast_1.jpeg')
                st.write('Blast')
        with col[2]:
                st.image('smut_test_0.png')
                st.write('Smut')
        with col[3]:
                st.image('fusarium_head_blight_test_0.png')
                st.write('Fusarium Head Blight')
        with col[4]:
                st.image('tan_spot_24.jpeg')
                st.write('Tan Spot')
                
        st.write('''It imports ultralytics and uses the YOLOv8 model to train and test data. 
	YOLOv8 is an evolution in the YOLO (You Only Look Once) series of real time detection model. 
 	Its core functionality revolves around a single-stage detector that processes images in one pass through the network, making it highly efficient for real-time applications.''')
        st.subheader('Steps to use the app')
        st.markdown('''
        - Take a clear image
        - Upload the image
        - Analyse the image and the name of the disease will be displayed in the result panel below''')
	
@st.cache_resource
def models():
	mod = YOLO('best.pt')
	return mod
	
with st.container():
        img = st.file_uploader('Upload your image',type=['jpg','png','jpeg'])
        analyse = st.button('Analyse')
	
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
		col1,col2 = st.columns(2)
		col1.write(res[0].names[label[0]].title() +' \n '+'Confidence level:'+ str(conf[0]))
		col2.write(res[0].names[label[1]].title() +' with '+ str(conf[1])+' Confidence')

      
