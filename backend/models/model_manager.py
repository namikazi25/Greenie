import google.generativeai as genai
from langchain.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, Any, Optional, List
import os
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ModelManager:
    """Manager for handling different AI models and providing a unified interface."""
    
    def __init__(self):
        """Initialize the model manager with available models."""
        try:
            # Initialize the Gemini model directly
            self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Initialize the Langchain wrapper for Gemini
            self.langchain_model = GoogleGenerativeAI(model="gemini-1.5-flash", 
                                                     google_api_key=os.getenv("GEMINI_API_KEY"))
            
            logger.info("ModelManager initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing ModelManager: {str(e)}")
            raise
    
    def generate_text(self, prompt: str) -> str:
        """Generate text using the default Gemini model.
        
        Args:
            prompt: The prompt text
            
        Returns:
            The generated text response
        """
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error generating text: {str(e)}")
            return f"Error generating response: {str(e)}"
    
    def generate_with_image(self, prompt: str, image_path: str) -> str:
        """Generate text using the Gemini model with an image input.
        
        Args:
            prompt: The prompt text
            image_path: Path to the image file
            
        Returns:
            The generated text response
        """
        try:
            # Read the image file
            with open(image_path, "rb") as f:
                image_data = f.read()
            
            # Generate content with the image
            response = self.gemini_model.generate_content([prompt, image_data])
            return response.text
        except Exception as e:
            logger.error(f"Error generating text with image: {str(e)}")
            return f"Error analyzing image: {str(e)}"
    
    def run_langchain_chain(self, template: str, input_variables: Dict[str, Any]) -> str:
        """Run a Langchain chain with the specified template and input variables.
        
        Args:
            template: The prompt template string
            input_variables: Dictionary of input variables for the template
            
        Returns:
            The generated text response
        """
        try:
            # Create a prompt template
            prompt = PromptTemplate(
                template=template,
                input_variables=list(input_variables.keys())
            )
            
            # Create and run the chain
            chain = LLMChain(llm=self.langchain_model, prompt=prompt)
            response = chain.run(**input_variables)
            
            return response
        except Exception as e:
            logger.error(f"Error running Langchain chain: {str(e)}")
            return f"Error generating response: {str(e)}"
    
    def switch_model(self, model_name: str) -> bool:
        """Switch the active model to a different one.
        
        Args:
            model_name: The name of the model to switch to
            
        Returns:
            Whether the switch was successful
        """
        try:
            # Currently only supporting Gemini models
            if model_name in ['gemini-1.5-flash', 'gemini-1.5-pro']:
                self.gemini_model = genai.GenerativeModel(model_name)
                self.langchain_model = GoogleGenerativeAI(model=model_name, 
                                                         google_api_key=os.getenv("GEMINI_API_KEY"))
                logger.info(f"Switched to model: {model_name}")
                return True
            else:
                logger.warning(f"Unsupported model: {model_name}")
                return False
        except Exception as e:
            logger.error(f"Error switching model: {str(e)}")
            return False