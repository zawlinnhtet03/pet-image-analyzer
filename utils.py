import google.generativeai as genai
from PIL import Image
import io
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_gemini(api_key):
    try:
        genai.configure(api_key=api_key)
        # Using the latest Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Test if model is properly initialized
        if not model:
            raise ValueError("Failed to initialize Gemini model")
        return model
    except Exception as e:
        logger.error(f"Error initializing Gemini AI: {str(e)}")
        raise Exception(f"Failed to initialize AI model: {str(e)}")

def analyze_pet_image(model, image):
    prompt = """
    You are a pet expert. Analyze this pet image and provide ONLY the following information in EXACTLY this format:

    Type: [specify if it's a dog, cat, etc.]
    Breed: [specific breed name]
    Personality: [list 3-4 personality traits visible in the image]
    Best For: [describe ideal adopter profile]
    Environment: [describe ideal living conditions]

    Important: Maintain this exact format with these exact headers. Each section must be present and filled.
    """

    try:
        logger.info("Sending image to Gemini AI for analysis")
        response = model.generate_content([prompt, image])

        if not response or not response.text:
            raise ValueError("Empty response from Gemini AI")

        # Log the raw response for debugging
        logger.info(f"Raw Gemini response: {response.text}")

        response_text = response.text.strip()
        if not all(section in response_text for section in ['Type:', 'Breed:', 'Personality:', 'Best For:', 'Environment:']):
            raise ValueError("Response missing required sections")

        logger.info("Successfully received analysis from Gemini AI")
        return response_text
    except Exception as e:
        logger.error(f"Error during image analysis: {str(e)}")
        raise Exception(f"Failed to analyze image: {str(e)}")

def parse_analysis_result(result):
    try:
        sections = {}
        current_section = None
        current_content = []

        for line in result.split('\n'):
            line = line.strip()
            if not line:
                continue

            # Check if this line is a new section
            if any(line.startswith(section + ':') for section in ['Type', 'Breed', 'Personality', 'Best For', 'Environment']):
                # Save previous section if it exists
                if current_section and current_content:
                    sections[current_section] = ' '.join(current_content)

                # Start new section
                key, value = line.split(':', 1)
                current_section = key.strip()
                current_content = [value.strip()]
            elif current_section:
                # Add to current section's content
                current_content.append(line)

        # Save the last section
        if current_section and current_content:
            sections[current_section] = ' '.join(current_content)

        # Validate required sections
        required_sections = ['Type', 'Breed', 'Personality', 'Best For', 'Environment']
        missing_sections = [section for section in required_sections if section not in sections]

        if missing_sections:
            raise ValueError(f"Missing required sections: {', '.join(missing_sections)}")

        return sections
    except Exception as e:
        logger.error(f"Error parsing analysis result: {str(e)}")
        raise Exception(f"Failed to parse analysis result: {str(e)}")

def format_image(uploaded_file):
    try:
        if uploaded_file is None:
            raise ValueError("No file was uploaded")

        image = Image.open(uploaded_file)

        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize if too large
        max_size = 1024
        if max(image.size) > max_size:
            ratio = max_size / max(image.size)
            new_size = tuple([int(x * ratio) for x in image.size])
            image = image.resize(new_size, Image.Resampling.LANCZOS)

        return image
    except Exception as e:
        logger.error(f"Error formatting image: {str(e)}")
        raise Exception(f"Failed to process image: {str(e)}")