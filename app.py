from fastapi import FastAPI, Depends, TemplateResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def default(token: Annotated[str, Depends(oauth2_scheme)]) -> TemplateResponse:
    """Renders a dynamic HTML page with a welcome message"""
    welcome_message = "Welcome to your application!"  # Dynamic content
    return TemplateResponse("index.html", {"welcome_message": welcome_message})

