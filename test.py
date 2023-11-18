import requests

def movies_search(user_input):
    api_url = "http://main.khorsander.fun:5000/search_movies"
    data = {"user_input": user_input}
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        result_message = response.json()["results"]
        print(result_message)
        return result_message
    else:
        print('fail')
        print(f"Error: {response.status_code}")
        return f"Error: {response.status_code}"


movies_search("oppenheimer")