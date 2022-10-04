from prodigy import *
class uci():
  def __init__(self):
    self.board = chess.Board()
  
  def communication(self):
    ply = 3
    mensagem = ""
    while mensagem != "quit":
      mensagem = input()
      self.uci_commands(ply, mensagem)
  
  def uci_commands(self,depth: int, mensagem: str):
    mensagem = mensagem.strip()
    tokens = mensagem.split(" ")
    while "" in tokens:
        tokens.remove("")

    if mensagem == "quit":
        sys.exit()

    if mensagem == "uci":
        print("id name Prodigy") 
        print("id author Felipe langoni Ramos")
        print("uciok")
        return

    if mensagem == "isready":
        print("readyok")
        return

    if mensagem == "ucinewgame":
        return

    if mensagem.startswith("position"):
        if len(tokens) < 2:
            return

        if tokens[1] == "startpos":
            self.board.reset()
            moves_start = 2
        elif tokens[1] == "fen":
            fen = " ".join(tokens[2:8])
            self.board.set_fen(fen)
            moves_start = 8
        else:
            return

        if len(tokens) <= moves_start or tokens[moves_start] != "moves":
            return

        for move in tokens[(moves_start+1):]:
            self.board.push_uci(move)

    if mensagem == "d":
        print(self.board)
        print(self.board.fen())

    if mensagem[0:2] == "go":
        movimento = engine(self.board,depth)
        movimento = movimento.movement()
        print(f"bestmove {movimento}")
        return
      
prodigy = uci()
prodigy.communication()
