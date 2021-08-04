import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
print(type(response))

#-----------------------------

response = requests.get('https://api.github.com/search/repositories',
 params={'q': 'requests+language:python'},)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}') 
print(f'Repository description: {repository["description"]}')  