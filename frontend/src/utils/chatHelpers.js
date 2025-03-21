/**
 * Utility functions for chat functionality in the Greenie app
 */

import { formatDate, truncateText, generateId, extractEcologicalKeywords } from './helpers';

/**
 * Format a message object for display
 * @param {Object} message - The message object
 * @returns {Object} Formatted message object
 */
export const formatMessage = (message) => {
  return {
    ...message,
    formattedTime: formatDate(new Date(message.timestamp)),
    displayText: message.text || '',
  };
};

/**
 * Create a new user message object
 * @param {string} text - Message text
 * @param {string|null} imageUri - Optional image URI
 * @returns {Object} Message object
 */
export const createUserMessage = (text, imageUri = null) => {
  return {
    id: generateId(),
    text: text,
    image: imageUri,
    isUser: true,
    timestamp: new Date().toISOString(),
  };
};

/**
 * Create a new bot message object
 * @param {string} text - Message text
 * @returns {Object} Message object
 */
export const createBotMessage = (text) => {
  return {
    id: generateId(),
    text: text,
    isUser: false,
    timestamp: new Date().toISOString(),
  };
};

/**
 * Create an error message object
 * @param {string} errorText - Error message text
 * @returns {Object} Error message object
 */
export const createErrorMessage = (errorText = 'Sorry, there was an error processing your request. Please try again.') => {
  return {
    id: generateId(),
    text: errorText,
    isUser: false,
    timestamp: new Date().toISOString(),
    isError: true,
  };
};

/**
 * Create a typing indicator message
 * @returns {Object} Typing indicator message object
 */
export const createTypingIndicator = () => {
  return {
    id: 'typing-indicator',
    isTyping: true,
    isUser: false,
    timestamp: new Date().toISOString(),
  };
};

/**
 * Generate a title for a chat session based on the first message
 * @param {string} firstMessage - The first message in the chat
 * @returns {string} Generated title
 */
export const generateChatTitle = (firstMessage) => {
  if (!firstMessage) return 'New Chat';
  
  // Extract keywords
  const keywords = extractEcologicalKeywords(firstMessage);
  
  if (keywords.length > 0) {
    // Use the first keyword in the title
    return `Chat about ${keywords[0]}`;
  }
  
  // Fallback to truncated message
  return truncateText(firstMessage, 25);
};

/**
 * Check if a message contains an image request
 * @param {string} text - Message text
 * @returns {boolean} Whether the message is requesting image analysis
 */
export const isImageRequest = (text) => {
  if (!text) return false;
  
  const lowerText = text.toLowerCase();
  const imageRequestTerms = [
    'identify', 'what is this', 'what plant', 'what flower',
    'what tree', 'what species', 'recognize', 'diagnose',
    'plant disease', 'leaf problem', 'pest', 'analyze photo',
    'analyze image', 'check this plant'
  ];
  
  return imageRequestTerms.some(term => lowerText.includes(term));
};

/**
 * Parse bot response to extract structured data if available
 * @param {string} response - Bot response text
 * @returns {Object} Parsed response with any structured data
 */
export const parseBotResponse = (response) => {
  try {
    // Check if the response contains JSON
    if (response.includes('{') && response.includes('}')) {
      // Extract JSON part (simple approach, might need refinement)
      const jsonMatch = response.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const jsonStr = jsonMatch[0];
        const data = JSON.parse(jsonStr);
        
        // Return structured response
        return {
          text: response.replace(jsonStr, '').trim(),
          structuredData: data,
          hasStructuredData: true
        };
      }
    }
    
    // No structured data found
    return {
      text: response,
      structuredData: null,
      hasStructuredData: false
    };
  } catch (error) {
    console.error('Error parsing bot response:', error);
    return {
      text: response,
      structuredData: null,
      hasStructuredData: false
    };
  }
};