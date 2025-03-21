import google.generativeai as genai
from typing import Optional, Dict, Any
import os
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class PlannerAgent:
    """Agent responsible for creating a plan based on the user's message."""
    
    def __init__(self):
        """Initialize the planner agent with the Gemini model."""
        try:
            # Initialize the Gemini model
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            logger.info("PlannerAgent initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing PlannerAgent: {str(e)}")
            raise
    
    def create_plan(self, message: str, image_path: Optional[str] = None) -> Dict[str, Any]:
        """Create a plan based on the user's message and optional image.
        
        Args:
            message: The user's message
            image_path: Optional path to an uploaded image
            
        Returns:
            A dictionary containing the plan details
        """
        try:
            # Prepare the prompt for the model
            prompt = f"""You are an ecological assistant. Create a plan to respond to the following query:
            
            User Query: {message}
            
            Your plan should include:
            1. What information needs to be gathered
            2. What sources should be consulted
            3. What format the response should take
            
            Return your plan as a structured JSON object.
            """
            
            # If an image is provided, include it in the generation
            if image_path:
                # Read the image file
                with open(image_path, "rb") as f:
                    image_data = f.read()
                
                # Generate content with the image
                response = self.model.generate_content([prompt, image_data])
            else:
                # Generate content without an image
                response = self.model.generate_content(prompt)
            
            # Extract the plan from the response
            plan = response.text
            
            # For now, return a simple dictionary with the plan
            # In a real implementation, this would parse the response into a structured format
            return {
                "plan": plan,
                "requires_image_analysis": image_path is not None,
                "requires_web_search": "research" in message.lower() or "information" in message.lower(),
                "requires_database": False  # Could be determined based on the plan
            }
            
        except Exception as e:
            logger.error(f"Error creating plan: {str(e)}")
            # Return a fallback plan in case of error
            return {
                "plan": "Provide a simple response based on general knowledge",
                "requires_image_analysis": False,
                "requires_web_search": False,
                "requires_database": False
            }