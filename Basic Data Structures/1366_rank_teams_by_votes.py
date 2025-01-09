from collections import defaultdict
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        O(N⋅M+M^2logM) 
        len of votes times the len of element
        MlogM to sort
        NM to run the loop
        Space
        O(m^2) list of size of each element
        plus sometimes m due to sorting
        list tracks the number of votes the team received for each position.
        We iterate through each vote and update the count of votes for each team at the respective position.
        """
        rank_count = defaultdict(lambda: [0] * len(votes[0]))
        # Count the votes for each team at each position
        for vote in votes:
            for i, team in enumerate(vote):
                rank_count[team][i] += 1

        # Sort the teams based on rank counts and alphabetical order
        sorted_teams = sorted(rank_count.keys(), 
                            key=lambda team: (rank_count[team], -ord(team)), 
                            reverse=True)

        return "".join(sorted_teams)

    
    def rank_teams_with_matrix(votes):
        rows = len(votes[0])  # Number of teams
        cols = len(votes[0])  # Number of positions in ranking
        d = [[0 for _ in range(cols)] for _ in range(rows)]  # Create a 2D matrix for counts

        team_index = {team: idx for idx, team in enumerate(votes[0])}  # Map teams to indices

        # Fill the matrix with vote counts
        for vote in votes:
            for position, team in enumerate(vote):
                d[team_index[team]][position] += 1

        # Sort the teams based on the matrix and tie-breaking alphabetically
        teams = list(votes[0])
        teams.sort(key=lambda team: (d[team_index[team]], -ord(team)), reverse=True)

        return "".join(teams)