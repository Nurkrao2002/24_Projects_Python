import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake
rake_nltk_var = Rake()
text = """Hello! Welcome to Josh Innovations,
Course: Python Programming in 2nd Floor at Ameerpet"""
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)