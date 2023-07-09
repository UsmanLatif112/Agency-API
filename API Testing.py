import csv
import requests

# Data
Campaign_id = "17784"
Client_id = "1874"
Keyword_name = "usmanAPITesting"

"""Change clinet name and data of keyword you want to create"""


# List of APIs to be called
api_list = [
    {
        "url": "http://67.225.255.186:8010/campaigns/create/",
        "method": "POST",
        "params": {

            "business_gmb_cid": "9864995318794434072",
            "campaign_name": "Five Guys13",
            "client_name": "SAMI",
            "keywords_for_analysis": "Fast food restaurant,American restaurant"
        }
    },
    {
        "url": f"http://67.225.255.186:8010/campaigns/{Campaign_id}/",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://67.225.255.186:8010/campaigns/list/all/",
        "method": "GET",
        "params": None
    },
    
    {
        "url": "http://67.225.255.186:8010/clients/create/",
        "method": "POST",
        "params": {
            "client_name": "muz112112112222"
        }
    },
    {
        "url": f"http://67.225.255.186:8010/clients/{Client_id}/",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://67.225.255.186:8010/clients/clients/list/",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://67.225.255.186:8010/geo/gifs/urls/list",
        "method": "GET",
        "params":{
            "page": 1,
            "size": 50
        }
    },
    {
        "url": f"http://67.225.255.186:8010/geo/gifs/urls/campaign/{Campaign_id}",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://67.225.255.186:8010/geo/grid/urls/list/all/",
        "method": "GET",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/geo/grid/urls/{Campaign_id}/",
        "method": "GET",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/geo/grid/urls/latest/{Campaign_id}",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://67.225.255.186:8010/keyword/create/",
        "method": "POST",
        "params": {

            "campaign_id": "17784",
            "keyword": "usmanAPITesting"
        }
    },
    {
        "url": f"http://67.225.255.186:8010/keyword/delete/{Keyword_name}/{Campaign_id}",
        "method": "DELETE",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/campaigns/delete/{Campaign_id}/",
        "method": "DELETE",
        "params": None
    },
    # Add more API URLs as needed
]

# Authorization token
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBdXRvbWF0aW9uIEFQSSIsIlRPS0VOIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnpkV0lpT2lKQmRYUnZiV0YwYVc5dUlFRlFTU0lzSW5OamIzQmxjeUk2VzEwc0ltbGtJam95TmpreUxDSmxlSEFpT2pFMk9UQTJNall6TVRkOS5pTVI0TkxBZEdhRUQwRkdTY2l3R05xcGF3LW9SU01jMW1Ob2RzbktoM09VIiwiZXhwIjoyMDAzODI2MzE4fQ.kOQ9sS3W5NJz0EdLBKFLHyIVlclKuaxgVrtUBcmD6W4"

# Function to send API requests and save results in a CSV file
def hit_apis_and_save_results(api_list, auth_token):
    # Create a CSV file
    with open('api_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['API', 'Method', 'Response Code', 'Response Data'])

        # Iterate over each API in the list
        for api in api_list:
            url = api['url']
            method = api['method']
            params = api['params']

            headers = {
                'Authorization': f'Bearer {auth_token}',
                'Content-Type': 'application/json'
            }

            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=params, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                print(f"Unsupported HTTP method: {method}")
                continue

            # Get the response code and data
            response_code = response.status_code
            response_data = response.json() if response_code == 200 else ""

            # Write the results to the CSV file
            writer.writerow([url, method, response_code, response_data])

            # Print the results to the console
            print(f"API: {url}\nMethod: {method}\nResponse Code: {response_code}\nResponse Data: {response_data}\n")

# Call the function to hit the APIs and save the results
hit_apis_and_save_results(api_list, auth_token)
