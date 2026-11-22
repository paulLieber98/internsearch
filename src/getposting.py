import requests

import os
from pathlib import Path
from dotenv import *

#loading api
project_root = Path(__file__).resolve().parent.parent #cd ..
load_dotenv(project_root / ".env")
key = os.getenv("API_KEY")

request = requests.get("https://himalayas.app/jobs/api") #not using the "/search" api because this one w/o is unfiltered.

print(request)