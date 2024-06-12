def main():
    count = 0
    letter_count = {}
    sorted_count = {}
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    #assign book to "file_contents" as one long string.
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    #break string into letters and count
    for word in words :
        count += 1
        word_lower = word.lower()
        for letter in word_lower :
            #print(letter)
            if letter in alphabet:
                letter_count[letter] = letter_count.get(letter, 0) + 1
        
    #print(letter_count)
    #sorted_count = sorted(letter_count.items())
    #print(sorted_count)

    print(letter_count)
    tmp = sorted( [(k, v) for (v, k) in letter_count.items()], reverse=True)
    print(tmp)

    print("--- Begin report of books/frankenstein.txt")
    print(f"{count} words found in the document")
    print("")
    for i in range(0,len(tmp)) :
        print(f"The '{tmp[i][1]}' character was found {tmp[i][0]} times")
    print("--- End report ---")
 

 
      




main()
