import random
import sys


HANGMAN_PICS = [
    "",
    "\n  O",
    "\n  O\n  |",
    "\n  O\n /|",
    "\n  O\n /|\\",
    "\n  O\n /|\\\n /",
    "\n  O\n /|\\\n / \\",
]


def choose_word():
    words = [
        "hangman",
        "python",
        "challenge",
        "variable",
        "function",
        "iteration",
        "condition",
        "module",
        "package",
        "developer",
    ]
    return random.choice(words).lower()


def display_state(secret, correct_letters, wrong_guesses, attempts_left):
    revealed = " ".join(c if c in correct_letters else "_" for c in secret)
    pic_index = len(HANGMAN_PICS) - 1 - attempts_left
    pic_index = max(0, min(pic_index, len(HANGMAN_PICS) - 1))
    print("\n" + HANGMAN_PICS[pic_index])
    print(f"Word: {revealed}")
    print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
    print(f"Attempts left: {attempts_left}")


def prompt_guess(used_letters):
    while True:
        guess = input("Guess a letter or the full word: ").strip().lower()
        if not guess:
            print("Please enter a letter or word.")
            continue
        if not guess.isalpha():
            print("Only alphabetic characters are allowed.")
            continue
        if len(guess) == 1 and guess in used_letters:
            print("You've already tried that letter.")
            continue
        return guess


def play_round():
    secret = choose_word()
    correct_letters = set()
    wrong_guesses = set()
    attempts_left = 6

    print("\n--- Hangman ---")

    while attempts_left > 0:
        display_state(secret, correct_letters, wrong_guesses, attempts_left)
        guess = prompt_guess(correct_letters | wrong_guesses)

        # full-word guess
        if len(guess) > 1:
            if guess == secret:
                print(f"Correct — the word was '{secret}'. You win!")
                return True
            else:
                attempts_left -= 1
                print("Incorrect full-word guess.")
                continue

        # single letter
        if guess in secret:
            correct_letters.add(guess)
            print(f"Good guess: '{guess}' is in the word.")
            if all(ch in correct_letters for ch in secret):
                print(f"You revealed the word '{secret}'. You win!")
                return True
        else:
            wrong_guesses.add(guess)
            attempts_left -= 1
            print(f"Nope: '{guess}' is not in the word.")

    print(f"\nNo attempts left. The word was '{secret}'. Game over.")
    return False


def main():
    print("Play Hangman — guess letters to reveal the word.")
    try:
        while True:
            play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if not again or again[0] != 'y':
                print("Thanks for playing Hangman!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")
        sys.exit(0)


if __name__ == '__main__':
    main()
