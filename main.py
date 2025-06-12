import streamlit as st
import openai

# 🔐 Replace with your actual OpenAI API key or use environment variables for security
openai.api_key = "your-openai-api-key"

# Page config
st.set_page_config(
    page_title="SQL Query Generator",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Natural Language to SQL Query Generator")
st.markdown("Type a plain English question, and let the AI generate the SQL query and a quick explanation.")

# Input
prompt = st.text_area("🔍 Enter your query in plain English:", placeholder="e.g., Show me all customers who purchased more than $500 last month.")

# On button click
if st.button("Generate SQL"):
    if not prompt.strip():
        st.warning("Please enter a natural language prompt.")
    else:
        with st.spinner("Generating SQL..."):

            # OpenAI call
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "You are an expert SQL assistant. Given a plain English question, generate the SQL query and a one-line explanation of what the query does."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            # Extract response
            result = response['choices'][0]['message']['content'].strip()
            if result:
                st.subheader("🧾 SQL Query & Explanation")
                st.markdown(result)
            else:
                st.error("No response from AI. Try again.")

# Footer
st.markdown("---")
st.markdown("🧠 Built with Streamlit & OpenAI | Not responsible for execution of queries on live databases.")
