def read_user_file():
    filename = input("📂 Enter the name of the file to read (e.g., input.txt): ")

    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("\n📄 File Content:")
            print("----------------------------")
            print(content)
            print("----------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_user_file()
