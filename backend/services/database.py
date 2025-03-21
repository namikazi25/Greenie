from typing import Dict, Any, List, Optional
import os
from loguru import logger
import supabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

class DatabaseService:
    """Service for handling database operations for the Greenie app."""
    
    def __init__(self):
        """Initialize the database service."""
        try:
            if not SUPABASE_URL or not SUPABASE_KEY:
                logger.warning("Supabase credentials not found. Database functionality will be limited.")
                self.client = None
            else:
                self.client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)
                logger.info("DatabaseService initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing DatabaseService: {str(e)}")
            self.client = None
    
    def save_chat_session(self, session_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a chat session to the database.
        
        Args:
            session_data: Dictionary with session data
            
        Returns:
            Dictionary with operation result
        """
        try:
            if not self.client:
                return {
                    "error": "Database not configured",
                    "success": False
                }
            
            # Insert the session data into the chat_sessions table
            response = self.client.table('chat_sessions').insert(session_data).execute()
            
            # Check for errors
            if response.get('error'):
                logger.error(f"Error saving chat session: {response.get('error')}")
                return {
                    "error": f"Error saving chat session: {response.get('error')}",
                    "success": False
                }
            
            return {
                "success": True,
                "data": response.get('data', [])
            }
            
        except Exception as e:
            logger.error(f"Error saving chat session: {str(e)}")
            return {
                "error": f"Error saving chat session: {str(e)}",
                "success": False
            }
    
    def get_chat_sessions(self, user_id: Optional[str] = None) -> Dict[str, Any]:
        """Get all chat sessions for a user.
        
        Args:
            user_id: Optional user ID to filter sessions
            
        Returns:
            Dictionary with operation result
        """
        try:
            if not self.client:
                return {
                    "error": "Database not configured",
                    "success": False,
                    "sessions": []
                }
            
            # Query the chat_sessions table
            query = self.client.table('chat_sessions')
            
            # Filter by user_id if provided
            if user_id:
                query = query.eq('user_id', user_id)
            
            # Execute the query
            response = query.order('created_at', {'ascending': False}).execute()
            
            # Check for errors
            if response.get('error'):
                logger.error(f"Error getting chat sessions: {response.get('error')}")
                return {
                    "error": f"Error getting chat sessions: {response.get('error')}",
                    "success": False,
                    "sessions": []
                }
            
            return {
                "success": True,
                "sessions": response.get('data', [])
            }
            
        except Exception as e:
            logger.error(f"Error getting chat sessions: {str(e)}")
            return {
                "error": f"Error getting chat sessions: {str(e)}",
                "success": False,
                "sessions": []
            }
    
    def get_chat_messages(self, session_id: str) -> Dict[str, Any]:
        """Get all messages for a chat session.
        
        Args:
            session_id: The session ID
            
        Returns:
            Dictionary with operation result
        """
        try:
            if not self.client:
                return {
                    "error": "Database not configured",
                    "success": False,
                    "messages": []
                }
            
            # Query the chat_messages table
            response = self.client.table('chat_messages')\
                .eq('session_id', session_id)\
                .order('timestamp', {'ascending': True})\
                .execute()
            
            # Check for errors
            if response.get('error'):
                logger.error(f"Error getting chat messages: {response.get('error')}")
                return {
                    "error": f"Error getting chat messages: {response.get('error')}",
                    "success": False,
                    "messages": []
                }
            
            return {
                "success": True,
                "messages": response.get('data', [])
            }
            
        except Exception as e:
            logger.error(f"Error getting chat messages: {str(e)}")
            return {
                "error": f"Error getting chat messages: {str(e)}",
                "success": False,
                "messages": []
            }
    
    def save_chat_message(self, message_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a chat message to the database.
        
        Args:
            message_data: Dictionary with message data
            
        Returns:
            Dictionary with operation result
        """
        try:
            if not self.client:
                return {
                    "error": "Database not configured",
                    "success": False
                }
            
            # Insert the message data into the chat_messages table
            response = self.client.table('chat_messages').insert(message_data).execute()
            
            # Check for errors
            if response.get('error'):
                logger.error(f"Error saving chat message: {response.get('error')}")
                return {
                    "error": f"Error saving chat message: {response.get('error')}",
                    "success": False
                }
            
            return {
                "success": True,
                "data": response.get('data', [])
            }
            
        except Exception as e:
            logger.error(f"Error saving chat message: {str(e)}")
            return {
                "error": f"Error saving chat message: {str(e)}",
                "success": False
            }