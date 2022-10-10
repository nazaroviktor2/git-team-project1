"""Function to work with file."""
import os


def save_text_to_file(text: str, file_name: str) -> str:
    """Save some text to file.

    Args:
        text: str - text to save.
        file_name: str - file's name.

    Returns: str - path to saved file.
    """
    path = "{0}/{1}".format(os.getcwd(), file_name)
    with open(path, "w") as file_to_save:
        file_to_save.write(text)
    return path
