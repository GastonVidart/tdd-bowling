from src.bowling import play_bowling


def test_all_gutter():
    # modulo para testear la partida de todos ceros
    result, terminado = play_bowling(current_score=0, rolls=20, pins=0)
    assert result == 0
    assert terminado


def test_all_ones():
    # modulo para testear partida todos 1
    result, terminado = play_bowling(current_score=0, rolls=20, pins=1)
    assert result == 20
    assert terminado


def test_spare():
    result, terminado = play_bowling(current_score=0, rolls=1, pins=3)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=7)
    result, terminado = play_bowling(current_score=result, rolls=18, pins=1)
    assert result == 29
    assert terminado


def test_strike():
    result, terminado = play_bowling(current_score=0, rolls=1, pins=10)
    result, terminado = play_bowling(current_score=result, rolls=18, pins=1)
    assert result == 30
    assert terminado


def test_mezcla_strike_spare():
    result, terminado = play_bowling(current_score=0, rolls=1, pins=2)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=5)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=7)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=2)
    assert result == 16
    
    # spare
    result, terminado = play_bowling(current_score=result, rolls=1, pins=4)    
    result, terminado = play_bowling(current_score=result, rolls=1, pins=6)        
    result, terminado = play_bowling(current_score=result, rolls=1, pins=7)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=2)
    assert result == 42
        
    result, terminado = play_bowling(current_score=result, rolls=6, pins=3)
    assert result == 60    

    # strike
    result, terminado = play_bowling(current_score=result, rolls=1, pins=10)    
    result, terminado = play_bowling(current_score=result, rolls=1, pins=4)    
    result, terminado = play_bowling(current_score=result, rolls=1, pins=5)    
    assert result == 88    

    result, terminado = play_bowling(current_score=result, rolls=2, pins=4)
    assert result == 96
    assert terminado
