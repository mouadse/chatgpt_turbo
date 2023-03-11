import sys

import openai

from config import OPENAI_API_KEY

try:
    openai.api_key = OPENAI_API_KEY
except KeyError:
    sys.stderr.write("""
  You haven't set up your API key yet.

  If you don't have an API key yet, visit:

  https://platform.openai.com/signup

  1. Make an account or sign in
  2. Click "View API Keys" from the top right menu.
  3. Click "Create new secret key"

  Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
  """)
    exit(1)
