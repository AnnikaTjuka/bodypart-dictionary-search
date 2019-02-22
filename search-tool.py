"""
This tool looks up meanings of body part terms in the Oxford dictionary.
First, the script reads the body part list and returns a python list.
In the next step a request is sent to the Oxford dictionary API for each body part term.
The response is saved in a csv file.

###### work in progress ######

TODO:
- parse and interpret response and extract information
- store information in result CSV

--> Create script that combines all functions above
"""

import requests
import os
# import pandas as pd
import json


def read_bodyparttxt():
    """
    the text file bodyparts.txt includes the body part terms under investigation, the list can be extended or shortened
    the following function reads the body part list and returns a python list
    """
    with open('bodyparts.txt',"r") as f:
        bp = f.read().splitlines()
        return bp


def combine_url_bp(url, bodypart):
    """
    this function combines the Oxford API url with the body part list to perform the API requests
    """
    return url + bodypart

# this is the Oxford API url
OXFORD_API = "https://od-api.oxforddictionaries.com/api/v1/entries/en/"

# this is the ID and Key which are created after a registration at https://developer.oxforddictionaries.com/
headers = {
    'app_id': os.environ.get('OXFORD_APP_ID'),
    'app_key': os.environ.get('OXFORD_APP_KEY')
    }

# the result of the function read_bodyparttxt() is saved under the variable 'bodyparts'
bodyparts = read_bodyparttxt()


"""
the following loop creates
1. the full_url with each body part term
2. a request is sent to the Oxford dictionary API and the response is saved in 'response'
3. the response data is
4. the function json.loads encodes the text data in the variable 'response'
5. the function json.get selects the list 'results'
6. in the variables 'first_result', 'lexical_entry', 'senses' the individual sublists are saved
"""
for x in bodyparts:
    full_url = combine_url_bp(url=OXFORD_API, bodypart=x)
    response = requests.request("GET", full_url, headers=headers)
    json_data = json.loads(response.text)
    result_list = json_data.get('results')
    first_result = result_list[0]
    lexical_entry = first_result.get('lexicalEntries')[1].get('entries')
    senses = lexical_entry[0].get('senses')[0]
    print(senses)




