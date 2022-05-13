import datetime
import os

from dotenv import load_dotenv

from notion import notion_handler
from oura_wrapper import oura_wrapper

load_dotenv()


def new_life_page():
    notion_client.add_new_page(daily_data['active_calories'], 10, "6h50m")


oura_ring = oura_wrapper(os.getenv("OURA_TOKEN"))
daily_data = oura_ring.get_daily_activity("2022-05-12", "2022-05-13")
sleep_data = oura_ring.get_daily_sleep("2022-05-12", "2022-05-13")
print(sleep_data)
# print(datetime.timedelta(seconds=sleep_data['duration']))
print(datetime.timedelta(seconds=sleep_data['total']))
notion_client = notion_handler(os.getenv("NOTION_TOKEN"), os.getenv("DB_ID"))

# new_life_page()
