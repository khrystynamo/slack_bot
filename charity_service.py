from data_provider import GoogleSpreadSheetDataProvider


class CharityService:
    def __init__(self):
        self.provider = GoogleSpreadSheetDataProvider("Charity")

    def get_charity_info(self):
        records = self.provider.get_all_data()
        return self.__convert_records_to_blocks(records)

    def __convert_records_to_blocks(self, records):
        blocks = []
        header = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*Name* | *Link to Pay* | *Target*"},
        }

        blocks.append(header)
        blocks.append({"type": "divider"})

        for item in records:
            row = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{item['charity_name']} | <{item['link_for_pay']}|Pay Here> | {item['target']}",
                },
            }

            blocks.append(row)
            blocks.append({"type": "divider"})

        return blocks
