from data_provider import GoogleSpreadSheetDataProvider


class GiftService:
    def __init__(self):
        self.provider = GoogleSpreadSheetDataProvider("Gifts")

    def get_gifts_info(self):
        records = self.provider.get_all_data()
        active_gifts = [
            record
            for record in records
            if record["Is_active"] == "TRUE" and float(record["Amount"]) >= 1
        ]

        if active_gifts:
            return self.__convert_records_to_blocks(active_gifts)

        return None

    def __convert_records_to_blocks(self, records):
        blocks = []

        table = "```"
        table += "Gift            | Value          | Description\n"
        table += "---------------------------------------------\n"

        for item in records:
            gift_name = str(item["Gift_name"]).ljust(15)
            value = str(item["Value"]).ljust(15)
            description = str(item["Description"])

            table += f"{gift_name} | {value} | {description}\n"

        table += "```"
        row = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": table,
            },
        }

        blocks.append(row)

        return blocks
