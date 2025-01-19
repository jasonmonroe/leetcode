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
| Average-Weighted Systems
"""

# Import Libraries
import random
import uuid
from datetime import date

import helpers
from helpers import uid

import next_choice_system
import point_score_system
import redistribution_system
import rem_candidates_system


# Parent class of all voting systems
class VotingSystem:
    pass



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

"""
|--------------------------------------------------------------------------
| Top Remaining Candidates System
|--------------------------------------------------------------------------
| This system is used by the state of Alaska. Instead of choosing one candidate,
| you fill in the oval in column one for the candidate you would most like to win,
| then vote for your second choice in column two and so on.  Ranking other candidates
| does not impact your first choice and you do not have to rank them all.  You should 
| only mark one oval in each row and one oval in each column. 
|  
| The ballots are tallied and scored by it's first choice votes.  If a candidate
| gets at least half of the votes in round one, they win.  If this doesn't happen, it's 
| continued to next round and the candidate with the least nth choice votes is eliminated.
| Count the voter's next remaining candidate choice instead of their choice for the 
| eliminated candidate (meaning they still have a say in who wins).
|
| Repeat these steps in rounds until there are only two candidates and now whomever
| has the most votes is determined the winner.

| @link https://www.elections.alaska.gov/election-information/
| @link https://www.youtube.com/watch?v=lLU3lbrxMBI
| @link https://www.youtube.com/watch?v=oHRPMJmzBBw
"""

"""
|--------------------------------------------------------------------------
| Next Choice System
|--------------------------------------------------------------------------
| If no winner, go to every ballot and count the next choice votes for the 
| candidate. Continue this process until a candidate receives more than half
| of the votes do determine the winner.
|
| Note: No candidates are eliminated until the final round.
"""


"""
|--------------------------------------------------------------------------
| Redistribution System
|--------------------------------------------------------------------------
| If no winner, remove the candidate with the least amount of votes.  Then 
| take the ballots and count the next choice votes of losing candidate and 
| redistribute them to the remaining candidates.  Continue this process until
| a candidate receives more than half of the votes do determine the winner.
"""



"""
|--------------------------------------------------------------------------
| Average-Weighted Systems
|--------------------------------------------------------------------------
| Take the number of points of each candidate for each voting system and weigh
| them to determine an overall winner. 
|
| Voting System Weights:
|   Remaining Candidates: 34%
|   Next Choice: 22%
|   Redistribution: 22%
|   Point Score: 22%
"""
class AverageWeightystem:
    pass

### Run Program
benchmark_id = uid(6)
print(f'\nStart Benchmark ID: {benchmark_id}')

elect = Election()

# Tally Point Score System

# Tally Remaining Candidates System

# Tally Next Choice System

# Tally Redistribution System

# Tally Average-Weighted Systems

# Show Results

### End of Program
