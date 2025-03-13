from pathlib import Path
import re

from os import listdir, system, name
from os.path import isfile, join

type StrPath = str | Path

template_dir = "templates"


def main():
    clear()
    print(
        "Welcome to templater. Select a template you would like to run the templater on."
    )
    print()

    directory_options = finder(template_dir, False)

    if len(directory_options) == 0:
        print(
            "ERROR: Please create a template first. Use the README.md if you need help creating one."
        )
        exit(-1)

    for i, option in enumerate(directory_options):
        print(f"{i + 1}. {option}")

    print()

    selected_option = input("Type your option here: ")

    while True:
        try:
            selected_option = int(selected_option)
        except ValueError:
            selected_option = input("ERROR: Invalid option. Type your option here: ")
            continue

        if selected_option < 1 or selected_option > len(directory_options):
            selected_option = input("ERROR: Invalid option. Type your option here: ")
            continue

        break

    # Should never happen.
    if isinstance(selected_option, str):
        exit(-1)

    selected_directory = directory_options[selected_option - 1]
    selected_files = finder(join(template_dir, selected_directory), True)

    template_found = False
    for file in selected_files:
        if file == "template.txt":
            template_found = True

    if not template_found:
        print(
            f"ERROR: Missing the following files:{' template.txt' if not template_found else ''}"
        )
        exit(-1)

    clear()

    key_value: dict[str, str] = {}

    template = None

    with open(join(template_dir, selected_directory, "template.txt"), "r") as f:
        template = f.read()

    if template is None:
        print("ERROR: Failed to read template.")
        exit(-1)

    variables = find_variables(template)

    print("Template: ")
    print()
    print(template)
    print()

    for variable in variables:
        value = input(f"Enter value for {variable}: ")
        key_value[variable] = value

    result = format_strings(template, key_value)

    clear()
    print("Outputting the result below:")
    print()
    print(result)
    exit(0)


def format_strings(template: str, values: dict[str, str]):
    """
    Finds all cases where the variable should be inserted into the template
    and returns a string with all the values interlaced.

    NOTE: If the variable is somehow None, it will instead put in an empty string, "".
    """
    return re.sub(
        r"{(\w+)}",
        lambda match: str(values.get(match.group(1), "")),
        template,
    )


def find_variables(template: str) -> list[str]:
    """
    Finds all variables used in the template, with a maintained order of where it is seen.
    """
    exists = set()
    all_variables = re.findall(r"\{(.*?)\}", template)

    res: list[str] = []
    for variable in all_variables:
        if variable in exists:
            continue

        exists.add(variable)
        res.append(variable)

    return res


def finder(directory: StrPath, is_file: bool):
    """
    Helper function to help search for files or directories.
    """
    if is_file:
        return [f for f in listdir(directory) if isfile(join(directory, f))]
    else:
        return [f for f in listdir(directory) if not isfile(join(directory, f))]


def clear():
    """
    Clears the screen.
    """
    lines = 100
    if name == "posix":
        system("clear")
    elif name in ("nt", "dos", "ce"):
        system("cls")
    else:
        print("\n" * lines)


if __name__ == "__main__":
    main()
