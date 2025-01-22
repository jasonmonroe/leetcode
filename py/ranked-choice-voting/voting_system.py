# Voting System
import math
from helpers import show_output, MAX_CHOICES, NO_VOTE_VAL, FIRST_CHOICE_INDEX, map_id_to_candidate_index

class VotingSystem:
    """
    Base class for voting systems.

    Attributes:
        title (str): The title of the voting system.
        candidates (list): A list of candidates in the election.
        ballots (list): A list of ballots cast in the election.
        winner_id (int): The ID of the winning candidate.
        majority (int): The majority vote needed to win the election.
        voter_cnt (int): The number of voters in the election.
        choice_vals (list): Weighted choice values for each place.
    """

    def __init__(self, candidates, ballots):
        self.title = ''
        self.candidates = candidates
        self.ballots = ballots
        self.winner_id = None
        #self.extra_votes = 0 # Extra votes to add to the majority vote.
        self.voter_cnt = len(ballots)
        self.majority = round(self.voter_cnt / 2)

        #print('__init__ Majority:', self.majority)

        # Define weighted choice values for each place.
        self.choice_vals = [
            1,     # 1st Place
            1 / 2, # 2nd Place
            1 / 4, # 3rd Place
            1 / 8  # 4th Place
        ]

    def determine_loser(self):
        """
        Determine the candidate with the fewest votes.
        If there is a tie, break the tie by comparing the next place voted for count.

        :return:
            Candidate: The candidate with the fewest votes
        """

        # Get the candidate with the fewest votes.
        pool_of_candidates = self.get_pool_of_candidates()
        #print('Pool of candidates left:', len(pool_of_candidates))
        if show_output is True:
            print('Pool of candidates left:', len(pool_of_candidates))

        # If there is only one candidate left, declare them the winner by technicality.
        if len(pool_of_candidates) == 1:
            winning_candidate = pool_of_candidates[FIRST_CHOICE_INDEX]
            winning_candidate.is_winner = True
            self.winner_id = winning_candidate.id

            print('Only one candidate left:', winning_candidate.id)
            print('No candidate has won a majority.  Declaring remaining candidate winner by technicality.')

            return None

        # Handle the case where multiple candidates have the same minimum points:
        # 1. Find the minimum total points.
        # 2. Identify all candidates with this minimum total.
        # 3. If there are multiple candidates with the same minimum points, break the tie by comparing the next place votes.
        # 4. The candidate with the fewest next place votes is the tie-breaker.
        min_votes_candidates = self.get_lowest_voted_candidate(pool_of_candidates)

        if len(min_votes_candidates) == 1:
            return min_votes_candidates[FIRST_CHOICE_INDEX]

        else:
            # We have multiple candidates that have the same number of votes.
            # Break the tie by looking at the next place voted for count.
            vote_choice = 0
            return self.tie_breaker(min_votes_candidates, vote_choice)

    # Note: This method used in CandidateEliminationSystem & NextChoiceSystem
    def determine_winner(self, round_num=1):
        """
        Checks each candidate to see if they have the majority vote needed to win the election.

        Returns:
        bool: True if a candidate has the majority vote, False otherwise.
        """

        print('Determining winner... Round:', round_num)
        print('Majority to win: ', self.majority)

        for i in range (0, len(self.candidates)):
            print('Candidate:', self.candidates[i].id, 'Total:', self.candidates[i].total)
            if self.candidates[i].total > self.majority:
                self.candidates[i].is_winner = True
                self.winner_id = self.candidates[i].id
                print(f'Winner Declared! Candidate {self.candidates[i].id} ', self.candidates[i].name, 'Total:', self.candidates[i].total)
                return True
            else:
                print(f'Round: {round_num} Total:{self.candidates[i].total}, Candidate {self.candidates[i].id} does not have majority.')

        print('No winner found.\n')
        return False

    #@staticmethod
    def get_lowest_voted_candidate(self, candidates):
        """
        Get the candidate with the least number of votes.

        Returns:
           list: A list of candidates with the lowest total points.
        """

        print('Getting lowest voted candidate...')
        for candidate in candidates:
            print(f'Debug:Candidate ID: {candidate.id} Total: {candidate.total}')
        min_total = min(candidate.total for candidate in candidates)
        print('Minimum total:', min_total)
        return [candidate for candidate in candidates if candidate.total == min_total]


    def remove_loser_from_ballot(self, loser):
        """
        Remove the losing candidate from the ballot.

        :param loser:
            Candidate: The losing candidate.

        :return:
        """

        print(f'* Removing loser {loser.id} from ballot.')
        for i in range (0, len(self.ballots)):
            for j in range(len(self.ballots[i]) - 1, -1, -1):
                if self.ballots[i][j] == loser.id:
                    self.ballots[i].pop(j) # Remove candidate from contention
                    #print(f'New Ballot {self.ballots[i]}')

        print('\nBallots after removal:', self.ballots)

    def get_pool_of_candidates(self):
        """
        Get the pool of candidates that are still in contention.
        
        :returns: 
            list: A list of candidates that are still in contention.
        """
        return [candidate for candidate in self.candidates if candidate.is_winner is None]

    def reset_candidate_totals(self):
        """
        Reset the total points for each candidate so we can count the first choice each round.
        """
        
        for i in range(0, len(self.candidates)):
            self.candidates[i].total = 0


    # Used in NextChoiceSystem
    def tie_breaker(self, candidates, choice):
        """
        Break the tie by comparing the next place voted for count.
        Note: This function uses multiple candidates.

        :param candidates:
        :param choice:
        :return:
        """

        if show_output is True:
            print('Attempting to break tie...')

        next_choice = choice + 1

        # Initialize min votes with first index.
        min_votes = candidates[0].votes[next_choice]
        min_candidate = candidates[0]

        # Start with the next candidate in the list.
        for i in range (1, len(candidates)):
            print('Tie Breaker Candidate ID:', candidates[i].id, 'Votes:', candidates[i].votes[choice])
            if next_choice < MAX_CHOICES:
                if candidates[i].votes[next_choice] < min_votes:
                    min_votes = candidates[i].votes[next_choice]
                    min_candidate = candidates[i]

        if show_output is True:
            print('Returning minimum Candidate:', min_candidate.id)

        return min_candidate

    # Used in Weighted System
    def break_tie_weighted(self, tied_candidates, choice):
        print('Breaking tie...')
        winner_id = None
        tie_breaker_total = 0
        next_tied_candidates = []

        # If there is a tie in total points break the tie with whom got the most first place votes.
        for i in range (0, len(tied_candidates)):
            candidate = tied_candidates[i]
            total = 0

            for j in range (0, len(self.choice_vals)):
                total += candidate.votes[j] * self.choice_vals[j]
                candidate.total += total

                if total > tie_breaker_total:
                    tie_breaker_total = total
                    winner_id = candidate.id

                elif total == tie_breaker_total:
                    next_tied_candidates.append(candidate)

        # Recursion
        if len(next_tied_candidates) > 0:

            # Update the place value (started at 1st) and break the tie again.
            next_choice = choice + 1

            if next_choice < MAX_CHOICES:
                winner_id = self.break_tie_weighted(next_tied_candidates, next_choice)

        return winner_id
