import requests

import os
from pathlib import Path
from dotenv import *

#loading api key
project_root = Path(__file__).resolve().parent.parent #cd ..
load_dotenv(project_root / ".env")
key = os.getenv("API_KEY")




response = requests.get(
    "https://himalayas.app/jobs/api", #not using the "/search" api because this one w/o is unfiltered.
    headers = {
            "Authorization": f"Bearer {key}"
        }
    )

if response.status_code == 200: #200 <-> succeeded
    data = response.json() #process response object into json

    for job in data['jobs']:
        # print(f"{data['jobs'][job]['title']}")
        print(job['title'])
