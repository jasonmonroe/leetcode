# Voting System
import math
from helpers import show_output, MAX_CHOICES, NO_VOTE_VAL, FIRST_CHOICE_INDEX, map_id_to_candidate_index, sort_candidates

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
        self.voter_cnt = len(ballots)
        self.majority = round(self.voter_cnt / 2)
        self.choice_vals = []


    def show_banner(self):
        """
        Show the banner for the voting system.
        """

        title_val = f'\n- {self.title.upper()} VOTING SYSTEM -'
        title_len = len(title_val)

        print(title_val)
        print('-' * title_len)

    @staticmethod
    def declare_winner(name):
        """
        Output the winner of the election.
        """

        print('\n----- WINNER -----')
        print('', name)
        print('------------------')

    def determine_loser(self):
        """
        Determine the candidate with the fewest votes.
        If there is a tie, break the tie by comparing the next place voted for count.

        :return:
            Candidate: The candidate with the fewest votes
        """

        # Get the candidate with the fewest votes.
        pool_of_candidates = self.get_pool_of_candidates()

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
        min_votes_candidates = self.get_lowest_voted_candidate(pool_of_candidates, 'total')

        if len(min_votes_candidates) == 1:
            return min_votes_candidates[FIRST_CHOICE_INDEX]

        else:
            # We have multiple candidates that have the same number of votes.
            # Break the tie by looking at the next place voted for count.
            return self.break_tie(min_votes_candidates, 'min', FIRST_CHOICE_INDEX)


    def determine_winner_by_popular(self):
        """
        Determine the winner based on the highest total points.
        Determined by popularity

        :param str rules: The rules to determine the winner.
        :param int round_num: The current round number.
        :return: Candidates candidates: The list of candidates.
        """

        candidate = None
        candidates = self.get_highest_voted_candidate(self.candidates, 'total')

        if len(candidates) == 1:
            candidate = candidates[FIRST_CHOICE_INDEX]

        elif len(candidates) > 1:
            candidate = self.break_tie(candidates, 'max', FIRST_CHOICE_INDEX)

        if candidate is not None:
            self.declare_winner(candidate.name)

        else:
            print('* No winner found *')

        self.candidates = sort_candidates(self.candidates)

        return self.candidates

    def determine_winner_by_majority(self, round_num=1):
        """
        Determines winner by majority.
        Checks each candidate to see if they have the majority vote needed to win the election.

        Returns:
        bool: True if a candidate has the majority vote, False otherwise.
        """

        #print('Determining winner... Round:', round_num)
        #print('Majority to win: ', self.majority)
        print('Round #', round_num)
        for i in range (0, len(self.candidates)):
            print('Candidate:', self.candidates[i].id, 'Total:', self.candidates[i].total)
            if self.candidates[i].total > self.majority:
                self.candidates[i].is_winner = True
                self.winner_id = self.candidates[i].id

                self.declare_winner(self.candidates[i].name)
                return True
            #else:
                #print(f'Round: {round_num} Total:{self.candidates[i].total}, Candidate {self.candidates[i].id} does not have majority.')

        print('* No winner found *\n')
        return False

    @staticmethod
    def get_highest_voted_candidate(candidates, data, choice=None):
        """
        Get the candidate with the highest number of votes.

        :param list candidates: A list of candidates to compare.
        :param string data: The data to compare.
        :param int choice: The choice to compare (optional)

        Returns:
           list: A list of candidates with the highest total points.
        """

        if data == 'total':
            return [max(candidates, key=lambda c: c.total)]
        else:
            return [max(candidates, key=lambda c: c.votes[choice])]

        """
        print('Getting highest voted candidate...')
        for candidate in candidates:
            print(f'Debug:Candidate ID: {candidate.id} Total: {candidate.total}')
        highest_total_pts = max(candidate.total for candidate in candidates)
        print('Maximum total:', highest_total_pts)
        return [candidate for candidate in candidates if candidate.total == highest_total_pts]
        """

    @staticmethod
    def get_lowest_voted_candidate(candidates, type, choice=None):
        """
        Get the candidate with the lowest number of votes.

        :param list candidates: A list of candidates to compare.
        :param string type: The data type to compare.
        :param int choice: The choice to compare (optional)

        Returns:
           list: A list of candidates with the lowest total points.
        """

        if type == 'total':
            return [min(candidates, key=lambda c: c.total)]
        else:
            return [min(candidates, key=lambda c: c.votes[choice])]

        """
        return min(candidates, key=lambda c: c.total)

        print('Getting lowest voted candidate...')
        for candidate in candidates:
            print(f'Debug:Candidate ID: {candidate.id} Total: {candidate.total}')
        lowest_total_pts = min(candidate.total for candidate in candidates)
        print('Minimum total:', lowest_total_pts)
        return [candidate for candidate in candidates if candidate.total == lowest_total_pts]
        """

    def remove_loser_from_ballot(self, loser):
        """
        Remove the losing candidate from the ballot.

        :param loser:
            Candidate: The losing candidate.

        :return:
        """

        for i in range (0, len(self.ballots)):
            for j in range(len(self.ballots[i]) - 1, -1, -1):
                if self.ballots[i][j] == loser.id:
                    self.ballots[i].pop(j) # Remove candidate from contention

        #if show_output is True:
            #print(f'* Removing loser {loser.id} from ballot.')
            #print('Ballots after removal:', self.ballots)


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
        
        #for i in range(0, len(self.candidates)):
        #    self.candidates[i].total = 0

        for candidate in self.candidates:
            candidate.total = 0

    def break_tie(self, candidates, mode, choice):
        """
        Break the tie by comparing the next choice voted for count.
        Note: We can break a tie with the highest or lowest total points.

        :param candidates candidates: List or candidates to compare.
        :param string mode: Declaring highest or lowest total points to aggregate.
        :param int choice: Choice order to break the tie.
        :return: candidate: candidate with the highest/lowest votes.
        """

        print(f'break_tie({candidates}, {mode}, {choice})')

        #next_choice = choice + 1
        choice += 1
        #print('next_choice:', next_choice, 'MAX_CHOICES:', MAX_CHOICES)

        if choice < MAX_CHOICES:
            while len(candidates) > 1 and choice < MAX_CHOICES:

                if mode == 'min':
                    candidates = self.get_lowest_voted_candidate(candidates, 'votes', choice)
                    #candidates = [min(candidates, key=lambda c: c.votes[choice])]

                elif mode == 'max':
                    candidates = self.get_highest_voted_candidate(candidates, 'votes', choice)
                    #candidates = [max(candidates, key=lambda c: c.votes[choice])]

                # If there are still multiple candidates with the same number of votes, break the tie again.
                candidates = self.break_tie(candidates, mode, choice)

            # Finally, only one candidate left.
            if len(candidates) == 1:
                return candidates[0]

            print('Warning: No clear winner.')
            return None

        else:
            print('Warning: Out of choices and still no clear winner.')
            return None

            """
            
            if mode == 'min':

                # Initialize min votes with first index.
                min_votes = min(candidates, key=lambda x: x.votes[next_choice])
                print('(min) Min votes:', min_votes)
                min_votes = candidates[0].votes[next_choice]
                print('Min votes:', min_votes)
                exit()
                min_candidate = candidates[0]

                # Start with the next candidate in the list to get next minimum value
                for i in range(1, len(candidates)):
                    if candidates[i].votes[next_choice] < min_votes:
                        min_votes = candidates[i].votes[next_choice]
                        min_candidate = candidates[i]

                if show_output is True:
                    print('Returning minimum Candidate:', min_candidate.id)


                    if candidate1[next_choice] < candidate2[next_choice]:
                        return candidate1

                    elif candidate1[next_choice] == candidate2[next_choice]:
                        return self.break_tie(candidate1, candidate2, mode, next_place, MAX_CHOICES)

                    else:
                        return candidate2
            elif mode == 'max':
                print('\nMAX')
                
                
                highest_candidates = max(candidates, key=lambda c: c.votes[next_choice])
                
                if (len(highest_candidates) > 1):
                    print('Next Tie Breaker...')
                    next_choice += 1
                    max_votes = self.break_tie(highest_candidates, mode, next_choice)
                    
                #print('(max) Max votes:', max_votes.votes[next_choice], 'id:', max_votes.id,  'name:', max_votes.name)
                #max_votes = candidates[0].votes[next_choice]
                #print('Max votes:', max_votes)
                #exit()
                #if candidate1[next_place] > candidate2[next_place]:
                #    return candidate1
                #elif candidate1[next_place] == candidate2[next_place]:
                #    return self.break_tie(candidate1, candidate2, mode, next_place, MAX_CHOICES)
               #else:
                #    return candidate2
            """
 
    # If two candidates have the same min/max values, break the tie by looking at the next place voted for count.
    # @todo - delete not needed
    def break_tie2(self, candidate1, candidate2, mode, place):
        """
        Break the tie by comparing the next place voted for count.
        Note: We can break tie with the highest or lowest total points.

        :param candidate1:
        :param candidate2:
        :param mode:
        :param place:
        :return:
        """
        next_place = place + 1

        if next_place < MAX_CHOICES:
            if mode == 'min':
                if candidate1[next_place] < candidate2[next_place]:
                    return candidate1

                elif candidate1[next_place] == candidate2[next_place]:
                    return self.break_tie2(candidate1, candidate2, mode, next_place, MAX_CHOICES)

                else:
                    return candidate2
            elif mode == 'max':
                if candidate1[next_place] > candidate2[next_place]:
                    return candidate1
                elif candidate1[next_place] == candidate2[next_place]:
                    return self.break_tie2(candidate1, candidate2, mode, next_place, MAX_CHOICES)
                else:
                    return candidate2
        else:
            return None


    # Used in NextChoiceSystem
    # @todo -remove
    def break_tie_min(self, candidates, choice):
        """
        Break the tie by comparing the next place voted for count.
        Note: This function uses multiple candidates.

        :param candidates:
        :param choice:
        :return: candidate: candidate with the fewest votes.
        """
        print('show_output = ', show_output)
        print('Candidate Count:', len(candidates))
        for i in range(0, len(candidates)):
            print('Debug Tie Breaker Candidate ID:', candidates[i].id, 'Total:', candidates[i].total)

        print('line 195')
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
