import requests

url = "https://api.adviceslip.com/advice"

# Make a request to the API
response = requests.get(url)

# Convert JSON response into a Python dictionary
data = response.json()

# Extract the cat fact
fact = data["slip"]["advice"]

print("Advice:")
print(fact)