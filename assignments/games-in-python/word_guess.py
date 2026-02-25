import random
import sys


def choose_word():
    words = [
        "python",
        "developer",
        "algorithm",
        "function",
        "variable",
        "iteration",
        "string",
        "condition",
        "module",
        "package",
    ]
    return random.choice(words).lower()


def display_state(secret, correct_letters, wrong_guesses, attempts_left):
    revealed = " ".join(c if c in correct_letters else "_" for c in secret)
    print(f"\nWord: {revealed}")
    print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
    print(f"Attempts left: {attempts_left}")


def prompt_guess(used_letters):
    while True:
        guess = input("Enter a letter or guess the full word: ").strip().lower()
        if not guess:
            print("Please enter something.")
            continue
        if guess.isalpha() is False:
            print("Please use only alphabetic characters.")
            continue
        if len(guess) == 1:
            if guess in used_letters:
                print("You already tried that letter.")
                continue
        return guess


def play_round():
    secret = choose_word()
    correct_letters = set()
    wrong_guesses = set()
    attempts_left = 6

    print("\n--- New Game: Word Guess ---")

    while attempts_left > 0:
        display_state(secret, correct_letters, wrong_guesses, attempts_left)
        guess = prompt_guess(correct_letters | wrong_guesses)

        # full-word guess
        if len(guess) > 1:
            if guess == secret:
                print(f"Correct! The word was '{secret}'. You win!")
                return True
            else:
                attempts_left -= 1
                print("Incorrect full-word guess.")
                continue

        # single-letter guess
        if guess in secret:
            correct_letters.add(guess)
            print(f"Good: '{guess}' is in the word.")
            # check if all letters revealed
            if all(ch in correct_letters for ch in secret):
                print(f"Well done! The word was '{secret}'. You win!")
                return True
        else:
            wrong_guesses.add(guess)
            attempts_left -= 1
            print(f"Sorry: '{guess}' is not in the word.")

    print(f"\nOut of attempts. The word was '{secret}'. Better luck next time.")
    return False


def main():
    print("Classic Word-Guessing Game")
    try:
        while True:
            play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if not again or again[0] != 'y':
                print("Thanks for playing!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")
        sys.exit(0)


if __name__ == '__main__':
    main()
