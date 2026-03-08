import streamlit as st
import os
from groq import Groq

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry / Category")

objective = st.selectbox(
    "Campaign Objective",
    ["Engagement", "Promotion", "Awareness", "Product Launch"]
)

products = st.text_area("Describe the brand products/services")

if st.button("Generate Tweets"):

    client = Groq(api_key="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")

    prompt = f"""
You are a social media strategist.

Brand name: {brand}
Industry: {industry}
Campaign objective: {objective}
Products: {products}

Step 1: Analyse the brand voice and provide:
- tone
- target audience
- communication style
- content themes

Step 2: Generate 10 tweets in that voice.

Tweet style mix:
- engaging
- promotional
- witty
- informative

Output format:

Brand Voice Summary:
- bullet points

Tweets:
1.
2.
3.
...
10.
"""

    response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="llama-3.1-8b-instant",
    temperature=0.8
    )

    st.write(response.choices[0].message.content)