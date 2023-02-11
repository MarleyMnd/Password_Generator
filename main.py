from zxcvbn import zxcvbn
import string
import secrets
import os


def choose_parameters(possible_characters: str) -> tuple[int, str]:
    """ Ask the user for the length of the password, as well as what it will be composed of. """

    # Ask for the possible characters composing the password
    print("""══════════════════════════════════════════╣ Composition ╠══════════════════════════════════════════
    
1. Only letters             4. Letters and numbers              7. Lettres, numbers and punctuation
2. Only numbers             5. Letters and punctuation
3. Only punctuation         6. Numbers and punctuation
""")
    compo = int(input("Choose an option: "))
    while compo not in [1, 2, 3, 4, 5, 6, 7]:
        compo = int(input("\nChoose an option between 1 and 7: "))

    # Selecting characters
    letters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation

    if compo == 1:  # Only letters
        possible_characters = letters
    elif compo == 2:  # Only numbers
        possible_characters = numbers
    elif compo == 3:  # Only punctuation
        possible_characters = punctuation
    elif compo == 4:  # Letters + numbers
        possible_characters = letters + numbers
    elif compo == 5:  # Letters + punctuation
        possible_characters = letters + punctuation
    elif compo == 6:  # Numbers + punctuation
        possible_characters = numbers + punctuation
    elif compo == 7:  # Letters + numbers + punctuation
        possible_characters = letters + numbers + punctuation

    # Ask for the length
    os.system('cls')
    print("""════════════════════════════════════╣ Length of the password ╠═════════════════════════════════════

         It is recommended to generate a password long enough to avoid brute force attacks. 
                                The minimum length is 8 characters.""")
    length = int(input("\nEnter a number greater then 8: "))
    while length <= 7:
        length = int(input("\nThe length must be at least 8: "))

    return length, possible_characters


def generate(length: int, possible_characters: str) -> str:
    """ Generates the password """

    password = ''
    # Generates the secured password depending on the possible characters
    for i in range(length):
        password += str(''.join(secrets.choice(possible_characters)))
    return password


def check_strength(password: str) -> int:
    strength = zxcvbn(password)

    if strength['score'] == 1:
        strength = 'weak'
    elif strength['score'] == 2:
        strength = 'quite good'
    elif strength['score'] == 3:
        strength = 'strong'
    elif strength['score'] == 4:
        strength = 'really strong'

    return strength


def print_password(length: int, password: str, strength: int):
    """ Prints the password """

    # Color/font palette
    red = '\x1b[31m'
    bold = '\x1b[1m'
    reset = '\x1b[0m'

    os.system('cls')
    print("════════════════════════════════════╣ Result ╠═════════════════════════════════════\n")
    print(f"Your password of length {length} is {bold}{red}{password}{reset}")
    print(f"""It is {strength} according to the "zxcvbn" password analyzer.""")


def main():
    # Gets parameters
    length, possible_characters = choose_parameters('a')

    # Generates the password
    password = generate(length, possible_characters)

    # Checks its strength
    strength = check_strength(password)

    # Displays the password
    print_password(length, password, strength)
    input("\nPress Enter to close...")


if __name__ == '__main__':
    main()
