import requests

import os
from pathlib import Path
from dotenv import *

#loading api key
project_root = Path(__file__).resolve().parent.parent #cd ..
load_dotenv(project_root / ".env")
key = os.getenv("API_KEY")




def make_request(cursor):
    r = requests.get(
        "https://himalayas.app/jobs/api", #not using the "/search" api because this one w/o is unfiltered.
        params={
            "cursor": cursor
        },
        headers = {
                "Authorization": f"Bearer {key}"
        }
    )
    return r

response = make_request(None)


if response.status_code == 200: #200 <-> succeeded
    data = response.json() #process response object into json

    #looping thru jobs on CURRENT page
    for job in data['jobs']:
        print(job['title'])


    # print("NEXT CURSOR: ", data['nextCursor']) # MjAyNi0xMS0yM1QwMzoyNTo0My41MTQ5NjdafDI1Mzg1NDM



    data = make_request(data['nextCursor'])

    page = 1

    while True:
        if data.status_code != 200:
            print("request failed")
            print("status code: ", data.status_code)
            break #break completely out of loop
        
        if data.json()['nextCursor'] is None:
            print("no more pages")
            break

        
        print(f"---------------------------PAGE {page} DONE---------------------------")

        #looping thru jobs on CURRENT page
        for job in data.json()['jobs']:
            print(job['title'])
        

        data = make_request(data.json()['nextCursor'])
        page+=1

        
