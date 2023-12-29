import os
import shutil
import sqlite3
import time
from datetime import datetime, timedelta
import getpass
from db import insert_visits
from helper import read_config_file


def current_webkit_timestamp_minus_one_hour():
    current_utc_time = datetime.utcnow()
    one_hour_ago = current_utc_time - timedelta(hours=2)
    webkit_epoch = datetime(1601, 1, 1)
    delta = one_hour_ago - webkit_epoch
    webkit_timestamp = int(delta.total_seconds() * 1e6)  # for converting time to microseconds

    return webkit_timestamp


def browser_history_collector_worker():
    # Path to Chrome history database on Windows
    while True:
        history_db_path = os.path.join(
            f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        )
        shutil.copy2(history_db_path, 'temp_history.db')
        connection = sqlite3.connect('temp_history.db')
        cursor = connection.cursor()
        start_timestamp = current_webkit_timestamp_minus_one_hour()
        query = f"SELECT url,title,last_visit_time FROM urls WHERE last_visit_time >= {start_timestamp}"
        cursor.execute(query)
        urls = cursor.fetchall()
        connection.close()
        os.remove('temp_history.db')
        insert_visits(urls)

        time.sleep(read_config_file('browser_history_sync_frequency'))


if __name__ == "__main__":
    browser_history_collector_worker()
