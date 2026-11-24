import requests

import os
from pathlib import Path
from dotenv import *

import time #adding delay to avoid error 429 (too many requests)

#loading api key
project_root = Path(__file__).resolve().parent.parent #cd ..
load_dotenv(project_root / ".env")
key = os.getenv("API_KEY")



#makes request to api everytime called
def make_request(cursor):
    """
    makes a request to the Himilayas API. 
    takes in CURSOR param to flip to next page || pagination

    """

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



#MAIN LOGIC

#make initial request WITHOUT CURSOR ARGUMENT BC PAGE 0
response = make_request(None)

#assumes code = 200 --> green light
if response.status_code == 200: #200 <-> succeeded
    data = response.json() #process response object into json

    #looping thru jobs on CURRENT page
    for job in data['jobs']:
        print(job['title'])

    #makes request w/ cursor arg to flip to next page/set
    data = make_request(data['nextCursor'])

    
    page = 1 #to keep track visually in terminal
    while True: 

        #if request fails/anything else than succeeds
        if data.status_code != 200:
            print("request failed")
            print("status code: ", data.status_code)
            break #break completely out of loop

        #if no more next page/set
        if data.json()['nextCursor'] is None:
            print("no more pages") 
            break 

        print(f"---------------------------PAGE {page} DONE---------------------------")

        #looping thru jobs on CURRENT page
        for job in data.json()['jobs']:
            print(job['title'])

        #next page/set
        time.sleep(2)
        data = make_request(data.json()['nextCursor'])
        page+=1

        
