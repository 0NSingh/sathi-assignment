import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from genai.gemini import parse_query
from pydantic import BaseModel
import re
import json
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class userQuery(BaseModel):
    data: str
def format_response(response):
    clean_json = re.sub(r"```json|```", "", response).strip()
    parsed = json.loads(clean_json)
    return parsed
@app.get("/",tags=["Root"])
def root():
    return {"message": "Welcome to the Query Parser API"}
@app.post("/query",tags=["Query Parser"])
def query(request: userQuery):
    print(request.data)
    responsefromgemini=parse_query(request.data)
    return format_response(responsefromgemini)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
