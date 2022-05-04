from notion_client import Client


class Notion:
    def __init__(self, notion_token):
        self.notion_token = notion_token
        self.notion = Client(auth=self.notion_token)

    def add_new_page(self, page_name):
        return "hello"
