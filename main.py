print("NAME: RYAN HERMOSO")
print("SECTION: BS COMPUTER SCIENCE 1E")
print("DATE: JANUARY 03, 2024")
print("INSTRYCTOR:MR. RALPH ANGELO BAGUIO")
def reverse_text():
    while True:
        user_input = input("Enter a text: ")

        if user_input.isdigit():
            print("Error Reported! Enter text only.")
        else:
            reversed_text = user_input[::-1]
            print("Reversed text:", reversed_text)
            break


if __name__ == "__main__":
    reverse_text()

