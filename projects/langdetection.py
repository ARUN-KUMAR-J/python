from langdetect import detect
text="ein vater und eine mutter"
language=detect(text)
print("Language detected: ",language)