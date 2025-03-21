FROM node:16

WORKDIR /app

# Install dependencies
COPY frontend/package.json ./
RUN npm install

# Copy frontend code
COPY frontend/ .

# Expose ports for Expo
EXPOSE 19000 19001 19002

# Start the Expo development server
CMD ["npm", "start"]