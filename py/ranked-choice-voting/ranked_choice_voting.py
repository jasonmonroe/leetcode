"""
|--------------------------------------------------------------------------
| Ranked Choice Voting
|--------------------------------------------------------------------------
| Jason Monroe
| jason@jasonmonroe.com
| ranked_choice_voting.py
|
| January 19, 2025
|--------------------------------------------------------------------------
| Overview:  Voters approved a revamp of the election season where no longer
| is it who gets the most votes wins the election but now a rank-choice voting
| system that takes into account overall voter sentiment.
|
| This system allows voters to rank their choices in order of preference. If
| a candidate receives more than half of the first choice votes, they win.
|
| This is a script to run multiple elections to determine a winner by a ranked
| choice.
| The systems are: Point Score, Remaining Candidates, Next Choice, Redistribution,
| Voted-Weighted Systems
"""

# Import Libraries
from election import Election
from helpers import uid
from redistribution_system import RedistributionSystem
from rem_candidates_system import RemainingCandidatesSystem
from weighted_score_system import WeightedScoreSystem

"""
|--------------------------------------------------------------------------
| All Voting Weighted System
|--------------------------------------------------------------------------
| Take the number of points of each candidate for each voting system and weigh
| them to determine an overall winner. 
|
| Voting System Weights:
|   - Weighted (Point) Score: 25%
|   - Remaining Candidates: 50%
|   - Redistribution: 25%
"""
class AllVotingWeightedSystem:
    def __init__(self):

        # Voting System Weights
        self.weighted_score = 0.25
        self.remaining_candidates = 0.50
        self.redistribution = 0.25

    def calc_totals_by_system(self, weighted, remaining, redistribution):
        """
        Calculate the total points for each candidate based on the weighted system.

        :param float weighted: The weighted score system total.
        :param float remaining: The remaining candidates system total.
        :param float redistribution: The redistribution system total.

        :return: None
        """

        candidates = []



### Run Program
benchmark_id = uid(6)
print(f'\n* Start Benchmark ID: {benchmark_id} *')

# Create and run election
elect = Election()
elect.election_day()

# Make copies of the candidates and ballots for each system. This is to ensure the original data is not modified.
ballots = elect.ballots.copy()
candidates = elect.candidates.copy()


# Tally Weighted Score System
#print('\n\n- WEIGHTED SCORE SYSTEM -')
weight_candidates = candidates.copy()
weight = WeightedScoreSystem(weight_candidates, ballots.copy())
print(f'\n- {weight.title.upper()} VOTING SYSTEM -')
weight.score_ballots()
weight.determine_winner()



# Tally Remaining Candidates System
#print('\n\n- REMAINING CANDIDATES SYSTEM -')
rem_candidates = candidates.copy()
rem = RemainingCandidatesSystem(rem_candidates, ballots.copy())
print(f'\n- {rem.title.upper()} VOTING SYSTEM -')
rem.score_ballots()



# Tally Redistribution System
redistribution_candidates = candidates.copy()
redistribution = RedistributionSystem(redistribution_candidates, ballots.copy())
print(f'\n- {redistribution.title.upper()} VOTING SYSTEM -')
redistribution.score_ballots()


# Tally Average-Weighted Systems
print('- AVERAGE WEIGHTED SYSTEM -')
all_weighted = AllVotingWeightedSystem()


# Show Results
print(f'\n* End Benchmark ID: {benchmark_id} *')

### End of Program
