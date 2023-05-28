import sys
import os
# Get the path to the project's root directory
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the Python path
sys.path.insert(0, root_path)

from src.sentence_validator import SentenceValidator

def test_sentence_validator():
    """
    Test case to verify the SentenceValidator class.

    It checks the validity of different sentences using the SentenceValidator class.

    Assertions:
    - The first sentence is a valid sentence, so it should return True.
    - The second sentence consists of numbers only, so it should return False.
    - The third sentence consists of symbols only, so it should return False.
    """
    validator = SentenceValidator()

    sentence1 = "Hello, how are you?"
    sentence2 = "42"
    sentence3 = "?!!!!!!?"

    assert validator.is_valid_sentence(sentence1) is True
    assert validator.is_valid_sentence(sentence2) is False
    assert validator.is_valid_sentence(sentence3) is False