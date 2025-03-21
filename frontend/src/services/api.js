import { createClient } from '@supabase/supabase-js';

// Initialize Supabase client
// In a real app, these would be stored in environment variables
const supabaseUrl = 'YOUR_SUPABASE_URL';
const supabaseKey = 'YOUR_SUPABASE_KEY';
const supabase = createClient(supabaseUrl, supabaseKey);

// API endpoint for the backend
const API_URL = 'http://localhost:8000';

// Function to send a message to the backend
export const sendMessage = async (message, image = null) => {
  try {
    // Prepare the request data
    const formData = new FormData();
    formData.append('message', message);
    
    // If an image is provided, append it to the form data
    if (image) {
      const imageUri = image;
      const filename = imageUri.split('/').pop();
      const match = /\.([\w\d_]+)$/.exec(filename);
      const type = match ? `image/${match[1]}` : 'image';
      
      formData.append('image', {
        uri: imageUri,
        name: filename,
        type,
      });
    }
    
    // Send the request to the backend
    const response = await fetch(`${API_URL}/api/chat`, {
      method: 'POST',
      body: formData,
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error sending message:', error);
    throw error;
  }
};

// Function to save a chat session
export const saveChatSession = async (sessionData) => {
  try {
    const { data, error } = await supabase
      .from('chat_sessions')
      .insert(sessionData);
      
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Error saving chat session:', error);
    throw error;
  }
};

// Function to get all chat sessions
export const getChatSessions = async () => {
  try {
    const { data, error } = await supabase
      .from('chat_sessions')
      .select('*')
      .order('created_at', { ascending: false });
      
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Error getting chat sessions:', error);
    throw error;
  }
};

// Function to get a specific chat session
export const getChatSession = async (sessionId) => {
  try {
    const { data, error } = await supabase
      .from('chat_sessions')
      .select('*')
      .eq('id', sessionId)
      .single();
      
    if (error) throw error;
    return data;
  } catch (error) {
    console.error('Error getting chat session:', error);
    throw error;
  }
};