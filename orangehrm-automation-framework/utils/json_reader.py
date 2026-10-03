import json
import os


def get_test_data(file_name="credentials.json"):
    # Builds the absolute path to the test_data folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "test_data", file_name)

    with open(file_path, "r") as file:
        return json.load(file)