import string

alphabet = string.ascii_lowercase

def cypher(cyphertext, key, operator):
    decoded = ""
    for c in cyphertext:
        if operator == "right":
            try:
                correct_index = (alphabet.index(c) + key) % 26
                decoded += alphabet[correct_index]
            except ValueError:
                decoded += c
        elif operator == "left":
            try:
                correct_index = (alphabet.index(c) - key) % 26
                decoded += alphabet[correct_index]
            except ValueError:
                decoded += c
    return decoded


if __name__ == "__main__":
    full_loop = 0
    while full_loop != 1:
        try:
            cyphertext = input("Please enter a message: ").lower()
            key = int(input("Please enter a number: "))
            operator = input("Right or Left for your offset direction: ")
            print(cypher(cyphertext, key, operator))
            again = input("Try again? y/n").lower()

            while True:
                if again in  ["n", "no"]:
                    full_loop = 1
                    break
                elif again in ["y", "yes"]:
                    break
                else:
                    print("Invalid input. Try again.")

        except ValueError:
            print("Please enter whole numbers only")
