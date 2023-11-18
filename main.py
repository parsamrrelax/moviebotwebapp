from pyscript import document
import sqlite3
from fuzzywuzzy import fuzz, process

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
    # Connect to the database
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    # Query the database for rows where season is -1
    c.execute("SELECT name, season, episode, quality, col1, x265 FROM mytable WHERE season = '-1'")
    rows = c.fetchall()

    # Find all close matches to the user input in the first column (name) of the table
    matches = process.extract(user_input, [row[0] for row in rows], limit=len(rows), scorer=fuzz.token_set_ratio)

    # Filter out the matches with scores lower than the cutoff
    matches = [match for match in matches if match[1] >= 85]

    if matches:
        # Get the corresponding values from the rows
        results = []
        for match in matches:
            for row in rows:
                if row[0] == match[0]:
                    name = row[0]
                    season = row[1]
                    episode = row[2]
                    quality = row[3]
                    url = row[4]
                    x265 = row[5]

                    if season != '-1' and episode != 'null':
                        result = f"_Season{season}_ , _Episode{episode}_ , _{quality}_, _{x265}_ \n`{url}`"
                    else:
                        result = f"_{quality}_ _{x265}_\n`{url}`"

                    results.append(result)

        if results:
            # Split the results into multiple messages if there are too many
            result_chunks = [results[i:i+10] for i in range(0, len(results), 10)]
            for result_chunk in result_chunks:
                message = 'Matches found:\n\n' + '\n\n'.join(result_chunk)
                print(message)
                return message
    else:
        print('No matches found')

    # Close the database connection
    conn.close()

