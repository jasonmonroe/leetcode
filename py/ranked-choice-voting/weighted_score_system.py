"""
|--------------------------------------------------------------------------
| Weighted Score System
|--------------------------------------------------------------------------
| This is a system where you rank the candidates in order of preference.
| first place votes are weighted by 1, second place votes are weighted by 1/2,
| third place votes are weighted by 1/3, and fourth place votes are weighted by 1/4.
| Multiply the number of votes by the weight and add them up to determine the
| winner.
|
| Note: No candidates are eliminated until the final round.
"""

from helpers import map_id_to_candidate_index, sort_candidates, show_output
from voting_system import VotingSystem

class WeightedScoreSystem(VotingSystem):
    def __init__(self, candidates, ballots):
        super().__init__(candidates, ballots) # constructor of parent class

    """
    Score candidate points based on votes ranked by choice.
    """
    def score_ballots(self):
        for c in range (0, len(self.candidates)):
            total = 0
            for j in range (0, len(self.choice_vals)):
                print('Candidate:', self.candidates[c].id, 'Votes:', self.candidates[c].votes[j], 'x Choice:', self.choice_vals[j])
                total += self.candidates[c].votes[j] * self.choice_vals[j]

            self.candidates[c].total = total
            print(f'Weighted Totals: Candidate {self.candidates[c].id} Total: {self.candidates[c].total}')

    """
    Determine the winner based on the highest total points.
    # Override the parent class method.
    """
    def determine_winner(self, round_num = None):
        if show_output is True:
            print('Determining winner...')

        winner_id = None
        total = 0
        tied_candidates = []

        for i in range (0, len(self.candidates)):

            # If a candidate has more points than the current points leader temporarily set that candidate as the winner.
            if self.candidates[i].total > total:
                total = self.candidates[i].total
                winner_id = self.candidates[i].id

            elif self.candidates[i].total == total:
                tied_candidates.append(self.candidates[i])

        if len(tied_candidates) > 0:
            # Set init placement to 0 for first place.
            first_choice_index = 0
            winner_id = self.break_tie_weighted(tied_candidates, first_choice_index)

        if winner_id is not None:
            self.winner_id = winner_id
            winner_index = map_id_to_candidate_index(self.winner_id, self.candidates)
            self.candidates[winner_index].is_winner = True
            print('Winner Declared! ', self.candidates[winner_index].name)
        else:
            print('No winner found.')

        # Order candidates by total descending.
        self.candidates = sort_candidates(self.candidates)
