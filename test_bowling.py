from src.bowling import play_bowling

def test_all_gutter():
    #modulo para testear la partida de todos ceros
    result = play_bowling(current_score = 0, rolls = 20, pins = 0)
    assert result == 0


def test_all_ones():
    result = play_bowling(current_score = 0, rolls = 20, pins = 1)
    assert result == 20
