import sys
from string import punctuation


def text_analyzer(text = ''):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""

    if not type(text).__name__ == "str":
        print("AssertionError: argument is not a string")
        return

    if (len(text) == 0):
        print("What is the text to analyze?")
        text = input()

    # upper = lower = punc = space = 0
    # length = len(set(text.replace(' ', '')))
    length = len(set(text) - set(' '))
    upper = len([letter for letter in text if letter.isupper()])
    lower = len([letter for letter in text if letter.islower()])
    punc = len([letter for letter in text if letter in punctuation])
    space = text.count(' ')
    # for letter in text:
    #     if letter.isupper():
    #         upper += 1
    #     if letter.islower():
    #         lower += 1
    #     if letter in punctuation:
    #         punc += 1
    #     if letter == ' ':
    #         space += 1

    print(f"The text contains {length} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punc} punctuation mark(s)")
    print(f"- {space} space(s)")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()