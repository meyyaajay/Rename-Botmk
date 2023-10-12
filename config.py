import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21726979")

API_HASH = os.environ.get("API_HASH", "2f58b8b5306cbdd0ecb681d2ebdf08cf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6447120598:AAHhoaMBy4N7PtizyWqw5ILVKHSGuB8HCPo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "darkstoremk3") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://ajay:ajay3@ajay.dvwpjuq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1564392560').split()]

PORT = os.environ.get("PORT", "8080")
