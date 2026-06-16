from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import recipes

app = FastAPI()

# CORS FIX (frontend working)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173" , "https://your-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router)