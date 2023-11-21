self.move_history_san = []
        self.white_board = [["or2","on2","ob2","oq1","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
        self.black_board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q1","k","b2","n2","r2"]]

        self.OPPONENT_PERSPECTIVE_PIECE_LABELS = {

            "_":"_",
            "p1": "op1", "p2": "op2", "p3": "op3", "p4": "op4", "p5": "op5", "p6": "op6", "p7": "op7", "p8": "op8",
            "n1": "on1", "n2": "on2", "n3": "on3", "n4": "on4", "n5": "on5", "n6": "on6", "n7": "on7", "n8": "on8", "n9": "on9", "n10": "on10",
            "b1": "ob1", "b2": "ob2", "b3": "ob3", "b4": "ob4", "b5": "ob5", "b6": "ob6", "b7": "ob7", "b8": "ob8", "b9": "ob9", "b10": "ob10",
            "r1": "or1", "r2": "or2", "r3": "or3", "r4": "or4", "r5": "or5", "r6": "or6", "r7": "or7", "r8": "or8", "r9": "or9", "r10": "or10",
            "q1": "oq1", "q2": "oq2", "q3": "oq3", "q4": "oq4", "q5": "oq5", "q6": "oq6", "q7": "oq7", "q8": "oq8", "q9": "oq9",
            "k": "ok",

        }


def reset_game_state(self):
        """
        Reset the game state to its initial configuration.

        This method resets the chess game state by reassigning the initial board configuration to both the white player's
        board and the black player's board. It also clears the move history.

        Returns:
            None
        """
        self.move_history_san = []
        self.white_board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q1","k","b2","n2","r2"]]
        self.white_board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q1","k","b2","n2","r2"]]
        
    def get_white_board(self) -> List[List[str]]:
        """
        Get the latest board state from the white player's perspective.

        Returns:
            List[List[str]]: The 2D array representing the white player's board.
        """
        return self.white_board


    def get_black_board(self) -> List[List[str]]:
        """
        Get the latest board state from the black player's perspective.

        Returns:
            List[List[str]]: The 2D array representing the black player's board.
        """
        return self.black_board


    def get_move_history_san(self) -> List[str]:
        """
        Get the history of moves in Standard Algebraic Notation.

        Returns:
            List[str]: The list of moves in Standard Algebraic Notation.
        """
        return self.move_history_san




    def get_reversed_board_perspective(self, board: List[str]) -> List[str]:
        """
        Returns the Reversed board perspective to that of the opposite player's.

        Parameters:
        - board (List[str]): The chessboard from the white player's perspective.

        Returns:
        List[str]: The reversed board state, reflecting the opposite player's perspective.
        """
        # Rotates the board 180 degrees
        board = [row[::-1] for row in board[::-1]]

        # Changes piece labels to reflect the opponent's perspective
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = self.OPPONENT_PERSPECTIVE_PIECE_LABELS[board[i][j]]
        
        return board


    def update_game_state(self):

        latest_move_history_san = self.fetch_latest_move_history_san

        # Returns early because game is already in the latest state
        if(len(latest_move_history_san) == len(self.move_history_san)):
            return
        else:
            latest_move_index = len(self.move_history_san)
