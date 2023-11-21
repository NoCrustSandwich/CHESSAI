self.move_history_san = []
        

        


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




    


    def update_game_state(self):

        latest_move_history_san = self.fetch_latest_move_history_san

        # Returns early because game is already in the latest state
        if(len(latest_move_history_san) == len(self.move_history_san)):
            return
        else:
            latest_move_index = len(self.move_history_san)
