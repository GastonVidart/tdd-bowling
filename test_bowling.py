from src.bowling import play_bowling

def test_all_gutter():
    result = play_bowling(current_score = 0, rolls = 20, pins = 0)
    assert result == 0
