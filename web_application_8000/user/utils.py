from globalconstants.global_constants import TOKEN_CSV_PATH
import http
from datetime import datetime

class FileOperation:

    @classmethod
    def write_token_to_file(cls, username, token):
        try:
            data = f"{datetime.now()},{username},{token}\n"
            with open(TOKEN_CSV_PATH, "a+t", encoding="utf-8") as file:
                file.write(data)
        except Exception as ex:
            raise Exception(
                status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=str(ex)
            )