/**
 * Format date to a readable string
 * @param {Date} date - The date to format
 * @returns {string} Formatted date string
 */
export const formatDate = (date) => {
  const now = new Date();
  const diff = now - date;
  
  // Less than a minute
  if (diff < 60000) {
    return 'Just now';
  }
  
  // Less than an hour
  if (diff < 3600000) {
    const minutes = Math.floor(diff / 60000);
    return `${minutes} ${minutes === 1 ? 'minute' : 'minutes'} ago`;
  }
  
  // Less than a day
  if (diff < 86400000) {
    const hours = Math.floor(diff / 3600000);
    return `${hours} ${hours === 1 ? 'hour' : 'hours'} ago`;
  }
  
  // Less than a week
  if (diff < 604800000) {
    const days = Math.floor(diff / 86400000);
    return `${days} ${days === 1 ? 'day' : 'days'} ago`;
  }
  
  // Format as date
  return date.toLocaleDateString();
};

/**
 * Truncate text to a specific length
 * @param {string} text - The text to truncate
 * @param {number} length - Maximum length
 * @returns {string} Truncated text
 */
export const truncateText = (text, length = 50) => {
  if (!text || text.length <= length) return text;
  return `${text.substring(0, length)}...`;
};

/**
 * Generate a random ID
 * @returns {string} Random ID
 */
export const generateId = () => {
  return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
};

/**
 * Format file size to human readable format
 * @param {number} bytes - File size in bytes
 * @returns {string} Formatted file size
 */
export const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Bytes';
  
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

/**
 * Extract ecological keywords from text
 * @param {string} text - The text to analyze
 * @returns {string[]} Array of ecological keywords found in the text
 */
export const extractEcologicalKeywords = (text) => {
  if (!text) return [];
  
  const lowerText = text.toLowerCase();
  const ecologicalTerms = [
    'plant', 'tree', 'flower', 'garden', 'soil', 'compost',
    'organic', 'sustainable', 'ecology', 'ecosystem', 'biodiversity',
    'climate', 'conservation', 'environment', 'green', 'recycling',
    'renewable', 'species', 'wildlife', 'forest', 'farming',
    'pesticide', 'fertilizer', 'drought', 'irrigation', 'harvest',
    'permaculture', 'pollinator', 'seed', 'native', 'invasive',
    'carbon', 'footprint', 'waste', 'water', 'energy', 'sustainability'
  ];
  
  // Find all ecological terms in the text
  const foundTerms = ecologicalTerms.filter(term => lowerText.includes(term));
  
  return foundTerms;
};