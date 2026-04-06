def get_user_sentence() -> str:
    """Get a sentence from the user.

    :return: user-entered sentence.
    """
    return input("Enter a sentence: ")


def count_sentence_words(phrase: str) -> int:
    """Count the number of words in a phrase.

    :param phrase: the phrase that will have its words counted.
    :return: the number of words in the phrase.
    """
    return len(phrase.split())


def get_longest_word(phrase: str) -> str:
    """Get the longest word in a given phrase.

    :param phrase: the phrase in which we will find the longest word.
    :return: the longest word in the phrase.
    """
    return max(phrase.split(), key=len)



def main() -> None:
    """Main execution of the program.
    """
    phrase = get_user_sentence()
    print("The number of words in the sentence is:", count_sentence_words(phrase))
    print(f"The longest word in the sentence is {get_longest_word(phrase)}")



if __name__ == "__main__":
    main()