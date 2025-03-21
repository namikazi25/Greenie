from typing import Dict, Any, Optional
import os
from loguru import logger
from PIL import Image
from ..models.model_manager import ModelManager

class ImageAnalysisService:
    """Service for analyzing images of plants, soil, and ecological subjects."""
    
    def __init__(self):
        """Initialize the image analysis service."""
        try:
            self.model_manager = ModelManager()
            logger.info("ImageAnalysisService initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing ImageAnalysisService: {str(e)}")
            raise
    
    def analyze_image(self, image_path: str, query: str = None) -> Dict[str, Any]:
        """Analyze an image and return information about it.
        
        Args:
            image_path: Path to the image file
            query: Optional specific query about the image
            
        Returns:
            Dictionary with analysis results
        """
        try:
            # Validate image file
            if not os.path.exists(image_path):
                return {"error": "Image file not found"}
            
            # Prepare the prompt based on the query
            if query:
                prompt = f"Analyze this image and answer the following question: {query}"
            else:
                prompt = """Analyze this image and provide the following information:
                1. Plant identification (species name, common name)
                2. Plant health assessment
                3. Any visible issues or diseases
                4. Care recommendations
                
                Format your response as detailed information that would be helpful for a gardener or plant enthusiast.
                """
            
            # Generate analysis using the model manager
            analysis = self.model_manager.generate_with_image(prompt, image_path)
            
            # Return the analysis results
            return {
                "analysis": analysis,
                "success": True
            }
            
        except Exception as e:
            logger.error(f"Error analyzing image: {str(e)}")
            return {
                "error": f"Error analyzing image: {str(e)}",
                "success": False
            }
    
    def identify_plant(self, image_path: str) -> Dict[str, Any]:
        """Identify a plant from an image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary with plant identification results
        """
        prompt = """Identify the plant in this image. Please provide:
        1. Scientific name (genus and species)
        2. Common name(s)
        3. Plant family
        4. Key identifying characteristics visible in the image
        5. Native region or habitat
        
        Format your response as detailed information that would be helpful for plant identification.
        """
        
        return self.analyze_image(image_path, prompt)
    
    def diagnose_plant_issue(self, image_path: str) -> Dict[str, Any]:
        """Diagnose plant health issues from an image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary with diagnosis results
        """
        prompt = """Diagnose any health issues with the plant in this image. Please provide:
        1. Identification of visible symptoms
        2. Potential causes (diseases, pests, nutrient deficiencies, etc.)
        3. Recommended treatments or interventions
        4. Preventative measures for the future
        
        Format your response as detailed information that would be helpful for treating plant problems.
        """
        
        return self.analyze_image(image_path, prompt)