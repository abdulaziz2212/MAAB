import os
import fitz  # PyMuPDF for PDF processing
import requests
from PIL import Image
import io

# Securely store bot token (replace with os.environ for security)
BOT_TOKEN = "8083082647:AAE7tqFwComfOqa3FAmmc7TSHmaNaDQ-_aQ"
CHANNEL_ID = "-1002269960068"  # Replace with your channel ID

# Directory where books are stored
BOOK_DIR = r"C:\Users\Victus\Downloads\Telegram Desktop\books"  # Ensure this is a folder

# Function to send message
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL_ID, "text": text, "parse_mode": "Markdown"}
    response = requests.post(url, data=data)
    print(response.json())

# Function to send an image
def send_photo(image_path,caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as img:
        files = {"photo": img}
        data = {"chat_id": CHANNEL_ID, "caption": caption}
        response = requests.post(url, data=data, files=files)
        print(response.json())
# Function to send a PDF file
def send_pdf(pdf_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(pdf_path, "rb") as pdf:
        files = {"document": pdf}
        data = {"chat_id": CHANNEL_ID}
        response = requests.post(url, data=data, files=files)
        print(response.json())

# Extract and save first page of PDF as an image
def extract_first_page_as_image(pdf_path):
    try:
        doc = fitz.open(pdf_path)  # Open PDF
        first_page = doc[0]  # Get the first page
        pix = first_page.get_pixmap()  # Render page as image

        img = Image.open(io.BytesIO(pix.tobytes("ppm")))  # Convert to image
        img_path = pdf_path.replace(".pdf", "_first_page.jpg")
        img.save(img_path, "JPEG")  # Save as JPEG
        return img_path
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

# Process each PDF in directory
def process_books(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if filename.endswith((".pdf",".epub")):
            book_title = f"📖 Book: {filename}"
            #send_message(f"📖 Book: {filename}")  # Send book name
            image_path = extract_first_page_as_image(file_path)  # Extract first page
            if image_path:
                send_photo(image_path,book_title)  # Send the image
            send_pdf(file_path)

# Run the function
process_books(BOOK_DIR)
