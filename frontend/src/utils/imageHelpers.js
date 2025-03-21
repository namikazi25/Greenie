/**
 * Utility functions for image handling in the Greenie app
 */

/**
 * Check if a file is a valid image
 * @param {string} uri - The file URI to check
 * @returns {boolean} Whether the file is a valid image
 */
export const isValidImage = (uri) => {
  if (!uri) return false;
  
  // Check file extension
  const validExtensions = ['jpg', 'jpeg', 'png', 'gif', 'webp'];
  const extension = uri.split('.').pop().toLowerCase();
  return validExtensions.includes(extension);
};

/**
 * Get image dimensions
 * @param {string} uri - The image URI
 * @returns {Promise<{width: number, height: number}>} Image dimensions
 */
export const getImageDimensions = (uri) => {
  return new Promise((resolve, reject) => {
    const image = new Image();
    image.onload = () => {
      resolve({
        width: image.width,
        height: image.height
      });
    };
    image.onerror = reject;
    image.src = uri;
  });
};

/**
 * Compress an image to reduce file size
 * @param {string} uri - The image URI
 * @param {number} quality - Compression quality (0-1)
 * @returns {Promise<string>} Compressed image URI
 */
export const compressImage = async (uri, quality = 0.7) => {
  // This is a placeholder for actual implementation
  // In a real app, you would use a library like react-native-image-manipulator
  console.log('Image compression would happen here with quality:', quality);
  return uri;
};

/**
 * Convert image URI to base64
 * @param {string} uri - The image URI
 * @returns {Promise<string>} Base64 encoded image
 */
export const imageToBase64 = async (uri) => {
  // This is a placeholder for actual implementation
  // In a real app, you would use fetch or FileReader to convert the image
  console.log('Converting image to base64');
  return 'base64_encoded_image_placeholder';
};

/**
 * Extract EXIF data from an image
 * @param {string} uri - The image URI
 * @returns {Promise<Object>} EXIF data
 */
export const getExifData = async (uri) => {
  // This is a placeholder for actual implementation
  // In a real app, you would use a library like react-native-exif
  return {
    make: 'Unknown',
    model: 'Unknown',
    datetime: new Date().toISOString(),
    gpsLatitude: null,
    gpsLongitude: null
  };
};