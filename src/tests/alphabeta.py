import chess


def assert_evaluation():
    board = chess.Board("2k3r1/1pp2p2/p1p2nrp/2q1p3/4P3/2NP1Q1P/PPP2PP1/R4RK1 w - - 0 16")
    score = evaluation(board,board.turn)
    assert score == 0