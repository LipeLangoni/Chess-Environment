import multiprocessing as mp
import tests.tools.game_tools as pg
import version_control.last_best_prodigy as prodigy_v3
import version_control.v2 as prodigy_v2

def create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2):
    with mp.Pool(processes=5) as pool:
        all_games = pool.starmap(pg.generate_game, [(player1, name1, ply1, player2, name2, ply2)] * num_games)

    pgn_strings = [str(game) for game in all_games]
    unified_pgn = "\n\n".join(pgn_strings)

    with open(file_name, "w") as pgn_file:
        pgn_file.write(unified_pgn)

if __name__ == '__main__':
    # Define your game parameters
    num_games = 50
    player1 = prodigy_v3.engine_v2
    name1 = "prodigy_v3"
    ply1 = 4
    player2 = prodigy_v2.engine
    name2 = "prodigy_v2"
    ply2 = 3
    file_name = f"{name1}_vs_{name2}.pgn"
    create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2)