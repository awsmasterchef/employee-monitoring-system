import os
import shutil
import sqlite3
from datetime import datetime, timedelta
import getpass


def dt2str(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def date_from_webkit(webkit_timestamp, tz):
    """Convert webkit(utc) to local datetime"""
    epoch_start = datetime(1601, 1, 1)
    delta = timedelta(hours=tz, microseconds=int(webkit_timestamp))
    return epoch_start + delta


def current_webkit_timestamp_minus_one_hour():
    current_utc_time = datetime.utcnow()
    one_hour_ago = current_utc_time - timedelta(hours=1)
    webkit_epoch = datetime(1601, 1, 1)
    delta = one_hour_ago - webkit_epoch
    webkit_timestamp = int(delta.total_seconds() * 1e6)  # for converting time to microseconds

    return webkit_timestamp


def get_chrome_history():
    # Path to Chrome history database on Windows
    history_db_path = os.path.join(
        f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    )
    print(history_db_path)
    shutil.copy2(history_db_path, 'temp_history.db')
    # Connect to the history database
    connection = sqlite3.connect('temp_history.db')
    cursor = connection.cursor()

    # Get URLs visited today
    start_timestamp = current_webkit_timestamp_minus_one_hour()
    query = f"SELECT * FROM urls WHERE last_visit_time >= {start_timestamp}"
    cursor.execute(query)

    # Fetch and print the results
    urls = cursor.fetchall()
    for url in urls:
        print(f"URL: {url[1]}")
        print(f"Title: {url[2]}")
        print(f"Visit Count: {url[3]}")
        print(f"Last Visit Time: {dt2str(date_from_webkit(url[5], 5.5))}")
        print()

    # Close the connection
    connection.close()


if __name__ == "__main__":
    get_chrome_history()
