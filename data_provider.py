import logging
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

logger = logging.getLogger(__name__)


def _get_now() -> str:
    return datetime.now().strftime("%Y-%m-%d")


class GoogleSpreadSheetDataProvider:
    def __init__(
        self,
        sheet_name: str,
        spreadsheet_id="1381W8jtx__oojEqkY-ae2hX6H9nyYmIlj4jRzpTicWo",
    ):
        SERVICE_ACCOUNT_FILE = "creds.json"

        SCOPES = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]

        credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        client = gspread.authorize(credentials)

        spreadsheet = client.open_by_key(spreadsheet_id)

        self.sheet = spreadsheet.worksheet(sheet_name)

    def append_data(self, data: list) -> None:
        data.append(_get_now())

        logger.debug(f"Append data: {data}")

        response = self.sheet.append_row(
            values=data, value_input_option="RAW", include_values_in_response=True
        )

        logger.debug(f"Received response from G-Sheets: {response}")

    def get_all_data(self):
        return self.sheet.get_all_records()
