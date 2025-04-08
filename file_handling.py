def process_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()

        words = content.split()
        word_count = len(words)

        content_upper = content.upper()

        with open(output_file, "w") as f:
            f.write("PROCESSED TEXT:\n")
            f.write(content_upper + "\n")
            f.write(f"\nWORD COUNT: {word_count}\n")

        print(f"Success! '{output_file}' has been created with the processed content and word count.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_file("input.txt", "output.txt")
