import logging
import translate
from flask import Flask, request, jsonify
from src.language import Language
from src.language_detector import LanguageDetector
from src.sentence_validator import SentenceValidator

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/lang_detection", methods=["POST"])
def lang_detection():
    """
    API endpoint for language detection.

    This endpoint receives a sentence in the request payload,
    validates its format using SentenceValidator, and detects the language using Language class.

    Returns:
        JSON response containing the detected language if the sentence is valid,
        otherwise returns "Not-valid sentence".
    """
    sentence = request.json.get('sentence')
    logger.info(f'original_sentence: {sentence}')

    validator = SentenceValidator()
    is_valid_sentence = validator.is_valid_sentence(sentence)

    if not is_valid_sentence:
        return 'Not-valid sentence', 400

    try:
        detector = LanguageDetector("../models/trained_model.pkl", "../encoders/label_encoder.pkl")
        language = Language(detector, translate)
        detected_language = language.detect_language(sentence)
        logger.info(f'detected_language: {detected_language}')
    except Exception as e:
        logger.error(f'Error occurred during language detection: {str(e)}')
        return 'Internal Server Error', 500

    return jsonify({'language': detected_language})


@app.route("/translation", methods=["POST"])
def translation():
    """
    API endpoint for translation.

    This endpoint receives a sentence in the request payload,
    validates its format using SentenceValidator, and performs translation if the sentence is valid.

    Returns:
        JSON response containing the translated sentence if the sentence is valid and supported,
        otherwise returns "Not-valid sentence" or "Not-supported".
    """
    sentence = request.json.get('sentence')

    validator = SentenceValidator()
    is_valid_sentence = validator.is_valid_sentence(sentence)

    if not is_valid_sentence:
        return 'Not-valid sentence', 400

    try:
        detector = LanguageDetector("../models/trained_model.pkl", "../encoders/label_encoder.pkl")
        language = Language(detector, translate)
        detected_language = language.detect_language(sentence)
        logger.info(f'detected_language: {detected_language}')

        if detected_language == 'Arabic':
            logger.info(f'original_sentence: {sentence}')
            ar_sentence = sentence
            en_sentence = language.translate_sentence('ar', sentence)
            logger.info(f'translated_sentence: {en_sentence}')
        elif detected_language == 'English':
            logger.info(f'original_sentence: {sentence}')
            en_sentence = sentence
            ar_sentence = language.translate_sentence('en', sentence)
            logger.info(f'translated_sentence: {ar_sentence}')
        else:
            return 'Not-supported', 400

        return jsonify({'ar': ar_sentence, 'en': en_sentence})
    except Exception as e:
        logger.error(f'Error occurred during translation: {str(e)}')
        return 'Internal Server Error', 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
