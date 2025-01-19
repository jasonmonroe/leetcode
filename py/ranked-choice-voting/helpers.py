"""
|--------------------------------------------------------------------------
| Ranked Choice Voting Helper Functions
|--------------------------------------------------------------------------
"""
# Import Libraries
import random
import uuid
from datetime import date

# Helper functions
MAX_CHOICES = 4
NO_VOTE_VAL = ''
PERCENTILE = 100
show_output = False

# Input voter ID and return index of candidate.
def map_id_to_candidate_index (voted_id, candidates):
    for index in range (0, len(candidates)):
        if voted_id == candidates[index].id:
            return index

# Return string of placement
def place_str (place, mode):
    if mode == 'a':
        attrs = ['first', 'second', 'third', 'fourth']
    else:
        attrs = ['1st Place', '2nd Place', '3rd Place', '4th Place']

    return attrs[place]

# Shortener get random index
def ridx (var):
    return random.randint(0, len(var) - 1)

# Unique ID for candidate
def uid(length=4):
    return str(uuid.uuid4())[:length]

def sort_candidates (candidates):
    return sorted (candidates, key=lambda candidate: candidate.total, reverse=True)

def get_totals_pct (candidate, max_points):
    return round ((candidate.total / max_points) * PERCENTILE, 2)


# Create a candidate object
class Candidate:
    def __init__(self, u_id, name, party):
        self.id = u_id
        self.name = name
        self.party = party
        self.is_winner = None # False = removed from pool, True = winner, None = still in pool
        self.votes = [0, 0, 0, 0]
        self.total = 0