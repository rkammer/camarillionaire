from dotenv import load_dotenv
from helpers import weather as w
import os
import json

load_dotenv()

print(w.get_formated_forecast())
