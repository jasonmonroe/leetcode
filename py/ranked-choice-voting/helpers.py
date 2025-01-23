"""
|--------------------------------------------------------------------------
| Ranked Choice Voting Helper Functions
|--------------------------------------------------------------------------
"""

# Import Libraries
import random
import uuid

# Helper functions
FIRST_CHOICE_INDEX = 0
MAX_CHOICES = 4

MIN_VOTERS = 9 #25
MAX_VOTERS = 15 #168000000

MIN_CANDIDATES = 2
MEDIAN_CANDIDATES = 8
MAX_CANDIDATES = 10 #128

NO_VOTE_VAL = ''
NO_VOTE_PCT_THRESHOLD = 3

PERCENTILE = 100
show_output = False

# Create a candidate object
class Candidate:
    def __init__(self, u_id, name, party):
        self.id = u_id
        self.name = name
        self.party = party
        self.is_winner = None # False = removed from pool, True = winner, None = still in pool
        self.votes = [0, 0, 0, 0]
        self.total = 0
        self.sys_totals = 0

# Input voter ID and return index of a candidate.
def map_id_to_candidate_index (voted_id, candidates):
    for index in range (0, len(candidates)):
        if voted_id == candidates[index].id:
            return index

# Better way to map ID to candidate index
def map_id_to_candidate_index2(voted_id, candidates):
    candidate_dict = {candidate.id: index for index, candidate in enumerate(candidates)}
    return candidate_dict.get(voted_id)

"""
Get the placement string for a candidate.
"""
def place_str (place, mode):
    if mode == 'a':
        attrs = ['first', 'second', 'third', 'fourth']
    else:
        attrs = ['1st Place', '2nd Place', '3rd Place', '4th Place']

    return attrs[place]

"""
Get a random index.
"""
def ridx (var):
    return random.randint(0, len(var) - 1)

"""
Get unique ID for candidate.
"""
def uid(length = 4):
    return str(uuid.uuid4())[:length]

"""
Sort the candidates by the total number of votes they have. Winner will be at the top.
"""
def sort_candidates (candidates):
    return sorted (candidates, key=lambda candidate: candidate.total, reverse = True)

"""
Get the total percentage of vote for a candidate.
"""
def get_totals_pct (candidate, max_points):
    return round ((candidate.total / max_points) * PERCENTILE, 2)
