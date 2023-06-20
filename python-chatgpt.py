import requests #req thru pythons generic libr, alternativley we could use "import openai" to req direclty from opeanai's lib

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json", 
    "Authorization": "Bearer " + api_key
}

request_data = {
     "model": "text-davinci-003",
     "prompt": "Write a python hello world script",
     "max_tokens": 7,
     "temperature": 0

}

response = requests.post(api_endpoint, headers=request_headers, json=request_data) #sends a post request to OpeanAi's endpoint with our APIkey and passing our req in JSON format 

#catch and print error if any:clear
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed, status code: {str(response.status_code)}")