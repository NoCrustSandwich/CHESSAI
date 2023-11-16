import requests
import re



percentToIndex = {
    '0':0,
    '14.29%':1,
    '28.57%':2,
    '42.86%':3,
    '57.14%':4,
    '71.43%':5,
    '85.71%':6,
    '100%':7

}


# Returns the popluated piece locations of a chess.com game
def getCurrentBoard(game_url, playerColor):

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

    all_occurrences = find_all_occurrences(html_content, search_substring)
    


    # Processes the html content and returns it as a tuple of pieces and repective index postions on an 8x8 board
    pieceLocations = []

    for pieceIndex in all_occurrences:

        pieceType = html_content[pieceIndex+22:pieceIndex+24]

        preprocessedLocation = html_content[pieceIndex+112:pieceIndex+140]

        splitStrings =  re.split(' ', preprocessedLocation)

        first_number = splitStrings[0]
        second_number = splitStrings[1]

        pieceLocations.append((pieceType,(percentToIndex[first_number],percentToIndex[second_number])))
            

    currentBoard = [["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"]]

    if playerColor == "w":
        for piece in pieceLocations:

            color = piece[0][0]

            if color == "w":
                pre = ""
            else:
                pre = "o"
            
            newPiece = pre + piece[0][1]

            currentBoard[piece[1][0]][piece[1][1]]  = newPiece


    else:

        for piece in pieceLocations:

            color = piece[0].pop(0)

            if color == "b":
                pre = ""
            else:
                pre = "o"
            
            newPiece = pre + piece

            currentBoard[piece[1][0]][piece[1][1]]  = newPiece


    return currentBoard









print(getCurrentBoard("https://www.chess.com/game/82182499198","w"))