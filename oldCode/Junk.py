self.move_history_san = []
        

        



        
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

            
 # Returns the move prediction made by ANN as source and target location arrays
    def get_move_prediction(self, perspective):

        if perspective == "w":
            board = self.board_white_perspective
        else:
            board = self.board_black_perspective

        switch_player = False

        # Repeat unitl valid move is made and instruction is given to switchplayer
        while not switch_player:

            print("Board Before Move"+str(board))

            # Retrieves predicted Qvalues from ANN and determines the predicted action based on the highest qvalue
            q_values = self.neuralNetwork.model.predict(self.preprosess_input(board))
            action = self.ACTION_SPACE[np.argmax(q_values)]

            observation, reward, done, info, switch_player, source_tile_location, target_tile_location = self.step(action, move_san_index, perspective)

            print(action)
            print(info)
            print("Board After Move"+str(observation))

        return startLocation, endLocation