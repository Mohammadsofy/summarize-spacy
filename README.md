📝 Text Summarizer using spaCy
📖 Project Description
This project is a simple yet effective Python program that generates summaries for English texts using the spaCy library.
It analyzes the input text, calculates word frequencies, and identifies the most important sentences.

🚀 How It Works
The user enters a text into the text variable inside the program.
The program uses a spaCy model to:
Detect sentences, words, and entities
Build a frequency distribution of the most important words
Each sentence is scored based on:
Word frequency
The top-scoring sentences are selected and combined to form a smart summary of the text.
📦 Requirements
Python
spaCy
spaCy English model (en_core_web_sm)
Built-in Python libraries:
collections
math
⚙️ Installation & Setup
Clone this repository.
Install dependencies.
Put the text you want to summarize inside the text variable in summary.py.
Run the program.