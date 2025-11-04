import requests

url = "https://catfact.ninja/fact"

# Make a request to the API
response = requests.get(url)

# Convert JSON response into a Python dictionary
data = response.json()

# Extract the cat fact
fact = data["fact"]

print("🐱 Random Cat Fact:")
print(fact)
