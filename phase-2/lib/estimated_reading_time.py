def estimated_reading_time(text):

    if text == "":
        return "Pick up a book!"
    if text == None:
        raise Exception("Unable to estimate a None value")
    words = text.split()
    count = len(words)
    time = count / 200
    return f"This will take you {time} minutes to read."

