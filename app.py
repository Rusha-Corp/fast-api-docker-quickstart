from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
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
async def default() -> str:
    """Renders a basic HTML page indicating application creation"""
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Your Application is Ready!</title>
        </head>
        <body>
            <h1>Congratulations! Your application has been created.</h1>
            <p>This is the default page. To get started, push your code to a version control system like Git.</p>
            <p> (You can find many tutorials online on how to use Git. Here's a dummy link for reference: https://git-scm.com/docs/gittutorial)</p>
        </body>
    </html>
    """

