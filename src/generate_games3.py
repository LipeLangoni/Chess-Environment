import multiprocessing as mp
import tests.tools.game_tools as pg
import version_control.last_best_prodigy as prodigy_v3
import version_control.v2 as prodigy_v2
from stockfish import Stockfish
import chess

def stockfish_1(board,ply):
    stockfish = Stockfish(path="/usr/games/stockfish",depth=5, parameters={"UCI_Elo": 800})
    stockfish.set_fen_position(board.fen())
    return chess.Move.from_uci(stockfish.get_best_move())

def stockfish_2(board,ply):
    stockfish2 = Stockfish(path="/usr/games/stockfish",depth=5, parameters={"UCI_Elo": 1000})
    stockfish2.set_fen_position(board.fen())
    return chess.Move.from_uci(stockfish2.get_best_move())

def create_pgn_file(file_name,num_games,player1,name1,ply1,player2,name2,ply2):
    all_games = []
    for Round in range(num_games):
        game = pg.generate_game(player1,name1,ply1,player2,name2,ply2,Round)
        all_games.append(game)
    pgn_strings = [str(game) for game in all_games]
    unified_pgn = "\n\n".join(pgn_strings)

    with open(file_name, "w") as pgn_file:
        pgn_file.write(unified_pgn)

if __name__ == '__main__':
    # Define your game parameters
    num_games = 50
    player1 = stockfish_2
    name1 = "stockfish_1000_rating"
    ply1 = 0
    player2 = stockfish_1
    name2 = "stockfish_800_rating"
    ply2 = 0
    file_name = f"{name1}_vs_{name2}.pgn"
    create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2)












