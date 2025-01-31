from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import uvicorn

app = FastAPI()

MODEL_NAME = "mistralai/Mistral-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, torch_dtype=torch.float16, device_map="auto"
)

class TextRequest(BaseModel):
    prompt: str
    max_length: int = 256
    temperature: float = 0.7

@app.post("/generate")
def generate_text(request: TextRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs, max_length=request.max_length, temperature=request.temperature
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}

@app.get("/")
def read_root():
    return {"message": "DeepSeek Alternative API is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
