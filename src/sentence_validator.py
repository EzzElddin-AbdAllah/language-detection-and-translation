import re

class SentenceValidator:
    """
    SentenceValidator class for verifying the validity of sentences.
    """

    def __init__(self):
        self.pattern = r'^(?!(\d+|[^\w\s]+)$).*$'

    def is_valid_sentence(self, sentence):
        """
        Verify if a sentence is a valid sentence and not in an invalid format.

        Args:
            sentence (str): The sentence to be verified.

        Returns:
            bool: True if the sentence is valid, False otherwise.
        """
        match = re.match(self.pattern, sentence)
        return bool(match)