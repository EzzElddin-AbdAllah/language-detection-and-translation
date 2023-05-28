class Language:
    """
    Language class for language detection and translation.

    Args:
        detect_model: The language detection model.
        translate_model: The translation model.

    Attributes:
        detect_model: The language detection model.
        translate_model: The translation model.
    """

    def __init__(self, detect_model, translate_model):
        self.detect_model = detect_model
        self.translate_model = translate_model

    def detect_language(self, sentence):
        """
        Detects the language of a given sentence.

        Args:
            sentence (str): The sentence to detect the language for.

        Returns:
            str: The detected language code.
        """
        return self.detect_model.detect(sentence)

    def translate_sentence(self, lang, sentence):
        """
        Translates a sentence from the source language to the target language.

        Args:
            lang (str): The source language of the sentence.
            sentence (str): The sentence to be translated.

        Returns:
            str: The translated sentence in the target language.
        """
        langs_map = {'ar': 'en', 'en': 'ar'}
        translator = self.translate_model.Translator(from_lang=lang, to_lang=langs_map[lang])
        translated_sentence = translator.translate(sentence)
        return translated_sentence