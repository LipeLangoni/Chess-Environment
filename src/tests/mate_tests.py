import chess
from src.version_control import last_best_prodigy as prodigy_v3

engine = prodigy_v3.engine_v2

def test_check_mate_in_one():
  board = chess.Board("1kr4r/ppp5/8/8/8/5Q2/PPP3B1/1KR4R w - - 0 1")

  print("---------First Test---------")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "f3b7")
    assert str(move) == "f3b7"
    print("Sucess")

  print("---------Second Test---------")
  board = chess.Board("1kr4r/ppp5/4b3/8/2q5/5Q2/PPP3B1/1KR4R b - - 0 1")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "c4a2")
    assert str(move) == "c4a2"
    print("Sucess")

  print("---------Third Test---------")
  board = chess.Board("1kr4r/pp5R/2p1b3/8/2q5/1P6/P1P2QB1/1KR3B1 w - - 0 1")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "f2a7")
    assert str(move) == "f2a7"
    print("Sucess")

  print("---------Forth Test---------")
  board = chess.Board("1kr4r/pp4bR/2p1b3/8/8/1Pq5/P1P2QB1/1KR3B1 b - - 0 1")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "c3b2 and c3a1")
    assert str(move) == "c3b2" or str(move) == "c3a1"
    print("Sucess")


def test_check_mated_in_one():
  board = chess.Board("1kr4r/ppp5/8/8/8/5Q2/PPP3B1/1KR4R b - - 0 1")

  print("---------First Test---------")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "c7c6")
    assert str(move) == "c7c6"
    print("Sucess")

  print("---------Second Test---------")
  board = chess.Board("1kr4r/ppp5/2n1b3/8/2q5/5Q2/PPP3B1/1KR4R w - - 0 1")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply))
    assert not board.is_checkmate()
    print("Sucess")

  print("---------Third Test---------")
  board = chess.Board("4r3/p5k1/1pR5/3B1p2/1b1P1N2/1N4P1/r7/6K1 w - - 4 32")
  
  move = engine(board,ply)
  move = move.movement(4)
  print(str(move) + " :" + str(4))
  assert str(move) == "f4d3"
  print("Sucess")


  print("---------Forth Test---------")
  board = chess.Board("1kr4r/pp4bR/2p1b3/8/8/1Pq5/P1P2QB1/1KR3B1 w - - 0 1")
  for ply in range(1,4):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "h7g7, f2a7 and g1h2")
    assert str(move) == "h7g7" or str(move) == "f2a7" or str(move) == "g1h2"
    print("Sucess")
  
  print("---------Fith Test---------")
  board = chess.Board("1r5k/p2b1Qp1/1qp4p/8/2B5/P1P1P2P/5PP1/3R2K1 b - - 2 31")
  
  move = engine(board,ply)
  move = move.movement(4)
  print(str(move) + " :" + str(4))
  assert str(move) == "d7h3"
  print("Sucess")

def test_check_mate_in_two():
  print("---------First Test---------")
  board = chess.Board("1k5r/8/8/8/8/4R3/PPP5/1K6 b - - 0 1")
  move = engine(board,0)
  move = move.movement(3)
  print(str(move) + " :" + str(2) + " :" + "h8h1")
  assert str(move) == "h8h1"
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  board.push(move)
  move = engine(board,2)
  move = move.movement(3)
  print(str(move) + " :" + str(2) + " :" + "h1e1")
  assert str(move) == "h1e1"
  print("Sucess")

  print("---------Second Test---------")
  board = chess.Board("1k6/ppp5/3r4/8/8/4R3/PPP5/1K6 w - - 0 1")
  move = engine(board,2)
  move = move.movement(3)
  print(str(move) + " :" + str(2) + " :" + "e3e8")
  assert str(move) == "e3e8"
  board.push(move)
  move = engine(board,2)
  move = move.movement(3)
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "e8d8")
  assert str(move) == "e8d8"
  print("Sucess")

  # print("---------Third Test---------")
  # board = chess.Board("1kr5/ppp5/8/4q3/8/2P5/P6r/1KR5 b - - 0 1")
  # move = engine(board,3)
  # move = move.movement(3)
  # print(str(move) + " :" + str(3) + " :" + "e5b5")
  # assert str(move) == "e5b5"
  # board.push(move)
  # move = engine(board,3)
  # move = move.movement(3)
  # board.push(move)
  # move = engine(board,3)
  # move = move.movement(3)
  # print(str(move) + " :" + str(3) + " :" + "b5b2")
  # assert str(move) == "b5b2"
  # print("Sucess")

  print("---------Forth Test---------")
  board = chess.Board("1kr5/p6R/2p2q2/8/4Q3/8/P1P4r/1KR5 w - - 0 1")
  move = engine(board,2)
  move = move.movement(3)
  print(str(move) + " :" + str(2) + " :" + "e4b4")
  assert str(move) == "e4b4"
  board.push(move)
  move = engine(board,2)
  move = move.movement(3)
  board.push(move)
  move = engine(board,2)
  move = move.movement(3)
  print(str(move) + " :" + str(2) + " :" + "b4b7")
  assert str(move) == "b4b7"
  print("Sucess")