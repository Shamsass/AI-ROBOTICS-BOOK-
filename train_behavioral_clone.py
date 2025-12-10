def count_words_in_file(file_path):
    """Reads a text file and returns the total word count."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Split the content by whitespace and count the resulting elements
            word_count = len(content.split())
        return word_count
    except FileNotFoundError:
        return f"Error: File not found at path: {file_path}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example Usage:
# 1. Create a file named 'example.txt' with some text in the same directory.
# 2. Run the script.
file_to_check = 'example.txt'
total_words = count_words_in_file(file_to_check)
print(f"The file '{file_to_check}' contains {total_words} words.")