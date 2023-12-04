import chess
import random

class engine():
  def __init__(self, board, ply):
    self.board = board
    self.ply = ply
    self.cor = self.board.turn

  def is_ending(self):
      queens = 0
      minors = 0

      queens+= len(self.board.pieces(chess.QUEEN,True))
      queens+= len(self.board.pieces(chess.QUEEN,True))

      pecas = [chess.ROOK, chess.BISHOP, chess.QUEEN]

      for peca in pecas:
        minors += len(self.board.pieces(peca,True))
        minors += len(self.board.pieces(peca,False))

      if queens == 0 or (queens == 2 and minors <= 1):
        return True

      return False

  def Piece_Square_Table(self, color):
    pawntable = [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0]

    knightstable = [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50]

    bishopstable = [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20]

    rookstable = [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0]

    queenstable = [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 5, 5, 5, 5, 5, 0, -10,
        0, 0, 5, 5, 5, 5, 0, -5,
        -5, 0, 5, 5, 5, 5, 0, -5,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20]

    if self.is_ending():
      kingstable = [
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
]
    else:
      kingstable = [
          20, 30, 10, 0, 0, 10, 30, 20,
          20, 20, -10, -10, -10, -10, 20, 20,
          -10, -20, -20, -20, -20, -20, -20, -10,
          -20, -30, -30, -40, -40, -30, -30, -20,
          -30, -40, -40, -50, -50, -40, -40, -30,
          -30, -40, -40, -50, -50, -40, -40, -30,
          -30, -40, -40, -50, -50, -40, -40, -30,
          -30, -40, -40, -50, -50, -40, -40, -30]


    pecas = {chess.PAWN:pawntable, chess.ROOK:rookstable, chess.BISHOP:bishopstable,chess.KNIGHT:knightstable, chess.QUEEN:queenstable, chess.KING:kingstable}
    pecas_indx = {chess.PAWN:0, chess.ROOK:1, chess.BISHOP:2,chess.KNIGHT:3, chess.QUEEN:4, chess.KING:5}
    pecas_w = [0,0,0,0,0,0]
    pecas_b = [0,0,0,0,0,0]

    for peca in pecas:
       for i in self.board.pieces(peca, color):
          pecas_w[pecas_indx[peca]] += pecas[peca][i]

    for peca in pecas:
       for i in self.board.pieces(peca, not color):
          pecas_b[pecas_indx[peca]] -= pecas[peca][chess.square_mirror(i)]

    score = sum([i + b for i,b in zip(pecas_w,pecas_b)])

    return score

  def avaliacao(self,cor):
    if self.board.is_checkmate():
      if self.board.turn == self.cor:
        return +9999
      else:
        return -9999
        
    score = 0
    pecas = {chess.PAWN:100, chess.ROOK:500,
    chess.BISHOP:300.15,chess.KNIGHT:300,
    chess.QUEEN:900}

    for peca, valor in pecas.items():
      score += len(self.board.pieces(peca,cor)) * valor
      score -= len(self.board.pieces(peca, not cor)) * valor

    score += self.Piece_Square_Table(self.board.turn)
    return score


  def negamax(self, alpha, beta, ply):

    if ply == 0 or self.board.is_checkmate():
      return self.avaliacao(self.board.turn)

    score = 0
    best_value = -1000
    #sorted_moves = sorted(list(self.board.legal_moves), key=is_check_move, reverse=True)
    #print(list(self.board.legal_moves))
    for move in list(self.board.legal_moves):
      self.board.push(move)
      score = -self.negamax(-beta, -alpha, ply-1)
      # print("------- "+str(ply)+ "------")
      # print(str(move) + " : " + str(score))
      self.board.pop()
      if best_value < score:
        best_value = score

      if score >= beta:
        # print("-------Eureka Cutoff------")
        # print(str(move) + " : " + str(score) + " : " + str(beta))
        return beta
      
    
      

      alpha = max(score, alpha)

    return best_value

  def quisce(self,alpha,beta,ply):
    if ply == 0:
      return self.avaliacao(self.board.turn)

    stand_pat = self.avaliacao(self.board.turn)
    if stand_pat >= beta:
      return beta

    delta = 1000

    if alpha < stand_pat:
      alpha = stand_pat

    for move in list(self.board.legal_moves):
      if self.board.is_capture(move):
        self.board.push(move)
        score = -self.quisce(-beta, -alpha, ply-1)
        self.board.pop()

        if move.promotion:
            delta+=750
        if stand_pat < alpha-delta:
            return alpha
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha

  def check_move(self,ply):
    if self.board.is_checkmate():
        if self.board.turn == self.cor:
          return +9999
        else:
          return -9999
    if ply == 0:
      return self.avaliacao(self.board.turn)

    score = 0

    best_value = -1000
    for move in list(self.board.legal_moves):
      #print("Candidate: ",move)
      self.board.push(move)
      score = -self.check_move(ply-1)
      self.board.pop()
      # print(f"-----Depth {ply} -----")
      # print(move," : ",score)
      if score == 9999:
        return score

      if best_value < score:
        best_value = score


    return best_value


  def movement(self, ply):

    best_move = None
    best_value = -1000

    alpha = -1000
    beta = 1000

    for move in list(self.board.legal_moves):
      #print(move)
      self.board.push(move)
      score = -self.negamax(-beta, -alpha, ply)
      self.board.pop()

      if best_move == None:
          best_move = move
          best_value = score
          
      if best_value < score:
          best_value = score
          best_move = move

    return best_move