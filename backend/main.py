from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
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

#Define request body model
class QRRequest(BaseModel):
    url: str

@app.post("/generate_qr")
async def generate_qr(data: QRRequest):
    # Generate the QR code in memory
    img_buffer = generate_qr_code(data.url)
    
    # Return the QR code as a response (image)
    return StreamingResponse(
        img_buffer,
        media_type="image/png",
        headers={"Content-Disposition": 'attachment; filename="qrcode.png"'}
    )