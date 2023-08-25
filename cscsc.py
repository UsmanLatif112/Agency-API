import csv
import time
import requests

# ================================================
Campaign_id = "17798"
client_namee = "API CLIENT"
Client_id = "1874"
Keyword_name = "API TESTING"
# ================================================


# =========================

first_api_list = [
    
    # ====////Admin API////=======
    
    {
        "url": "http://50.28.76.71:7845/admin/apis/keywords/list/17889",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/business/categories/17888",
        "method": "GET",
        "params": None
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/update/keyword/values/serpapi/list/",
        "method": "PUT",
        "params":
            [
                {
                    "id": 0,
                    "organic_results_link": "string",
                    "top_primary_categories": "string",
                    "has_map": 1
                }
            ]
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/update/keyword/values/all/list/",
        "method": "PUT",
        "params":
            [
                {
                
                "id": 0,
                "page_score": 0,
                "keyword_in_url": 1,
                "keyword_in_page_title": 1,
                "keyword_in_h1": 1,
                "keyword_in_page_description": 1,
                "keyword_in_page_body": 1,
                "keyword_in_image_alt": 1,
                "keyword_in_body_content_score": 1,
                "geo_grid_keyword_id": "string",
                "grids_ranks": "string"
                
                }
            ]
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/update/keyword/values/all/list/serp/",
        "method": "PUT",
        "params":
            {
            
            "organic_results_link": "string",
            "top_primary_categories": "string",
            "has_map": 1,
            "id": 0,
            "page_score": 0,
            "keyword_in_url": 1,
            "keyword_in_page_title": 1,
            "keyword_in_h1": 1,
            "keyword_in_page_description": 1,
            "keyword_in_page_body": 1,
            "keyword_in_image_alt": 1,
            "keyword_in_body_content_score": 1
            
            }
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/update/keyword/analysis/categories/score/list/",
        "method": "PUT",
        "params":
            {
            
            "id": 0,
            "category_score": 0,
            "category_sub_score": 0
            
            }
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/update/keyword/analysis/all/list/",
        "method": "PUT",
        "params":
            {
            
            "search_volume": 0,
            "count_per_click": 0,
            "website_score": 0,
            "proximity_score": 0,
            "map_rank": 0,
            "keyword_analysis_status": 5,
            "geo_grid_sub_score": 0,
            "on_page_sub_score": 0,
            "id": 0
            
            }
    },
    {
        "url": "http://50.28.76.71:7845/admin/apis/call/procedure/manual/business/stats/",
        "method": "PUT",
        "params":
            {
            
            "business_id": 0,
            "start_month": "2022-08-03",
            "end_month": "2022-08-03"
            
            }
    },
    
    # ====////Agency////=======
    
    {
        "url": "http://50.28.76.71:7845/agency/301",
        "method": "GET",
        "params": None
    },
    
    {
        "url": "http://50.28.76.71:7845/agency/search/agencies/",
        "method": "GET",
        "params":{
            "search_query": 1,
            "page": 1,
            "size": 50
        }
    },
    {
        "url": "http://50.28.76.71:7845/agency/update/{id}/?id=",
        "method": "PUT",
        "params":{
            "id": 301
    }
    },
    {
        "url": "http://50.28.76.71:7845/business/get/{longitude}/id/{latitude}/?longitude=&latitude=",
        "method": "GET",
        "params":
            {
                "longitude": 10,
                "latitude": 15
            }
    },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params":{
    #         "page": 1,
    #         "size": 50
    #     }
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": f"http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": f"http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "POST",
    #     "params": {

    #         "campaign_id": Campaign_id,
    #         "keyword": Keyword_name
    #     }
    # },
    # {
    #     "url": f"http://50.28.76.71:7845",
    #     "method": "DELETE",
    #     "params": None
    # },
    # {
    #     "url": f"http://50.28.76.71:7845",
    #     "method": "DELETE",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "PATCH",
    #     "params": {
    #         "campaign_name": "Updated Campaign Name",
    #         "keywords_for_analysis": "Updated Keyword 1, Updated Keyword 2"
    #     }
    # },

    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "PUT",
    #     "params": {
    #         "keyword": "Updated Keyword"
    #     }
    # },
]

# =========================

second_api_list = [
     {
        "url": "http://50.28.76.71:7845",
        "method": "GET",
        "params": None
    },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "POST",
    #     "params": {

    #         "business_gmb_cid": "9864995318794434072",
    #         "campaign_name": "APITestingnew",
    #         "client_name": "SAMI",
    #         "keywords_for_analysis": "Fast food restaurant,American restaurant"
    #     }
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    
    # {
    #     "url": f"http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params":{
    #         "page": 1,
    #         "size": 50
    #     }
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "POST",
    #     "params": {

    #         "campaign_id": Campaign_id,
    #         "keyword": Keyword_name
    #     }
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "DELETE",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845",
    #     "method": "DELETE",
    #     "params": None
    # },
]


# ======================================

first_auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0YWRtaW4iLCJzY29wZXMiOltdLCJpZCI6MSwiZXhwIjoxNjkzMDQ4OTUwfQ.RktyNABxrI0mkSCsj6zwnx1zinxsanAtSN4ek1bRRF0"
second_auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0YWRtaW4iLCJzY29wZXMiOltdLCJpZCI6MSwiZXhwIjoxNjkzMDQ4OTUwfQ.RktyNABxrI0mkSCsj6zwnx1zinxsanAtSN4ek1bRRF0"

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

# Combine both API lists
# api_list = first_api_list + second_api_list
# auth_tokens = [first_auth_token, second_auth_token]

# Combine both API lists
api_list = first_api_list + second_api_list
auth_tokens = [first_auth_token] * len(first_api_list) + [second_auth_token] * len(second_api_list)  # Adjust auth_tokens list

# Initialize the response codes dictionary
response_codes_dict = {}

# ================================================

# Function to hit the APIs and save results for 6 hits in a CSV file
def hit_apis_and_save_results(api_list, auth_tokens, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['API', 'Method', 'Hit#', 'Response Code', 'Success', 'Response Time', 'Response Data'])

        response_codes_dict = {}

        # Iterate over each API in the list
        for api_index, api in enumerate(api_list):
            url = api['url']
            method = api['method']
            params = api['params']

            auth_token = auth_tokens[api_index // 6]  # Access the correct auth_token

            headers = {
                'Authorization': f'Bearer {auth_token}',
                'Content-Type': 'application/json'
            }

            # Perform 6 hits for each API
            for hit in range(1, 7):
                start_time = time.time()  # Record the start time
                response = None

                try:
                    # Make the API request
                    if method == 'GET':
                        response = requests.get(url, headers=headers, params=params)
                    elif method == 'POST':
                        response = requests.post(url, json=params, headers=headers)
                    elif method == 'PUT':
                        response = requests.put(url, json=params, headers=headers)
                    elif method == 'PATCH':
                        response = requests.patch(url, json=params, headers=headers)
                    elif method == 'DELETE':
                        response = requests.delete(url, headers=headers)

                    # Get the response code and calculate the response time
                    response_code = response.status_code if response is not None else None
                    response_time = time.time() - start_time if response is not None else 'N/A'
                    
                    # Check if the response is 429 and save it to the 429 CSV
                    if response_code == 429:
                        with open('csv_429_API.csv', 'a', newline='') as csv_file:
                            writer_429 = csv.writer(csv_file)
                            writer_429.writerow([url, method, response_code, f'HIT#{hit}'])

                    # Check if the response is successful or not
                    if response is not None:
                        if 200 <= response_code < 300:
                            success = 'Success'
                            try:
                                response_data = response.json()
                            except ValueError:
                                response_data = response.text
                        else:
                            success = 'Fail'
                            response_data = custom_error_messages.get(response_code, 'No Data')
                            if url not in response_codes_dict:
                                response_codes_dict[url] = {}
                            response_codes_dict[url][hit] = response_code
                    else:
                        success = 'Fail'
                        response_data = 'No Response'

                    # Print data for the hit in the terminal
                    print(f"{url},{method},HIT#{hit},{response_code},{success},{response_time:.2f},{response_data}")

                    # Write the results to the CSV file for the hit
                    writer.writerow([url, method, f"HIT#{hit}", response_code, success, response_time, response_data])

                    # Wait for 1 second before the next hit
                    time.sleep(0.5)

                except Exception as e:
                    # Handle exceptions
                    response_code = response.status_code if response is not None else None
                    response_time = 'N/A'
                    success = 'Fail'
                    response_data = custom_error_messages.get(response_code, 'No Data') if response_code is not None else 'No Response'
                    error_message = str(e)

                    # Print data for the failed hit in the terminal
                    print(f"{url},{method},HIT#{hit},{response_code},{success},{response_time},{response_data},{error_message}")

                    # Write the results to the CSV file for the failed hit
                    writer.writerow([url, method, f"HIT#{hit}", response_code, success, response_time, response_data])

                    # Wait for 1 second before the next hit
                    time.sleep(0.5)

            # Print empty lines to create space between hits for each API
            for _ in range(1):
                print()
                writer.writerow([])

        # Print empty lines to create space between API lists
        for _ in range(4):
            print()
            writer.writerow([])

    # Write the 429 API list to a new CSV file
with open('csv_429_API.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['API', 'Method', 'Response Code', 'Hit#'])

    for url, hit_dict in response_codes_dict.items():
        for hit, response_code in hit_dict.items():
            writer.writerow([url, api_list[url]["method"], response_code, f'HIT#{hit}'])

        # Print empty lines to create space between hits for each API
            for _ in range(1):
                print()
                writer.writerow([])
                writer.writerow([])

# Call the function to hit the APIs and save the results
hit_apis_and_save_results(api_list, auth_tokens, 'api_results.csv')