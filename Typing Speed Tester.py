import time
sentence = "Python makes automation simple."
input("Press Enter to start typing...")
start = time.time()
typed = input(sentence + "\n> ")
end = time.time()
wpm = len(typed.split()) / ((end - start) / 60)
print(f"WPM: {wpm:.2f}")
