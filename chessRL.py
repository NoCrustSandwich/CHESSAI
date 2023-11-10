import gym
from gym import spaces
import chess
import chess.svg
from PIL import Image
import numpy as np
import cairo





class ChessEnv(gym.Env):
    def __init__(self):


        # White / Black
        # p = 1  | p = -1
        # n = 2  | n = -2
        # b = 3  | b = -3
        # r = 4  | r = -4
        # q = 5  | q = -5
        # k = 6  | k = -6

        super(ChessEnv, self).__init__()

        self.board = [  [-4,-2,-3,-5,-6,-3,-2,-4],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [1,1,1,1,1,1,1,1],
                        [4,2,3,5,6,3,2,4]]

        
        self.action_space = spaces.Discrete(154) # Max possible moves = 154
        self.observation_space = spaces.Box(low=-6, high=6, shape=(8, 8), dtype=int)



    def reset(self):
        # Reset the board to its initial state
        self.board = [[-4, -2, -3, -5, -6, -3, -2, -4],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [4, 2, 3, 5, 6, 3, 2, 4]]
        return np.array(self.board)
    



    def step(self, action):
            # Implement the logic for executing a move based on the action
            # Update the board and calculate the reward
            # ...

            # Placeholder return values
            observation = np.array(self.board)
            reward = 0.0
            done = False
            info = {}

            return observation, reward, done, info



    def render(self, mode='human'):
        if mode == 'human':
            print(self.board)
        elif mode == 'rgb_array':
            return self.board_to_image()

    def close(self):
        pass

    def get_observation(self):
        # Convert the chess board state to a 3D array
        obs = np.zeros((8, 8), dtype=int)
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece is not None:
                obs[chess.square_rank(square)][chess.square_file(square)][piece.piece_type - 1] = piece.color

        return obs

    def action_to_move(self, action):
        # Convert action index to chess.Move
        return list(self.board.legal_moves)[action]

    def calculate_reward(self):
        # Implement your reward logic here
        # For example, you can use the difference in material, checkmate, etc.
        return 0

    def board_to_image(self):
        # Convert the chess board to an RGB image (PNG format)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)
        context = cairo.Context(surface)
        context.scale(400, 400)  # Scale to fit the surface

        # Render the chess board
        svg_image = chess.svg.board(board=self.board)
        cairo.svg.surface(context, svg_image)

        # Convert the cairo surface to a PIL image
        img = Image.frombuffer("RGBA", (400, 400), surface.get_data(), "raw", "BGRA", 0, 1)

        return np.array(img)




# Weighting based king to oposite weight region control
# max possible moves = 154
print(chess.Board())