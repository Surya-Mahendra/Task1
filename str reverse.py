def reverse_string(input_string):
    return input_string[::-1]

def main():
    user_input = input("Enter a string to reverse: ")
    reversed_output = reverse_string(user_input)
    print("Reversed string:", reversed_output)
if __name__ == "__main__":
   main()