#Create a .env file in your project directory: with secrets
"""
ACCOUNT_SID=********
AUTH_TOKEN=********
WHATSAPP_FROM=whatsapp:*********
WHATSAPP_TO=whatsapp:********
"""
"""
Remove Extra Spaces: Ensure there are no spaces around the = sign.
Remove Quotes: Do not use quotes around the values.
"""

#Load environment variables in your code

"""
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
"""

# ADD .gitignore file to the project directory
"""
Update .gitignore
Ensure that your .env file is added to .gitignore so it doesn't get committed to the repository."""
""".env -- add this to gitignore file"""

