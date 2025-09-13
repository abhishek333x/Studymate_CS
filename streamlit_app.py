"""
StudyMate Hub
Run with: streamlit run streamlit_app.py
"""
import streamlit as st
from streamlit_option_menu import option_menu
import requests

st.set_page_config(page_title="StudyMate Hub", page_icon="📚", layout="wide")

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .stButton>button {
        border-radius: 2em;
        font-size: 1.1em;
        padding: 0.6em 2em;
        background: linear-gradient(90deg, #6a82fb 0%, #fc5c7d 100%);
        color: white;
        border: none;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #fc5c7d 0%, #6a82fb 100%);
        color: #fff;
        box-shadow: 0 2px 8px #fc5c7d33;
    }
    .stFileUploader>div>div {
        border-radius: 1em;
        border: 2px solid #6a82fb;
    }
    .stTextInput>div>div>input {
        border-radius: 1em;
        border: 2px solid #fc5c7d;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "StudyMate Hub",
        ["Home", "Ask PDF", "Camera OCR", "Flashcards", "Quizzes", "Summaries", "Notes", "References", "Podcast", "Mentor", "✨ Extra Features"],
        icons=["house", "file-earmark-text", "camera", "card-text", "patch-question", "file-earmark-richtext", "journal-text", "bookmark-check", "mic", "person-badge", "stars"],
        menu_icon="mortarboard", default_index=1,
        styles={
            "container": {"padding": "0!important", "background-color": "#f7f9fa"},
            "icon": {"color": "#fc5c7d", "font-size": "1.2em"},
            "nav-link": {"font-size": "1.1em", "text-align": "left", "margin":"0.2em", "border-radius": "1em"},
            "nav-link-selected": {"background": "linear-gradient(90deg, #6a82fb 0%, #fc5c7d 100%)", "color": "white"},
        }
    )

if selected == "Ask PDF":
    st.title("📄 StudyMate PDF Q&A")
    st.write("Upload a PDF, ask any question, and get an answer powered by AI!")
    with st.form("pdf_qa_form"):
        pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
        question = st.text_input("Type your question")
        submit = st.form_submit_button("Ask")
    if submit and pdf_file and question:
        with st.spinner("Processing and getting your answer..."):
            files = {"file": (pdf_file.name, pdf_file, "application/pdf")}
            data = {"question": question}
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/qa/",
                    files=files,
                    data=data,
                    timeout=120
                )
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer returned.")
                    st.success("**Answer:**\n" + answer)
                else:
                    st.error(f"Backend error: {response.status_code}\n{response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
    elif submit:
        st.warning("Please upload a PDF and enter a question.")

elif selected == "Home":
    st.title("📚 StudyMate Hub")
    st.markdown("""
    Welcome to **StudyMate Hub**! Your all-in-one AI-powered student assistant. Use the sidebar to explore features like PDF Q&A, Flashcards, Quizzes, Summaries, and more.
    """)
    st.info("Select a feature from the sidebar to get started.")

elif selected == "✨ Extra Features":
    st.title("✨ Extra Features")
    st.markdown("""
    <div style='padding:2em;background:linear-gradient(90deg,#fc5c7d11,#6a82fb11);border-radius:2em;'>
    <h3>🚀 Advanced & Wow Features</h3>
    <ul style='font-size:1.1em;'>
      <li>🧑‍🏫 <b>AI Mentor Personas</b> (Math Teacher, Science Guru, Coding Mentor)</li>
      <li>🧸 <b>ELI5 Mode</b> – Explain complex topics in simple words</li>
      <li>🏆 <b>Gamified Learning</b> – Points, badges, streaks</li>
      <li>🧠 <b>Mind-map Generator</b> (graphviz/networkx)</li>
      <li>📝 <b>Exam-prep Mode</b> – Auto sample papers</li>
      <li>⏰ <b>Smart Revision Scheduler</b> (spaced repetition)</li>
      <li>🤝 <b>Real-Time Collaborative Notes</b></li>
      <li>🛤️ <b>Adaptive Learning Path</b></li>
      <li>🔗 <b>Contextual Q&A Link-Back</b> to exact page/snippet</li>
      <li>📊 <b>Concept Visualizer / Diagram Generator</b></li>
      <li>🔥 <b>Daily Challenge & Peer Leaderboard</b></li>
      <li>📴 <b>Offline Mode</b> for low-internet users</li>
      <li>🔌 <b>Plug-in System</b> for extra mini-tools</li>
      <li>☁️ <b>One-Click Cloud Deploy Helper</b></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
