"""
|--------------------------------------------------------------------------
| Next Choice System
|--------------------------------------------------------------------------
| If no winner, go to every ballot and count the next choice votes for the
| candidate. Continue this process until a candidate receives more than half
| of the votes do determine the winner.
|
| Note: No candidates are eliminated until the final round.
"""
class NextChoiceSystem:
    def __init__(self):
        print('Next Choice System')
