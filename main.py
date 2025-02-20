import streamlit as st
import google.generativeai as genai
from utils import initialize_gemini, analyze_pet_image, parse_analysis_result, format_image
from styles import load_css
import os
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Pet Analyzer AI",
    page_icon="🐾",
    layout="wide"
)

# Load custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="pet-header">
        <h1>🐾 Pet Analyzer AI</h1>
        <p>Discover detailed insights about pets through AI-powered analysis</p>
    </div>
""", unsafe_allow_html=True)

# Initialize Gemini AI
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    if not api_key:
        st.error("🔑 Gemini API key not found. Please make sure you've provided a valid API key.")
        st.stop()

    model = initialize_gemini(api_key)
except Exception as e:
    st.error(f"⚠️ Failed to initialize AI model: {str(e)}")
    st.stop()

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# File upload section with enhanced UI
# st.markdown("""
#     <div class="upload-section">
#         <h3>📸 Upload a Pet Photo</h3>
#         <p>Drop your image here or click to browse</p>
#     </div>
# """, unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    try:
        # Create columns for layout
        col1, col2 = st.columns([1, 2])

        with col1:
            # Display uploaded image with enhanced styling
            st.markdown('<div class="pet-image">', unsafe_allow_html=True)
            st.image(uploaded_file, caption="", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            with st.spinner("🔍 Analyzing your pet..."):
                # Process and analyze image
                image = format_image(uploaded_file)
                if not image:
                    st.error("Failed to process the uploaded image. Please try another photo.")
                    st.stop()

                analysis = analyze_pet_image(model, image)
                result = parse_analysis_result(analysis)

                # Pet Type & Breed Card
                # st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown('<h3 class="section-header">🏷️ Pet Type & Breed</h3>', unsafe_allow_html=True)
                st.write(f"**Type:** {result.get('Type', 'Unknown')}")
                st.write(f"**Breed:** {result.get('Breed', 'Unknown')}")
                # st.markdown('</div>', unsafe_allow_html=True)

                # Personality Card
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown('<h3 class="section-header">💫 Personality Traits</h3>', unsafe_allow_html=True)
                st.write(result.get('Personality', 'No personality information available'))
                st.markdown('</div>', unsafe_allow_html=True)

                # Adoption Recommendations Card
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown('<h3 class="section-header">💝 Adoption Match</h3>', unsafe_allow_html=True)

                st.markdown('<div class="recommendation-item">', unsafe_allow_html=True)
                st.write("👥 **Best For:**")
                st.write(result.get('Best For', 'No adoption recommendations available'))
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('<div class="recommendation-item">', unsafe_allow_html=True)
                st.write("🏠 **Ideal Environment:**")
                st.write(result.get('Environment', 'No environment information available'))
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ {str(e)}")
        logger.error(f"Error processing request: {str(e)}")
else:
    # Display placeholder message with icon
    st.info("👆 Upload a photo of a pet to get started!")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Powered by AI🎁</p>
    </div>
""", unsafe_allow_html=True)
