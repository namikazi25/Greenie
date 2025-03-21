import uvicorn
import os
import sys
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv

# Add the parent directory to the Python path to resolve imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Now import after path is set
from backend.api.chat import app

# Load environment variables
load_dotenv()

# Configure logger
logger.add(
    "logs/app.log",
    rotation="500 MB",
    retention="10 days",
    level="INFO",
    backtrace=True,
    diagnose=True,
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting server on port {port}")
    uvicorn.run("backend.api.chat:app", host="0.0.0.0", port=port, reload=True)