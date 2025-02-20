import segno
import re

print("Enter your link to generate:")
sender = input().strip()  # Remove extra spaces

if not sender:  # Check if input is empty
    print("Error: No input provided!")
else:
    # Cleaning the filename
    safe_filename = re.sub(r"[^\w\-]", "_", sender.replace("https://", "").replace("http://", ""))
    
    # Generate the QR code
    qrcode = segno.make_qr(sender, mode="byte")
    qrcode.save(f"{safe_filename}.png", scale=7)

    print(f"QR code saved as {safe_filename}.png")