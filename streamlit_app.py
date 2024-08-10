from ultralytics import YOLO
import streamlit as st
from PIL import Image
import streamlit_analytics

st.set_page_config(layout="wide")

with streamlit_analytics.track():
	st.markdown('''
    	<style>
    	.st-emotion-cache-1jzia57.e1nzilvr2 #danger-zone
    	{
        display: none;
    	}
    	.st-emotion-cache-1r7h7mk.eqpbllx1
    	{
        display: none;
    	}
    	</style>
    	''',unsafe_allow_html=True)
	
	def set_language():
	    if f"selected_language" in st.session_state:
	        lang = st.session_state[f"selected_language"]
	        # st.experimental_set_query_params(**{f"lang": lang})
	        return lang
	    return "English"

	# Load the model
	@st.cache_resource
	def models():
	    mod = YOLO('best.pt')
	    return mod
	
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
	        st.header('Safeguarding Global Food Security')
	        st.write('''Wheat is one of the most vital crops for human consumption, feeding billions of people worldwide. 
  		However, this essential crop is under constant threat from a wide range of diseases caused by pathogens and pests. 
    		Every year, these threats result in significant losses—equivalent to 21.5% of global wheat production. 
      		This translates to an astonishing 209 million tonnes of wheat, valued at an estimated $31 billion, lost annually.''')
	        st.subheader('Understanding the Challenge')
	        st.write('''The challenge of wheat disease is multifaceted. Wheat crops are susceptible to various pathogens, including fungi, bacteria, viruses, and pests, 
  		each capable of devastating entire fields if not detected and managed early. 
    		Diseases like rusts, mildew, and blight, alongside pests like aphids and stem flies, can drastically reduce yield quality and quantity. 
      		The economic impact is profound, affecting not only farmers but also the global food supply chain, 
		leading to increased prices and food insecurity in vulnerable regions.''')
		
	elif selected_language == "Hindi":
	    # About the app section
	    with st.container():
	        st.header('वैश्विक खाद्य सुरक्षा की रक्षा करना')
	        st.write('''गेहूं मानव उपभोग के लिए सबसे महत्वपूर्ण फसलों में से एक है, जो दुनिया भर में अरबों लोगों का पेट भरता है। 
  		हालाँकि, यह आवश्यक फसल रोगजनकों और कीटों के कारण होने वाली विभिन्न प्रकार की बीमारियों से लगातार खतरे में है। 
    		हर साल, इन खतरों के परिणामस्वरूप महत्वपूर्ण नुकसान होता है - जो वैश्विक गेहूं उत्पादन के 21.5% के बराबर है। 
      		इसका मतलब है कि आश्चर्यजनक रूप से 209 मिलियन टन गेहूं, जिसकी अनुमानित कीमत 31 बिलियन डॉलर है, हर साल नष्ट हो जाता है।''')
	        st.subheader('चुनौती को समझना')
	        st.write('''गेहूं की बीमारी की चुनौती बहुआयामी है। गेहूं की फसलें कवक, बैक्टीरिया, वायरस और कीटों सहित विभिन्न रोगजनकों के प्रति संवेदनशील होती हैं। 
  		यदि शीघ्र पता नहीं लगाया गया और प्रबंधित नहीं किया गया तो प्रत्येक पूरे क्षेत्र को तबाह करने में सक्षम है। 
    		एफिड्स और तना मक्खियों जैसे कीटों के साथ-साथ जंग, फफूंदी और झुलसा जैसी बीमारियाँ उपज की गुणवत्ता और मात्रा को काफी कम कर सकती हैं। 
      		आर्थिक प्रभाव गहरा है, न केवल किसानों को बल्कि वैश्विक खाद्य आपूर्ति श्रृंखला को भी प्रभावित कर रहा है। 
		जिससे कमजोर क्षेत्रों में कीमतें बढ़ीं और खाद्य असुरक्षा पैदा हुई।''')
		    
	elif selected_language == "Punjabi":
	    # About the app section
	    with st.container():
	        st.header('ਗਲੋਬਲ ਭੋਜਨ ਸੁਰੱਖਿਆ ਦੀ ਸੁਰੱਖਿਆ')
	        st.write('''
	        ਕਣਕ ਮਨੁੱਖੀ ਖਪਤ ਲਈ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਫਸਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ, ਜੋ ਦੁਨੀਆ ਭਰ ਦੇ ਅਰਬਾਂ ਲੋਕਾਂ ਨੂੰ ਭੋਜਨ ਦਿੰਦੀ ਹੈ। 
  		ਹਾਲਾਂਕਿ, ਇਹ ਜ਼ਰੂਰੀ ਫਸਲ ਰੋਗਾਣੂਆਂ ਅਤੇ ਕੀੜਿਆਂ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਬਿਮਾਰੀਆਂ ਦੀ ਇੱਕ ਵਿਸ਼ਾਲ ਸ਼੍ਰੇਣੀ ਤੋਂ ਲਗਾਤਾਰ ਖਤਰੇ ਵਿੱਚ ਹੈ। 
    		ਹਰ ਸਾਲ, ਇਹਨਾਂ ਧਮਕੀਆਂ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ - ਵਿਸ਼ਵਵਿਆਪੀ ਕਣਕ ਉਤਪਾਦਨ ਦੇ 21.5% ਦੇ ਬਰਾਬਰ। 
      		ਇਹ ਇੱਕ ਹੈਰਾਨੀਜਨਕ 209 ਮਿਲੀਅਨ ਟਨ ਕਣਕ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਜਿਸਦੀ ਕੀਮਤ $31 ਬਿਲੀਅਨ ਹੈ, ਸਾਲਾਨਾ ਗੁਆਚ ਜਾਂਦੀ ਹੈ।''')
		st.subheader('ਚੁਣੌਤੀ ਨੂੰ ਸਮਝਣਾ')
		st.write('''ਕਣਕ ਦੀ ਬਿਮਾਰੀ ਦੀ ਚੁਣੌਤੀ ਬਹੁਪੱਖੀ ਹੈ। ਕਣਕ ਦੀ ਫ਼ਸਲ ਉੱਲੀ, ਬੈਕਟੀਰੀਆ, ਵਾਇਰਸ ਅਤੇ ਕੀੜਿਆਂ ਸਮੇਤ ਵੱਖ-ਵੱਖ ਜਰਾਸੀਮਾਂ ਲਈ ਸੰਵੇਦਨਸ਼ੀਲ ਹੁੰਦੀ ਹੈ, 
  		ਹਰ ਇੱਕ ਪੂਰੇ ਖੇਤਰ ਨੂੰ ਤਬਾਹ ਕਰਨ ਦੇ ਸਮਰੱਥ ਹੈ ਜੇਕਰ ਜਲਦੀ ਖੋਜਿਆ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਨਾ ਕੀਤਾ ਜਾਵੇ। 
    		ਕੀੜਿਆਂ ਜਿਵੇਂ ਕਿ ਐਫੀਡਜ਼ ਅਤੇ ਸਟੈਮ ਫਲਾਈਜ਼ ਦੇ ਨਾਲ-ਨਾਲ ਜੰਗਾਲ, ਫ਼ਫ਼ੂੰਦੀ ਅਤੇ ਝੁਲਸ ਵਰਗੀਆਂ ਬਿਮਾਰੀਆਂ, ਉਪਜ ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ ਮਾਤਰਾ ਨੂੰ ਬਹੁਤ ਜ਼ਿਆਦਾ ਘਟਾ ਸਕਦੀਆਂ ਹਨ। 
      		ਆਰਥਿਕ ਪ੍ਰਭਾਵ ਡੂੰਘਾ ਹੈ, ਜੋ ਨਾ ਸਿਰਫ਼ ਕਿਸਾਨਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦਾ ਹੈ, ਸਗੋਂ ਵਿਸ਼ਵ ਖੁਰਾਕ ਸਪਲਾਈ ਲੜੀ ਨੂੰ ਵੀ ਪ੍ਰਭਾਵਿਤ ਕਰਦਾ ਹੈ, 
		ਜਿਸ ਨਾਲ ਕਮਜ਼ੋਰ ਖੇਤਰਾਂ ਵਿੱਚ ਵਧੀਆਂ ਕੀਮਤਾਂ ਅਤੇ ਭੋਜਨ ਦੀ ਅਸੁਰੱਖਿਆ ਹੁੰਦੀ ਹੈ।''')

	# Display disease images with captions
	if selected_language == "English":
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
		
	elif selected_language == "Hindi":
		col = st.columns(7)
		with col[0]:
			st.image('aphid_1.jpeg', caption='एफिड')
		with col[1]:
		        st.image('brown_rust_3.jpeg', caption='भूरा जंग')
		with col[2]:
			st.image('mite_26.jpeg', caption='घुन')
		with col[3]:
		        st.image('stem_fly_30.jpeg', caption='तना मक्खी')
		with col[4]:
		        st.image('black_rust_1.jpeg', caption='काला जंग')
		with col[5]:
		        st.image('common_root_rot_55.jpeg', caption='सामान्य जड़ सड़न')
		with col[6]:
		        st.image('leaf_blight_38.jpeg', caption='पत्ती का झुलसा रोग')
			
		col1 = st.columns(7)
		with col1[0]:
		        st.image('septoria_5.jpeg.png', caption='सेप्टोरिया')
		with col1[1]:
		        st.image('tan_spot_24.jpeg', caption='टैन स्पॉट')
		with col1[2]:
		        st.image('blast_1.jpeg', caption='ब्लास्ट')
		with col1[3]:
		        st.image('fusarium_head_blight_test_0.png', caption='फ्यूजेरियम हेड ब्लाइट')
		with col1[4]:
		        st.image('mildew_82.png', caption='फफूंदी')
		with col1[5]:
		        st.image('smut_test_0.png', caption='मैल')
		with col1[6]:
		        st.image('yellow_rust_256.png', caption='पीला रतुआ')

	elif selected_language == "Punjabi":
		col = st.columns(7)
		with col[0]:
			st.image('aphid_1.jpeg', caption='ਐਫੀਡ')
		with col[1]:
		        st.image('brown_rust_3.jpeg', caption='ਭੂਰਾ ਜੰਗਾਲ')
		with col[2]:
			st.image('mite_26.jpeg', caption='ਮਾਈਟ')
		with col[3]:
		        st.image('stem_fly_30.jpeg', caption='ਸਟੈਮ ਫਲਾਈ')
		with col[4]:
		        st.image('black_rust_1.jpeg', caption='ਕਾਲਾ ਜੰਗਾਲ')
		with col[5]:
		        st.image('common_root_rot_55.jpeg', caption='ਆਮ ਜੜ੍ਹ ਸੜਨ')
		with col[6]:
		        st.image('leaf_blight_38.jpeg', caption='ਪੱਤਾ ਝੁਲਸ')
			
		col1 = st.columns(7)
		with col1[0]:
		        st.image('septoria_5.jpeg.png', caption='ਸੇਪਟੋਰੀਆ')
		with col1[1]:
		        st.image('tan_spot_24.jpeg', caption='ਟੈਨ ਸਪਾਟ')
		with col1[2]:
		        st.image('blast_1.jpeg', caption='ਬਲਾਸਟ')
		with col1[3]:
		        st.image('fusarium_head_blight_test_0.png', caption='ਫੁਸਾਰਿਅਮ ਸਿਰ ਝੁਲਸ')
		with col1[4]:
		        st.image('mildew_82.png', caption='ਫ਼ਫ਼ੂੰਦੀ')
		with col1[5]:
		        st.image('smut_test_0.png', caption='ਸ੍ਮਟ')
		with col1[6]:
		        st.image('yellow_rust_256.png', caption='ਪੀਲੀ ਜੰਗਾਲ')

	if selected_language == "English":
		st.subheader('The Role of Technology in Early Detection')
		st.write('''In response to these challenges, technology offers a powerful solution. 
	  	The Wheat Detection web app harnesses the power of artificial intelligence and machine learning to identify diseases in wheat crops at an early stage. 
	    	By analyzing images of wheat fields, the app can accurately detect signs of disease, enabling farmers to take prompt action. 
	      	Early detection is critical in preventing the spread of disease, protecting crop yields, and ensuring a stable food supply.''')
		st.image('farmer.webp')
		st.subheader('How It Works')
		st.markdown('''
		1. Image Capture: Farmers capture images of their wheat fields using a smartphone or drone.
		2. Analysis: The app processes these images using advanced machine learning algorithms trained to recognize specific disease patterns.
		3. Diagnosis: The app provides an instant diagnosis, identifying the type of disease and offering suggestions for treatment.
		4. Actionable Insights: Farmers receive recommendations on how to manage the detected disease, including optimal pesticide use and agronomic practices to mitigate the impact.''')
		st.subheader('The Impact')
		st.write('By integrating this technology into their farming practices, farmers can significantly reduce the losses caused by wheat diseases. The Wheat Detection app not only helps in preserving crop yields but also contributes to global efforts in achieving food security and reducing hunger. The economic benefits are also substantial, allowing farmers to maximize their profits and ensuring that the wheat market remains stable.')
		st.subheader('Join the Movement')
		st.write('As we move towards a future where technology plays an integral role in agriculture, the Wheat Detection app is at the forefront of this revolution. Join us in protecting one of the world’s most important crops and securing the future of global food security.')
		
		st.subheader('Steps to use the app')
		st.markdown('''
		- Take a clear image
		- Upload the image
		- Analyze the image and the name and confidence level of the disease along with the causes, preventions, and remedies will be displayed in the result panel below''')
		
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

	if selected_language == "Hindi":
		st.subheader('प्रारंभिक जांच में प्रौद्योगिकी की भूमिका')
		st.write('''इन चुनौतियों के जवाब में, प्रौद्योगिकी एक शक्तिशाली समाधान प्रदान करती है। 
	  	व्हीट डिटेक्शन वेब ऐप प्रारंभिक चरण में गेहूं की फसलों में बीमारियों की पहचान करने के लिए कृत्रिम बुद्धिमत्ता और मशीन लर्निंग की शक्ति का उपयोग करता है। 
	    	गेहूं के खेतों की छवियों का विश्लेषण करके, ऐप बीमारी के लक्षणों का सटीक पता लगा सकता है, जिससे किसान तुरंत कार्रवाई कर सकेंगे। 
	      	रोग के प्रसार को रोकने, फसल की पैदावार की रक्षा करने और स्थिर खाद्य आपूर्ति सुनिश्चित करने के लिए शीघ्र पता लगाना महत्वपूर्ण है।''')
		st.image('farmer.webp')
		st.subheader('यह काम किस प्रकार करता है')
		st.markdown('''
		1. छवि कैप्चर: किसान स्मार्टफोन या ड्रोन का उपयोग करके अपने गेहूं के खेतों की तस्वीरें खींचते हैं।
		2. विश्लेषण: ऐप विशिष्ट रोग पैटर्न को पहचानने के लिए प्रशिक्षित उन्नत मशीन लर्निंग एल्गोरिदम का उपयोग करके इन छवियों को संसाधित करता है।
		3. निदान: ऐप तत्काल निदान प्रदान करता है, बीमारी के प्रकार की पहचान करता है और उपचार के लिए सुझाव देता है।
		4. कार्रवाई योग्य अंतर्दृष्टि: किसानों को प्रभाव को कम करने के लिए इष्टतम कीटनाशकों के उपयोग और कृषि संबंधी प्रथाओं सहित पता चला बीमारी का प्रबंधन करने के बारे में सिफारिशें प्राप्त होती हैं।''')
		st.subheader('प्रभाव')
		st.write('इस तकनीक को अपनी कृषि पद्धतियों में एकीकृत करके, किसान गेहूं की बीमारियों से होने वाले नुकसान को काफी कम कर सकते हैं। व्हीट डिटेक्शन ऐप न केवल फसल की पैदावार को संरक्षित करने में मदद करता है बल्कि खाद्य सुरक्षा प्राप्त करने और भूख को कम करने के वैश्विक प्रयासों में भी योगदान देता है। आर्थिक लाभ भी पर्याप्त हैं, जिससे किसानों को अपने मुनाफे को अधिकतम करने की अनुमति मिलती है और यह सुनिश्चित होता है कि गेहूं बाजार स्थिर बना रहे।')
		st.subheader('आंदोलन में शामिल हों')
		st.write('जैसे-जैसे हम ऐसे भविष्य की ओर बढ़ रहे हैं जहां प्रौद्योगिकी कृषि में एक अभिन्न भूमिका निभाएगी, गेहूं डिटेक्शन ऐप इस क्रांति में सबसे आगे है। दुनिया की सबसे महत्वपूर्ण फसलों में से एक की रक्षा करने और वैश्विक खाद्य सुरक्षा के भविष्य को सुरक्षित करने में हमारे साथ जुड़ें।')
		
		st.subheader('ऐप का उपयोग करने के चरण')
		st.markdown('''
		- साफ़ छवि लें
		- छवि अपलोड करें
		- छवि का विश्लेषण करें और बीमारी के नाम और आत्मविश्वास के स्तर के साथ-साथ कारण, रोकथाम और उपचार नीचे परिणाम पैनल में प्रदर्शित किए जाएंगे।''')
		
		# Image upload and analysis section
		with st.container():
		    img = st.file_uploader('अपनी छवि अपलोड करें', type=['jpg', 'png', 'jpeg'])
		    analyse = st.button('विश्लेषण करें')
		    
		if analyse:
		    if img is not None:
		        img = Image.open(img)
		        st.markdown('छवि विज़ुअलाइज़ेशन')
		        st.image(img)
		        st.subheader('गेहूं की ये फसल हुई प्रभावित:')
		        model = models()
		        res = model.predict(img)
		        label = res[0].probs.top5
		        conf = res[0].probs.top5conf
		        conf = conf.tolist()
		        st.write('बीमारी: ' + str(res[0].names[label[0]].title()))
		        st.write('आत्मविश्वास स्तर: ' + str(conf[0]))
		        
		        if str(res[0].names[label[0]].title()) == 'एफिड':
		            st.write('''एफिड्स रस-चूसने वाले, मुलायम शरीर वाले कीड़ों का एक समूह है जो पिनहेड के आकार के होते हैं।''')
		            st.markdown('''कारण:
		            \n- एफिड्स रस चूसकर गेहूं के पौधों को प्रभावित करते हैं, जिससे उपज कम हो जाती है।''')
		            st.markdown('''रोकथाम:
		            \n- गेहूं की प्रतिरोधी किस्में लगाएं.
		            \n- कीटनाशक साबुन या नीम के तेल का प्रयोग करें।
		            \n- लेडीबग जैसे प्राकृतिक शिकारियों को प्रोत्साहित करें।''')
		            st.markdown('''उपाय:
		            \n- यदि संक्रमण गंभीर हो तो कीटनाशकों का प्रयोग करें।
		            \n- एफिड जीवन चक्र को बाधित करने के लिए फसल चक्र जैसी सांस्कृतिक प्रथाओं का उपयोग करें।''')
		
		        if str(res[0].names[label[0]].title()) == 'भूरा जंग':
		            st.write('''भूरा रतुआ गर्मियों के अंत में विकसित होता है और इसके परिणामस्वरूप हरी पत्ती के क्षेत्र में महत्वपूर्ण नुकसान होता है और इसलिए, उपज और विशिष्ट वजन में कमी आती है।''')
		            st.markdown('''कारण:
		            \n- पुकिनिया ट्रिटिसिना कवक के कारण होता है।''')
		            st.markdown('''रोकथाम:
		            \n- गेहूं की प्रतिरोधी किस्में लगाएं।
		            \n- निवारक उपाय के रूप में फफूंदनाशकों का प्रयोग करें।''')
		            st.markdown('''उपाय:
		            \n- रोग का शीघ्र पता चलने पर फफूंदनाशी का प्रयोग करें।
		            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
		
		        if str(res[0].names[label[0]].title()) == 'घुन':
		            st.write('''घुन छोटे, लाल-भूरे से लेकर काले, आठ पैरों वाले अरचिन्ड होते हैं जो विशेष रूप से गर्म, शुष्क परिस्थितियों में गेहूं की फसलों को संक्रमित करते हैं। 
		            वे हवा, मशीनरी और संक्रमित पौधों की सामग्री से फैलते हैं।''')
		            st.markdown('''कारण:
		            \n- घुन गेहूं के पौधों को संक्रमित करते हैं, रस चूसते हैं और वायरस फैलाते हैं।
		            \n- घुन गेहूं के पौधों को संक्रमित करते हैं, रस चूसते हैं और वायरस फैलाते हैं।''')
		            st.markdown('''रोकथाम:
		            \n- घुन प्रतिरोधी गेहूं की किस्मों का प्रयोग करें।
		            \n- यदि आवश्यक हो तो मिटिसाइड्स का प्रयोग करें।
		            \n- उचित सिंचाई से संक्रमण के खतरे को कम करने में मदद मिल सकती है।''')
		            st.markdown('''उपाय:
		            \n- उचित माइटसाइड्स का प्रयोग करें।
		            \n- क्षेत्र में उचित स्वच्छता बनाए रखें।''')
		
		        if str(res[0].names[label[0]].title()) == 'तना मक्खी':
		            st.write('''गेहूँ के तने का चूरा (सेफस सिंक्टस) हाइमनोप्टेरा (अर्थात मधुमक्खियाँ, ततैया और चींटियाँ) क्रम में सेफिडे परिवार का एक आदिम, ततैया जैसा कीट है। 
		            इसके लार्वा वसंत और सर्दियों के गेहूं के महत्वपूर्ण कीट हैं, जिससे फसलों की गुणवत्ता और उपज कम हो जाती है।''')
		            st.markdown('''कारण:
		            \n- तना मक्खियाँ गेहूँ के पौधों पर अंडे देती हैं, और लार्वा तने में दब जाते हैं।''')
		            st.markdown('''रोकथाम:
		            \n- चरम स्टेम फ्लाई गतिविधि से बचने के लिए जल्दी रोपण करें।
		            \n- निवारक उपाय के रूप में कीटनाशकों का प्रयोग करें।''')
		            st.markdown('''उपाय:
		            \n- लार्वा अवस्था में कीटनाशकों का प्रयोग करें।
		            \n-संक्रमित पौधों को हटा कर नष्ट कर दें।''')
		
		        if str(res[0].names[label[0]].title()) == 'काला जंग':
		            st.write('''काला रतुआ गेहूं के पौधों के तनों और पत्तियों को प्रभावित करता है, जिससे उपज में काफी नुकसान होता है और आर्थिक क्षति होती है। 
		            यह काले या गहरे भूरे रंग के उभरे हुए दाने पैदा करता है जिनमें जंग के रंग के बीजाणु होते हैं। अगर नियंत्रित नहीं किया गया तो यह तेजी से फैल सकता है और पूरे खेतों को तबाह कर सकता है।''')
		            st.markdown('''कारण:
		            \n- पुकिनिया ग्रेमिनिस कवक के कारण होता है।''')
		            st.markdown('''रोकथाम:
		            \n- गेहूं की प्रतिरोधी किस्में लगाएं।
		            \n- फफूंदनाशकों का प्रयोग सावधानी से करें।''')
		            st.markdown('''उपाय:
		            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
		            \n- संक्रमित पौधे के मलबे को नष्ट कर दें।''')
		
		        if str(res[0].names[label[0]].title()) == 'सामान्य जड़ सड़न':
		            st.write('''गेहूं की जड़ सड़न विभिन्न कवक के कारण होती है जो गेहूं के पौधों की जड़ों और मुकुट ऊतक पर आक्रमण करते हैं। 
		            संक्रमित पौधों ने मुकुट और जड़ के ऊतकों को नष्ट कर दिया है, जिसके परिणामस्वरूप पानी और पोषक तत्वों का अवशोषण रुक गया है।''')
		            st.markdown('''कारण:
		            \n- बाइपोलारिस सोरोकिनियाना जैसे कवक के कारण होता है।''')
		            st.markdown('''रोकथाम:
		            \n- रोगमुक्त बीजों का प्रयोग करें।
		            \n- गैर-मेज़बान फसलों के साथ फसल चक्र लागू करें।''')
		            st.markdown('''उपाय:
		            \n- उचित फफूंदनाशकों का प्रयोग करें।
		            \n-मिट्टी की जल निकासी में सुधार करें।''')
		
		        if str(res[0].names[label[0]].title()) == 'पत्ती का झुलसा रोग':
		            st.write('''युवा पौधों पर चमकीले पीले किनारों के साथ लाल भूरे अंडाकार धब्बे दिखाई देते हैं। गंभीर मामलों में, कई धब्बे मिलकर पत्तियों के सूखने का कारण बनते हैं।''')
		            st.markdown('''कारण:
		            \n- बाइपोलारिस और अल्टरनेरिया प्रजाति जैसे कवक के कारण होता है।''')
		            st.markdown('''रोकथाम:
		            \n- प्रतिरोधी किस्में लगाएं।
		            \n- फफूंदनाशकों का प्रयोग सावधानी से करें।''')
		            st.markdown('''उपाय:
		            \n- लक्षणों की शुरुआत में फफूंदनाशी लगाएं।
		            \n- संक्रमित पौधे के अवशेषों को हटाएं और नष्ट करें।''')
		
		        if str(res[0].names[label[0]].title()) == 'सेप्टोरिया':
		            st.write('''सेप्टोरिया ट्रिटिसी ब्लॉच मौसमों के बीच ठूंठ पर जीवित रहता है। 
		            देर से शरद ऋतु और शुरुआती सर्दियों में, बारिश या भारी ओस के कारण ठूंठ में पेरिथेसिया से हवा-जनित एस्कॉस्पोर निकलते हैं, जिससे बीमारी बड़ी दूरी तक फैल जाती है।''')
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
				
	if selected_language == "English":
		st.subheader('The Role of Technology in Early Detection')
		st.write('''In response to these challenges, technology offers a powerful solution. 
	  	The Wheat Detection web app harnesses the power of artificial intelligence and machine learning to identify diseases in wheat crops at an early stage. 
	    	By analyzing images of wheat fields, the app can accurately detect signs of disease, enabling farmers to take prompt action. 
	      	Early detection is critical in preventing the spread of disease, protecting crop yields, and ensuring a stable food supply.''')
		st.image('farmer.webp')
		st.subheader('How It Works')
		st.markdown('''
		1. Image Capture: Farmers capture images of their wheat fields using a smartphone or drone.
		2. Analysis: The app processes these images using advanced machine learning algorithms trained to recognize specific disease patterns.
		3. Diagnosis: The app provides an instant diagnosis, identifying the type of disease and offering suggestions for treatment.
		4. Actionable Insights: Farmers receive recommendations on how to manage the detected disease, including optimal pesticide use and agronomic practices to mitigate the impact.''')
		st.subheader('The Impact')
		st.write('By integrating this technology into their farming practices, farmers can significantly reduce the losses caused by wheat diseases. The Wheat Detection app not only helps in preserving crop yields but also contributes to global efforts in achieving food security and reducing hunger. The economic benefits are also substantial, allowing farmers to maximize their profits and ensuring that the wheat market remains stable.')
		st.subheader('Join the Movement')
		st.write('As we move towards a future where technology plays an integral role in agriculture, the Wheat Detection app is at the forefront of this revolution. Join us in protecting one of the world’s most important crops and securing the future of global food security.')
		
		st.subheader('Steps to use the app')
		st.markdown('''
		- Take a clear image
		- Upload the image
		- Analyze the image and the name and confidence level of the disease along with the causes, preventions, and remedies will be displayed in the result panel below''')
		
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

