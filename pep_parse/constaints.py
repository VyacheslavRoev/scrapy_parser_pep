import os

from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv('DOMAIN', default='peps.python.org')
URL = os.getenv('URL', default='https://peps.python.org/')
