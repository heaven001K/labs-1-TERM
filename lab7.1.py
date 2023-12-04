import logging
class InvalidVotesError(Exception):
    """Raised when an invalid number of votes is provided."""
    pass


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as e:
                if mode == "console":
                    logging.error(f"Exception {exception.__name__}: {e}")
                elif mode == "file":
                    logging.basicConfig(filename='error.log', level=logging.ERROR)
                    logging.error(f"Exception {exception.__name__}: {e}")
                else:
                    raise ValueError("Invalid mode. Use 'console' or 'file'.")
        return wrapper
    return decorator

"""class candidate """
class Candidate:
    """
    Represents a candidate in an election.

    Attributes:
        name (str): The name of the candidate.
        votes (int): The number of votes received by the candidate.
    """
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes


class Elections:
    """
    Manages an election with a collection of candidates.

    Attributes:
        candidates (dict): A dictionary where candidate names are keys, and their votes are values.
    """
    def __init__(self):
        self.candidates = {}

    @logged(InvalidVotesError, mode="console")
    def add_candidate(self, candidate_people):
        """
        Adds a candidate to the election.

        Args:
            candidate (Candidate): The candidate to be added.
        """
        if candidate_people.votes < 0:
            raise InvalidVotesError("Number of votes must be non-negative.")
        
        self.candidates[candidate_people.name] = candidate_people.votes

    def calculate_winner(self):
        """
        Calculates the winner of the election based on the candidate 
        with the highest number of votes.

        Returns:
            str or None: The name of the winning candidate or None if there are no candidates.
        """
        if not self.candidates:
            return None

        winner_people = max(self.candidates, key=self.candidates.get)
        return winner_people

    def congratulate_winner(self):
        """
        Congratulates the winner of the election.
        """
        winner = self.calculate_winner()
        if winner:
            print(f"Congratulations, {winner}! You are the winner of the election.")
    def get_percentage(self, votes):
        """
        Calculates the percentage of votes compared to the total votes.

        Args:
            votes (int): The number of votes for a candidate.

        Returns:
            float: The percentage of votes.
        """
        total_votes = sum(self.candidates.values())

        try:
            percentage = (votes / total_votes) * 100
        except ZeroDivisionError:
            percentage = 0

        return percentage

    def get_results(self):
        """
        Prints the results of the election, including each candidate's votes and 
        the percentage of total votes.
        """
        print("Election Results:")
        print("-----------------")
        for name, votes in self.candidates.items():
            percentage = self.get_percentage(votes)
            print(f'Candidate {name} has {votes} votes, which is {percentage}% of all votes')
    
if __name__ == "__main__":
    election = Elections()
    candidates_data = [Candidate("a", -0), Candidate("b", 51), Candidate("c", 60)]

    for candidate in candidates_data:
        election.add_candidate(candidate)

    winner = election.calculate_winner()
    if winner:
        print(f"The winner is {winner} with {election.candidates[winner]} votes")
    else:
        print("No winner. There are no candidates in the election.")

    election.get_results()
    election.congratulate_winner()