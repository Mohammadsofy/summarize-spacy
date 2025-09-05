import spacy
from collections import Counter
import math
nlp = spacy.load("en_core_web_sm")
text = """
spaCy is a popular open-source library for Natural Language Processing in Python.
It is designed specifically for production use and real-world applications.
spaCy provides pre-trained models for many languages, including English and Arabic.
With spaCy, you can easily perform tasks like tokenization, part-of-speech tagging, and named entity recognition.
The library is known for its speed and efficiency compared to other NLP tools.
spaCy integrates well with deep learning frameworks such as TensorFlow and PyTorch.
It also supports custom pipelines, allowing developers to add their own components.
Many companies and researchers use spaCy for text analysis, chatbots, and information extraction.
"""
doc = nlp(text)
sentences = list(doc.sents)
word_freq = Counter()
for token in doc:
    if token.is_alpha and not token.is_stop:
        word_freq[token.text.lower()] += 1
# word_freq = Counter(token.text.lower() for token in doc if token.is_alpha and not token.is_stop)
max_freq = max(word_freq.values())
for word in word_freq:
    word_freq[word] /= max_freq

sentence_scores = {}
for sent in sentences:
    score = 0
    for word in sent:
        if word.text.lower() in word_freq:
            score += word_freq[word.text.lower()]
    for ent in sent.ents:
            
            score += 1.5
    sentence_scores[sent] = score


scores = list(sentence_scores.values())
average_score = sum(scores)/len(scores)
sum_sq = 0
for s in scores:
    sum_sq += (s - average_score) ** 2
std_dev = math.sqrt(sum_sq / len(scores))
# std_dev = math.sqrt(sum((s - average_score)**2 for s in scores)/len(scores))

summary_sentences = []
for sent, score in sentence_scores.items():
    if score >= average_score + 0.5 * std_dev:
        summary_sentences.append(sent.text.strip())

# summary_sentences = [sent.text.strip() for sent, score in sentence_scores.items() if score >= average_score + 0.5*std_dev]

summary = " ".join(summary_sentences)
print("SMART SUMMARY:")
print(summary)




