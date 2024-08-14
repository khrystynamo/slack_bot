import random
from data_provider import GoogleSpreadSheetDataProvider


class SupportService:
    def __init__(self):
        self.provider = GoogleSpreadSheetDataProvider("Support")

    def get_random_message(self) -> str:
        records = self.provider.get_all_data()
        return random.choice(records)["description"]
