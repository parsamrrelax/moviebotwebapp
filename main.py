from pyscript import document
import requests

# def translate_english(event):
#     input_text = document.querySelector("#english")
#     english = input_text.value
#     output_div = document.querySelector("#output")
#     output_div.innerText = arrr.translate(english)

def handle_movies_choice(event):
    user_movies_input = document.querySelector("#movies_search")
    user_movies_choice = user_movies_input.value
    output_div = document.querySelector("#output")
    output_div.innerText = movies_search(user_movies_choice)


def movies_search(user_input):
    api_url = "http://main.khorsander.fun:5000/search_movies"
    data = {"user_input": user_input}
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        result_message = response.json()["results"]
        return result_message
    else:
        return f"Error: {response.status_code}"


# def handle_movies_choice(event):
#     user_movies_input = document.querySelector("#movies_search")
#     user_movies_choice = user_movies_input.value
#     output_div = document.querySelector("#output")
    
#     # Make an HTTP POST request to the Flask API
#     api_url = "http://5.42.87.92:5000/search_movies"
#     data = {"user_input": user_movies_choice}
#     response = requests.post(api_url, json=data)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         result_message = response.json()["results"]
#         output_div.innerText = result_message
#     else:
#         output_div.innerText = f"Error: {response.status_code}"

# # Attach the function to the button click event
# movies_button = document.querySelector("#movies_button")
# movies_button.addEventListener("click", handle_movies_choice)
