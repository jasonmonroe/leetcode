"""
|--------------------------------------------------------------------------
| Redistribution System
|--------------------------------------------------------------------------
| If no winner, remove the candidate with the least amount of votes.  Then
| take the ballots and count the next choice votes of losing candidate and
| redistribute them to the remaining candidates.  Continue this process until
| a candidate receives more than half of the votes do determine the winner.
"""
class RedistributionSystem:
    def __init__(self):

        print('Redistribution System')

