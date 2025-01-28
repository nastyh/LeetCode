"""
The game has exactly 2 players.
Each player scores 1pt at a time.
Each player starts with 0 points.

The player with a score >= 4 wins but they must win by 2 pts.
4 to 2 wins
4 to 3 does not win
5 to 3 wins

If the score is tied at or above 3, we change both scores to 3 and keep going until one player wins by 2 [(4-4) -> (3-3)]

Implement:
increment_score
curent_score
show the winner
"""
class TennisGame:
    def __init__(self, player1: str, player2: str):
        """Initialize the game with two players starting at 0 points."""
        self.player1 = player1
        self.player2 = player2
        self.scores = {player1: 0, player2: 0}

    def increment_score(self, player: str):
        """
        Increment the score of a given player.
        If both players are tied at or above 3, reset both scores to 3.
        """
        if self.is_game_over():
            raise ValueError("Game is already over!")
        
        self.scores[player] += 1
        player1_score = self.scores[self.player1]
        player2_score = self.scores[self.player2]

        # Reset scores to 3-3 if tied at or above 3
        if player1_score >= 3 and player2_score >= 3 and player1_score == player2_score:
            self.scores[self.player1] = 3
            self.scores[self.player2] = 3

    def current_score(self) -> str:
        """
        Return the current score as a string in the format "player1_score-player2_score".
        """
        return f"{self.scores[self.player1]}-{self.scores[self.player2]}"

    def is_game_over(self) -> bool:
        """
        Check if the game is over.
        A player wins if their score is >= 4 and they are ahead by at least 2 points.
        """
        player1_score = self.scores[self.player1]
        player2_score = self.scores[self.player2]
        return (player1_score >= 4 or player2_score >= 4) and abs(player1_score - player2_score) >= 2

    def winner(self) -> str:
        """
        Return the winner of the game if the game is over, otherwise return None.
        """
        if not self.is_game_over():
            return None
        return self.player1 if self.scores[self.player1] > self.scores[self.player2] else self.player2
    
def test_tennis_game():
    game = TennisGame("Player1", "Player2")

    # Initial score
    assert game.current_score() == "0-0"
    assert not game.is_game_over()
    assert game.winner() is None

    # Player1 scores 3 points
    game.increment_score("Player1")
    assert game.current_score() == "1-0"
    game.increment_score("Player1")
    assert game.current_score() == "2-0"
    game.increment_score("Player1")
    assert game.current_score() == "3-0"
    assert not game.is_game_over()

    # Player2 scores 3 points, ties it to 3-3
    game.increment_score("Player2")
    assert game.current_score() == "3-1"
    game.increment_score("Player2")
    assert game.current_score() == "3-2"
    game.increment_score("Player2")
    assert game.current_score() == "3-3"

    # Both players score one point, resetting to 3-3
    game.increment_score("Player1")
    assert game.current_score() == "4-3"
    game.increment_score("Player2")
    assert game.current_score() == "3-3"  # Reset to 3-3

    # Player1 scores two consecutive points to win
    game.increment_score("Player1")
    assert game.current_score() == "4-3"
    game.increment_score("Player1")
    assert game.is_game_over()
    assert game.winner() == "Player1"

    # A new game scenario: Player2 wins by 2
    game = TennisGame("Player1", "Player2")
    game.increment_score("Player1")
    game.increment_score("Player2")
    game.increment_score("Player1")
    game.increment_score("Player2")
    game.increment_score("Player1")
    game.increment_score("Player2")
    game.increment_score("Player2")
    game.increment_score("Player2")
    assert game.current_score() == "3-5"
    assert game.is_game_over()
    assert game.winner() == "Player2"

    print("All test cases passed!")

# Run the test
test_tennis_game()

