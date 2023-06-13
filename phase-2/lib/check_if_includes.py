def check_if_includes(text):
    if text == "":
        raise Exception("No text found, try again!")
    if "#TODO" in text:
        return "This contains TODO"
    return "This doesn't contain #TODO"
