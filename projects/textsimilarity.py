from fuzzywuzzy import fuzz

text1="hello my name is Arun Kumar"
text2="arun that is my communataion name"
similarity =fuzz.ratio(text1,text2)
print(similarity)