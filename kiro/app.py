import streamlit as st

st.set_page_config(page_title="Multilingual Mandi AI", layout="centered")

st.title("🌾 Multilingual Mandi AI")
st.write("AI-powered mandi price explanation in local languages")

# Sample mandi prices
sample_prices = {
    "Tomato": 1800,
    "Onion": 2200,
    "Potato": 1600,
    "Chilli": 4500
}

crop = st.selectbox("Select crop", list(sample_prices.keys()))
language = st.selectbox("Select language", ["Telugu", "Hindi", "Tamil", "English"])

price = sample_prices[crop]

st.write(f"📊 Current mandi price: ₹{price} per quintal")

if st.button("Get AI Explanation"):
    if language == "Telugu":
        output = f"""
{crop} ప్రస్తుతం ధర క్వింటాల్‌కు ₹{price}.
ఇది మార్కెట్‌లో సాధారణ స్థాయి ధర.
ఇప్పుడే అమ్ముకోవచ్చు లేదా కొంతకాలం వేచి చూడవచ్చు.
"""
    elif language == "Hindi":
        output = f"""
{crop} का वर्तमान मूल्य ₹{price} प्रति क्विंटल है।
यह सामान्य बाजार मूल्य है।
"""
    elif language == "Tamil":
        output = f"""
{crop} தற்போதைய விலை குவிண்டாலுக்கு ₹{price}.
விலை சராசரி நிலையில் உள்ளது.
"""
    else:
        output = f"""
The current price of {crop} is ₹{price} per quintal.
This is an average market price.
"""

    st.subheader("AI Response")
    st.write(output)
