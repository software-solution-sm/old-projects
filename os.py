import os

def run_shell():
    while True:
        # Get user input
        user_input = input("$ ")

        # Exit the shell if the user enters 'exit' or 'quit'
        if user_input.lower() in ['exit', 'quit']:
            break

        # Run the command
        try:
            result = os.system(user_input)
            print(f"Command executed with return code {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Simple Python Shell")
    run_shell()

