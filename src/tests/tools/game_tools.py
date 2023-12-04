import time
import chess
import chess.polyglot as plg
import random
import inspect
#from IPython.display import display, HTML, clear_output
from datetime import datetime
import chess.pgn
import chess.polyglot
import subprocess


def side(player):
    return "White" if player == chess.WHITE else "Black"
def display_board(board, use_svg):
    if use_svg:
        return board._repr_svg_()
    else:
        return "<pre>" + str(board) + "</pre>"

# Meus incrementos
def controle_de_vantagem(board):
  scoreW = 0
  scoreB = 0
  pawn, knight, bishop, queen = chess.PAWN,chess.KNIGHT,chess.BISHOP, chess.QUEEN
  dic = {pawn:1, knight:3,bishop:3.15,chess.ROOK:5,queen:10}

  for piece, value in dic.items():
    scoreW+= len(board.pieces(piece, chess.WHITE)) * value
    scoreB+= len(board.pieces(piece, chess.BLACK)) * value
  
  resultW = "{:.2f}".format(scoreW - scoreB)
  resultB = "{:.2f}".format(scoreB - scoreW)

  resultado = ("White:" + str(resultW) + ", BLack:" + str(resultB))

  return resultado


# def play_game(player1, ply1, player2, ply2, visual="svg", pause=0.1):
#     use_svg = (visual == "svg")
#     board = chess.Board()
#     book_paths = ["/home/lipelangoni/Documents/Prodigy_Engine/baron30.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/komodo.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/rodent.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/gm2001.bin"]
#     book = chess.polyglot.open_reader(random.choice(book_paths))
#     try:
#         while not board.is_game_over(claim_draw=True):
#             openings = []
#             for entry in book.find_all(board):
#                 openings.append(entry.move)

#             if len(openings) != 0:
#                 uci = random.choice(openings)

#             elif board.turn == chess.WHITE:
#               if inspect.isclass(player1):
#                 uci = player1(board,ply1)
#                 uci = uci.movement(ply1)
#               else:
#                 uci = player1(board,ply1)
#             else:
#               if inspect.isclass(player2):
#                 uci = player2(board,ply2)
#                 uci = uci.movement(ply2)
#               else:
#                 uci = player2(board,ply2)
#             name = side(board.turn)
#             print(uci)
#             board.push(uci)
#             controle = controle_de_vantagem(board)
#             board_stop = display_board(board, use_svg)
#             html = "<b>Vantagem :'%s',Move %s %s, Play '%s':</b><br/>%s" % (controle,
#                        len(board.move_stack), name, uci, board_stop)
#             if visual is not None:
#                 if visual == "svg":
#                     clear_output(wait=True)
#                 display(HTML(html))
#                 if visual == "svg":
#                     time.sleep(pause)
#     except KeyboardInterrupt:
#         return (None, board)
#     result = None
#     if board.is_checkmate():
#         msg = "checkmate: " + side(not board.turn) + " wins!"
#         result = not board.turn
#     elif board.is_stalemate():
#         msg = "draw: stalemate"
#     elif board.is_fivefold_repetition():
#         msg = "draw: 5-fold repetition"
#     elif board.is_insufficient_material():
#         msg = "draw: insufficient material"
#     elif board.can_claim_draw():
#         msg = "draw: claim"
#     if visual is not None:
#         print(msg)
#     return (result, msg, board)


def test_game(player1,ply1,player2,ply2):
    board = chess.Board()

    game = chess.pgn.Game()
    game.headers["Event"] = "Prodigy Self Play"
    game.headers["Date"] = datetime.today()
    game.headers["White"] = str(player1).replace("class","")
    game.headers["Black"] = str(player2).replace("class","")
    for i in range(200):
        if board.turn == chess.WHITE:
            if inspect.isclass(player1):
                move = player1(board,ply1)
                move = move.movement(ply1)
            else:
                move = player1(board,ply1)
            if move == None:
                return game
            
        else: 
            if inspect.isclass(player2):
                move = player2(board,ply2)
                move = move.movement(ply2)
            else:
                move = player2(board,ply2)
            if move == None:
                return game
        board.push(move)
        if i == 0:
            node = game.add_variation(move)
        else:
            node = node.add_variation(move)
        if board.is_checkmate():
            result = not board.turn
            if result == True:
                game.headers["Result"] = "1-0"
            else:
                game.headers["Result"] = "0-1"
            return game
        elif board.is_stalemate():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.is_fivefold_repetition():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.is_insufficient_material():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.can_claim_draw():
                game.headers["Result"] = "1/2-1/2"
                return game

def generate_game(player1,name1,ply1,player2,name2,ply2,Round):
    board = chess.Board()

    book_paths = ["/home/lipelangoni/Documents/Prodigy_Engine/baron30.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/komodo.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/rodent.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/gm2001.bin"]
    book = chess.polyglot.open_reader(random.choice(book_paths))
      
    game = chess.pgn.Game()
    game.headers["Event"] = "Prodigy_tets"
    game.headers["Round"] = Round
    game.headers["Date"] = datetime.today()
    game.headers["White"] = name1
    game.headers["Black"] = name2
    game.headers["WhiteElo"] = "1000"
    for i in range(200):
        openings = []
        for entry in book.find_all(board):
            openings.append(entry.move)

        if len(openings) != 0:
            move = random.choice(openings)

        elif board.turn == chess.WHITE:
            if inspect.isclass(player1):
                move = player1(board,ply1)
                move = move.movement(ply1)
            else:
                move = player1(board,ply1)
            if move == None:
                return game
            
        else: 
            if inspect.isclass(player2):
                move = player2(board,ply2)
                move = move.movement(ply2)
            else:
                move = player2(board,ply2)
            if move == None:
                return game
        board.push(move)
        if i == 0:
            node = game.add_variation(move)
        else:
            node = node.add_variation(move)
        if board.is_checkmate():
            result = not board.turn
            if result == True:
                game.headers["Result"] = "1-0"
            else:
                game.headers["Result"] = "0-1"
            return game
        elif board.is_stalemate():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.is_fivefold_repetition():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.is_insufficient_material():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.can_claim_draw():
                game.headers["Result"] = "1/2-1/2"
                return game

def generate_game_uci_commnication(player1,name1,ply1,player2,name2,ply2,Round):
    board = chess.Board()

    book_paths = ["/home/lipelangoni/Documents/Prodigy_Engine/baron30.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/komodo.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/rodent.bin","/home/lipelangoni/Documents/Prodigy_Engine/src/bin/gm2001.bin"]
    book = chess.polyglot.open_reader(random.choice(book_paths))
      
    game = chess.pgn.Game()
    game.headers["Event"] = "Prodigy_tets"
    game.headers["Round"] = Round
    game.headers["Date"] = datetime.today()
    game.headers["White"] = name1
    game.headers["Black"] = name2
    game.headers["WhiteElo"] = "1000"
    for i in range(1000):
        openings = []
        for entry in book.find_all(board):
            openings.append(entry.move)

        if len(openings) != 0:
            move = random.choice(openings)

        elif board.turn == chess.WHITE:
            if inspect.isclass(player1):
                move = player1(board,ply1)
                move = move.movement(ply1)
            else:
                engine_process = subprocess.Popen(
                        ["wine",player1],
                        stdin=subprocess.PIPE, 
                        stdout=subprocess.PIPE,  
                        stderr=subprocess.PIPE,  
                        text=True  
                        )
                comando = f"position fen {board.fen()}\n"
                engine_process.stdin.write(comando)
                engine_process.stdin.flush()

                comando_go = "go\n"
                engine_process.stdin.write(comando_go)
                engine_process.stdin.flush()

                move = None
                for linha in engine_process.stdout:
                    if linha.startswith("bestmove"):
                        move = linha.split()[1]
                        break
                if move != None:
                    move = chess.Move.from_uci(move)               
            if move == None:
                return game
            
        else: 
            if inspect.isclass(player2):
                move = player2(board,ply2)
                move = move.movement(ply2)
            else:
                engine_process = subprocess.Popen(
                        ["wine",player2],
                        stdin=subprocess.PIPE,  # Para permitir a escrita no processo
                        stdout=subprocess.PIPE,  # Para capturar a saída do processo
                        stderr=subprocess.PIPE,  # Se você quiser capturar erros
                        text=True  # Para trabalhar com texto (strings) em vez de bytes
                        )
                comando = f"position fen {board.fen()}\n"
                engine_process.stdin.write(comando)
                engine_process.stdin.flush()

                comando_go = "go\n"
                engine_process.stdin.write(comando_go)
                engine_process.stdin.flush()

                move = None
                for linha in engine_process.stdout:
                    if linha.startswith("bestmove"):
                        move = linha.split()[1]
                        break
                if move != None:
                    move = chess.Move.from_uci(move)   
            if move == None:
                return game
        board.push(move)
        if i == 0:
            node = game.add_variation(move)
        else:
            node = node.add_variation(move)
        if board.is_checkmate():
            result = not board.turn
            if result == True:
                game.headers["Result"] = "1-0"
            else:
                game.headers["Result"] = "0-1"
            return game
        elif board.is_stalemate():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.is_fivefold_repetition():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.is_insufficient_material():
                game.headers["Result"] = "1/2-1/2"
                return game
        elif board.can_claim_draw():
                game.headers["Result"] = "1/2-1/2"
                return game
    