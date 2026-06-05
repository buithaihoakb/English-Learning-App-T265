"""
Vocabulary Learning Module
"""

import pyttsx3
from database.db_manager import DatabaseManager

class VocabularyManager:
    """Manages vocabulary learning and practice"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
    
    def add_word(self, word, pronunciation, definition, example, pos, level, category, audio_path=None, image_path=None):
        """Add a new vocabulary word"""
        return self.db.add_vocabulary(word, pronunciation, definition, example, pos, level, category, audio_path, image_path)
    
    def get_words_for_learning(self, level, count=20):
        """Get vocabulary words for learning session"""
        return self.db.get_vocabulary_by_level(level, count)
    
    def get_all_words(self, limit=None):
        """Get all vocabulary words"""
        return self.db.get_all_vocabulary(limit)
    
    def pronounce_word(self, word):
        """Speak the word using text-to-speech"""
        try:
            self.engine.say(word)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error pronouncing word: {e}")
    
    def pronounce_sentence(self, sentence):
        """Speak a sentence using text-to-speech"""
        try:
            self.engine.say(sentence)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error pronouncing sentence: {e}")
    
    def track_word_practice(self, user_id, vocabulary_id, is_correct):
        """Track user's word practice attempt"""
        return self.db.track_vocabulary_practice(user_id, vocabulary_id, is_correct)
    
    def get_user_progress(self, user_id, limit=None):
        """Get user's vocabulary learning progress"""
        return self.db.get_user_vocabulary_progress(user_id, limit)
    
    def get_mastered_words(self, user_id):
        """Get words that user has mastered (high confidence level)"""
        progress = self.get_user_progress(user_id)
        return [word for word in progress if word['confidence_level'] >= 4]
    
    def get_weak_words(self, user_id):
        """Get words that user struggles with (low confidence level)"""
        progress = self.get_user_progress(user_id)
        return [word for word in progress if word['confidence_level'] <= 1]
    
    def create_sample_vocabulary(self):
        """Create sample vocabulary data"""
        sample_words = [
            # B2 Level Business Vocabulary
            ("Entrepreneurship", "ˌɑːn.trə.prə.ˈnɜːr.ʃɪp", "The activity of setting up and running a business", 
             "She showed great entrepreneurship by starting her own company.", "Noun", "B2", "Business"),
            
            ("Negotiate", "nɪˈɡoʊ.ʃi.eɪt", "To discuss something with someone to reach an agreement",
             "We will negotiate the terms of the contract.", "Verb", "B2", "Business"),
            
            ("Procurement", "prəˈkjʊr.mənt", "The action of obtaining or procuring something",
             "The procurement process is handled by the purchasing department.", "Noun", "B2", "Business"),
            
            ("Stakeholder", "ˈsteɪk.hoʊl.dɚ", "A person with an interest in a business or organization",
             "We need to consider all stakeholders in this decision.", "Noun", "B2", "Business"),
            
            ("Leverage", "ˈlev.ər.ɪdʒ", "To use something to maximum effect",
             "We can leverage our resources to improve efficiency.", "Verb", "B2", "Business"),
            
            # B2 Level Academic Vocabulary
            ("Methodology", "ˌmeθ.ə.ˈdɑːl.ə.dʒi", "A system of principles and practices in academic or technical work",
             "The research methodology was clearly explained in the paper.", "Noun", "B2", "Academic"),
            
            ("Hypothesis", "haɪˈpɑːθ.ə.sɪs", "A suggested explanation made on the basis of limited evidence",
             "The scientist tested her hypothesis through experimentation.", "Noun", "B2", "Academic"),
            
            ("Comprehensive", "ˌkɑːm.prɪˈhen.sɪv", "Complete; including all or nearly all elements",
             "The report provides a comprehensive overview of the subject.", "Adjective", "B2", "Academic"),
            
            ("Facilitate", "fəˈsɪl.ə.teɪt", "To make something easier or help it to happen",
             "The moderator will facilitate the discussion between the participants.", "Verb", "B2", "Academic"),
            
            ("Integrate", "ˈɪn.tɪ.ɡreɪt", "To combine or coordinate with something else",
             "We plan to integrate new technology into our system.", "Verb", "B2", "Academic"),
        ]
        
        for word_data in sample_words:
            self.add_word(*word_data)
