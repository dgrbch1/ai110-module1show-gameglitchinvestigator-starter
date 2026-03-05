from logic_utils import check_guess, get_range_for_difficulty, update_score, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Bug 1 fix - Hard range was 1,50 which is easier than Normal 1,100
def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, "Hard should have a larger range than Normal"


# Bug 2 fix - wrong guesses on even attempts were rewarding +5 instead of -5
def test_wrong_guess_always_loses_points():
    score = update_score(100, "Too High", 2)  # attempt 2 is even — was the bugged case
    assert score < 100, "A wrong guess should never increase the score"

def test_too_low_always_loses_points():
    score = update_score(100, "Too Low", 2)
    assert score < 100, "A Too Low guess should never increase the score"


# Bug 3 fix - Too High and Too Low outcomes were swapped
def test_higher_guess_is_too_high():
    result = check_guess(99, 1)  # guess way above secret
    assert result == "Too High", "Guess above secret should return Too High"

def test_lower_guess_is_too_low():
    result = check_guess(1, 99)  # guess way below secret
    assert result == "Too Low", "Guess below secret should return Too Low"
