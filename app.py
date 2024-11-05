from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(directory="templates")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def default(request: Request):
    """Renders a dynamic HTML page with a welcome message"""
    welcome_message = "Welcome to your application!"  # Dynamic content
    return templates.TemplateResponse("index.html", {"request": request, "welcome_message": welcome_message})

