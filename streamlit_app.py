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

        if str(res[0].names[label[0]].title()) == 'Brown Rust':
            st.write('''Brown rust tends to develops in late summer and results in a significant loss of green leaf area and, hence, yield and specific weight.''')
            st.markdown('''Causes:
            - Caused by the fungus Puccinia triticina.''')
            st.markdown('''Preventions:
            - Plant resistant wheat varieties. 
            - Apply fungicides as a preventive measure.''')
            st.markdown('''Remedies:
            - Use fungicides when the disease is detected early.
            - Remove and destroy infected plant debris.''')

        if str(res[0].names[label[0]].title()) == 'Mite':
            st.write('''Mites are tiny, reddish-brown to black, eight-legged arachnids that infest wheat crops, particularly in hot, dry conditions. 
            They spread via wind, machinery, and infected plant material.''')
            st.markdown('''Causes:
            - Mites infest wheat plants, sucking sap and transmitting viruses.''')
            st.markdown('''Preventions:
            - Use mite-resistant wheat varieties.
            - Apply miticides if necessary.
            - Proper irrigation can help reduce the risk of infestation.''')
            st.markdown('''Remedies:
            - Apply appropriate miticides.
            - Maintain proper field hygiene.''')

        if str(res[0].names[label[0]].title()) == 'Stem Fly':
            st.write('''The wheat stem sawfly (Cephus cinctus) is a primitive, wasp-like insect from the family Cephidae in the order Hymenoptera (i.e. bees, wasps, and ants). 
            Its larvae are significant pests of spring and winter wheat, leading to reduced quality and yield of the crops.''')
            st.markdown('''Causes:
            - Stem flies lay eggs on wheat plants, and larvae burrow into stems.''')
            st.markdown('''Preventions:
            - Plant early to avoid peak stem fly activity.
            - Use insecticides as a preventive measure.''')
            st.markdown('''Remedies:
            - Apply insecticides at the larval stage.
            - Remove and destroy infested plants.''')

        if str(res[0].names[label[0]].title()) == 'Black Rust':
            st.write('''Black Rust affects the stems and leaves of wheat plants, causing significant yield losses and economic damage. 
            It produces black or dark brown raised pustules containing rust-colored spores. If not controlled, it can quickly spread and devastate entire fields.''')
            st.markdown('''Causes:
            - Caused by the fungus Puccinia graminis.''')
            st.markdown('''Preventions:
            - Plant resistant wheat varieties.
            - Use fungicides preventively.''')
            st.markdown('''Remedies:
            - Apply fungicides when symptoms appear.
            - Destroy infected plant debris.''')

        if str(res[0].names[label[0]].title()) == 'Common Root Rot':
            st.write('''Wheat root rots are caused by various fungi that invade the roots and crown tissue of wheat plants. 
            Infected plants have destroyed crown and root tissues, resulting in halted water and nutrient uptake.''')
            st.markdown('''Causes:
            - Caused by fungi such as Bipolaris sorokiniana.''')
            st.markdown('''Preventions:
            - Use disease-free seeds.
            - Implement crop rotation with non-host crops.''')
            st.markdown('''Remedies:
            - Apply appropriate fungicides.
            - Improve soil drainage.''')

        if str(res[0].names[label[0]].title()) == 'Leaf Blight':
            st.write('''Reddish brown oval spots appear on young seedlings with bright yellow margins. In severe cases, several spots coalesce to cause drying of leaves.''')
            st.markdown('''Causes:
            - Caused by fungi such as Bipolaris and Alternaria species.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Use fungicides preventively.''')
            st.markdown('''Remedies:
            - Apply fungicides at the onset of symptoms.
            - Remove and destroy infected plant residues.''')

        if str(res[0].names[label[0]].title()) == 'Septoria':
            st.write('''Septoria tritici blotch survives on stubble between seasons. 
            In late autumn and early winter, rain or heavy dew triggers the release of wind-borne ascospores from perithecia in the stubble, allowing the disease to spread over large distances.''')
            st.markdown('''Causes:
            - Caused by the fungus Septoria tritici.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Use fungicides preventively.''')
            st.markdown('''Remedies:
            - Apply fungicides when symptoms appear.
            - Remove and destroy infected leaves.''')

        if str(res[0].names[label[0]].title()) == 'Tan Spot':
            st.write('''Tan spot, also known as yellow leaf spot, is an economically significant disease in wheat grown in the U.S. and Canada. 
            It initially appears as small, brown spots on the leaves of susceptible wheat varieties.''')
            st.markdown('''Causes:
            - Caused by the fungus Pyrenophora tritici-repentis.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Use crop rotation and clean seed.''')
            st.markdown('''Remedies:
            - Apply fungicides at early signs of infection.
            - Remove and destroy infected plant debris.''')

        if str(res[0].names[label[0]].title()) == 'Blast':
            st.write('''Wheat blast is a devastating disease that emerged in Brazil in the 1980s and has since spread to nearby and distant countries. 
            Climate change is expected to facilitate its spread, particularly in tropical regions.''')
            st.markdown('''Causes:
            - Caused by the fungus Magnaporthe oryzae.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Avoid excessive nitrogen fertilization.''')
            st.markdown('''Remedies:
            - Apply fungicides at the first sign of symptoms.
            - Practice crop rotation.''')

        if str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
            st.write('''Fusarium Head Blight is a severe fungal disease leading to contaminated grain with mycotoxins. 
            It results in reduced yield, poor grain quality, and significant economic losses for wheat producers.''')
            st.markdown('''Causes:
            - Caused by fungi of the Fusarium species.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Use crop rotation and clean seed.''')
            st.markdown('''Remedies:
            - Apply fungicides at the flowering stage.
            - Avoid planting in fields with high Fusarium pressure.''')

        if str(res[0].names[label[0]].title()) == 'Mildew':
            st.write('''Powdery mildew in wheat begins as surface patches of white mycelium and can eventually cover the entire leaf, with mature infections showing black spore cases. 
            This wind-borne disease thrives in cool, wet weather and can cause yield losses of up to 40%.''')
            st.markdown('''Causes:
            - Caused by the fungus Blumeria graminis.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Apply fungicides preventively.''')
            st.markdown('''Remedies:
            - Apply fungicides when symptoms appear.
            - Ensure good air circulation in the field.''')

        if str(res[0].names[label[0]].title()) == 'Smut':
            st.write('''Loose smut has a wide distribution and can occur anywhere wheat is produced. 
            Mild symptoms may be present prior to heading, including yellowish leaf streaks and stiff, dark green leaves.''')
            st.markdown('''Causes:
            - Caused by fungi like the Ustilago species.''')
            st.markdown('''Preventions:
            - Use smut-resistant varieties.
            - Treat seeds with fungicides before planting.''')
            st.markdown('''Remedies:
            - Destroy infected plants.
            - Use appropriate fungicides.''')

        if str(res[0].names[label[0]].title()) == 'Yellow Rust':
            st.write('''The characteristic symptom of yellow rust is of parallel rows of yellowish orange coloured pustules on the leaves of adult plants. 
            Epidemics of yellow rust often start as individual plants, usually in the autumn.''')
            st.markdown('''Causes:
            - Caused by the fungus Puccinia striiformis.''')
            st.markdown('''Preventions:
            - Plant resistant varieties.
            - Apply fungicides preventively.''')
            st.markdown('''Remedies:
            - Apply fungicides when symptoms appear.
            - Remove and destroy infected plant debris.''')


