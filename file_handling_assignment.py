def main():
    # File Creation and Writing
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("145678\n")
            file.write("This are the numbers 98765.\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    # File Reading and Display
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("File contents after writing:")
            print(contents)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    # File Appending
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending additional line.\n")
            file.write("67890\n")
            file.write("Another line with mixed content 04235.\n")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

    # Reading and Displaying File Contents Again
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("File contents after appending:")
            print(contents)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")