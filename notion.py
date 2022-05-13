import datetime

from notion_client import Client


class notion_handler:
    def __init__(self, notion_token, notion_db_id):
        self.notion_token = notion_token
        self.notion = Client(auth=self.notion_token)
        self.notion_db_id = notion_db_id

    def add_new_page(self, calories_burned: int, running_time: int, sum_sleep_time: str) -> str:
        self.notion.pages.create(
            **{
                'parent': {'database_id': self.notion_db_id},
                'properties': {
                    'title': {
                        'title': [
                            {
                                'text': {
                                    'content': "life info"
                                }
                            }
                        ]
                    },
                    'Date': {
                        'date': {
                            'start': self.today()
                        }
                    },
                    '消費カロリー': {
                        'number': calories_burned
                    },
                    'ランニング時間': {
                        'number': running_time
                    },
                    '合計睡眠時間': {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": sum_sleep_time},
                            },
                        ],
                    }
                }
            }
        )

    @staticmethod
    def today() -> str:
        return datetime.datetime.today().strftime("%Y-%m-%d")
