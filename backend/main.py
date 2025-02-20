from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from qr_generator import generate_qr_code  # Import the generator function

app = FastAPI()

@app.get("/generate_qr")
async def generate_qr(url: str):
    # Generate the QR code in memory
    img_buffer = generate_qr_code(url)
    
    # Return the QR code as a response (image)
    return StreamingResponse(img_buffer, media_type="image/png")