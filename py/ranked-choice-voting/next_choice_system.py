"""
|--------------------------------------------------------------------------
| Next Choice System
|--------------------------------------------------------------------------
| If no winner, go to every ballot and count the next choice votes for the
| candidate. Continue this process until a candidate receives more than half
| of the votes do determine the winner.
|
| Note: No candidates are eliminated until the final round.
|
"""
from helpers import map_id_to_candidate_index, sort_candidates, place_str, MAX_CHOICES, NO_VOTE_VAL, FIRST_CHOICE_INDEX
from voting_system import VotingSystem

class NextChoiceSystem(VotingSystem):
    def __init__(self, candidates, ballots):
        super().__init__(candidates, ballots)
        self.title = 'Next Choice'

    def recount_ballots(self, vote_choice):
        """
        Count all first place votes to determine winner.
        If no majority, count every voter's next choice votes and add to the total.
        :param int vote_choice: The current vote choice.

        :return: None
        """

        for i in range(0, len(self.candidates)):
            self.candidates[i].total += self.candidates[i].votes[vote_choice]

    def score_ballots(self):
        self.reset_candidate_totals()

        candidate_cnt = len(self.candidates)
        choice_cnt = min(MAX_CHOICES, candidate_cnt)

        self.recount_ballots(FIRST_CHOICE_INDEX)
        vote_choice = FIRST_CHOICE_INDEX

        while self.determine_winner(vote_choice) is not True and vote_choice <= choice_cnt:

            for vote_choice in range (1, choice_cnt): # 1, 2, 3, n ...
                print('Vote Choice:', vote_choice, ' ')

                for i in range(0, len(self.ballots)):
                    voted_id = self.ballots[i][vote_choice]

                    if voted_id != NO_VOTE_VAL:
                        index = map_id_to_candidate_index(voted_id, self.candidates)
                        self.candidates[index].total += 1
                        print('Voted ID:', voted_id, 'Total:', self.candidates[index].total)
                    else:
                        print(f'Voter {i} did not vote for {place_str(vote_choice, "p")}.')
