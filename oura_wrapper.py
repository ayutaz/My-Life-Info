import requests


class oura_wrapper:
    base_url = 'https://api.ouraring.com/'

    def __init__(self, notion_token):
        self.notion_token = notion_token

    def create_url(self, endpoint_url) -> str:
        return self.base_url + endpoint_url + "?access_token=" + self.notion_token

    def get_user_info(self) -> dict:
        return requests.get(self.create_url("v1/userinfo")).json()

    def get_headers(self) -> dict:
        return {
            "Authorization": "Bearer " + self.notion_token,
            "Content-Type": "application/json"
        }

    def get_daily_activity(self, start_date: str, end_date: str) -> dict:
        params = {
            "start_date": start_date,
            "end_date": end_date
        }
        return requests.get(
            self.create_url("v2/usercollection/daily_activity"),
            headers=self.get_headers(),
            params=params
        ).json()['data'][0]

    def get_daily_sleep(self, start_date: str, end_date: str) -> dict:
        params = {
            "start_date": start_date,
            "end_date": end_date
        }
        return requests.get(
            self.create_url("v1/sleep"),
            headers=self.get_headers(),
            params=params
        ).json()['sleep'][0]
