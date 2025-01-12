import requests

make ='toyota'
key = 'uILckHM1IlbQ2TWSyMAPsQ==YF1jwKJdgsVUxeho'
api_url = 'https://freetestapi.com/api/v1/cars?limit=10'

response = requests.get(api_url)

try:    
    # check if the request was successful
    if response.status_code == 200:
        # Get the data in JSON format
        data = response.json()
        print("A view of cars: \n", data)
    else:
        print(f"Error on the request: {response.status_code}")
except Exception as e:
    print(f"An error happened: {e}")