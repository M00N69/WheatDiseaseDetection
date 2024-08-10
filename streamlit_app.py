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
