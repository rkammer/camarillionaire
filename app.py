from dotenv  import load_dotenv
from helpers import weather as w
from helpers import tweet   as t
from helpers import voice   as v
import os
import json

load_dotenv()

#back to og
# t.update_status(
#     w.get_formated_forecast()
# )

v.speak("""
   Hello World!
""")
