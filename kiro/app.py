import streamlit as st

st.set_page_config(page_title="Multilingual Mandi AI", layout="centered")

st.title("🌾 Multilingual Mandi AI")
st.write("AI-powered mandi price explanation in local languages")

# Input
crop = st.text_input("Enter crop name", "Tomato")
language = st.selectbox("Select language", ["Telugu", "Hindi", "Tamil", "English"])
price = st.number_input("Enter current price (₹/quintal)", value=1800)

if st.button("Get AI Explanation"):
    if language == "Telugu":
        output = f"""
టమోటా ప్రస్తుతం ధర క్వింటాల్‌కు ₹{price}.
ఇది గత వారంతో పోలిస్తే సాధారణ స్థాయి ధర.
మీ ప్రాంతంలో సరఫరా ఎక్కువగా ఉంటే కొంతకాలం వేచి చూడటం మంచిది.
"""
    elif language == "Hindi":
        output = f"""
टमाटर का वर्तमान मूल्य ₹{price} प्रति क्विंटल है।
यह सामान्य स्तर का मूल्य है।
यदि आप तुरंत बेचते हैं तो ठीक है, अन्यथा कुछ दिन प्रतीक्षा कर सकते हैं।
"""
    elif language == "Tamil":
        output = f"""
தக்காளியின் தற்போதைய விலை குவிண்டாலுக்கு ₹{price}.
விலை சராசரி நிலையில் உள்ளது.
விற்பனைக்கு முன் சந்தை நிலையை கவனிக்கவும்.
"""
    else:
        output = f"""
The current price of {crop} is ₹{price} per quintal.
This is an average market price.
You may sell now or wait based on local demand.
"""

    st.subheader("AI Response")
    st.write(output)
