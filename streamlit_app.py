from ultralytics import YOLO
import streamlit as st
from PIL import Image
import streamlit_analytics
from streamlit_carousel import carousel
from st_screen_stats import ScreenData

st.set_page_config(page_title="WheatCheck",page_icon="WheatCheck clear logo.png",layout="wide")

screenD = ScreenData(setTimeout=1000)
screen_d = screenD.st_screen_data()

if(screen_d['screen']['height']<screen_d['screen']['width']):
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
		
		languages = ["English", "ਪੰਜਾਬੀ", "हिंदी"]
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
		    if selected_language == "English":
		        col[1].markdown("<h1 style='text-align: center; color: white;'>WheatCheck - Wheat Disease Detection</h1>", unsafe_allow_html=True)
		    elif selected_language == "हिंदी":
		        col[1].markdown("<h1 style='text-align: center; color: white;'>वीटचेक - गेहूँ रोग का पता लगाये</h1>", unsafe_allow_html=True)
		    elif selected_language == "ਪੰਜਾਬੀ":
		        col[1].markdown("<h1 style='text-align: center; color: white;'>ਵੀਟਚੈੱਕ - ਕਣਕ ਦੀ ਬਿਮਾਰੀ ਦਾ ਪਤਾ ਲਗਾਓ</h1>", unsafe_allow_html=True)
		
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
			
		elif selected_language == "हिंदी":
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
			    
		elif selected_language == "ਪੰਜਾਬੀ":
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
			
		elif selected_language == "हिंदी":
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
	
		elif selected_language == "ਪੰਜਾਬੀ":
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
			        if int(conf[0]) < 95:
				        st.write('No Disease Detected')
			        else:
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
			
				        elif str(res[0].names[label[0]].title()) == 'Brown Rust':
				            st.write('''Brown rust tends to develops in late summer and results in a significant loss of green leaf area and, hence, yield and specific weight.''')
				            st.markdown('''Causes:
				            \n- Caused by the fungus Puccinia triticina.''')
				            st.markdown('''Preventions:
				            \n- Plant resistant wheat varieties. 
				            \n- Apply fungicides as a preventive measure.''')
				            st.markdown('''Remedies:
				            \n- Use fungicides when the disease is detected early.
				            \n- Remove and destroy infected plant debris.''')
				
				        elif str(res[0].names[label[0]].title()) == 'Mite':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Stem Fly':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Black Rust':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Common Root Rot':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Leaf Blight':
				            st.write('''Reddish brown oval spots appear on young seedlings with bright yellow margins. In severe cases, several spots coalesce to cause drying of leaves.''')
				            st.markdown('''Causes:
				            \n- Caused by fungi such as Bipolaris and Alternaria species.''')
				            st.markdown('''Preventions:
				            \n- Plant resistant varieties.
				            \n- Use fungicides preventively.''')
				            st.markdown('''Remedies:
				            \n- Apply fungicides at the onset of symptoms.
				            \n- Remove and destroy infected plant residues.''')
				
				        elif str(res[0].names[label[0]].title()) == 'Septoria':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Tan Spot':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Blast':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Mildew':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Smut':
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
				
				        elif str(res[0].names[label[0]].title()) == 'Yellow Rust':
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
	
		if selected_language == "हिंदी":
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
			        
			        if str(res[0].names[label[0]].title()) == 'Aphid':
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
			
			        if str(res[0].names[label[0]].title()) == 'Brown Rust':
			            st.write('''भूरा रतुआ गर्मियों के अंत में विकसित होता है और इसके परिणामस्वरूप हरी पत्ती के क्षेत्र में महत्वपूर्ण नुकसान होता है और इसलिए, उपज और विशिष्ट वजन में कमी आती है।''')
			            st.markdown('''कारण:
			            \n- पुकिनिया ट्रिटिसिना कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- गेहूं की प्रतिरोधी किस्में लगाएं।
			            \n- निवारक उपाय के रूप में फफूंदनाशकों का प्रयोग करें।''')
			            st.markdown('''उपाय:
			            \n- रोग का शीघ्र पता चलने पर फफूंदनाशी का प्रयोग करें।
			            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mite':
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
			
			        if str(res[0].names[label[0]].title()) == 'Stem Fly':
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
			
			        if str(res[0].names[label[0]].title()) == 'Black Rust':
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
			
			        if str(res[0].names[label[0]].title()) == 'Common Root Rot':
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
			
			        if str(res[0].names[label[0]].title()) == 'Leaf Blight':
			            st.write('''युवा पौधों पर चमकीले पीले किनारों के साथ लाल भूरे अंडाकार धब्बे दिखाई देते हैं। गंभीर मामलों में, कई धब्बे मिलकर पत्तियों के सूखने का कारण बनते हैं।''')
			            st.markdown('''कारण:
			            \n- बाइपोलारिस और अल्टरनेरिया प्रजाति जैसे कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग सावधानी से करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षणों की शुरुआत में फफूंदनाशी लगाएं।
			            \n- संक्रमित पौधे के अवशेषों को हटाएं और नष्ट करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Septoria':
			            st.write('''सेप्टोरिया ट्रिटिसी ब्लॉच मौसमों के बीच ठूंठ पर जीवित रहता है। 
			            देर से शरद ऋतु और शुरुआती सर्दियों में, बारिश या भारी ओस के कारण ठूंठ में पेरिथेसिया से हवा-जनित एस्कॉस्पोर निकलते हैं, जिससे बीमारी बड़ी दूरी तक फैल जाती है।''')
			            st.markdown('''कारण:
			            \n- सेप्टोरिया ट्रिटिसी कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग सावधानी से करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
			            \n- संक्रमित पत्तियों को हटाकर नष्ट कर दें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Tan Spot':
			            st.write('''टैन स्पॉट, जिसे पीली पत्ती वाले धब्बे के रूप में भी जाना जाता है, अमेरिका और कनाडा में उगाए जाने वाले गेहूं में एक आर्थिक रूप से महत्वपूर्ण बीमारी है। 
			            यह प्रारंभ में अतिसंवेदनशील गेहूं की किस्मों की पत्तियों पर छोटे, भूरे धब्बों के रूप में दिखाई देता है।''')
			            st.markdown('''कारण:
			            \n- पायरेनोफोरा ट्रिटिसी-रेपेंटिस कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फसल चक्र और स्वच्छ बीज का प्रयोग करें।''')
			            st.markdown('''उपाय:
			            \n- संक्रमण के शुरुआती लक्षणों पर फफूंदनाशी लगाएं।
			            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Blast':
			            st.write('''व्हीट ब्लास्ट एक विनाशकारी बीमारी है जो 1980 के दशक में ब्राज़ील में उभरी और तब से आस-पास और दूर-दराज के देशों में फैल गई है। 
			            उम्मीद है कि जलवायु परिवर्तन से इसके प्रसार में आसानी होगी, खासकर उष्णकटिबंधीय क्षेत्रों में।''')
			            st.markdown('''कारण:
			            \n- मैग्नापोर्थे ओराइजी कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- अत्यधिक नाइट्रोजन उर्वरक डालने से बचें।''')
			            st.markdown('''उपाय:
			            \n- लक्षणों के पहले संकेत पर फफूंदनाशी लगाएं।
			            \n- फसल चक्र का अभ्यास करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
			            st.write('''फ्यूसेरियम हेड ब्लाइट एक गंभीर कवक रोग है जिसके कारण अनाज मायकोटॉक्सिन से दूषित हो जाता है। 
			            इसके परिणामस्वरूप उपज में कमी, अनाज की खराब गुणवत्ता और गेहूं उत्पादकों को महत्वपूर्ण आर्थिक नुकसान होता है।''')
			            st.markdown('''कारण:
			            \n-फ्यूसेरियम प्रजाति के कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फसल चक्र और स्वच्छ बीज का प्रयोग करें।''')
			            st.markdown('''उपाय:
			            \n- फूल आने की अवस्था में फफूंदनाशकों का प्रयोग करें।
			            \n- उच्च फ्यूजेरियम दबाव वाले खेतों में रोपण से बचें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mildew':
			            st.write('''गेहूं में ख़स्ता फफूंदी सफेद मायसेलियम की सतह पर धब्बे के रूप में शुरू होती है और अंततः पूरी पत्ती को कवर कर सकती है, जिसमें परिपक्व संक्रमण के साथ काले बीजाणु के मामले दिखाई देते हैं। 
			            हवा से फैलने वाली यह बीमारी ठंडे, गीले मौसम में पनपती है और उपज को 40% तक नुकसान पहुंचा सकती है।''')
			            st.markdown('''कारण:
			            \n- ब्लूमेरिया ग्रेमिनिस कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग रोकथाम के लिए करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
			            \n- खेत में अच्छा वायु संचार सुनिश्चित करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Smut':
			            st.write('''ढीली स्मट का व्यापक वितरण होता है और यह कहीं भी हो सकता है जहां गेहूं का उत्पादन होता है। 
			            शीर्षासन से पहले हल्के लक्षण मौजूद हो सकते हैं, जिनमें पीली पत्ती की धारियाँ और कड़ी, गहरे हरे रंग की पत्तियाँ शामिल हैं।''')
			            st.markdown('''कारण:
			            \n- यूस्टिलैगो प्रजाति जैसे कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- स्मट-प्रतिरोधी किस्मों का उपयोग करें।
			            \n- रोपण से पहले बीजों को फफूंदनाशकों से उपचारित करें।''')
			            st.markdown('''उपाय:
			            \n- संक्रमित पौधों को नष्ट कर दें।
			            \n- उचित फफूंदनाशकों का प्रयोग करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Yellow Rust':
			            st.write('''पीले रतुआ का विशिष्ट लक्षण वयस्क पौधों की पत्तियों पर पीले नारंगी रंग की फुंसियों की समानांतर पंक्तियाँ होना है। 
			            पीले रतुआ की महामारी अक्सर व्यक्तिगत पौधों के रूप में शुरू होती है, आमतौर पर शरद ऋतु में।''')
			            st.markdown('''कारण:
			            \n- पुकिनिया स्ट्राइफोर्मिस कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग रोकथाम के लिए करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
			            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
					
		if selected_language == "ਪੰਜਾਬੀ":
			st.subheader('ਸ਼ੁਰੂਆਤੀ ਖੋਜ ਵਿੱਚ ਤਕਨਾਲੋਜੀ ਦੀ ਭੂਮਿਕਾ')
			st.write('''ਇਹਨਾਂ ਚੁਣੌਤੀਆਂ ਦੇ ਜਵਾਬ ਵਿੱਚ, ਤਕਨਾਲੋਜੀ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਹੱਲ ਪੇਸ਼ ਕਰਦੀ ਹੈ। 
		  	Wheat Detection ਵੈੱਬ ਐਪ ਸ਼ੁਰੂਆਤੀ ਪੜਾਅ 'ਤੇ ਕਣਕ ਦੀਆਂ ਫਸਲਾਂ ਵਿੱਚ ਬਿਮਾਰੀਆਂ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਨਕਲੀ ਬੁੱਧੀ ਅਤੇ ਮਸ਼ੀਨ ਸਿਖਲਾਈ ਦੀ ਸ਼ਕਤੀ ਨੂੰ ਵਰਤਦਾ ਹੈ। 
		    	ਕਣਕ ਦੇ ਖੇਤਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ, ਐਪ ਬਿਮਾਰੀ ਦੇ ਲੱਛਣਾਂ ਦਾ ਸਹੀ ਪਤਾ ਲਗਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਕਿਸਾਨਾਂ ਨੂੰ ਤੁਰੰਤ ਕਾਰਵਾਈ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ। 
		      	ਬਿਮਾਰੀ ਦੇ ਫੈਲਣ ਨੂੰ ਰੋਕਣ, ਫਸਲਾਂ ਦੀ ਉਪਜ ਦੀ ਰੱਖਿਆ ਕਰਨ, ਅਤੇ ਇੱਕ ਸਥਿਰ ਭੋਜਨ ਸਪਲਾਈ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਸ਼ੁਰੂਆਤੀ ਖੋਜ ਮਹੱਤਵਪੂਰਨ ਹੈ।''')
			st.image('farmer.webp')
			st.subheader('ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ')
			st.markdown('''
			1. ਚਿੱਤਰ ਕੈਪਚਰ: ਕਿਸਾਨ ਸਮਾਰਟਫੋਨ ਜਾਂ ਡਰੋਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਕਣਕ ਦੇ ਖੇਤਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਕੈਪਚਰ ਕਰਦੇ ਹਨ।
			2. ਵਿਸ਼ਲੇਸ਼ਣ: ਐਪ ਖਾਸ ਰੋਗਾਂ ਦੇ ਪੈਟਰਨਾਂ ਨੂੰ ਪਛਾਣਨ ਲਈ ਸਿਖਲਾਈ ਪ੍ਰਾਪਤ ਤਕਨੀਕੀ ਮਸ਼ੀਨ ਸਿਖਲਾਈ ਐਲਗੋਰਿਦਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹਨਾਂ ਚਿੱਤਰਾਂ 'ਤੇ ਪ੍ਰਕਿਰਿਆ ਕਰਦੀ ਹੈ।
			3. ਨਿਦਾਨ: ਐਪ ਇੱਕ ਤਤਕਾਲ ਨਿਦਾਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਬਿਮਾਰੀ ਦੀ ਕਿਸਮ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ ਅਤੇ ਇਲਾਜ ਲਈ ਸੁਝਾਅ ਪੇਸ਼ ਕਰਦਾ ਹੈ।
			4. ਕਾਰਵਾਈਯੋਗ ਸੂਝ: ਕਿਸਾਨਾਂ ਨੂੰ ਇਸ ਬਾਰੇ ਸਿਫ਼ਾਰਸ਼ਾਂ ਮਿਲਦੀਆਂ ਹਨ ਕਿ ਖੋਜੀ ਗਈ ਬਿਮਾਰੀ ਦਾ ਪ੍ਰਬੰਧਨ ਕਿਵੇਂ ਕਰਨਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਭਾਵ ਨੂੰ ਘਟਾਉਣ ਲਈ ਅਨੁਕੂਲ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਅਤੇ ਖੇਤੀ ਵਿਗਿਆਨਿਕ ਅਭਿਆਸਾਂ ਸ਼ਾਮਲ ਹਨ।''')
			st.subheader('ਪ੍ਰਭਾਵ')
			st.write('ਇਸ ਤਕਨੀਕ ਨੂੰ ਆਪਣੇ ਖੇਤੀ ਅਭਿਆਸਾਂ ਵਿੱਚ ਜੋੜ ਕੇ, ਕਿਸਾਨ ਕਣਕ ਦੀਆਂ ਬਿਮਾਰੀਆਂ ਕਾਰਨ ਹੋਣ ਵਾਲੇ ਨੁਕਸਾਨ ਨੂੰ ਕਾਫ਼ੀ ਹੱਦ ਤੱਕ ਘਟਾ ਸਕਦੇ ਹਨ। Wheat Detection ਐਪ ਨਾ ਸਿਰਫ਼ ਫ਼ਸਲਾਂ ਦੀ ਪੈਦਾਵਾਰ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ, ਸਗੋਂ ਭੋਜਨ ਸੁਰੱਖਿਆ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਅਤੇ ਭੁੱਖਮਰੀ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਵਿਸ਼ਵਵਿਆਪੀ ਯਤਨਾਂ ਵਿੱਚ ਵੀ ਯੋਗਦਾਨ ਪਾਉਂਦੀ ਹੈ। ਆਰਥਿਕ ਲਾਭ ਵੀ ਕਾਫੀ ਹੁੰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਕਿਸਾਨਾਂ ਨੂੰ ਵੱਧ ਤੋਂ ਵੱਧ ਲਾਭ ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ ਅਤੇ ਕਣਕ ਦੀ ਮੰਡੀ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ।')
			st.subheader('ਅੰਦੋਲਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ')
			st.write('ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਇੱਕ ਅਜਿਹੇ ਭਵਿੱਖ ਵੱਲ ਵਧਦੇ ਹਾਂ ਜਿੱਥੇ ਤਕਨਾਲੋਜੀ ਖੇਤੀਬਾੜੀ ਵਿੱਚ ਇੱਕ ਅਨਿੱਖੜਵਾਂ ਭੂਮਿਕਾ ਨਿਭਾਉਂਦੀ ਹੈ, ਕਣਕ ਖੋਜ ਐਪ ਇਸ ਕ੍ਰਾਂਤੀ ਵਿੱਚ ਸਭ ਤੋਂ ਅੱਗੇ ਹੈ। ਦੁਨੀਆ ਦੀਆਂ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਫਸਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਦੀ ਰੱਖਿਆ ਕਰਨ ਅਤੇ ਵਿਸ਼ਵ ਭੋਜਨ ਸੁਰੱਖਿਆ ਦੇ ਭਵਿੱਖ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਵਿੱਚ ਸਾਡੇ ਨਾਲ ਸ਼ਾਮਲ ਹੋਵੋ।')
			
			st.subheader('ਐਪ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਕਦਮ')
			st.markdown('''
			- ਇੱਕ ਸਪਸ਼ਟ ਚਿੱਤਰ ਲਓ
			- ਚਿੱਤਰ ਅੱਪਲੋਡ ਕਰੋ
			- ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ ਅਤੇ ਬਿਮਾਰੀ ਦੇ ਨਾਮ ਅਤੇ ਵਿਸ਼ਵਾਸ ਪੱਧਰ ਦੇ ਨਾਲ ਕਾਰਨ, ਰੋਕਥਾਮ ਅਤੇ ਉਪਚਾਰ ਹੇਠਾਂ ਨਤੀਜੇ ਪੈਨਲ ਵਿੱਚ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੇ ਜਾਣਗੇ।''')
			
			# Image upload and analysis section
			with st.container():
			    img = st.file_uploader('ਆਪਣੀ ਤਸਵੀਰ ਅੱਪਲੋਡ ਕਰੋ', type=['jpg', 'png', 'jpeg'])
			    analyse = st.button('ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ')
			    
			if analyse:
			    if img is not None:
			        img = Image.open(img)
			        st.markdown('ਚਿੱਤਰ ਵਿਜ਼ੂਅਲਾਈਜ਼ੇਸ਼ਨ')
			        st.image(img)
			        st.subheader('ਕਣਕ ਦੀ ਇਹ ਫਸਲ ਇਨ੍ਹਾਂ ਕਾਰਨਾਂ ਕਰਕੇ ਪ੍ਰਭਾਵਿਤ ਹੋਈ ਹੈ:')
			        model = models()
			        res = model.predict(img)
			        label = res[0].probs.top5
			        conf = res[0].probs.top5conf
			        conf = conf.tolist()
			        st.write('ਰੋਗ: ' + str(res[0].names[label[0]].title()))
			        st.write('ਵਿਸ਼ਵਾਸ ਪੱਧਰ: ' + str(conf[0]))
			        
			        if str(res[0].names[label[0]].title()) == 'Aphid':
			            st.write('''ਐਫੀਡਜ਼ ਰਸ ਚੂਸਣ ਵਾਲੇ, ਨਰਮ ਸਰੀਰ ਵਾਲੇ ਕੀੜਿਆਂ ਦਾ ਇੱਕ ਸਮੂਹ ਹੈ ਜੋ ਕਿ ਪਿੰਨਹੈੱਡ ਦੇ ਆਕਾਰ ਦੇ ਹੁੰਦੇ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਐਫੀਡਸ ਰਸ ਚੂਸ ਕੇ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਝਾੜ ਘੱਟ ਜਾਂਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਕੀਟਨਾਸ਼ਕ ਸਾਬਣ ਜਾਂ ਨਿੰਮ ਦੇ ਤੇਲ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਲੇਡੀਬੱਗ ਵਰਗੇ ਕੁਦਰਤੀ ਸ਼ਿਕਾਰੀਆਂ ਨੂੰ ਉਤਸ਼ਾਹਿਤ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਕੀਟਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ ਜੇਕਰ ਸੰਕਰਮਣ ਗੰਭੀਰ ਹੋਵੇ।
			            \n- ਐਫਿਡ ਜੀਵਨ ਚੱਕਰ ਨੂੰ ਵਿਗਾੜਨ ਲਈ ਫਸਲੀ ਚੱਕਰ ਵਰਗੀਆਂ ਸੱਭਿਆਚਾਰਕ ਅਭਿਆਸਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Brown Rust':
			            st.write('''ਭੂਰੀ ਜੰਗਾਲ ਗਰਮੀਆਂ ਦੇ ਅਖੀਰ ਵਿੱਚ ਵਿਕਸਤ ਹੁੰਦਾ ਹੈ ਅਤੇ ਨਤੀਜੇ ਵਜੋਂ ਹਰੇ ਪੱਤਿਆਂ ਦੇ ਖੇਤਰ ਵਿੱਚ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ ਅਤੇ, ਇਸਲਈ, ਝਾੜ ਅਤੇ ਖਾਸ ਭਾਰ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Puccinia triticina ਉੱਲੀ ਦੇ ਕਾਰਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ। 
			            \n- ਰੋਕਥਾਮ ਉਪਾਅ ਵਜੋਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਬਿਮਾਰੀ ਦਾ ਛੇਤੀ ਪਤਾ ਲੱਗਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mite':
			            st.write('''ਦੇਕਣ ਛੋਟੇ, ਲਾਲ-ਭੂਰੇ ਤੋਂ ਕਾਲੇ, ਅੱਠ ਪੈਰਾਂ ਵਾਲੇ ਅਰਚਨਿਡ ਹੁੰਦੇ ਹਨ ਜੋ ਕਣਕ ਦੀਆਂ ਫਸਲਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ, ਖਾਸ ਕਰਕੇ ਗਰਮ, ਸੁੱਕੀਆਂ ਸਥਿਤੀਆਂ ਵਿੱਚ। 
			            ਇਹ ਹਵਾ, ਮਸ਼ੀਨਰੀ ਅਤੇ ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਦੀ ਸਮੱਗਰੀ ਰਾਹੀਂ ਫੈਲਦੇ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਕੀੜੇ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਨੂੰ ਸੰਕਰਮਿਤ ਕਰਦੇ ਹਨ, ਰਸ ਚੂਸਦੇ ਹਨ ਅਤੇ ਵਾਇਰਸ ਫੈਲਾਉਂਦੇ ਹਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਕੀਟ-ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਜੇਕਰ ਲੋੜ ਹੋਵੇ ਤਾਂ ਮਾਈਟੀਸਾਈਡਸ ਲਾਗੂ ਕਰੋ।
			            \n- ਸਹੀ ਸਿੰਚਾਈ ਸੰਕਰਮਣ ਦੇ ਜੋਖਮ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਉਚਿਤ ਮਾਈਟੀਸਾਈਡਸ ਲਾਗੂ ਕਰੋ।
			            \n- ਖੇਤ ਦੀ ਸਹੀ ਸਫਾਈ ਬਣਾਈ ਰੱਖੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Stem Fly':
			            st.write('''ਕਣਕ ਦੇ ਤਣੇ ਦੀ ਆਰਾ (Cephus cinctus) Hymenoptera (ਜਿਵੇਂ ਕਿ ਮਧੂ-ਮੱਖੀਆਂ, ਭਾਂਡੇ ਅਤੇ ਕੀੜੀਆਂ) ਦੇ ਕ੍ਰਮ ਵਿੱਚ ਸੇਫੀਡੇ ਪਰਿਵਾਰ ਵਿੱਚੋਂ ਇੱਕ ਆਦਿਮ, ਭਾਂਡੇ-ਵਰਗੇ ਕੀੜੇ ਹਨ। 
			            ਇਸ ਦੇ ਲਾਰਵੇ ਬਸੰਤ ਅਤੇ ਸਰਦੀਆਂ ਦੀ ਕਣਕ ਦੇ ਮਹੱਤਵਪੂਰਨ ਕੀੜੇ ਹਨ, ਜਿਸ ਨਾਲ ਫਸਲਾਂ ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ ਝਾੜ ਘਟਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਡੰਡੀ ਦੀਆਂ ਮੱਖੀਆਂ ਕਣਕ ਦੇ ਪੌਦਿਆਂ 'ਤੇ ਅੰਡੇ ਦਿੰਦੀਆਂ ਹਨ, ਅਤੇ ਲਾਰਵੇ ਤਣੀਆਂ ਵਿੱਚ ਛਾ ਜਾਂਦੇ ਹਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਪੀਕ ਸਟੈਮ ਫਲਾਈ ਗਤੀਵਿਧੀ ਤੋਂ ਬਚਣ ਲਈ ਜਲਦੀ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਉਪਾਅ ਵਜੋਂ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲਾਰਵੇ ਪੜਾਅ 'ਤੇ ਕੀਟਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Black Rust':
			            st.write('''ਕਾਲੀ ਕੁੰਗੀ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਦੇ ਤਣੇ ਅਤੇ ਪੱਤਿਆਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਉਪਜ ਦਾ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਅਤੇ ਆਰਥਿਕ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ। 
			            ਇਹ ਕਾਲੇ ਜਾਂ ਗੂੜ੍ਹੇ ਭੂਰੇ ਰੰਗ ਦੇ ਉੱਚੇ ਹੋਏ ਛਾਲੇ ਪੈਦਾ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਜੰਗਾਲ-ਰੰਗ ਦੇ ਬੀਜਾਣੂ ਹੁੰਦੇ ਹਨ। ਜੇਕਰ ਕੰਟਰੋਲ ਨਾ ਕੀਤਾ ਜਾਵੇ, ਤਾਂ ਇਹ ਤੇਜ਼ੀ ਨਾਲ ਫੈਲ ਸਕਦਾ ਹੈ ਅਤੇ ਪੂਰੇ ਖੇਤਾਂ ਨੂੰ ਤਬਾਹ ਕਰ ਸਕਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Puccinia graminis ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Common Root Rot':
			            st.write('''ਕਣਕ ਦੀਆਂ ਜੜ੍ਹਾਂ ਦੀਆਂ ਸੜਨ ਵੱਖ-ਵੱਖ ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦੀਆਂ ਹਨ ਜੋ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਦੀਆਂ ਜੜ੍ਹਾਂ ਅਤੇ ਤਾਜ ਦੇ ਟਿਸ਼ੂ 'ਤੇ ਹਮਲਾ ਕਰਦੀਆਂ ਹਨ। 
			            ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੇ ਤਾਜ ਅਤੇ ਜੜ੍ਹਾਂ ਦੇ ਟਿਸ਼ੂਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰ ਦਿੱਤਾ ਹੈ, ਜਿਸਦੇ ਨਤੀਜੇ ਵਜੋਂ ਪਾਣੀ ਅਤੇ ਪੌਸ਼ਟਿਕ ਤੱਤਾਂ ਦੀ ਖਪਤ ਰੁਕ ਜਾਂਦੀ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਬਾਇਪੋਲਾਰਿਸ ਸੋਰੋਕਿਨਿਆਨਾ ਵਰਗੀ ਉੱਲੀ ਦੇ ਕਾਰਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਗ ਮੁਕਤ ਬੀਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਗੈਰ-ਹੋਸਟ ਫਸਲਾਂ ਦੇ ਨਾਲ ਫਸਲੀ ਰੋਟੇਸ਼ਨ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਢੁਕਵੀਆਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਮਿੱਟੀ ਦੀ ਨਿਕਾਸੀ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Leaf Blight':
			            st.write('''ਚਮਕਦਾਰ ਪੀਲੇ ਹਾਸ਼ੀਏ ਵਾਲੇ ਛੋਟੇ ਬੂਟਿਆਂ 'ਤੇ ਲਾਲ ਭੂਰੇ ਅੰਡਾਕਾਰ ਧੱਬੇ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। ਗੰਭੀਰ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਕਈ ਚਟਾਕ ਪੱਤੇ ਦੇ ਸੁੱਕਣ ਦਾ ਕਾਰਨ ਬਣਦੇ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਬਾਇਪੋਲਾਰਿਸ ਅਤੇ ਅਲਟਰਨੇਰੀਆ ਸਪੀਸੀਜ਼ ਵਰਗੀਆਂ ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣਾਂ ਦੀ ਸ਼ੁਰੂਆਤ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Septoria':
			            st.write('''ਸੇਪਟੋਰੀਆ ਟ੍ਰਾਈਟੀਸੀ ਬਲੋਚ ਮੌਸਮਾਂ ਦੇ ਵਿਚਕਾਰ ਪਰਾਲੀ 'ਤੇ ਜਿਉਂਦਾ ਰਹਿੰਦਾ ਹੈ। 
			            ਪਤਝੜ ਦੇ ਅਖੀਰ ਅਤੇ ਸਰਦੀਆਂ ਦੇ ਸ਼ੁਰੂ ਵਿੱਚ, ਮੀਂਹ ਜਾਂ ਭਾਰੀ ਤ੍ਰੇਲ ਪਰਾਲੀ ਵਿੱਚ ਪੈਰੀਥੀਸੀਆ ਤੋਂ ਹਵਾ ਦੁਆਰਾ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਐਸਕੋਸਪੋਰਸ ਨੂੰ ਛੱਡਣ ਦਾ ਕਾਰਨ ਬਣਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਬਿਮਾਰੀ ਵੱਡੀ ਦੂਰੀ ਤੱਕ ਫੈਲ ਜਾਂਦੀ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਸੇਪਟੋਰੀਆ ਟ੍ਰਾਈਟੀਸੀ ਉੱਲੀ ਦੇ ਕਾਰਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਸੰਕਰਮਿਤ ਪੱਤਿਆਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Tan Spot':
			            st.write('''ਟੈਨ ਸਪਾਟ, ਜਿਸ ਨੂੰ ਪੀਲੇ ਪੱਤੇ ਦੇ ਸਥਾਨ ਵਜੋਂ ਵੀ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਅਮਰੀਕਾ ਅਤੇ ਕੈਨੇਡਾ ਵਿੱਚ ਉਗਾਈ ਜਾਣ ਵਾਲੀ ਕਣਕ ਵਿੱਚ ਆਰਥਿਕ ਤੌਰ 'ਤੇ ਮਹੱਤਵਪੂਰਨ ਬਿਮਾਰੀ ਹੈ। 
			            ਇਹ ਸ਼ੁਰੂਆਤੀ ਤੌਰ 'ਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਛੋਟੇ, ਭੂਰੇ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਪਾਈਰੇਨੋਫੋਰਾ ਟ੍ਰਾਈਟੀਸੀ-ਰੇਪੇਂਟਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਫਸਲ ਰੋਟੇਸ਼ਨ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲਾਗ ਦੇ ਸ਼ੁਰੂਆਤੀ ਸੰਕੇਤਾਂ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Blast':
			            st.write('''ਕਣਕ ਦਾ ਧਮਾਕਾ ਇੱਕ ਵਿਨਾਸ਼ਕਾਰੀ ਬਿਮਾਰੀ ਹੈ ਜੋ 1980 ਦੇ ਦਹਾਕੇ ਵਿੱਚ ਬ੍ਰਾਜ਼ੀਲ ਵਿੱਚ ਸਾਹਮਣੇ ਆਈ ਸੀ ਅਤੇ ਉਦੋਂ ਤੋਂ ਨੇੜਲੇ ਅਤੇ ਦੂਰ ਦੇ ਦੇਸ਼ਾਂ ਵਿੱਚ ਫੈਲ ਗਈ ਹੈ। 
			            ਜਲਵਾਯੂ ਪਰਿਵਰਤਨ ਤੋਂ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਉਹ ਇਸ ਦੇ ਫੈਲਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ, ਖਾਸ ਕਰਕੇ ਗਰਮ ਖੰਡੀ ਖੇਤਰਾਂ ਵਿੱਚ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਮੈਗਨਾਪੋਰਥ ਓਰੀਜ਼ਾ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਬਹੁਤ ਜ਼ਿਆਦਾ ਨਾਈਟ੍ਰੋਜਨ ਖਾਦ ਪਾਉਣ ਤੋਂ ਬਚੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣਾਂ ਦੇ ਪਹਿਲੇ ਲੱਛਣਾਂ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਫਸਲ ਰੋਟੇਸ਼ਨ ਦਾ ਅਭਿਆਸ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
			            st.write('''ਫੁਸੇਰੀਅਮ ਹੈੱਡ ਬਲਾਈਟ ਇੱਕ ਗੰਭੀਰ ਫੰਗਲ ਬਿਮਾਰੀ ਹੈ ਜੋ ਮਾਈਕੋਟੌਕਸਿਨ ਨਾਲ ਦੂਸ਼ਿਤ ਅਨਾਜ ਵੱਲ ਲੈ ਜਾਂਦੀ ਹੈ। 
			            ਇਸ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਝਾੜ ਘਟਦਾ ਹੈ, ਅਨਾਜ ਦੀ ਮਾੜੀ ਗੁਣਵੱਤਾ, ਅਤੇ ਕਣਕ ਉਤਪਾਦਕਾਂ ਲਈ ਮਹੱਤਵਪੂਰਨ ਆਰਥਿਕ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਫੁਸੇਰੀਅਮ ਸਪੀਸੀਜ਼ ਦੇ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਫਸਲ ਰੋਟੇਸ਼ਨ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਫੁੱਲਾਂ ਦੇ ਪੜਾਅ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਉੱਚ ਫੁਸੇਰੀਅਮ ਦਬਾਅ ਵਾਲੇ ਖੇਤਾਂ ਵਿੱਚ ਬੀਜਣ ਤੋਂ ਬਚੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mildew':
			            st.write('''ਕਣਕ ਵਿੱਚ ਪਾਊਡਰਰੀ ਫ਼ਫ਼ੂੰਦੀ ਚਿੱਟੇ ਮਾਈਸੀਲੀਅਮ ਦੇ ਸਤਹ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ ਅਤੇ ਅੰਤ ਵਿੱਚ ਪੂਰੇ ਪੱਤੇ ਨੂੰ ਢੱਕ ਸਕਦੀ ਹੈ, ਪਰਿਪੱਕ ਲਾਗਾਂ ਨਾਲ ਕਾਲੇ ਬੀਜਾਣੂ ਦੇ ਕੇਸ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। 
			            ਇਹ ਹਵਾ ਦੁਆਰਾ ਫੈਲਣ ਵਾਲੀ ਬਿਮਾਰੀ ਠੰਡੇ, ਗਿੱਲੇ ਮੌਸਮ ਵਿੱਚ ਵਧਦੀ ਹੈ ਅਤੇ 40% ਤੱਕ ਝਾੜ ਦਾ ਨੁਕਸਾਨ ਕਰ ਸਕਦੀ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਬਲੂਮੇਰੀਆ ਗ੍ਰਾਮਿਨਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਖੇਤ ਵਿੱਚ ਚੰਗੀ ਹਵਾ ਦਾ ਸੰਚਾਰ ਯਕੀਨੀ ਬਣਾਓ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Smut':
			            st.write('''ਢਿੱਲੀ smut ਦੀ ਇੱਕ ਵਿਆਪਕ ਵੰਡ ਹੁੰਦੀ ਹੈ ਅਤੇ ਜਿੱਥੇ ਵੀ ਕਣਕ ਪੈਦਾ ਹੁੰਦੀ ਹੈ ਉੱਥੇ ਹੋ ਸਕਦੀ ਹੈ। 
			            ਸਿਰਲੇਖ ਤੋਂ ਪਹਿਲਾਂ ਹਲਕੇ ਲੱਛਣ ਮੌਜੂਦ ਹੋ ਸਕਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ਪੱਤਿਆਂ ਦੀਆਂ ਪੀਲੀਆਂ ਧਾਰੀਆਂ ਅਤੇ ਸਖ਼ਤ, ਗੂੜ੍ਹੇ ਹਰੇ ਪੱਤੇ ਸ਼ਾਮਲ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Ustilago ਸਪੀਸੀਜ਼ ਵਰਗੀ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ.''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- smut-ਰੋਧਕ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਬੀਜਣ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜਾਂ ਨੂੰ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨਾਲ ਇਲਾਜ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰੋ।
			            \n- ਢੁਕਵੀਆਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Yellow Rust':
			            st.write('''ਪੀਲੀ ਜੰਗਾਲ ਦਾ ਵਿਸ਼ੇਸ਼ ਲੱਛਣ ਬਾਲਗ ਪੌਦਿਆਂ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਪੀਲੇ ਸੰਤਰੀ ਰੰਗ ਦੇ ਛਾਲਿਆਂ ਦੀਆਂ ਸਮਾਨਾਂਤਰ ਕਤਾਰਾਂ ਹਨ। 
			            ਪੀਲੀ ਜੰਗਾਲ ਦੀ ਮਹਾਂਮਾਰੀ ਅਕਸਰ ਵਿਅਕਤੀਗਤ ਪੌਦਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ, ਆਮ ਤੌਰ 'ਤੇ ਪਤਝੜ ਵਿੱਚ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Puccinia striformis ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
else:
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
		st.write('''<style>
		[data-testid="column"] {
		    width: calc(25% - 1rem) !important;
		    flex: 1 1 calc(25% - 1rem) !important;
		    min-width: calc(20% - 1rem) !important;
		}
		</style>''', unsafe_allow_html=True)
		
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
		
		languages = ["English", "ਪੰਜਾਬੀ", "हिंदी"]
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
		    col = st.columns([1,3])
		    col[0].image('logo.png')
		    col[1].text('')
		    col[1].text('')
		    col[1].text('')
		    col[1].text('')
		    if selected_language == "English":
		        col[1].markdown("<h1 style='text-align: center; color: white;'>WheatCheck - Wheat Disease Detection</h1>", unsafe_allow_html=True)
		    elif selected_language == "हिंदी":
		        col[1].markdown("<h1 style='text-align: center; color: white;'>वीटचेक - गेहूँ रोग का पता लगाये</h1>", unsafe_allow_html=True)
		    elif selected_language == "ਪੰਜਾਬੀ":
		        col[1].markdown("<h1 style='text-align: center; color: white;'>ਵੀਟਚੈੱਕ - ਕਣਕ ਦੀ ਬਿਮਾਰੀ ਦਾ ਪਤਾ ਲਗਾਓ</h1>", unsafe_allow_html=True)
		
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
			
		elif selected_language == "हिंदी":
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
			    
		elif selected_language == "ਪੰਜਾਬੀ":
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
			image_items = [
				dict(
			        title="Aphid",
			        img="aphid_1.jpeg",
				text=""
				),
				dict(
			        title="Brown Rust",
			        img="brown_rust_3.jpeg",
				text=""
				),
				dict(
			        title="Mite",
			        img="mite_26.jpeg",
				text=""
				),
				dict(
			        title="Stem Fly",
			        img="stem_fly_30.jpeg",
				text=""
				),
				dict(
			        title="Black Rust",
			        img="black_rust_1.jpeg",
				text=""
				),
				dict(
			        title="Common Root Rot",
			        img="common_root_rot_55.jpeg",
				text=""
				),
				dict(
			        title="Leaf Blight",
			        img="leaf_blight_38.jpeg",
				text=""
				),
				dict(
			        title="Septoria",
			        img="septoria_5.png",
				text=""
				),
				dict(
			        title="Tan Spot",
			        img="tan_spot_24.jpeg",
				text=""
				),
				dict(
			        title="Blast",
			        img="blast_1.jpeg",
				text=""
				),
				dict(
			        title="Fusarium Head Blight",
			        img="fusarium_head_blight_test_0.png",
				text=""
				),
				dict(
			        title="Mildew",
			        img="mildew_82.png",
				text=""
				),
				dict(
			        title="Smut",
			        img="smut_test_0.png",
				text=""
				),
				dict(
			        title="Yellow Rust",
			        img="yellow_rust_256.png",
				text=""
				),
				]
			carousel(items=image_items)
			
		elif selected_language == "हिंदी":
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
	
		elif selected_language == "ਪੰਜਾਬੀ":
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
	
		if selected_language == "हिंदी":
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
			        
			        if str(res[0].names[label[0]].title()) == 'Aphid':
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
			
			        if str(res[0].names[label[0]].title()) == 'Brown Rust':
			            st.write('''भूरा रतुआ गर्मियों के अंत में विकसित होता है और इसके परिणामस्वरूप हरी पत्ती के क्षेत्र में महत्वपूर्ण नुकसान होता है और इसलिए, उपज और विशिष्ट वजन में कमी आती है।''')
			            st.markdown('''कारण:
			            \n- पुकिनिया ट्रिटिसिना कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- गेहूं की प्रतिरोधी किस्में लगाएं।
			            \n- निवारक उपाय के रूप में फफूंदनाशकों का प्रयोग करें।''')
			            st.markdown('''उपाय:
			            \n- रोग का शीघ्र पता चलने पर फफूंदनाशी का प्रयोग करें।
			            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mite':
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
			
			        if str(res[0].names[label[0]].title()) == 'Stem Fly':
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
			
			        if str(res[0].names[label[0]].title()) == 'Black Rust':
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
			
			        if str(res[0].names[label[0]].title()) == 'Common Root Rot':
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
			
			        if str(res[0].names[label[0]].title()) == 'Leaf Blight':
			            st.write('''युवा पौधों पर चमकीले पीले किनारों के साथ लाल भूरे अंडाकार धब्बे दिखाई देते हैं। गंभीर मामलों में, कई धब्बे मिलकर पत्तियों के सूखने का कारण बनते हैं।''')
			            st.markdown('''कारण:
			            \n- बाइपोलारिस और अल्टरनेरिया प्रजाति जैसे कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग सावधानी से करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षणों की शुरुआत में फफूंदनाशी लगाएं।
			            \n- संक्रमित पौधे के अवशेषों को हटाएं और नष्ट करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Septoria':
			            st.write('''सेप्टोरिया ट्रिटिसी ब्लॉच मौसमों के बीच ठूंठ पर जीवित रहता है। 
			            देर से शरद ऋतु और शुरुआती सर्दियों में, बारिश या भारी ओस के कारण ठूंठ में पेरिथेसिया से हवा-जनित एस्कॉस्पोर निकलते हैं, जिससे बीमारी बड़ी दूरी तक फैल जाती है।''')
			            st.markdown('''कारण:
			            \n- सेप्टोरिया ट्रिटिसी कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग सावधानी से करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
			            \n- संक्रमित पत्तियों को हटाकर नष्ट कर दें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Tan Spot':
			            st.write('''टैन स्पॉट, जिसे पीली पत्ती वाले धब्बे के रूप में भी जाना जाता है, अमेरिका और कनाडा में उगाए जाने वाले गेहूं में एक आर्थिक रूप से महत्वपूर्ण बीमारी है। 
			            यह प्रारंभ में अतिसंवेदनशील गेहूं की किस्मों की पत्तियों पर छोटे, भूरे धब्बों के रूप में दिखाई देता है।''')
			            st.markdown('''कारण:
			            \n- पायरेनोफोरा ट्रिटिसी-रेपेंटिस कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फसल चक्र और स्वच्छ बीज का प्रयोग करें।''')
			            st.markdown('''उपाय:
			            \n- संक्रमण के शुरुआती लक्षणों पर फफूंदनाशी लगाएं।
			            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Blast':
			            st.write('''व्हीट ब्लास्ट एक विनाशकारी बीमारी है जो 1980 के दशक में ब्राज़ील में उभरी और तब से आस-पास और दूर-दराज के देशों में फैल गई है। 
			            उम्मीद है कि जलवायु परिवर्तन से इसके प्रसार में आसानी होगी, खासकर उष्णकटिबंधीय क्षेत्रों में।''')
			            st.markdown('''कारण:
			            \n- मैग्नापोर्थे ओराइजी कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- अत्यधिक नाइट्रोजन उर्वरक डालने से बचें।''')
			            st.markdown('''उपाय:
			            \n- लक्षणों के पहले संकेत पर फफूंदनाशी लगाएं।
			            \n- फसल चक्र का अभ्यास करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
			            st.write('''फ्यूसेरियम हेड ब्लाइट एक गंभीर कवक रोग है जिसके कारण अनाज मायकोटॉक्सिन से दूषित हो जाता है। 
			            इसके परिणामस्वरूप उपज में कमी, अनाज की खराब गुणवत्ता और गेहूं उत्पादकों को महत्वपूर्ण आर्थिक नुकसान होता है।''')
			            st.markdown('''कारण:
			            \n-फ्यूसेरियम प्रजाति के कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फसल चक्र और स्वच्छ बीज का प्रयोग करें।''')
			            st.markdown('''उपाय:
			            \n- फूल आने की अवस्था में फफूंदनाशकों का प्रयोग करें।
			            \n- उच्च फ्यूजेरियम दबाव वाले खेतों में रोपण से बचें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mildew':
			            st.write('''गेहूं में ख़स्ता फफूंदी सफेद मायसेलियम की सतह पर धब्बे के रूप में शुरू होती है और अंततः पूरी पत्ती को कवर कर सकती है, जिसमें परिपक्व संक्रमण के साथ काले बीजाणु के मामले दिखाई देते हैं। 
			            हवा से फैलने वाली यह बीमारी ठंडे, गीले मौसम में पनपती है और उपज को 40% तक नुकसान पहुंचा सकती है।''')
			            st.markdown('''कारण:
			            \n- ब्लूमेरिया ग्रेमिनिस कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग रोकथाम के लिए करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
			            \n- खेत में अच्छा वायु संचार सुनिश्चित करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Smut':
			            st.write('''ढीली स्मट का व्यापक वितरण होता है और यह कहीं भी हो सकता है जहां गेहूं का उत्पादन होता है। 
			            शीर्षासन से पहले हल्के लक्षण मौजूद हो सकते हैं, जिनमें पीली पत्ती की धारियाँ और कड़ी, गहरे हरे रंग की पत्तियाँ शामिल हैं।''')
			            st.markdown('''कारण:
			            \n- यूस्टिलैगो प्रजाति जैसे कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- स्मट-प्रतिरोधी किस्मों का उपयोग करें।
			            \n- रोपण से पहले बीजों को फफूंदनाशकों से उपचारित करें।''')
			            st.markdown('''उपाय:
			            \n- संक्रमित पौधों को नष्ट कर दें।
			            \n- उचित फफूंदनाशकों का प्रयोग करें।''')
			
			        if str(res[0].names[label[0]].title()) == 'Yellow Rust':
			            st.write('''पीले रतुआ का विशिष्ट लक्षण वयस्क पौधों की पत्तियों पर पीले नारंगी रंग की फुंसियों की समानांतर पंक्तियाँ होना है। 
			            पीले रतुआ की महामारी अक्सर व्यक्तिगत पौधों के रूप में शुरू होती है, आमतौर पर शरद ऋतु में।''')
			            st.markdown('''कारण:
			            \n- पुकिनिया स्ट्राइफोर्मिस कवक के कारण होता है।''')
			            st.markdown('''रोकथाम:
			            \n- प्रतिरोधी किस्में लगाएं।
			            \n- फफूंदनाशकों का प्रयोग रोकथाम के लिए करें।''')
			            st.markdown('''उपाय:
			            \n- लक्षण दिखाई देने पर फफूंदनाशक लगाएं।
			            \n- संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।''')
					
		if selected_language == "ਪੰਜਾਬੀ":
			st.subheader('ਸ਼ੁਰੂਆਤੀ ਖੋਜ ਵਿੱਚ ਤਕਨਾਲੋਜੀ ਦੀ ਭੂਮਿਕਾ')
			st.write('''ਇਹਨਾਂ ਚੁਣੌਤੀਆਂ ਦੇ ਜਵਾਬ ਵਿੱਚ, ਤਕਨਾਲੋਜੀ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਹੱਲ ਪੇਸ਼ ਕਰਦੀ ਹੈ। 
		  	Wheat Detection ਵੈੱਬ ਐਪ ਸ਼ੁਰੂਆਤੀ ਪੜਾਅ 'ਤੇ ਕਣਕ ਦੀਆਂ ਫਸਲਾਂ ਵਿੱਚ ਬਿਮਾਰੀਆਂ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਨਕਲੀ ਬੁੱਧੀ ਅਤੇ ਮਸ਼ੀਨ ਸਿਖਲਾਈ ਦੀ ਸ਼ਕਤੀ ਨੂੰ ਵਰਤਦਾ ਹੈ। 
		    	ਕਣਕ ਦੇ ਖੇਤਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ, ਐਪ ਬਿਮਾਰੀ ਦੇ ਲੱਛਣਾਂ ਦਾ ਸਹੀ ਪਤਾ ਲਗਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਕਿਸਾਨਾਂ ਨੂੰ ਤੁਰੰਤ ਕਾਰਵਾਈ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ। 
		      	ਬਿਮਾਰੀ ਦੇ ਫੈਲਣ ਨੂੰ ਰੋਕਣ, ਫਸਲਾਂ ਦੀ ਉਪਜ ਦੀ ਰੱਖਿਆ ਕਰਨ, ਅਤੇ ਇੱਕ ਸਥਿਰ ਭੋਜਨ ਸਪਲਾਈ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਸ਼ੁਰੂਆਤੀ ਖੋਜ ਮਹੱਤਵਪੂਰਨ ਹੈ।''')
			st.image('farmer.webp')
			st.subheader('ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ')
			st.markdown('''
			1. ਚਿੱਤਰ ਕੈਪਚਰ: ਕਿਸਾਨ ਸਮਾਰਟਫੋਨ ਜਾਂ ਡਰੋਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਕਣਕ ਦੇ ਖੇਤਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਕੈਪਚਰ ਕਰਦੇ ਹਨ।
			2. ਵਿਸ਼ਲੇਸ਼ਣ: ਐਪ ਖਾਸ ਰੋਗਾਂ ਦੇ ਪੈਟਰਨਾਂ ਨੂੰ ਪਛਾਣਨ ਲਈ ਸਿਖਲਾਈ ਪ੍ਰਾਪਤ ਤਕਨੀਕੀ ਮਸ਼ੀਨ ਸਿਖਲਾਈ ਐਲਗੋਰਿਦਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹਨਾਂ ਚਿੱਤਰਾਂ 'ਤੇ ਪ੍ਰਕਿਰਿਆ ਕਰਦੀ ਹੈ।
			3. ਨਿਦਾਨ: ਐਪ ਇੱਕ ਤਤਕਾਲ ਨਿਦਾਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਬਿਮਾਰੀ ਦੀ ਕਿਸਮ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ ਅਤੇ ਇਲਾਜ ਲਈ ਸੁਝਾਅ ਪੇਸ਼ ਕਰਦਾ ਹੈ।
			4. ਕਾਰਵਾਈਯੋਗ ਸੂਝ: ਕਿਸਾਨਾਂ ਨੂੰ ਇਸ ਬਾਰੇ ਸਿਫ਼ਾਰਸ਼ਾਂ ਮਿਲਦੀਆਂ ਹਨ ਕਿ ਖੋਜੀ ਗਈ ਬਿਮਾਰੀ ਦਾ ਪ੍ਰਬੰਧਨ ਕਿਵੇਂ ਕਰਨਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਭਾਵ ਨੂੰ ਘਟਾਉਣ ਲਈ ਅਨੁਕੂਲ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਅਤੇ ਖੇਤੀ ਵਿਗਿਆਨਿਕ ਅਭਿਆਸਾਂ ਸ਼ਾਮਲ ਹਨ।''')
			st.subheader('ਪ੍ਰਭਾਵ')
			st.write('ਇਸ ਤਕਨੀਕ ਨੂੰ ਆਪਣੇ ਖੇਤੀ ਅਭਿਆਸਾਂ ਵਿੱਚ ਜੋੜ ਕੇ, ਕਿਸਾਨ ਕਣਕ ਦੀਆਂ ਬਿਮਾਰੀਆਂ ਕਾਰਨ ਹੋਣ ਵਾਲੇ ਨੁਕਸਾਨ ਨੂੰ ਕਾਫ਼ੀ ਹੱਦ ਤੱਕ ਘਟਾ ਸਕਦੇ ਹਨ। Wheat Detection ਐਪ ਨਾ ਸਿਰਫ਼ ਫ਼ਸਲਾਂ ਦੀ ਪੈਦਾਵਾਰ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ, ਸਗੋਂ ਭੋਜਨ ਸੁਰੱਖਿਆ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਅਤੇ ਭੁੱਖਮਰੀ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਵਿਸ਼ਵਵਿਆਪੀ ਯਤਨਾਂ ਵਿੱਚ ਵੀ ਯੋਗਦਾਨ ਪਾਉਂਦੀ ਹੈ। ਆਰਥਿਕ ਲਾਭ ਵੀ ਕਾਫੀ ਹੁੰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਕਿਸਾਨਾਂ ਨੂੰ ਵੱਧ ਤੋਂ ਵੱਧ ਲਾਭ ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ ਅਤੇ ਕਣਕ ਦੀ ਮੰਡੀ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ।')
			st.subheader('ਅੰਦੋਲਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ')
			st.write('ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਇੱਕ ਅਜਿਹੇ ਭਵਿੱਖ ਵੱਲ ਵਧਦੇ ਹਾਂ ਜਿੱਥੇ ਤਕਨਾਲੋਜੀ ਖੇਤੀਬਾੜੀ ਵਿੱਚ ਇੱਕ ਅਨਿੱਖੜਵਾਂ ਭੂਮਿਕਾ ਨਿਭਾਉਂਦੀ ਹੈ, ਕਣਕ ਖੋਜ ਐਪ ਇਸ ਕ੍ਰਾਂਤੀ ਵਿੱਚ ਸਭ ਤੋਂ ਅੱਗੇ ਹੈ। ਦੁਨੀਆ ਦੀਆਂ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਫਸਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਦੀ ਰੱਖਿਆ ਕਰਨ ਅਤੇ ਵਿਸ਼ਵ ਭੋਜਨ ਸੁਰੱਖਿਆ ਦੇ ਭਵਿੱਖ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਵਿੱਚ ਸਾਡੇ ਨਾਲ ਸ਼ਾਮਲ ਹੋਵੋ।')
			
			st.subheader('ਐਪ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਕਦਮ')
			st.markdown('''
			- ਇੱਕ ਸਪਸ਼ਟ ਚਿੱਤਰ ਲਓ
			- ਚਿੱਤਰ ਅੱਪਲੋਡ ਕਰੋ
			- ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ ਅਤੇ ਬਿਮਾਰੀ ਦੇ ਨਾਮ ਅਤੇ ਵਿਸ਼ਵਾਸ ਪੱਧਰ ਦੇ ਨਾਲ ਕਾਰਨ, ਰੋਕਥਾਮ ਅਤੇ ਉਪਚਾਰ ਹੇਠਾਂ ਨਤੀਜੇ ਪੈਨਲ ਵਿੱਚ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੇ ਜਾਣਗੇ।''')
			
			# Image upload and analysis section
			with st.container():
			    img = st.file_uploader('ਆਪਣੀ ਤਸਵੀਰ ਅੱਪਲੋਡ ਕਰੋ', type=['jpg', 'png', 'jpeg'])
			    analyse = st.button('ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ')
			    
			if analyse:
			    if img is not None:
			        img = Image.open(img)
			        st.markdown('ਚਿੱਤਰ ਵਿਜ਼ੂਅਲਾਈਜ਼ੇਸ਼ਨ')
			        st.image(img)
			        st.subheader('ਕਣਕ ਦੀ ਇਹ ਫਸਲ ਇਨ੍ਹਾਂ ਕਾਰਨਾਂ ਕਰਕੇ ਪ੍ਰਭਾਵਿਤ ਹੋਈ ਹੈ:')
			        model = models()
			        res = model.predict(img)
			        label = res[0].probs.top5
			        conf = res[0].probs.top5conf
			        conf = conf.tolist()
			        st.write('ਰੋਗ: ' + str(res[0].names[label[0]].title()))
			        st.write('ਵਿਸ਼ਵਾਸ ਪੱਧਰ: ' + str(conf[0]))
			        
			        if str(res[0].names[label[0]].title()) == 'Aphid':
			            st.write('''ਐਫੀਡਜ਼ ਰਸ ਚੂਸਣ ਵਾਲੇ, ਨਰਮ ਸਰੀਰ ਵਾਲੇ ਕੀੜਿਆਂ ਦਾ ਇੱਕ ਸਮੂਹ ਹੈ ਜੋ ਕਿ ਪਿੰਨਹੈੱਡ ਦੇ ਆਕਾਰ ਦੇ ਹੁੰਦੇ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਐਫੀਡਸ ਰਸ ਚੂਸ ਕੇ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਝਾੜ ਘੱਟ ਜਾਂਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਕੀਟਨਾਸ਼ਕ ਸਾਬਣ ਜਾਂ ਨਿੰਮ ਦੇ ਤੇਲ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਲੇਡੀਬੱਗ ਵਰਗੇ ਕੁਦਰਤੀ ਸ਼ਿਕਾਰੀਆਂ ਨੂੰ ਉਤਸ਼ਾਹਿਤ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਕੀਟਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ ਜੇਕਰ ਸੰਕਰਮਣ ਗੰਭੀਰ ਹੋਵੇ।
			            \n- ਐਫਿਡ ਜੀਵਨ ਚੱਕਰ ਨੂੰ ਵਿਗਾੜਨ ਲਈ ਫਸਲੀ ਚੱਕਰ ਵਰਗੀਆਂ ਸੱਭਿਆਚਾਰਕ ਅਭਿਆਸਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Brown Rust':
			            st.write('''ਭੂਰੀ ਜੰਗਾਲ ਗਰਮੀਆਂ ਦੇ ਅਖੀਰ ਵਿੱਚ ਵਿਕਸਤ ਹੁੰਦਾ ਹੈ ਅਤੇ ਨਤੀਜੇ ਵਜੋਂ ਹਰੇ ਪੱਤਿਆਂ ਦੇ ਖੇਤਰ ਵਿੱਚ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ ਅਤੇ, ਇਸਲਈ, ਝਾੜ ਅਤੇ ਖਾਸ ਭਾਰ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Puccinia triticina ਉੱਲੀ ਦੇ ਕਾਰਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ। 
			            \n- ਰੋਕਥਾਮ ਉਪਾਅ ਵਜੋਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਬਿਮਾਰੀ ਦਾ ਛੇਤੀ ਪਤਾ ਲੱਗਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mite':
			            st.write('''ਦੇਕਣ ਛੋਟੇ, ਲਾਲ-ਭੂਰੇ ਤੋਂ ਕਾਲੇ, ਅੱਠ ਪੈਰਾਂ ਵਾਲੇ ਅਰਚਨਿਡ ਹੁੰਦੇ ਹਨ ਜੋ ਕਣਕ ਦੀਆਂ ਫਸਲਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ, ਖਾਸ ਕਰਕੇ ਗਰਮ, ਸੁੱਕੀਆਂ ਸਥਿਤੀਆਂ ਵਿੱਚ। 
			            ਇਹ ਹਵਾ, ਮਸ਼ੀਨਰੀ ਅਤੇ ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਦੀ ਸਮੱਗਰੀ ਰਾਹੀਂ ਫੈਲਦੇ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਕੀੜੇ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਨੂੰ ਸੰਕਰਮਿਤ ਕਰਦੇ ਹਨ, ਰਸ ਚੂਸਦੇ ਹਨ ਅਤੇ ਵਾਇਰਸ ਫੈਲਾਉਂਦੇ ਹਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਕੀਟ-ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਜੇਕਰ ਲੋੜ ਹੋਵੇ ਤਾਂ ਮਾਈਟੀਸਾਈਡਸ ਲਾਗੂ ਕਰੋ।
			            \n- ਸਹੀ ਸਿੰਚਾਈ ਸੰਕਰਮਣ ਦੇ ਜੋਖਮ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਉਚਿਤ ਮਾਈਟੀਸਾਈਡਸ ਲਾਗੂ ਕਰੋ।
			            \n- ਖੇਤ ਦੀ ਸਹੀ ਸਫਾਈ ਬਣਾਈ ਰੱਖੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Stem Fly':
			            st.write('''ਕਣਕ ਦੇ ਤਣੇ ਦੀ ਆਰਾ (Cephus cinctus) Hymenoptera (ਜਿਵੇਂ ਕਿ ਮਧੂ-ਮੱਖੀਆਂ, ਭਾਂਡੇ ਅਤੇ ਕੀੜੀਆਂ) ਦੇ ਕ੍ਰਮ ਵਿੱਚ ਸੇਫੀਡੇ ਪਰਿਵਾਰ ਵਿੱਚੋਂ ਇੱਕ ਆਦਿਮ, ਭਾਂਡੇ-ਵਰਗੇ ਕੀੜੇ ਹਨ। 
			            ਇਸ ਦੇ ਲਾਰਵੇ ਬਸੰਤ ਅਤੇ ਸਰਦੀਆਂ ਦੀ ਕਣਕ ਦੇ ਮਹੱਤਵਪੂਰਨ ਕੀੜੇ ਹਨ, ਜਿਸ ਨਾਲ ਫਸਲਾਂ ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ ਝਾੜ ਘਟਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਡੰਡੀ ਦੀਆਂ ਮੱਖੀਆਂ ਕਣਕ ਦੇ ਪੌਦਿਆਂ 'ਤੇ ਅੰਡੇ ਦਿੰਦੀਆਂ ਹਨ, ਅਤੇ ਲਾਰਵੇ ਤਣੀਆਂ ਵਿੱਚ ਛਾ ਜਾਂਦੇ ਹਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਪੀਕ ਸਟੈਮ ਫਲਾਈ ਗਤੀਵਿਧੀ ਤੋਂ ਬਚਣ ਲਈ ਜਲਦੀ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਉਪਾਅ ਵਜੋਂ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲਾਰਵੇ ਪੜਾਅ 'ਤੇ ਕੀਟਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Black Rust':
			            st.write('''ਕਾਲੀ ਕੁੰਗੀ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਦੇ ਤਣੇ ਅਤੇ ਪੱਤਿਆਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਉਪਜ ਦਾ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਅਤੇ ਆਰਥਿਕ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ। 
			            ਇਹ ਕਾਲੇ ਜਾਂ ਗੂੜ੍ਹੇ ਭੂਰੇ ਰੰਗ ਦੇ ਉੱਚੇ ਹੋਏ ਛਾਲੇ ਪੈਦਾ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਜੰਗਾਲ-ਰੰਗ ਦੇ ਬੀਜਾਣੂ ਹੁੰਦੇ ਹਨ। ਜੇਕਰ ਕੰਟਰੋਲ ਨਾ ਕੀਤਾ ਜਾਵੇ, ਤਾਂ ਇਹ ਤੇਜ਼ੀ ਨਾਲ ਫੈਲ ਸਕਦਾ ਹੈ ਅਤੇ ਪੂਰੇ ਖੇਤਾਂ ਨੂੰ ਤਬਾਹ ਕਰ ਸਕਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Puccinia graminis ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Common Root Rot':
			            st.write('''ਕਣਕ ਦੀਆਂ ਜੜ੍ਹਾਂ ਦੀਆਂ ਸੜਨ ਵੱਖ-ਵੱਖ ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦੀਆਂ ਹਨ ਜੋ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਦੀਆਂ ਜੜ੍ਹਾਂ ਅਤੇ ਤਾਜ ਦੇ ਟਿਸ਼ੂ 'ਤੇ ਹਮਲਾ ਕਰਦੀਆਂ ਹਨ। 
			            ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੇ ਤਾਜ ਅਤੇ ਜੜ੍ਹਾਂ ਦੇ ਟਿਸ਼ੂਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰ ਦਿੱਤਾ ਹੈ, ਜਿਸਦੇ ਨਤੀਜੇ ਵਜੋਂ ਪਾਣੀ ਅਤੇ ਪੌਸ਼ਟਿਕ ਤੱਤਾਂ ਦੀ ਖਪਤ ਰੁਕ ਜਾਂਦੀ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਬਾਇਪੋਲਾਰਿਸ ਸੋਰੋਕਿਨਿਆਨਾ ਵਰਗੀ ਉੱਲੀ ਦੇ ਕਾਰਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਗ ਮੁਕਤ ਬੀਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਗੈਰ-ਹੋਸਟ ਫਸਲਾਂ ਦੇ ਨਾਲ ਫਸਲੀ ਰੋਟੇਸ਼ਨ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਢੁਕਵੀਆਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਮਿੱਟੀ ਦੀ ਨਿਕਾਸੀ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Leaf Blight':
			            st.write('''ਚਮਕਦਾਰ ਪੀਲੇ ਹਾਸ਼ੀਏ ਵਾਲੇ ਛੋਟੇ ਬੂਟਿਆਂ 'ਤੇ ਲਾਲ ਭੂਰੇ ਅੰਡਾਕਾਰ ਧੱਬੇ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। ਗੰਭੀਰ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਕਈ ਚਟਾਕ ਪੱਤੇ ਦੇ ਸੁੱਕਣ ਦਾ ਕਾਰਨ ਬਣਦੇ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਬਾਇਪੋਲਾਰਿਸ ਅਤੇ ਅਲਟਰਨੇਰੀਆ ਸਪੀਸੀਜ਼ ਵਰਗੀਆਂ ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣਾਂ ਦੀ ਸ਼ੁਰੂਆਤ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Septoria':
			            st.write('''ਸੇਪਟੋਰੀਆ ਟ੍ਰਾਈਟੀਸੀ ਬਲੋਚ ਮੌਸਮਾਂ ਦੇ ਵਿਚਕਾਰ ਪਰਾਲੀ 'ਤੇ ਜਿਉਂਦਾ ਰਹਿੰਦਾ ਹੈ। 
			            ਪਤਝੜ ਦੇ ਅਖੀਰ ਅਤੇ ਸਰਦੀਆਂ ਦੇ ਸ਼ੁਰੂ ਵਿੱਚ, ਮੀਂਹ ਜਾਂ ਭਾਰੀ ਤ੍ਰੇਲ ਪਰਾਲੀ ਵਿੱਚ ਪੈਰੀਥੀਸੀਆ ਤੋਂ ਹਵਾ ਦੁਆਰਾ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਐਸਕੋਸਪੋਰਸ ਨੂੰ ਛੱਡਣ ਦਾ ਕਾਰਨ ਬਣਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਬਿਮਾਰੀ ਵੱਡੀ ਦੂਰੀ ਤੱਕ ਫੈਲ ਜਾਂਦੀ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਸੇਪਟੋਰੀਆ ਟ੍ਰਾਈਟੀਸੀ ਉੱਲੀ ਦੇ ਕਾਰਨ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਸੰਕਰਮਿਤ ਪੱਤਿਆਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Tan Spot':
			            st.write('''ਟੈਨ ਸਪਾਟ, ਜਿਸ ਨੂੰ ਪੀਲੇ ਪੱਤੇ ਦੇ ਸਥਾਨ ਵਜੋਂ ਵੀ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਅਮਰੀਕਾ ਅਤੇ ਕੈਨੇਡਾ ਵਿੱਚ ਉਗਾਈ ਜਾਣ ਵਾਲੀ ਕਣਕ ਵਿੱਚ ਆਰਥਿਕ ਤੌਰ 'ਤੇ ਮਹੱਤਵਪੂਰਨ ਬਿਮਾਰੀ ਹੈ। 
			            ਇਹ ਸ਼ੁਰੂਆਤੀ ਤੌਰ 'ਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਛੋਟੇ, ਭੂਰੇ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਪਾਈਰੇਨੋਫੋਰਾ ਟ੍ਰਾਈਟੀਸੀ-ਰੇਪੇਂਟਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਫਸਲ ਰੋਟੇਸ਼ਨ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲਾਗ ਦੇ ਸ਼ੁਰੂਆਤੀ ਸੰਕੇਤਾਂ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Blast':
			            st.write('''ਕਣਕ ਦਾ ਧਮਾਕਾ ਇੱਕ ਵਿਨਾਸ਼ਕਾਰੀ ਬਿਮਾਰੀ ਹੈ ਜੋ 1980 ਦੇ ਦਹਾਕੇ ਵਿੱਚ ਬ੍ਰਾਜ਼ੀਲ ਵਿੱਚ ਸਾਹਮਣੇ ਆਈ ਸੀ ਅਤੇ ਉਦੋਂ ਤੋਂ ਨੇੜਲੇ ਅਤੇ ਦੂਰ ਦੇ ਦੇਸ਼ਾਂ ਵਿੱਚ ਫੈਲ ਗਈ ਹੈ। 
			            ਜਲਵਾਯੂ ਪਰਿਵਰਤਨ ਤੋਂ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਉਹ ਇਸ ਦੇ ਫੈਲਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ, ਖਾਸ ਕਰਕੇ ਗਰਮ ਖੰਡੀ ਖੇਤਰਾਂ ਵਿੱਚ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਮੈਗਨਾਪੋਰਥ ਓਰੀਜ਼ਾ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਬਹੁਤ ਜ਼ਿਆਦਾ ਨਾਈਟ੍ਰੋਜਨ ਖਾਦ ਪਾਉਣ ਤੋਂ ਬਚੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣਾਂ ਦੇ ਪਹਿਲੇ ਲੱਛਣਾਂ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਫਸਲ ਰੋਟੇਸ਼ਨ ਦਾ ਅਭਿਆਸ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Fusarium Head Blight':
			            st.write('''ਫੁਸੇਰੀਅਮ ਹੈੱਡ ਬਲਾਈਟ ਇੱਕ ਗੰਭੀਰ ਫੰਗਲ ਬਿਮਾਰੀ ਹੈ ਜੋ ਮਾਈਕੋਟੌਕਸਿਨ ਨਾਲ ਦੂਸ਼ਿਤ ਅਨਾਜ ਵੱਲ ਲੈ ਜਾਂਦੀ ਹੈ। 
			            ਇਸ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਝਾੜ ਘਟਦਾ ਹੈ, ਅਨਾਜ ਦੀ ਮਾੜੀ ਗੁਣਵੱਤਾ, ਅਤੇ ਕਣਕ ਉਤਪਾਦਕਾਂ ਲਈ ਮਹੱਤਵਪੂਰਨ ਆਰਥਿਕ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਫੁਸੇਰੀਅਮ ਸਪੀਸੀਜ਼ ਦੇ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਫਸਲ ਰੋਟੇਸ਼ਨ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਫੁੱਲਾਂ ਦੇ ਪੜਾਅ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਉੱਚ ਫੁਸੇਰੀਅਮ ਦਬਾਅ ਵਾਲੇ ਖੇਤਾਂ ਵਿੱਚ ਬੀਜਣ ਤੋਂ ਬਚੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Mildew':
			            st.write('''ਕਣਕ ਵਿੱਚ ਪਾਊਡਰਰੀ ਫ਼ਫ਼ੂੰਦੀ ਚਿੱਟੇ ਮਾਈਸੀਲੀਅਮ ਦੇ ਸਤਹ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ ਅਤੇ ਅੰਤ ਵਿੱਚ ਪੂਰੇ ਪੱਤੇ ਨੂੰ ਢੱਕ ਸਕਦੀ ਹੈ, ਪਰਿਪੱਕ ਲਾਗਾਂ ਨਾਲ ਕਾਲੇ ਬੀਜਾਣੂ ਦੇ ਕੇਸ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। 
			            ਇਹ ਹਵਾ ਦੁਆਰਾ ਫੈਲਣ ਵਾਲੀ ਬਿਮਾਰੀ ਠੰਡੇ, ਗਿੱਲੇ ਮੌਸਮ ਵਿੱਚ ਵਧਦੀ ਹੈ ਅਤੇ 40% ਤੱਕ ਝਾੜ ਦਾ ਨੁਕਸਾਨ ਕਰ ਸਕਦੀ ਹੈ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- ਬਲੂਮੇਰੀਆ ਗ੍ਰਾਮਿਨਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਖੇਤ ਵਿੱਚ ਚੰਗੀ ਹਵਾ ਦਾ ਸੰਚਾਰ ਯਕੀਨੀ ਬਣਾਓ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Smut':
			            st.write('''ਢਿੱਲੀ smut ਦੀ ਇੱਕ ਵਿਆਪਕ ਵੰਡ ਹੁੰਦੀ ਹੈ ਅਤੇ ਜਿੱਥੇ ਵੀ ਕਣਕ ਪੈਦਾ ਹੁੰਦੀ ਹੈ ਉੱਥੇ ਹੋ ਸਕਦੀ ਹੈ। 
			            ਸਿਰਲੇਖ ਤੋਂ ਪਹਿਲਾਂ ਹਲਕੇ ਲੱਛਣ ਮੌਜੂਦ ਹੋ ਸਕਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ਪੱਤਿਆਂ ਦੀਆਂ ਪੀਲੀਆਂ ਧਾਰੀਆਂ ਅਤੇ ਸਖ਼ਤ, ਗੂੜ੍ਹੇ ਹਰੇ ਪੱਤੇ ਸ਼ਾਮਲ ਹਨ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Ustilago ਸਪੀਸੀਜ਼ ਵਰਗੀ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ.''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- smut-ਰੋਧਕ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।
			            \n- ਬੀਜਣ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜਾਂ ਨੂੰ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨਾਲ ਇਲਾਜ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰੋ।
			            \n- ਢੁਕਵੀਆਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।''')
			
			        if str(res[0].names[label[0]].title()) == 'Yellow Rust':
			            st.write('''ਪੀਲੀ ਜੰਗਾਲ ਦਾ ਵਿਸ਼ੇਸ਼ ਲੱਛਣ ਬਾਲਗ ਪੌਦਿਆਂ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਪੀਲੇ ਸੰਤਰੀ ਰੰਗ ਦੇ ਛਾਲਿਆਂ ਦੀਆਂ ਸਮਾਨਾਂਤਰ ਕਤਾਰਾਂ ਹਨ। 
			            ਪੀਲੀ ਜੰਗਾਲ ਦੀ ਮਹਾਂਮਾਰੀ ਅਕਸਰ ਵਿਅਕਤੀਗਤ ਪੌਦਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ, ਆਮ ਤੌਰ 'ਤੇ ਪਤਝੜ ਵਿੱਚ।''')
			            st.markdown('''ਕਾਰਨ:
			            \n- Puccinia striformis ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।''')
			            st.markdown('''ਰੋਕਥਾਮ:
			            \n- ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।
			            \n- ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।''')
			            st.markdown('''ਉਪਾਅ:
			            \n- ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।
			            \n- ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।''')
