import multiprocessing as mp
import tests.tools.game_tools as pg
import version_control.last_best_prodigy as prodigy_v3
import version_control.v2 as prodigy_v2


def create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2):
    for game_num in range(48, num_games + 1):
        game = pg.generate_game_uci_commnication(player1, name1, ply1, player2, name2, ply2,game_num)
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
    player1 = '/home/lipelangoni/Downloads/acqua/acqua.exe'
    name1 = "acqua"
    ply1 = 0
    player2 = prodigy_v3.engine_v2
    name2 = "prodigy_v3"
    ply2 = 4
    file_name = f"{name1}_vs_{name2}_mate_corrected.pgn"
    create_pgn_file(file_name, num_games, player1, name1, ply1, player2, name2, ply2)

