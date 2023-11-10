import requests

game_url = "https://www.chess.com/game/daily/583143785"
response = requests.get(game_url)

# https request
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the game page.")

# Finds the occurences of the pieces present
def find_all_occurrences(text, search_substring):
    occurrences = []
    index = text.find(search_substring)

    while index != -1:
        occurrences.append(index)
        index = text.find(search_substring, index + 1)

    return occurrences


search_substring = "var(--theme-piece-set-"

index = html_content.find(search_substring)

all_occurrences = find_all_occurrences(html_content, search_substring)

if all_occurrences:
    print(f"'{search_substring}' found at indices: {all_occurrences}")
else:
    print(f"'{search_substring}' not found in the text.")


