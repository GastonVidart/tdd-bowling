from src.bowling import play_bowling

# Primer Ciclo
def test_all_gutter():
    # modulo para testear la partida de todos ceros
    result, terminado = play_bowling(current_score=-1, rolls=20, pins=0)
    assert result == 0
    assert terminado

# Segundo Ciclo
def test_all_ones():
    # modulo para testear partida todos 1
    result, terminado = play_bowling(current_score=-1, rolls=20, pins=1)
    assert result == 20
    assert terminado

# Tercero Ciclo
def test_spare():
    result, terminado = play_bowling(current_score=-1, rolls=1, pins=3)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=7)
    result, terminado = play_bowling(current_score=result, rolls=18, pins=1)
    assert result == 29
    assert terminado

# Cuarto Ciclo
def test_strike():
    result, terminado = play_bowling(current_score=-1, rolls=1, pins=10)
    result, terminado = play_bowling(current_score=result, rolls=18, pins=1)
    assert result == 30
    assert terminado

# Quinto Ciclo
def test_mezcla_strike_spare():
    result, terminado = play_bowling(current_score=-1, rolls=1, pins=2)
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

# Sexto Ciclo 1
def test_ronda_10_all_strike():
    result, terminado = play_bowling(current_score=-1, rolls=18, pins=0)
    result, terminado = play_bowling(current_score=result, rolls=3, pins=10)
    assert result == 30
    assert terminado

# Sexto Ciclo 2
def test_ronda_10_strike_spare():
    result, terminado = play_bowling(current_score=-1, rolls=18, pins=0)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=10)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=4)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=6)
    assert result == 20
    assert terminado

# Sexto Ciclo 3
def test_ronda_10_strike():
    result, terminado = play_bowling(current_score=-1, rolls=18, pins=0)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=10)
    result, terminado = play_bowling(current_score=result, rolls=2, pins=4)
    assert result == 18
    assert terminado

# Sexto Ciclo 4
def test_ronda_10_spare_strike():
    result, terminado = play_bowling(current_score=-1, rolls=18, pins=0)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=4)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=6)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=10)
    assert result == 20
    assert terminado

# Sexto Ciclo 5
def test_ronda_10_spare():
    result, terminado = play_bowling(current_score=-1, rolls=18, pins=0)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=4)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=6)
    result, terminado = play_bowling(current_score=result, rolls=1, pins=5)
    assert result == 15
    assert terminado

# Septimo Ciclo 
def test_all_strike():
    result, terminado = play_bowling(current_score=-1, rolls=12, pins=10)
    assert result == 300
    assert terminado

# Octavo Ciclo 1
def test_score():
    # test maximo puntaje posible hasta 300, test con 301
    result, terminado = play_bowling(current_score=301, rolls=1, pins=7)
    assert result == -2
    assert not terminado

    # test minimo puntaje posible hasta -2, test con -3
    result, terminado = play_bowling(current_score=-3, rolls=1, pins=7)
    assert result == -2
    assert not terminado

# Octavo Ciclo 2
def test_pins():
    # test maximos pins tirados hasta 10, test con 11
    result, terminado = play_bowling(current_score=-1, rolls=1, pins=11)
    assert result == -2
    assert not terminado

    # test minimos pins tirados hasta 0, test con -1
    result, terminado = play_bowling(current_score=-1, rolls=1, pins=-1)
    assert result == -2
    assert not terminado

    # test maximos pins tirados por ronda, test con dos tiros de 7
    result, terminado = play_bowling(current_score=-1, rolls=2, pins=7)
    assert result == -2
    assert not terminado

# Octavo Ciclo
def test_rondas():
    # test maximas rondas posibles hasta 10, test con 22 tiros = 11 rondas
    result, terminado = play_bowling(current_score=-1, rolls=22, pins=5)
    assert result == -2
    assert not terminado

    # test minimas rondas posibles hasta 10, test con -1
    result, terminado = play_bowling(current_score=-1, rolls=-1, pins=5)
    assert result == -2
    assert not terminado