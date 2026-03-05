#FIX: Refactored from app.py into logic_utils.py using Claude Agent mode. Fixed Hard range from 1,50 to 1,1000.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 1000  #Bug 1 fix - Hard was returning 1,50 which is easier than Normal (1,100), changed to 1,1000
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


#FIX: Refactored from app.py using Claude Agent mode. Fixed return type from tuple to plain string so tests pass. Fixed swapped hint outcomes.
def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome string.

    Returns: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"  #Bug 3 fix - hints "Too High" and "Too Low" were swapped, misleading players
    return "Too Low"


#FIX: Refactored from app.py using Claude Agent mode. Fixed scoring so wrong guesses always subtract points, never reward them.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5  #Bug 2 fix - wrong guesses on even attempts were rewarding +5 points instead of -5

    return current_score
