import os
import requests
import fitz # PyMuPDF
from dotenv import load_dotenv
import csv
import pandas as pd

MAX_FILE_SIZE_MB = 50 #Bots can currently send files of any type of up to 50 MB in size
LOG_FILE = "book_uploads.csv"


load_dotenv()   #load a .env file

BOT_TOKEN = os.getenv('BOT_TOKEN')  #Get the bot token from .env file


CHANNEL_ID = os.getenv("CHANNEL_ID","-1002269960068") #ID of telegram channel
BOOK_DIR = os.getenv("BOOK_DIR", r"D:\books")

def send_photo(photo_path):
    """Sends a photo to the Telegram channel."""
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(photo_path,'rb') as image:

            data = {'chat_id':CHANNEL_ID}
            files= {"photo" :image}
            response = requests.post(url,data=data,files=files)

                
            # Extract message ID to reply with the document
            message_id = response.json().get('result', {}).get('message_id')
            print(f"Photo{response.json()}")
            return message_id
        
    except Exception as e:
        print(f"Error sending photo: {e}")
        return None  # Return None if sending fails

def send_document(doc_path,message_id):
    """Sends a document PDF to the Telegram channel, replying to the photo message."""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    try:
        with open(doc_path,'rb') as document:
            data = {"chat_id":CHANNEL_ID}

            # Reply to the photo if message_id is available
            if message_id:
                data["reply_to_message_id"] = message_id

            files = {"document":document}
            response = requests.post(url, data=data, files=files)
            print(f"document {response.json()}")
            return response.json().get("ok", False)
    except Exception as e:
        print(f"Error sending document: {e}")
              
def extract_first_page_image(path_to_doc):
    """Extracts the first page of a PDF and saves it as an image."""

    try:
        with fitz.open(path_to_doc) as doc:
            page = doc.load_page(0)
            matrix = fitz.Matrix(2,2)
            image = page.get_pixmap(matrix=matrix)

            # Create a unique filename for the image
            output_filename = os.path.splitext(path_to_doc)[0] + "_first_page.png"

            image.save(output_filename)

            return os.path.abspath(output_filename)
        
    except Exception as e:
        print(f"Error processing {path_to_doc}: {e}")
        return None
    

def log_upload_status(filename, file_path, status):
    """Log the upload status of books in a CSV file"""
    file_exists = os.path.isfile(LOG_FILE)
    
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Book Name", "File Path", "Status"])
        
        writer.writerow([filename, file_path, status])

def filter_send_files(csv_file):
    try:
        df = pd.read_csv(csv_file)
        # Ensure the 'Status' column exists
        if 'Status' not in df.columns:
            print("Error: 'Status' column is missing in the CSV file.")
            return None, None
        success_files = df[df['Status']=='Success']
        failed_files = df[df['Status']== "Failed - Too large"]
        # Optional: print or return the two DataFrames for inspection
        print("Successful uploads:")
        print(success_files)
        print("\nFailed uploads:")
        print(failed_files)

        # Returning two DataFrames: one for successful files and one for failed files
        return success_files, failed_files
    
    except Exception as e:
        print(f"Error reading or processing the CSV file: {e}")
        return None, None

def process_books(directory_path):
    """Processes all books in the directory, sending images and documents to Telegram."""

    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if file_path.endswith(".pdf"):
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB

            if file_size_mb > MAX_FILE_SIZE_MB:
                print(f"Skipping {filename}: File size exceeds 50MB")
                log_upload_status(filename,file_path,"Failed - Too large")
                continue

            image_path = extract_first_page_image(file_path)
            message_id = None   # Default value in case image extraction fails
            if image_path:
                message_id =send_photo(image_path)

            success=send_document(file_path,message_id)
            log_upload_status(filename, file_path, "Success" if success else "Failed - Telegram Error")



# Run the process
process_books(BOOK_DIR)

filter_send_files(LOG_FILE)