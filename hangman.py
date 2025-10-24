import random

# List of predefined words
words = ["python", "developer", "hangman", "program", "code"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6
word_display = ["_"] * len(word)

print("🎯 Welcome to the Hangman Game!")
print("Guess the word, one letter at a time.")
print(f"You have {attempts} incorrect guesses allowed.\n")

while attempts > 0:
    print("Word:", " ".join(word_display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
        if "_" not in word_display:
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}\n")

else:
    print("💀 Game Over! The word was:", word)
if __name__ == "__main__":
    main()
