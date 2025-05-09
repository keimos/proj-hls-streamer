# backend/app/main.py
from fastapi import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Video Streamning API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Video Streaming API"}