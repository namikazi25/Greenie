import google.generativeai as genai
import requests
from typing import Dict, Any, Optional
import os
import json
from loguru import logger
from dotenv import load_dotenv
from ..services.web_search import WebSearchService
from ..services.image_analysis import ImageAnalysisService
from ..models.model_manager import ModelManager

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ExecutorAgent:
    """Agent responsible for executing the plan created by the planner."""
    
    def __init__(self):
        """Initialize the executor agent with the Gemini model."""
        try:
            # Initialize the model manager and services
            self.model_manager = ModelManager()
            self.web_search = WebSearchService()
            self.image_analysis = ImageAnalysisService()
            logger.info("ExecutorAgent initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing ExecutorAgent: {str(e)}")
            raise
    
    def execute_plan(self, plan: Dict[str, Any]) -> str:
        """Execute the plan created by the planner.
        
        Args:
            plan: The plan dictionary from the planner agent
            
        Returns:
            The result of executing the plan
        """
        try:
            # Extract plan details
            plan_text = plan.get("plan", "")
            requires_image_analysis = plan.get("requires_image_analysis", False)
            requires_web_search = plan.get("requires_web_search", False)
            image_path = plan.get("image_path", None)
            
            # Prepare context for the model
            context = f"Plan: {plan_text}\n\n"
            
            # Perform web search if required
            if requires_web_search:
                search_results = self.web_search.search(plan_text)
                if search_results.get("success", False):
                    formatted_results = self.web_search.format_search_results(search_results.get("results", []))
                    context += f"Web Search Results:\n{formatted_results}\n\n"
            
            # Perform image analysis if required
            if requires_image_analysis and image_path:
                analysis_results = self.image_analysis.analyze_image(image_path)
                if analysis_results.get("success", False):
                    context += f"Image Analysis Results:\n{analysis_results.get('analysis', '')}\n\n"
            
            # Prepare the prompt for the model
            prompt = f"""You are an ecological assistant. Execute the following plan to provide a helpful response:
            
            {context}
            
            Based on the plan and available information, provide a detailed, accurate, and helpful response.
            Focus on ecological information, gardening advice, plant identification, or research information as appropriate.
            """
            
            # Generate content using the model manager
            result = self.model_manager.generate_text(prompt)
            
            return result
            
        except Exception as e:
            logger.error(f"Error executing plan: {str(e)}")
            # Return a fallback response in case of error
            return "I'm sorry, I encountered an issue while processing your request. Please try again or ask a different question."
    
    def _perform_web_search(self, query: str) -> str:
        """Perform a web search using the Brave Search API.
        
        Args:
            query: The search query
            
        Returns:
            The search results as a string
        """
        try:
            if not BRAVE_API_KEY:
                return "Web search capability not available."
                
            # Prepare the search query
            search_query = query.strip()
            
            # Add ecological context to the query
            if not any(term in search_query.lower() for term in ["plant", "ecology", "garden", "farm", "soil", "crop"]):
                search_query = f"ecology {search_query}"
            
            # Make the API request
            headers = {
                "X-Subscription-Token": BRAVE_API_KEY,
                "Accept": "application/json"
            }
            
            params = {
                "q": search_query,
                "count": 5  # Limit to 5 results
            }
            
            response = requests.get(
                "https://api.search.brave.com/res/v1/web/search",
                headers=headers,
                params=params
            )
            
            if response.status_code != 200:
                logger.error(f"Brave Search API error: {response.status_code}")
                return "Web search failed."
            
            # Parse the response
            data = response.json()
            
            # Extract the search results
            results = []
            for web in data.get("web", {}).get("results", []):
                title = web.get("title", "")
                description = web.get("description", "")
                results.append(f"Title: {title}\nDescription: {description}\n")
            
            # Join the results
            return "\n".join(results)
            
        except Exception as e:
            logger.error(f"Error performing web search: {str(e)}")
            return "Web search failed due to an error."