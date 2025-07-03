import os
from dotenv import load_dotenv

def load_headers():
    load_dotenv(override=True)
    headers = {'Token':os.getenv('Token')}
    return headers