import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
st.set_page_config(page_title="Automated Content Generator", page_icon="✍️", layout="wide")

st.title("✍️ Automated Content Generator")
st.caption("Project B | Generate drafts using structured prompt templates.")

def get_api_key():
    try:
        return st.secrets.get("OPENAI_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")
    except Exception:
        return os.getenv("OPENAI_API_KEY", "")

def make_prompt(kind, topic, tone, audience, length, extra):
    return f"""Write a {kind} about: {topic}
Tone: {tone}
Target audience: {audience}
Length: {length}
Additional instructions: {extra if extra.strip() else 'None'}

Requirements:
- Create an appropriate title.
- Organize the content with headings when useful.
- Keep the writing clear, original, and suitable for the audience.
- Do not invent statistics, quotations, or citations.
- Return the finished draft only."""

def generate_content(prompt):
    key = get_api_key()
    if not key:
        # Offline demo output to make the workflow testable without API credentials.
        return f"""# {st.session_state.topic}

**Demo output – API key not configured**

This is a sample draft generated from your content requirements.

## Introduction
{st.session_state.topic} is an important topic for {st.session_state.audience.lower()}. Understanding its key ideas helps readers build knowledge and make informed decisions.

## Key points
- **Overview:** Introduce the main idea and explain why it matters.
- **Important details:** Describe the topic using clear examples and practical information.
- **Application:** Explain how the topic can be used in everyday or academic situations.

## Conclusion
In conclusion, {st.session_state.topic} deserves attention because it offers useful ideas and opportunities for learning.

---
*Demo mode: configure an OpenAI API key in your environment or Streamlit secrets to generate a fully AI-written draft. This sample is provided to demonstrate the workflow.*"""
    client = OpenAI(api_key=key)
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
        instructions="You are a professional content writer. Follow the requested format, tone, and audience. Be accurate and do not fabricate sources.",
        input=prompt,
    )
    return response.output_text

with st.form("content_form"):
    st.subheader("Content requirements")
    content_type = st.selectbox(
        "Content type",
        ["Blog article", "Social media post", "Professional email", "Essay", "Product description"]
    )
    topic = st.text_input("Topic or subject", placeholder="Example: Artificial Intelligence in Education")
    tone = st.selectbox("Writing tone", ["Professional", "Friendly", "Informative", "Persuasive", "Academic"])
    audience = st.text_input("Target audience", value="College students")
    length = st.selectbox("Content length", ["Short", "Medium", "Detailed"], index=1)
    extra = st.text_area("Additional instructions (optional)", placeholder="Example: Include examples and a conclusion.")
    submitted = st.form_submit_button("Generate content", type="primary", use_container_width=True)

if submitted:
    if not topic.strip():
        st.error("Please enter a topic before generating content.")
    else:
        st.session_state.topic = topic.strip()
        st.session_state.audience = audience.strip() or "General readers"
        prompt = make_prompt(content_type, topic, tone, st.session_state.audience, length, extra)
        with st.spinner("Generating your draft..."):
            try:
                st.session_state.generated = generate_content(prompt)
                st.session_state.generated_type = content_type
            except Exception as error:
                st.error(f"Could not generate content: {error}")

if "generated" in st.session_state:
    st.divider()
    st.subheader("Generated content")
    st.caption(f"Type: {st.session_state.generated_type}")
    st.markdown(st.session_state.generated)
    st.download_button(
        "Download generated content (.txt)",
        data=st.session_state.generated,
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True,
    )

with st.expander("Project explanation"):
    st.markdown("""
    **Aim:** To automate the creation of different types of written content using prompt templates.

    **Working:** The user selects a content type and supplies topic, tone, audience, length, and extra instructions. The application combines these values into a structured prompt and generates a draft.

    **Experiment:** Generate the same topic as a blog and as a social media post. Compare the structure and tone.
    """)
