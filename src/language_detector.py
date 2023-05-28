import joblib

class LanguageDetector:
    """LanguageDetector class for detecting the language of a given sentence."""

    def __init__(self, model_path, encoder_path):
        """
        Initialize the LanguageDetector.

        Args:
            model_path (str): Path to the trained model file.
            encoder_path (str): Path to the label encoder file.
        """
        self.pipeline = joblib.load(model_path)
        self.label_encoder = joblib.load(encoder_path)

    def detect(self, sentence):
        """
        Detect the language of a given sentence.

        Args:
            sentence (str): The sentence to be processed.

        Returns:
            str: Detected language of the sentence.
        """
        label = self.pipeline.predict([sentence])[0]
        language = self.label_encoder.inverse_transform([label])[0]
        return language
