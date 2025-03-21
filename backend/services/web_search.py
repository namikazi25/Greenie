import requests
from typing import Dict, Any, List, Optional
import os
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Brave Search API
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"

class WebSearchService:
    """Service for performing web searches for ecological information."""
    
    def __init__(self):
        """Initialize the web search service."""
        self.api_key = BRAVE_API_KEY
        if not self.api_key:
            logger.warning("Brave Search API key not found. Web search functionality will be limited.")
    
    def search(self, query: str, count: int = 5) -> Dict[str, Any]:
        """Perform a web search for the given query.
        
        Args:
            query: The search query
            count: Number of results to return
            
        Returns:
            Dictionary with search results
        """
        try:
            if not self.api_key:
                return {
                    "error": "Search API key not configured",
                    "results": []
                }
            
            # Add ecological context to the query if not present
            search_query = query.strip()
            if not any(term in search_query.lower() for term in ["plant", "ecology", "garden", "farm", "soil", "crop"]):
                search_query = f"ecology {search_query}"
            
            # Make the API request
            headers = {
                "X-Subscription-Token": self.api_key,
                "Accept": "application/json"
            }
            
            params = {
                "q": search_query,
                "count": count
            }
            
            response = requests.get(BRAVE_SEARCH_URL, headers=headers, params=params)
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract relevant information from the response
                results = []
                for web_result in data.get("web", {}).get("results", []):
                    results.append({
                        "title": web_result.get("title", ""),
                        "url": web_result.get("url", ""),
                        "description": web_result.get("description", "")
                    })
                
                return {
                    "success": True,
                    "results": results
                }
            else:
                logger.error(f"Search API error: {response.status_code} - {response.text}")
                return {
                    "error": f"Search API error: {response.status_code}",
                    "results": []
                }
                
        except Exception as e:
            logger.error(f"Error performing web search: {str(e)}")
            return {
                "error": f"Error performing web search: {str(e)}",
                "results": []
            }
    
    def format_search_results(self, results: List[Dict[str, str]]) -> str:
        """Format search results into a readable string.
        
        Args:
            results: List of search result dictionaries
            
        Returns:
            Formatted string with search results
        """
        if not results:
            return "No search results found."
        
        formatted = "Search Results:\n\n"
        
        for i, result in enumerate(results, 1):
            formatted += f"{i}. {result['title']}\n"
            formatted += f"   {result['url']}\n"
            formatted += f"   {result['description']}\n\n"
        
        return formatted