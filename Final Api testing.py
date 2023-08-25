import csv
import time
import requests

# ================================================

# Campaign ID which is deleted in first in delete api and get single campaign data with campaign id.

Campaign_ID = "17852" 

# Campaign IDd which is used for other apis in which we need campaign id to get data

Campaign_IDd = "17900"

# Campaign IDdd which is used to add 8th keyword in campaign already having 7 keywords

Campaign_IDdd = "17898"

# Campaign IDdr which is used to delete last keyword of campaign 

Campaign_IDdr = "17912"

# Client id is used to get client api

Client_id = "2771"

# Keyword which is used to create keyword add keyword or delete keyword

Keyword_new = "mango"

# Client name which is used to create new client

Client_Name_New = "UsmanAPItesting112"

# ================================================

# data which is used to create new campaign

business_gmb_CID = "9864995318794434072"
Campaign_name = "Five Guys13"
Client_name = "SAMI"
keywords_for_analysis = "Red Royal Electric,American restaurant"

# =========================

api_list = [
    
    # ====////Admin API////=======
    
    {
        "url": "http://67.225.255.186:8010/campaigns/create/",
        "method": "POST",
        "params":
            {
            "business_gmb_cid": business_gmb_CID,
            "campaign_name": Campaign_name,
            "client_name": Client_name,
            "keywords_for_analysis": keywords_for_analysis
            }
    },
    
    {
        "url": "http://67.225.255.186:8010/campaigns/create/",
        "method": "POST",
        "params":
            {
            "business_gmb_cid": "98649953187944340729864995318",
            "campaign_name": Campaign_name,
            "client_name": Client_name,
            "keywords_for_analysis": keywords_for_analysis
            }
    },
    
    # =============================================================
    
    {
        "url": f"http://67.225.255.186:8010/campaigns/{Campaign_ID}/",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://67.225.255.186:8010/campaigns/177/",
        "method": "GET",
        "params": None
    },
    
    
    # =============================================================
    
    {
        "url": "http://67.225.255.186:8010/campaigns/list/all/",
        "method": "GET",
        "params": None
    },
    
    # =============================================================
    
    {
        "url": f"http://67.225.255.186:8010/campaigns/delete/{Campaign_ID}/",
        "method": "DELETE",
        "params": None
    },
    
    {
        "url": f"http://67.225.255.186:8010/campaigns/delete/1289/",
        "method": "DELETE",
        "params": None
    },
    
    {
        "url": f"http://67.225.255.186:8010/campaigns/delete/{Campaign_ID}/",
        "method": "DELETE",
        "params": None
    },
    
    # =============================================================
    
    {
        "url": "http://67.225.255.186:8010/clients/create/",
        "method": "POST",
        "params":
            {
                "client_name": Client_Name_New
                }
    },
    {
        "url": "http://67.225.255.186:8010/clients/create/",
        "method": "POST",
        "params":
            {
                "client_name": Client_Name_New
                }
    },
    
    # ======================================
    
    {
        "url": f"http://67.225.255.186:8010/clients/{Client_id}/",
        "method": "GET",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/clients/128/",
        "method": "GET",
        "params": None
    },
    
    # ======================================
    
    {
        "url": "http://67.225.255.186:8010/geo/gifs/urls/list/",
        "method": "GET",
        "params":
            {
            "Page": 1,
            "Size": 50
            }   
    },
    
    # ======================================
    
    {
        "url": f"http://67.225.255.186:8010/geo/gifs/urls/campaign/{Campaign_IDd}",
        "method": "GET",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/geo/gifs/urls/campaign/1205",
        "method": "GET",
        "params": None
    },
    
    # ======================================
    
    {
        "url": "http://67.225.255.186:8010/geo/grid/urls/list/all/",
        "method": "GET",
        "params": None
    },
    
    # ======================================
    
    
    {
        "url": f"http://67.225.255.186:8010/geo/grid/urls/{Campaign_IDd}/",
        "method": "GET",
        "params": None
    },
    
    {
        "url": f"http://67.225.255.186:8010/geo/grid/urls/1496/",
        "method": "GET",
        "params": None
    },
    
    # ======================================
    
    {
        "url": f"http://67.225.255.186:8010/geo/grid/urls/latest/{Campaign_IDd}",
        "method": "GET",
        "params": None
    },
    
    {
        "url": f"http://67.225.255.186:8010/geo/grid/urls/latest/8573",
        "method": "GET",
        "params": None
    },
    
    # ======================================
    
    {
        "url": "http://67.225.255.186:8010/keyword/create/",
        "method": "POST",
        "params":
             {
            "campaign_id": Campaign_IDd,
            "keyword": Keyword_new
            }
    },
    {
        "url": "http://67.225.255.186:8010/keyword/create/",
        "method": "POST",
        "params":
             {
            "campaign_id": Campaign_IDd,
            "keyword": Keyword_new
            }
    },
    {
        "url": "http://67.225.255.186:8010/keyword/create/",
        "method": "POST",
        "params":
            {
            "campaign_id": Campaign_IDdd,
            "keyword": "Pathan123"
            }
    },
    
    # ======================================
    
    {
        "url": f"http://67.225.255.186:8010/keyword/delete/{Keyword_new}/{Campaign_IDd}",
        "method": "DELETE",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/keyword/delete/{Keyword_new}/{Campaign_IDd}",
        "method": "DELETE",
        "params": None
    },
    {
        "url": f"http://67.225.255.186:8010/keyword/delete/fast food restaurant/{Campaign_IDdr}",
        "method": "DELETE",
        "params": None
    },
    
    # ======================================
    
    
    
]

# ======================================

auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBdXRvbWF0aW9uIEFQSSIsIlRPS0VOIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnpkV0lpT2lKQmRYUnZiV0YwYVc5dUlFRlFTU0lzSW5OamIzQmxjeUk2VzEwc0ltbGtJam95TmpreUxDSmxlSEFpT2pFMk9UUTNOekV3TURaOS52cHE0cHR6c195eG9taGl3Mkg3dWRNMFN0TGhzQ3BRakNmN3BWZ0lRZzhVIiwiZXhwIjoyMDA3OTcxMDA3fQ.yXEKEb1Wgw-YB3EltnQRhCNsmsQ--MD9Vlk4FAteUoc"

# ======================================

# Add a dictionary to store custom error messages for specific response codes
custom_error_messages = {
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfiable',
    418: 'iam',
    421: 'Misdirected Request',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',
    429: 'Too Many Requests',
}
# ================================================

# Initialize the response codes dictionary
response_codes_dict = {}

# ================================================

# Function to hit the APIs and save results in a CSV file
def hit_apis_and_save_results(api_list, auth_token, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['API', 'Method', 'Response Code', 'Status', 'Response Time', 'Response Message', 'Response Data'])
        writer.writerow('\n')
        
        
        # Iterate over each API in the list
        for api in api_list:
            url = api['url']
            method = api['method']
            params = api['params']

            headers = {
                'Authorization': f'Bearer {auth_token}',
                'Content-Type': 'application/json'
            }

            try:
                # Make the API request
                start_time = time.time()
                response = requests.request(method, url, json=params, headers=headers)
                response_code = response.status_code
                response_time = time.time() - start_time

                # Check if the response is successful or not
                if 200 <= response_code < 300:
                    status = 'Pass'
                else:
                    status = 'Fail'

                response_message = custom_error_messages.get(response_code, '')
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text

                # Write the results to the CSV file
                writer.writerow([url, method, response_code, status, response_time, response_message, response_data])
                writer.writerow('\n')

                # Print the results in the terminal
                print(f"API: {url}, Method: {method}, Response Code: {response_code}, Status: {status}, "
                      f"Response Time: {response_time:.2f}, Response Message: {response_message}, Response Data: {response_data}")
                
                # Wait for 1 second before the next API hit
                time.sleep(1)

            except Exception as e:
                print(f"Error occurred while processing API: {url}, Method: {method}, Error: {e}")

        print("API hits completed.")

# Call the function to hit the APIs and save the results
hit_apis_and_save_results(api_list, auth_token, 'API_result.csv')