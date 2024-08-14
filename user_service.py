from data_provider import GoogleSpreadSheetDataProvider


class UserService:
    def __init__(self):
        self.provider = GoogleSpreadSheetDataProvider("Send_scores")

    def add_thanks_to_user(
        self, from_user_id: str, to_user_id: str, description: str, score: int
    ):
        self.provider.append_data(
            [from_user_id, to_user_id, description, score],
        )

    def get_all_records_dict(self):
        result = {}
        records = self.provider.get_all_data()
        for record in records:
            to_user_id = record.pop("to_user_id")
            current_value = result.get(to_user_id)
            if current_value:
                current_value.append(record)
            else:
                current_value = [record]
            result[to_user_id] = current_value
        return result
