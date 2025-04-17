# AI Video Analyzer & Chat Agent

This project is an advanced **AI Video Analyzer and Chat Agent** built using **Streamlit**, powered by **Google's Gemini 1.5 Flash** and **LangChain's DuckDuckGo integration**. It provides an interactive platform for users to analyze videos, get AI-powered insights, and perform web searches all in one interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Uses and Scope](#uses-and-scope)
- [File Structure](#file-structure)
- [Software and Tools Requirements](#software-and-tools-requirements)
- [Getting Started](#getting-started)
- [Data Description](#data-description)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

## Project Overview

The **AI Video Analyzer & Chat Agent** is a powerful web application that combines video analysis capabilities with natural language processing and web search functionality. It uses Agno's Agent framework to integrate Google's Gemini 1.5 Flash model for video understanding and LangChain's DuckDuckGoSearchRun tool for supplementary web searches, providing users with comprehensive insights and information about their uploaded videos.

## Features

- **AI Agent Architecture**: Built using Agno's Agent framework for seamless AI integration
- **Video Upload & Processing**: Support for multiple video formats (MP4, MOV, AVI, MKV)
- **AI-Powered Analysis**: Video content analysis using Gemini 1.5 Flash
- **Interactive Chat Interface**: Real-time conversation with the AI about video content
- **LangChain Tools Integration**: Web search functionality using LangChain's DuckDuckGoSearchRun tool
- **Session Management**: Automatic timeout after 1 hour of inactivity
- **Responsive UI**: Clean and intuitive user interface with auto-scrolling chat
- **Multi-Modal Analysis**: Combines video understanding with text-based responses
- **Temporary File Handling**: Secure processing of uploaded videos

## Uses and Scope

The AI Video Analyzer & Chat Agent serves multiple purposes across different domains:

- **Content Analysis**: Quickly understand and extract insights from video content
- **Research & Education**: Analyze educational videos and gather supplementary information
- **Content Creation**: Help content creators understand and improve their videos
- **Information Synthesis**: Combine video analysis with web search results for comprehensive understanding
- **Interactive Learning**: Engage with video content through natural language conversations
- **Multi-Modal Processing**: Utilize Gemini 1.5 Flash for advanced video understanding
- **Tool-Augmented Search**: Leverage LangChain tools for enhanced web search capabilities

## File Structure

```sh
ai-video-analyzer
│
├── app.py                 # Main application
├── .env                   # Environment variables file
├── .env.example           # Example environment variables template
├── .gitignore             # Git ignore rules
└── requirements.txt       # Python dependencies
```

## Software and Tools Requirements

1. [GitHub Account](https://github.com/)
2. [Google AI Studio Account](https://aistudio.google.com/)
3. [Python 3.10+](https://www.python.org/downloads/)
4. [VSCode IDE](https://code.visualstudio.com/)
5. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
6. [Agno](https://docs.agno.com/)
7. [LangChain Tools](https://python.langchain.com/docs/integrations/tools/)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Google AI Studio API key
- Agno API key

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/ai-video-analyzer.git
   cd ai-video-analyzer
   ```

2. Create an Virtual Environment

   ```sh
   python -m venv venv
   ```

   - Activate the Virtual Environment
     ```sh
     venv/Scripts/Activate       # on windows
     source venv/bin/activate    # on mac
     ```

3. Install required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   ```sh
   cp .env.example .env
   ```

5. Edit the `.env` file and add your API keys:

   ```sh
   GOOGLE_API_KEY="your_google_api_key_here"
   AGNO_API_KEY="your_agno_api_key_here"
   ```

   - You'll need to:
     - Get a Google API key from [Google AI Studio](https://aistudio.google.com/)
     - Get an Agno API key from [Agno](https://app.agno.com/)

## Usage

1. Start the Streamlit application:

```sh
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload a video file in the supported format (MP4, MOV, AVI, MKV)

4. Wait for the video processing to complete

5. Start chatting with the AI about the video content:

   - Ask Questions:

     - Use the app to ask questions about the video content. The AI analyzes the video using Gemini 1.5 Flash and provides insightful answers.
     - e.g `What is the main theme of the video?`

   - Request Summaries & Analysis:

     - Get summaries, key points, or detailed breakdowns of the video content for better understanding.
     - e.g `Analyze the video and use key points to describe the detailed breakdown of the video content`

   - Search for Additional Information:

     - Use the integrated LangChain DuckDuckGoSearchRun tool to find related information or expand on the video's topic.
     - e.g `Summarize the video, use web search for the given information and authenticate it.`

   - Direct Web Search:
     - Alternatively, perform a direct web search for your query using the `Web Search 🔍` feature, powered by LangChain's search tools.
     - e.g `What is Agno?` (Let's say the video was about Agno, so you can directly web search for it in the same application and get results.)

### Agent Interaction

The application uses:

- Agno's Agent framework with Gemini 1.5 Flash to process and understand video content
- LangChain's DuckDuckGoSearchRun tool for web search capabilities
- Streamlit for the interactive UI
- Session state for maintaining conversation context

## Data Description

The application handles various types of data:

- **Video Files**: Supports MP4, MOV, AVI, and MKV formats
- **Chat History**: Stored in session state for the duration of the session
- **Processed Video Data**: Temporarily stored during analysis
- **Web Search Results**: Retrieved via LangChain's DuckDuckGoSearchRun tool in real-time
- **Agent State**: Managed by Agno's framework

## Future Enhancements

1. **Advanced Video Analysis**:

   - Scene detection and segmentation
   - Object and person recognition
   - Sentiment analysis of video content

2. **Enhanced User Experience**:

   - Custom video player controls
   - Timestamp-based questioning
   - Export functionality for chat history

3. **Performance Optimizations**:

   - Video compression before processing
   - Caching of frequent queries
   - Batch processing capabilities

4. **Additional Features**:
   - Multiple video comparison
   - Collaborative analysis sessions
   - Integration with additional LangChain tools (e.g., document loaders, memory modules)
   - Custom model fine-tuning options
   - Advanced LangChain-powered retrieval and search capabilities

## Acknowledgments

- Powered by Google's Gemini 1.5 Flash model
- Built with Agno's Agent framework
- Uses LangChain's DuckDuckGoSearchRun tool for web search capabilities
- Built with Streamlit's powerful web framework
- Inspired by the need for intelligent video analysis tools
