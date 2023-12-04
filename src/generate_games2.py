import multiprocessing as mp
import tests.tools.game_tools as pg
import version_control.last_best_prodigy as prodigy_v3
import version_control.v2 as prodigy_v2
from stockfish import Stockfish
import chess

def stockfish(board,ply):
    stockfish = Stockfish(path="/usr/games/stockfish",depth=5, parameters={"UCI_Elo": 1000})
    stockfish.set_fen_position(board.fen())
    return chess.Move.from_uci(stockfish.get_best_move())


def create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2):
    for game_num in range(44, num_games + 1):
        game = pg.generate_game(player1, name1, ply1, player2, name2, ply2,game_num)
        pgn_string = str(game)

        with open(file_name, "a") as pgn_file:
            if game_num > 1:
                # If this is not the first game, add an extra line for separation
                pgn_file.write("\n\n")
            pgn_file.write(pgn_string)
        print("Game ended:", game_num)

if __name__ == '__main__':
    # Define your game parameters
    num_games = 50
    player1 = prodigy_v3.engine_v2
    name1 = "prodigy_v3"
    ply1 = 4
    player2 = stockfish
    name2 = "stockfish"
    ply2 = 0
    file_name = f"{name1}_vs_{name2}_mate_corrected.pgn"
    create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2)












