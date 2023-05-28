import sys
import os
# Get the path to the project's root directory
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the Python path
sys.path.insert(0, root_path)

from src.language_detector import LanguageDetector
from src.language import Language
import translate


def test_detect_language():
    """
    Test the language detection functionality.

    This test case verifies that the language detection method correctly detects the language of a given sentence.
    """
    detector = LanguageDetector("../models/trained_model.pkl", "../encoders/label_encoder.pkl")
    language = Language(detector, translate)

    en_sentence = 'It was discontinued in February 2018.'
    ar_sentence = 'تعرف على ما إذا كان شخص ما يقول نكتة رائعة يمكنك أن تقول إنها جيدة.'

    detected_en_sentence = language.detect_language(en_sentence)
    detected_ar_sentence = language.detect_language(ar_sentence)

    assert detected_en_sentence == 'English' and detected_ar_sentence == 'Arabic'

def test_translate_sentence():
    """
    Test the sentence translation functionality.

    This test case verifies that the translation method translates a sentence from the source language to the target language.
    """
    detector = LanguageDetector("../models/trained_model.pkl", "../encoders/label_encoder.pkl")
    language = Language(detector, translate)
    translated_sentence = language.translate_sentence('en', 'It was discontinued in February 2018.')

    assert translated_sentence == 'تم إيقافه في فبراير 2018.'