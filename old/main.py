from pyscript import document
import asyncio
import json
from pyodide.http import pyfetch
from js import fetch
async def handle_movies_choice(event):
    user_movies_input = document.querySelector("#movies_search")
    user_movies_choice = user_movies_input.value
    output_div = document.querySelector("#output")
    output_div.innerText = await movies_search(user_movies_choice)


# async def movies_search(user_input):
#     api_url = "https://main.khorsander.fun/search_movies"
#     data = {"user_input": user_input}
#     json_string = json.dumps(data)
#     headers = {"Content-Type": "application/json"}
#     response = await pyfetch(url=api_url, method="POST", json=data, headers=headers)
#     content = (await response.bytes()).decode('utf-8')
#     if response.status == 200: 
#         return content
#     else:
#         return response.status


async def movies_search(user_input):

  api_url = "https://main.khorsander.fun/search_movies"

  data = {"user_input": user_input}
  headers = {"Content-Type": "application/json"}

  response = await fetch(api_url,
    method= 'POST', 
    json = data ,
    headers= headers,
  )

  if response.status == 200:
    json_data = await response.json()
    return json_data["results"]

  else:
    return f"Error: {response.status}"