"""
|--------------------------------------------------------------------------
| Point Score System
|--------------------------------------------------------------------------
| This is a system where you rank the candidates in order of preference.
| 1st place votes are weighted by 1, 2nd place votes are weighted by 1/2,
| 3rd place votes are weighted by 1/3 and 4th place votes are weighted by 1/4.
| Multiply the number of votes by the weight and add them up to determine the
| winner.
|
| Note: No candidates are eliminated until the final round.
"""
class PointScoreSystem:
    def __init__(self):
        print('Point Score System')
