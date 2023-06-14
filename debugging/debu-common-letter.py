def get_most_common_letter(text):
    counter = {}
    text.replace(" ", "")
    # removed the whitespace so it isn't counted
    for char in text.replace(' ', ''):
        counter[char] = counter.get(char, 0) + 1
        # counter is a dictionary that gets a key value pair of the char in text and the amount of times it
        #  appears in counter
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # sorted by the second element in item whic is the frequency value, then selecing the last with [-1] so 
    # the highest frequency and [0] to selct the letter key
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")