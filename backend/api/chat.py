from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from loguru import logger
from ..agents.planner import PlannerAgent
from ..agents.executor import ExecutorAgent
from ..agents.evaluator import EvaluatorAgent

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatResponse(BaseModel):
    response: str
    session_id: Optional[str] = None

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(
    message: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    try:
        # Log incoming request
        logger.info(f"Received chat request with message: {message}")
        
        # Save image if provided
        image_path = None
        if image:
            # Create uploads directory if it doesn't exist
            os.makedirs("uploads", exist_ok=True)
            
            # Save the uploaded image
            image_path = f"uploads/{image.filename}"
            with open(image_path, "wb") as f:
                f.write(await image.read())
            logger.info(f"Saved uploaded image to {image_path}")
        
        # Initialize agents
        planner = PlannerAgent()
        executor = ExecutorAgent()
        evaluator = EvaluatorAgent()
        
        # Generate plan
        plan = planner.create_plan(message, image_path)
        logger.info(f"Generated plan: {plan}")
        
        # Execute plan
        result = executor.execute_plan(plan)
        logger.info(f"Executed plan with result: {result}")
        
        # Evaluate result
        final_response = evaluator.evaluate_response(result, message)
        logger.info(f"Final response after evaluation: {final_response}")
        
        # Return response
        return ChatResponse(response=final_response)
    
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))