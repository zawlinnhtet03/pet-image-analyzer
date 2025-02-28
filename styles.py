# CSS styles for the application
def load_css():
    return """
    <style>
    /* Main container */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

    /* Header styles */
    .pet-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #FF6B6B 0%, #8E98FF 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.2);
    }

    .pet-header h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    .pet-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    /* Upload section */
    .upload-section {
        border: 3px dashed #CCCCFF;
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        margin-bottom: 3rem;
        background: rgba(255, 107, 107, 0.05);
        transition: all 0.3s ease;
    }

    .upload-section:hover {
        background: rgba(255, 107, 107, 0.1);
        transform: translateY(-2px);
    }

    /* Result cards */
    .result-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        transition: transform 0.3s ease;
    }

    .result-card:hover {
        transform: translateY(-3px);
    }

    .section-header {
        color: #FF6B6B;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .section-header i {
        font-size: 1.2rem;
    }

    /* Recommendation items */
    .recommendation-item {
        background: #F8F9FA;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        border-left: 4px solid #FF6B6B;
    }

    /* Image display */
    .pet-image {
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }

    /* Loading spinner */
    .stSpinner {
        text-align: center;
        color: #FF6B6B;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        margin-top: 3rem;
        border-top: 1px solid #eee;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .pet-header {
            padding: 1.5rem;
            margin-bottom: 2rem;
        }

        .pet-header h1 {
            font-size: 2rem;
        }

        .upload-section {
            padding: 2rem;
        }

        .result-card {
            padding: 1.5rem;
        }
    }
    </style>
    """
