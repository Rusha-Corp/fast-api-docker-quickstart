
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

@app.get("/health")
def hello(token: Annotated[str, Depends(oauth2_scheme)]) -> str:
    return "Hello World!"