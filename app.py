import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import google.generativeai as genai
from google.generativeai import upload_file, get_file
from duckduckgo_search import DDGS
import time
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Multimodal AI Agent - Chat & Video Analysis",
    page_icon="🎥",
    layout="wide",
)

# Custom CSS for better UI
st.markdown("""
    <style>
        .stChatFloatingInputContainer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: white;
            padding: 1rem;
            z-index: 100;
            max-width: 100% !important;
            width: 100% !important;
        }
        .main {
            margin-bottom: 100px;
        }
        .stChatMessage {
            max-width: 100% !important;
            width: 100% !important;
            margin: 1rem 0;
        }
        .stChatInputContainer {
            max-width: 100% !important;
            padding: 0 1rem;
        }
        .stChatInput {
            max-width: 100% !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Application Title and Header
st.title("AI Video Analyzer & Chat Agent 🤖🎥")
st.header("Powered by Gemini 1.5 Flash & DuckDuckGo")

def initialize_session_state():
    """Initialize all session state variables"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "processed_video_file" not in st.session_state:
        st.session_state.processed_video_file = None
    if "uploaded_video_name" not in st.session_state:
        st.session_state.uploaded_video_name = None
    if "last_activity" not in st.session_state:
        st.session_state.last_activity = time.time()

initialize_session_state()

@st.cache_resource
def initialize_agent():
    """Initialize the AI agent with Gemini model and DuckDuckGo tool"""
    return Agent(
        name="Video AI Chat Agent with Web Search",
        model=Gemini(id="gemini-1.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

def auto_scroll():
    """Auto-scroll to the bottom of the chat"""
    if st.session_state.chat_history:
        js = """
        <script>
            window.scrollTo(0, document.body.scrollHeight);
        </script>
        """
        st.markdown(js, unsafe_allow_html=True)

def check_session_timeout():
    """Check if session has timed out (1 hour of inactivity)"""
    if time.time() - st.session_state.last_activity > 3600:
        st.session_state.clear()
        st.experimental_rerun()
    st.session_state.last_activity = time.time()

def process_video(file):
    """Process uploaded video file using Gemini API"""
    try:
        # Check if we've already processed this video
        if (st.session_state.uploaded_video_name == file.name and 
            st.session_state.processed_video_file is not None):
            return True

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(file.read())
            video_path = temp_video.name

        with st.spinner("Processing video..."):
            processed_video = upload_file(video_path)
            while processed_video.state.name == "PROCESSING":
                time.sleep(1)
                processed_video = get_file(processed_video.name)

        if processed_video.state.name == "ACTIVE":
            st.session_state.processed_video_file = processed_video
            st.session_state.uploaded_video_name = file.name
            st.success("Video processing complete! 🎉")
            return True
        else:
            st.error("Video processing failed. Please try again.")
            return False
    except Exception as e:
        st.error(f"Video processing error: {e}")
        return False
    finally:
        # Clean up the temporary file
        if 'temp_video' in locals():
            os.unlink(temp_video.name)

def generate_response(query):
    """Generate AI response using video content and external knowledge"""
    try:
        prompt = f"Use the uploaded video content and external knowledge to answer the question: {query}"
        response = multimodal_Agent.run(prompt, videos=[st.session_state.processed_video_file])
        ai_response = response.content

        if not ai_response or len(ai_response.strip()) < 50:
            return perform_web_search(query)
        return ai_response
    except Exception as e:
        return f"An error occurred: {e}"

def perform_web_search(query):
    """Perform web search using DuckDuckGo"""
    try:
        with st.spinner("Searching the web..."):
            with DDGS() as ddgs:
                search_results = ddgs.text(query, max_results=3)
                results = "Here's what I found online:\n\n"
                for result in search_results:
                    results += f"- **{result['title']}**: {result['body'][:200]}...\n[Read More]({result['href']})\n\n"
                return results
    except Exception as e:
        return f"Search error: {e}"

# Initialize the agent
multimodal_Agent = initialize_agent()

# Check session timeout
check_session_timeout()

# Main UI Components
video_file = st.file_uploader(
    "Upload a video file to summarize",
    type=["mp4", "mov", "avi", "mkv"],
)

if video_file:
    # Only process if it's a new video or not processed yet
    if (st.session_state.uploaded_video_name != video_file.name or 
        st.session_state.processed_video_file is None):
        process_video(video_file)
    
    # Display video and chat interface
    st.video(video_file, format="video/mp4", start_time=0)
    
    # Chat interface
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(message["user"])
            with st.chat_message("assistant"):
                st.write(message["ai"])
    
    # Input interface
    col1, col2 = st.columns([5, 1])
    with col1:
        prompt = st.chat_input("Ask anything about the video...")
    with col2:
        search_button = st.button("Web Search 🔍")

    # Handle user input
    if prompt:
        with chat_container:
            with st.chat_message("user"):
                st.write(prompt)
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown("Thinking...")
                response = generate_response(prompt)
                message_placeholder.markdown(response)
            st.session_state.chat_history.append({"user": prompt, "ai": response})
            auto_scroll()

    # Handle web search
    if search_button and st.session_state.chat_history:
        last_query = st.session_state.chat_history[-1]["user"]
        with chat_container:
            with st.chat_message("assistant"):
                search_results = perform_web_search(last_query)
                st.markdown(search_results)
                st.session_state.chat_history.append(
                    {"user": f"🔍 Web search for: {last_query}", 
                     "ai": search_results}
                )
                auto_scroll()

else:
    st.info("Upload a video file to begin analysis.")