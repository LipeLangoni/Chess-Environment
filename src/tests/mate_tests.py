def check_mate_in_one(engine):
  board = chess.Board("1kr4r/ppp5/8/8/8/5Q2/PPP3B1/1KR4R w - - 0 1")

  print("---------First Test---------")
  for ply in range(0,3):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "f3b7")
    assert str(move) == "f3b7"
    print("Sucess")

  print("---------Second Test---------")
  board = chess.Board("1kr4r/ppp5/4b3/8/2q5/5Q2/PPP3B1/1KR4R b - - 0 1")
  for ply in range(0,3):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "c4a2")
    assert str(move) == "c4a2"
    print("Sucess")

  print("---------Third Test---------")
  board = chess.Board("1kr4r/pp5R/2p1b3/8/2q5/1P6/P1P2QB1/1KR3B1 w - - 0 1")
  for ply in range(0,3):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "f2a7")
    assert str(move) == "f2a7"
    print("Sucess")

  print("---------Forth Test---------")
  board = chess.Board("1kr4r/pp4bR/2p1b3/8/8/1Pq5/P1P2QB1/1KR3B1 b - - 0 1")
  for ply in range(0,3):
    move = engine(board,ply)
    move = move.movement(ply)
    print(str(move) + " :" + str(ply) + " :" + "c3b2 and c3a1")
    assert str(move) == "c3b2" or str(move) == "c3a1"
    print("Sucess")



    

def check_mate_in_two(engine):
  print("---------First Test---------")
  board = chess.Board("1k5r/8/8/8/8/4R3/PPP5/1K6 b - - 0 1")
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "h8h1")
  assert str(move) == "h8h1"
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "h1e1")
  assert str(move) == "h1e1"
  print("Sucess")

  print("---------Second Test---------")
  board = chess.Board("1k6/ppp5/3r4/8/8/4R3/PPP5/1K6 w - - 0 1")
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "e3e8")
  assert str(move) == "e3e8"
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "e8d8")
  assert str(move) == "e8d8"
  print("Sucess")

  print("---------Third Test---------")
  board = chess.Board("1kr5/ppp5/8/4q3/8/2P5/P6r/1KR5 b - - 0 1")
  move = engine(board,3)
  move = move.movement(3)
  print(str(move) + " :" + str(3) + " :" + "e5b5")
  assert str(move) == "e5b5"
  board.push(move)
  move = engine(board,3)
  move = move.movement(3)
  board.push(move)
  move = engine(board,3)
  move = move.movement(3)
  print(str(move) + " :" + str(3) + " :" + "b5b2")
  assert str(move) == "b5b2"
  print("Sucess")

  print("---------Forth Test---------")
  board = chess.Board("1kr5/p6R/2p2q2/8/4Q3/8/P1P4r/1KR5 w - - 0 1")
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "e4b4")
  assert str(move) == "e4b4"
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  board.push(move)
  move = engine(board,2)
  move = move.movement(2)
  print(str(move) + " :" + str(2) + " :" + "b4b7")
  assert str(move) == "b4b7"
  print("Sucess")