import requests
import re
import math


# Returns the popluated piece locations of a chess.com game
def getCurrentBoard(game_url):

    response = requests.get(game_url)

    # http request to chess.com
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

    # Seaches for this string which refers to populated pieces on the board
    search_substring = "var(--theme-piece-set-"

    index = html_content.find(search_substring)

    all_occurrences = find_all_occurrences(html_content, search_substring)


    # Processes the html content and returns it as a tuple of pieces and repective index postions on an 8x8 board
    pieceLocations = []

    for pieceIndex in all_occurrences:

        pieceType = html_content[pieceIndex+22:pieceIndex+24]

        preprocessedLocation = html_content[pieceIndex+112:pieceIndex+140]

        pattern = r"(\d+(\.\d+)?)(% )?(\d+) / (\d+(\.\d+)?)%"

        match = re.match(pattern, preprocessedLocation)

        if match:
            first_number = float(match.group(1))
            second_number = float(match.group(4))
            third_number = float(match.group(5))

            pieceLocations.append((pieceType,(math.ceil(first_number/third_number),math.ceil(second_number/third_number))))
            
    return pieceLocations



print(getCurrentBoard("https://www.chess.com/game/daily/583143785"))