from textblob import Word

text="heyy thiss is mee ArunKumar"
corrected_text=" ".join(Word(word).correct() for word in text.split())
print(corrected_text)