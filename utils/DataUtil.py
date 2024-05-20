import json


class DataUtil:

    @staticmethod
    def get_credentials_from_file(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data