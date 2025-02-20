import segno
import io
import re

def generate_qr_code(url: str):
    # Clean up the URL (optional)
    safe_filename = re.sub(r"[^\w\-]", "_", url.replace("https://", "").replace("http://", ""))
    
    # Generate the QR code
    qrcode = segno.make_qr(url, mode="byte")
    
    # Save QR code to a memory buffer instead of a file
    img_buffer = io.BytesIO()  # In-memory buffer
    qrcode.save(img_buffer, kind="png", scale=7)
    img_buffer.seek(0)  # Go back to the start of the buffer

    return img_buffer  # Return the image buffer