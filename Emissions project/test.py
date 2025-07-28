import requests

# The API endpoint URL
url = "https://official-joke-api.appspot.com/random_joke"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    joke = response.json()  # Parse JSON response into a Python dict
    print("Here's a joke for you:")
    print(f"{joke['setup']}")
    print(f"{joke['punchline']}")
else:
    print("Failed to get a joke. Status code:", response.status_code)