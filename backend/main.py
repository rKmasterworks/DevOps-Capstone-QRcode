from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from qr_generator import generate_qr_code  # Import the generator function
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/generate_qr")
async def generate_qr(url: str):
    # Generate the QR code in memory
    img_buffer = generate_qr_code(url)
    
    # Return the QR code as a response (image)
    return StreamingResponse(img_buffer, media_type="image/png")