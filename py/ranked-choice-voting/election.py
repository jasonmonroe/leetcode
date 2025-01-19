# Election Class
import helpers

class Election:
    def __init__(self):
        self.ballots = []
        self.candidates = []
        self.pool = []  # pool of candidates to vote on

    def show_banner(self):
        print('\n##########################')
        print('# E L E C T I O N  D A Y #')
        print('##########################')
        print('#', date.today().strftime("%B %d, %Y"))
        print('# Candidates:', len(self.candidates))
        print('# Voters:', len(self.ballots))
        print('##########################\n')

    @staticmethod
    def get_parties():
        return [
            'Constitution',
            'Democrat',
            'Green',
            'Libertarian',
            'No-Party Affiliation',
            'Progressive',
            'Reform',
            'Republican'
        ]

    @staticmethod
    def get_names():
        return {
            'first': [
                'Alexander',
                'Aïsha',
                'Amelia',
                'Anaïs',
                'Ananya',
                'Ava',
                'Benjamin',
                'Charlotte',
                'Chloë',
                'Dmitri',
                'Elijah',
                'Elizabeth',
                'Emma',
                'Ella',
                'Fatima',
                'Harper',
                'Henry',
                'Isabella',
                'James',
                'Jürgen',
                'León',
                'Lars',
                'Liam',
                'Lucas',
                'Matthew',
                'Michael',
                'Mia',
                'Ming',
                'Noah',
                'Oliver',
                'Olga',
                'Omar',
                'Samuel',
                'Scarlett',
                'Sophia',
                'Sofia',
                'Thiago',
                'William',
                'Yuki',
                'Zhang'
            ],
            'last': [
                'Abdullah',
                'Anderson',
                'Ben-Ali',
                'Brown',
                'Clark',
                'Davis',
                'Dupont',
                'Dubois',
                'Fernández',
                'Garcia',
                'García',
                'Gonzalez',
                'Harris',
                'Hussein',
                'Hernandez',
                'Johnson',
                'Johansson',
                'Jackson',
                'King',
                'Lee',
                'Lewis',
                'Lopez',
                'Martin',
                'Martin',
                'Martinez',
                'Moore',
                'Ramírez',
                'Ramirez',
                'Rodriguez',
                'Schmidt',
                'Sanchez',
                'Sharma',
                'Silva',
                'Smith',
                'Taylor',
                'Thomas',
                'Thompson',
                'Takahashi',
                'Ivanov',
                'Walker',
                'Wilson',
                'Wright',
                'Young',
                'Zhang',
                'Petrova'
            ]
        }

    # Validate input.  We only accept integers or blank space that will generate a random value.
    @staticmethod
    def validate_input (message, str_flag=False):
        while True:
            user_input = input(message)

            if user_input == '':
                return user_input

            try:
                if str_flag:
                    return str(user_input).lower()
                else:
                    return int(user_input)
            except ValueError:
                print('Invalid input. Please enter an integer or press enter for a random value to be used.')

    # @todo temp method
    def register_auto (self):
        candidate_cnt = 4
        self.declare_candidacy(candidate_cnt)

    # Secretary of State registers declared candidates for the primary election.
    def register (self):
        min_candidates = 1
        max_candidates = 32

        global show_output
        show_output = False
        if self.validate_input('\nShow output? (y/n) ', True) == 'y':
            show_output = True

        candidate_cnt = self.validate_input(f'How many candidates ({min_candidates} to {max_candidates}) will register for the primary? ')

        if candidate_cnt == '':
            candidate_cnt = random.randint(min_candidates, max_candidates)

        else:
            # Set candidate count within range.
            if candidate_cnt < min_candidates:
                candidate_cnt = min_candidates

            if candidate_cnt > max_candidates:
                candidate_cnt = max_candidates

        print(f'There are {candidate_cnt} candidates for this primary election.')

        # Register candidates
        self.declare_candidacy(candidate_cnt)

    # Declare candidacy by registering name party for the primary
    def declare_candidacy (self, candidate_cnt):
        full_names = Election.get_names()

        print('\nCandidates')
        for i in range(0, candidate_cnt) :
            party = random.choice(Election.get_parties())
            full_name = random.choice(full_names['first']) + ' ' + random.choice(full_names['last'])
            print(f'{i}, {full_name}, {party}')

            # Make sure each uid is unique
            self.candidates.append(Candidate(uid(), full_name, party))

    # Get the number of voters who registered for this election
    def get_voter_cnt(self):
        min_voters = 25
        max_voters = 168000000  # 168,000,000
        voter_cnt = self.validate_input('\nHow many voters are there? ')

        if voter_cnt == '':
            voter_cnt = random.randint(min_voters, 100)  # should be max_voters
        else:
            if voter_cnt < min_voters:
                voter_cnt = min_voters

            elif voter_cnt > max_voters:
                voter_cnt = max_voters

        print(f'{voter_cnt} voters will vote in this primary election.')

        return voter_cnt

    # Vote in the election.
    def vote (self):
        # Prompt for voters
        voter_cnt = self.get_voter_cnt()
        #voter_cnt = 10  # For testing purposes

        # Create a ballot for voters to vote on.
        choice_cnt = min(max_choices, len(self.candidates))

        print('\nVoting...')
        for i in range (0, voter_cnt):
            self.reset_pool()
            self.ballots.append([])

            if show_output == 'y':
                print(f'\nNew Ballot {self.ballots[i]}')
                print(f'Voter {i} is voting...')

            for j in range (0, choice_cnt):
                candidate_chosen = self.mark_candidate()
                self.ballots[i].append(candidate_chosen)

                if show_output is True:
                    p_str = place_str(j, 'p')
                    print(f'Voter {i} voted {p_str} for Candidate ID: {candidate_chosen}')

            # Display ballot for voter
            print(f'Voter {i} ballot: {self.ballots[i]}')

    # Mark candidate on ballot.
    def mark_candidate (self):

        # There's a small chance that a voter does not want to vote for a candidate at all.
        no_vote_pct_threshold = 3
        no_vote_odds = random.randint(0, percentile)

        # The odds are 10% that a voter does not choose a candidate otherwise vote
        if no_vote_odds <= no_vote_pct_threshold:
            return no_vote_val

        else:
            return self.choose_candidate()

    # Choose a candidate that has not been chosen before.
    # Note: We can expand this with more thorough logic in choosing a candidate.  For now just pick at random.
    def choose_candidate (self):
        return self.pool.pop(ridx(self.pool))

    # Reset the pool of candidates for new voters to vote on.
    # Note: Pool should not exceed the number of candidates.
    def reset_pool (self):
        self.pool = []
        for i in range (len(self.candidates)):
            self.pool.append(self.candidates[i].id)

    # Tally votes and store based on voter choice.
    def tally (self):
        print('\nTallying votes...')
        if show_output == 'y':
            print('\nTallying votes...')
            print(self.ballots)

        for i in range (0, len(self.ballots)):
            for vote_choice in range (0, len(self.ballots[i])):
                voted_id = self.ballots[i][vote_choice]

                if show_output is True:
                    print(f'Ballot {i} choice {vote_choice} for candidate {voted_id}')

                if voted_id != no_vote_val:
                    # Update the corresponding place attribute based on vote_choice
                    index = map_id_to_candidate_index(voted_id, self.candidates)
                    self.candidates[index].votes[vote_choice] += 1

                else:
                    if show_output is True:
                        p_str = place_str(vote_choice, 'p')
                        print(f'Warning: Voter {i} did not vote for {p_str}.')

        print('Votes tallied.')

        if show_output is True:
            for i in range (0, len(self.candidates)):
                print(f'Candidate {self.candidates[i].id} Total:{self.candidates[i].total} Votes:', self.candidates[i].votes)