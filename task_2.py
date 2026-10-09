
def analyze(s):
    w = s.split()
    u = set(w)

    vowels = sum(1 for c in s.lower() if c in "aeiou")

    print("Words:", len(w))
    print("Characters:", len(s))
    print("Longest:", max(w, key=len) if w else "")
    print("Shortest:", min(w, key=len) if w else "")
    print("Vowels:", vowels)
    print("Unique words:", len(u))
    print("Alphabetical:", sorted(w))

    with open("word-analysis.txt", "w") as f:
        f.write("Words: " + str(len(w)) + "\n")
        f.write("Characters: " + str(len(s)) + "\n")
        f.write("Longest: " + (max(w, key=len) if w else "") + "\n")
        f.write("Shortest: " + (min(w, key=len) if w else "") + "\n")
        f.write("Vowels: " + str(vowels) + "\n")
        f.write("Unique words: " + str(len(u)) + "\n")
        f.write("Alphabetical: " + str(sorted(w)) + "\n")


s = input("Enter sentence: ")
analyze(s)