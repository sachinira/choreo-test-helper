import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import openai

app = FastAPI(title="User Management Service")

# In-memory database
users_db = []

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    full_name: str

class Question(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "User Management Service is running"}

@app.post("/users/", response_model=User)
async def create_user(user: User):
    user.id = len(users_db) + 1
    users_db.append(user)
    return user

@app.get("/users/", response_model=List[User])
async def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            updated_user.id = user_id
            users_db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/ask")
async def ask_question(question: Question):
    openai_api_key = os.getenv("CHOREO_OPENAICONNECTIONPROJECT_OPENAI_API_KEY")
    openai_base_url = os.getenv("CHOREO_OPENAICONNECTIONPROJECT_SERVICEURL")

    # Initialize OpenAI client
    client = openai.OpenAI(
        api_key=openai_api_key,
        base_url=openai_base_url
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question.question}
            ]
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 