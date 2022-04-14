from globalconstants.global_constants import TOKEN_CSV_PATH
from datetime import datetime

class FileOperation:

    @classmethod
    def write_token_to_file(cls, username, token):
        data = f"{datetime.now()},{username},{token}\n"
        try:
            with open(TOKEN_CSV_PATH, "a+t", encoding="utf-8") as file:
                file.write(data)
        except Exception as ex:
            print(f"Error in write_token_to_file: {ex}")
            return False
        