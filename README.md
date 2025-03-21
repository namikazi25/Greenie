# Greenie - Ecological Assistant Mobile App

Greenie is a mobile application that provides an ecological bot to answer queries with images and document files. It helps gardeners, farmers, and ecological researchers get information about plants, crops, and ecological research questions.

## Features

- **Image Recognition**: Users can snap photos of flowers, plants, or crops to ask about issues like yellow leaves or dying flowers
- **Chat Interface**: Interactive chat with an AI assistant for ecological queries
- **Document Support**: Ability to process and return document files when needed
- **Session Management**: Save and manage different chat sessions

## Tech Stack

### Frontend
- React Native for cross-platform mobile development
- Navigation with sidebar for chat sessions management

### Backend
- Gemini 2.0 Flash as the base AI model
- Langchain for model switching and orchestration
- Agentic architecture with planner, executor, and evaluator agents

### Integrations
- Supabase for database management
- Brave Search API for web searches
- Valyu for Wikipedia retrievals
- Sevalla for model deployment

### Infrastructure
- Python virtual environment
- Docker containerization
- Prometheus and Grafana for monitoring
- Comprehensive logging and error handling

## Setup Instructions

### Prerequisites
- Node.js and npm
- Python 3.8+
- Docker

### Installation
1. Clone the repository
2. Install frontend dependencies: `cd frontend && npm install`
3. Install backend dependencies: `cd backend && pip install -r requirements.txt`
4. Set up environment variables (see `.env.example` files)
5. Start the development servers

## Project Structure

```
├── frontend/               # React Native application
│   ├── src/                # Source code
│   │   ├── components/     # Reusable UI components
│   │   ├── screens/        # App screens
│   │   ├── navigation/     # Navigation configuration
│   │   ├── services/       # API services
│   │   └── utils/          # Utility functions
│   ├── assets/             # Images, fonts, etc.
│   └── ...                 # Configuration files
├── backend/                # Python backend
│   ├── agents/             # Agent implementations
│   │   ├── planner.py      # Planning agent
│   │   ├── executor.py     # Execution agent
│   │   └── evaluator.py    # Evaluation agent
│   ├── api/                # API endpoints
│   ├── models/             # Model integrations
│   ├── services/           # External service integrations
│   ├── utils/              # Utility functions
│   │   ├── logging.py      # Logging configuration
│   │   └── error_handling.py # Error handling utilities
│   └── ...                 # Configuration files
├── docker/                 # Docker configuration
│   ├── frontend/           # Frontend Docker setup
│   └── backend/            # Backend Docker setup
└── ...                     # Root configuration files
```

## License

MIT