def verify_text(text):
    punctuation_marks = [".", "!", "?"]
    if not text[0].isupper():
        return "No capitalised first letter."
    for char in punctuation_marks:
        if text[-1] != char:
            return "No suitable ending punctuation mark"