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

v.speak("My Brother, the lecture of the EA. degree is divided into three sections. The first, being a recapitulation of the ceremonies there which you have just passed, will be omitted. The second, rationally explains why you were caused to submit to the various forms and ceremonies made use of during your initiation.")