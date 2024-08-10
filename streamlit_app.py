from ultralytics import YOLO
import streamlit as st
from PIL import Image
import streamlit_analytics


with streamlit_analytics.track():
	st.markdown('''
    	<style>
    	.st-emotion-cache-1jzia57.e1nzilvr2 #danger-zone
    	{
        display: none;
    	}
    	.st-emotion-cache-p5msec.eqpbllx1
    	{
        display: none;
    	}
    	</style>
    	''',unsafe_allow_html=True)

	st.set_page_config(layout="wide")
	
	def set_language():
	    if f"selected_language" in st.session_state:
	        lang = st.session_state[f"selected_language"]
	        # st.experimental_set_query_params(**{f"lang": lang})
	        return lang
	    return "English"
	
	languages = ["English", "Punjabi", "Hindi"]
	sel_lang = st.radio(
		"Language",
		options=languages,
		horizontal=True,
		key="selected_language",
	)
	selected_language = set_language()
	
	st.markdown(f"Selected Language: {selected_language}")
	
	# Logo and title section
	with st.container():
	    col = st.columns([3,9])
	    col[0].image('logo.png')
	    col[1].text('')
	    col[1].text('')
	    col[1].text('')
	    col[1].text('')
	    col[1].markdown("<h1 style='text-align: center; color: white;'>WheatCheck - Wheat Disease Detection</h1>", unsafe_allow_html=True)
	
	if selected_language == "English":
	    # About the app section
	    with st.container():
	        st.header('About the App')
	        st.write('''
		Wheat is a majorWheat suffers from numerous diseases caused by various pathogens and pests, 
	        resulting in annual losses equivalent to 21.5% of global wheat production, totaling 209 million tonnes valued at $31 billion.
	        This Wheat Disease Detection App aims to identify diseases affecting wheat crops and provides 
	        recommendations for treatment.
	        ''')
	
	elif selected_language == "Hindi":
	    # About the app section
	    with st.container():
	        st.header('About the App')
	        st.write('''
	            This Wheat Disease Detection App aims to identify diseases affecting wheat crops and provides 
	            recommendations for treatment. Wheat suffers from numerous diseases caused by various pathogens and pests, 
	            resulting in annual losses equivalent to 21.5% of global wheat production, totaling 209 million tonnes valued at $31 billion.
	        ''')
	
	elif selected_language == "Punjabi":
	    # About the app section
	    with st.container():
	        st.header('About the App')
	        st.write('''
	            This Wheat Disease Detection App aims to identify diseases affecting wheat crops and provides 
	            recommendations for treatment. Wheat suffers from numerous diseases caused by various pathogens and pests, 
	            resulting in annual losses equivalent to 21.5% of global wheat production, totaling 209 million tonnes valued at $31 billion.
	        ''')
	    
	# Display disease images with captions
	col = st.columns(7)
	with col[0]:
		st.image('aphid_1.jpeg', caption='Aphid')
	with col[1]:
	        st.image('brown_rust_3.jpeg', caption='Brown Rust')
	with col[2]:
		st.image('mite_26.jpeg', caption='Mite')
	with col[3]:
	        st.image('stem_fly_30.jpeg', caption='Stem Fly')
	with col[4]:
	        st.image('black_rust_1.jpeg', caption='Black Rust')
	with col[5]:
	        st.image('common_root_rot_55.jpeg', caption='Common Root Rot')
	with col[6]:
	        st.image('leaf_blight_38.jpeg', caption='Leaf Blight')
		
	col1 = st.columns(7)
	with col1[0]:
	        st.image('septoria_5.jpeg.png', caption='Septoria')
	with col1[1]:
	        st.image('tan_spot_24.jpeg', caption='Tan Spot')
	with col1[2]:
	        st.image('blast_1.jpeg', caption='Blast')
	with col1[3]:
	        st.image('fusarium_head_blight_test_0.png', caption='Fusarium Head Blight')
	with col1[4]:
	        st.image('mildew_82.png', caption='Mildew')
	with col1[5]:
	        st.image('smut_test_0.png', caption='Smut')
	with col1[6]:
	        st.image('yellow_rust_256.png', caption='Yellow Rust')
	        
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
	            \n- Aphids infest wheat plants by sucking sap, leading to reduced yield.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant wheat varieties.
	            \n- Use insecticidal soaps or neem oil.
	            \n- Encourage natural predators like ladybugs.''')
	            st.markdown('''Remedies:
	            \n- Apply insecticides if infestations are severe.
	            \n- Use cultural practices like crop rotation to disrupt aphid life cycles.''')
	
	        if str(res[0].names[label[0]].title()) == 'Brown Rust':
	            st.write('''Brown rust tends to develops in late summer and results in a significant loss of green leaf area and, hence, yield and specific weight.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Puccinia triticina.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant wheat varieties. 
	            \n- Apply fungicides as a preventive measure.''')
	            st.markdown('''Remedies:
	            \n- Use fungicides when the disease is detected early.
	            \n- Remove and destroy infected plant debris.''')
	
	        if str(res[0].names[label[0]].title()) == 'Mite':
	            st.write('''Mites are tiny, reddish-brown to black, eight-legged arachnids that infest wheat crops, particularly in hot, dry conditions. 
	            They spread via wind, machinery, and infected plant material.''')
	            st.markdown('''Causes:
	            \n- Mites infest wheat plants, sucking sap and transmitting viruses.''')
	            st.markdown('''Preventions:
	            \n- Use mite-resistant wheat varieties.
	            \n- Apply miticides if necessary.
	            \n- Proper irrigation can help reduce the risk of infestation.''')
	            st.markdown('''Remedies:
	            \n- Apply appropriate miticides.
	            \n- Maintain proper field hygiene.''')
	
	        if str(res[0].names[label[0]].title()) == 'Stem Fly':
	            st.write('''The wheat stem sawfly (Cephus cinctus) is a primitive, wasp-like insect from the family Cephidae in the order Hymenoptera (i.e. bees, wasps, and ants). 
	            Its larvae are significant pests of spring and winter wheat, leading to reduced quality and yield of the crops.''')
	            st.markdown('''Causes:
	            \n- Stem flies lay eggs on wheat plants, and larvae burrow into stems.''')
	            st.markdown('''Preventions:
	            \n- Plant early to avoid peak stem fly activity.
	            \n- Use insecticides as a preventive measure.''')
	            st.markdown('''Remedies:
	            \n- Apply insecticides at the larval stage.
	            \n- Remove and destroy infested plants.''')
	
	        if str(res[0].names[label[0]].title()) == 'Black Rust':
	            st.write('''Black Rust affects the stems and leaves of wheat plants, causing significant yield losses and economic damage. 
	            It produces black or dark brown raised pustules containing rust-colored spores. If not controlled, it can quickly spread and devastate entire fields.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Puccinia graminis.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant wheat varieties.
	            \n- Use fungicides preventively.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides when symptoms appear.
	            \n- Destroy infected plant debris.''')
	
	        if str(res[0].names[label[0]].title()) == 'Common Root Rot':
	            st.write('''Wheat root rots are caused by various fungi that invade the roots and crown tissue of wheat plants. 
	            Infected plants have destroyed crown and root tissues, resulting in halted water and nutrient uptake.''')
	            st.markdown('''Causes:
	            \n- Caused by fungi such as Bipolaris sorokiniana.''')
	            st.markdown('''Preventions:
	            \n- Use disease-free seeds.
	            \n- Implement crop rotation with non-host crops.''')
	            st.markdown('''Remedies:
	            \n- Apply appropriate fungicides.
	            \n- Improve soil drainage.''')
	
	        if str(res[0].names[label[0]].title()) == 'Leaf Blight':
	            st.write('''Reddish brown oval spots appear on young seedlings with bright yellow margins. In severe cases, several spots coalesce to cause drying of leaves.''')
	            st.markdown('''Causes:
	            \n- Caused by fungi such as Bipolaris and Alternaria species.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Use fungicides preventively.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides at the onset of symptoms.
	            \n- Remove and destroy infected plant residues.''')
	
	        if str(res[0].names[label[0]].title()) == 'Septoria':
	            st.write('''Septoria tritici blotch survives on stubble between seasons. 
	            In late autumn and early winter, rain or heavy dew triggers the release of wind-borne ascospores from perithecia in the stubble, allowing the disease to spread over large distances.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Septoria tritici.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Use fungicides preventively.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides when symptoms appear.
	            \n- Remove and destroy infected leaves.''')
	
	        if str(res[0].names[label[0]].title()) == 'Tan Spot':
	            st.write('''Tan spot, also known as yellow leaf spot, is an economically significant disease in wheat grown in the U.S. and Canada. 
	            It initially appears as small, brown spots on the leaves of susceptible wheat varieties.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Pyrenophora tritici-repentis.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Use crop rotation and clean seed.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides at early signs of infection.
	            \n- Remove and destroy infected plant debris.''')
	
	        if str(res[0].names[label[0]].title()) == 'Blast':
	            st.write('''Wheat blast is a devastating disease that emerged in Brazil in the 1980s and has since spread to nearby and distant countries. 
	            Climate change is expected to facilitate its spread, particularly in tropical regions.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Magnaporthe oryzae.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Avoid excessive nitrogen fertilization.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides at the first sign of symptoms.
	            \n- Practice crop rotation.''')
	
	        if str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
	            st.write('''Fusarium Head Blight is a severe fungal disease leading to contaminated grain with mycotoxins. 
	            It results in reduced yield, poor grain quality, and significant economic losses for wheat producers.''')
	            st.markdown('''Causes:
	            \n- Caused by fungi of the Fusarium species.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Use crop rotation and clean seed.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides at the flowering stage.
	            \n- Avoid planting in fields with high Fusarium pressure.''')
	
	        if str(res[0].names[label[0]].title()) == 'Mildew':
	            st.write('''Powdery mildew in wheat begins as surface patches of white mycelium and can eventually cover the entire leaf, with mature infections showing black spore cases. 
	            This wind-borne disease thrives in cool, wet weather and can cause yield losses of up to 40%.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Blumeria graminis.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Apply fungicides preventively.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides when symptoms appear.
	            \n- Ensure good air circulation in the field.''')
	
	        if str(res[0].names[label[0]].title()) == 'Smut':
	            st.write('''Loose smut has a wide distribution and can occur anywhere wheat is produced. 
	            Mild symptoms may be present prior to heading, including yellowish leaf streaks and stiff, dark green leaves.''')
	            st.markdown('''Causes:
	            \n- Caused by fungi like the Ustilago species.''')
	            st.markdown('''Preventions:
	            \n- Use smut-resistant varieties.
	            \n- Treat seeds with fungicides before planting.''')
	            st.markdown('''Remedies:
	            \n- Destroy infected plants.
	            \n- Use appropriate fungicides.''')
	
	        if str(res[0].names[label[0]].title()) == 'Yellow Rust':
	            st.write('''The characteristic symptom of yellow rust is of parallel rows of yellowish orange coloured pustules on the leaves of adult plants. 
	            Epidemics of yellow rust often start as individual plants, usually in the autumn.''')
	            st.markdown('''Causes:
	            \n- Caused by the fungus Puccinia striiformis.''')
	            st.markdown('''Preventions:
	            \n- Plant resistant varieties.
	            \n- Apply fungicides preventively.''')
	            st.markdown('''Remedies:
	            \n- Apply fungicides when symptoms appear.
	            \n- Remove and destroy infected plant debris.''')
