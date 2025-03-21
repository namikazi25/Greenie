import uvicorn
from api.chat import app
from loguru import logger
import os
from dotenv import load_dotenv

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
    uvicorn.run("api.chat:app", host="0.0.0.0", port=port, reload=True)