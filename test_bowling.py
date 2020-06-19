from src.bowling import play_bowling

def test_all_gutter():
    #modulo para testear la partida de todos ceros
    result, terminado = play_bowling(current_score = 0, rolls = 20, pins = 0)
    assert result == 0
    assert terminado

def test_all_ones():
    #modulo para testear partida todos 1
    result, terminado = play_bowling(current_score = 0, rolls = 20, pins = 1)
    assert result == 20
    assert terminado
    
def test_spare():
    result, terminado = play_bowling(current_score = 0, rolls = 1, pins = 3)
    result, terminado = play_bowling(current_score = result, rolls = 1, pins = 7)
    result, terminado = play_bowling(current_score = result, rolls = 18, pins = 1)
    assert result == 29 
    assert terminado