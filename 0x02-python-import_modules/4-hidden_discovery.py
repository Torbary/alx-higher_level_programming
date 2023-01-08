#!/usr/bin/python3

if __name__ == '__main__':
    import importlib.util
    import hidden_4

    # Get the names defined in hidden_4
    names = dir(hidden_4)

    # Filter out names that start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort the names alphabetically
    filtered_names.sort()

    # Print the names
    for name in filtered_names:
        print(name)
