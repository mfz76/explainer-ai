import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Lucid",
    page_icon="✦",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background-color: #0F1117;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.header {
    text-align: center;
    padding: 52px 0 36px 0;
}

.eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #7C6FE0;
    margin-bottom: 14px;
}

.title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.2rem;
    font-weight: 400;
    color: #E8E6F0;
    line-height: 1.1;
    margin-bottom: 14px;
}

.subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: #6B7090;
    font-weight: 300;
}

div[data-testid="stTextInput"] label {
    display: none !important;
}

div[data-testid="stTextInput"] input {
    background-color: #1A1D27 !important;
    border: 1.5px solid #2A2D45 !important;
    border-radius: 14px !important;
    color: #E8E6F0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.05rem !important;
    padding: 16px 20px !important;
    caret-color: #7C6FE0 !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #7C6FE0 !important;
    box-shadow: 0 0 0 3px rgba(124, 111, 224, 0.15) !important;
    outline: none !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #3D4060 !important;
}

div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #7C6FE0 0%, #5A50C8 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.97rem !important;
    letter-spacing: 0.02em !important;
    width: 100% !important;
    padding: 14px !important;
    margin-top: 4px !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stButton"] button:hover {
    background: linear-gradient(135deg, #8D80F0 0%, #6A60D8 100%) !important;
    box-shadow: 0 8px 28px rgba(124, 111, 224, 0.35) !important;
    transform: translateY(-1px) !important;
}

.output-wrapper {
    margin-top: 36px;
    border-radius: 18px;
    padding: 2px;
    background: linear-gradient(135deg, #7C6FE0, #2A2D45, #2A2D45);
}

.output-card {
    background-color: #141722;
    border-radius: 16px;
    padding: 32px 36px;
}

.output-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #7C6FE0;
    margin-bottom: 18px;
}

.output-text {
    font-family: 'Lora', serif;
    font-size: 1.05rem;
    line-height: 1.9;
    color: #B8B6CC;
}

.footer {
    text-align: center;
    color: #363A55;
    font-size: 0.7rem;
    font-family: 'DM Sans', sans-serif;
    margin-top: 52px;
    padding-bottom: 36px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <div class="eyebrow">✦ Powered by Llama 3.3</div>
    <div class="title">Lucid.</div>
    <div class="subtitle">Type any topic. Get a clear, engaging explanation in seconds.</div>
</div>
""", unsafe_allow_html=True)

# Input
topic = st.text_input(
    label="topic",
    placeholder="e.g. How does WiFi work? What is the stock market? What is a black hole?"
)

# Button + Output
if st.button("Explain →"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Thinking..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Explain '{topic}' in simple, clear, and engaging terms. "
                                f"Write like you're talking to a curious, intelligent 17-year-old. "
                                f"Use vivid real-world examples and make it genuinely interesting. "
                                f"Write in flowing paragraphs — no bullet points."
                            )
                        }
                    ]
                )
                explanation = response.choices[0].message.content

                st.markdown(f"""
                    <div class="output-wrapper">
                        <div class="output-card">
                            <div class="output-label">Explaining — {topic}</div>
                            <div class="output-text">{explanation}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            except KeyError:
                st.error("API key not found. Add GROQ_API_KEY to your Streamlit secrets.")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

# Footer
st.markdown(
    '<div class="footer">Lucid · Llama 3.3 · Groq · Built by Faraz</div>',
    unsafe_allow_html=True
)
