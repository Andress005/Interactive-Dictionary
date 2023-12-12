import json  

from difflib import get_close_matches


def load_dictionary(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: The data file is not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode the JSON file.")
        return {}

def translate(word, data):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif close_matches := get_close_matches(word, data.keys()):
        print(f"Do you want to find {close_matches[0]}?")
        decide = input("Press 'y' for yes and 'n' for no: ").lower()
        if decide == "y":
            close_matches = get_close_matches(word, data.keys())
            if close_matches:
                return data[close_matches[0]]
        elif decide == "n":
            return "Wrong search!! Please try again."
        else:
            return "Wrong input! Please enter 'y' or 'n'."
    else:
        return "Word not found. Please try again."

def main():
    file_path = 'path/to/your/data.json'  # Replace with the actual path to your data file
    data = load_dictionary(file_path)

    while True:
        word = input("Enter the word you want to search (or 'exit' to quit): ")

        if word.lower() == 'exit':
            break

        output = translate(word, data)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

if __name__ == "__main__":
    main()

