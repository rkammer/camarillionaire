from dotenv  import load_dotenv
from helpers import weather as w
from helpers import tweet   as t
import os
import json

load_dotenv()

t.update_status(
    w.get_formated_forecast()
)
