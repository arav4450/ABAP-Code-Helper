from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ollama 

app = FastAPI()

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


class CodeRequest(BaseModel):
    description: str  
    code: str = None  

# Model name 
MODEL_NAME = "codellama:7b"


@app.post("/generate_code")
async def generate_code(request: CodeRequest):
    try:
        prompt = f"Generate optimized ABAP code based on this description:\n\n{request.description}"
        response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
        generated_code = response.get("message", {}).get("content", "No code generated.")
        return {"generated_code": generated_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@app.post("/submit_code")
async def submit_code(request: CodeRequest):
    try:
        prompt = f"Analyze this ABAP code and provide feedback:\n\n{request.code}"
        response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
        feedback = response.get("message", {}).get("content", "No feedback received.")
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
