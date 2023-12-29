import sqlite3
import uuid

from urllib.parse import urlparse

from helper import dt2str, date_from_webkit


def create_connection(database='local_data.db'):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS browser_history (
            id TEXT PRIMARY KEY,
            url TEXT,
            title TEXT,
            last_visit_time TEXT
        )
    ''')
    return cursor, conn


def insert_visits(data, table_name='browser_history'):
    cursor, conn = create_connection()
    for row in data:
        print("Insrted")
        cursor.execute(f'''
            INSERT INTO {table_name} (id, url, title, last_visit_time)
            VALUES (?, ?, ?, ?)
        ''', (str(uuid.uuid4()), urlparse(row[0]).netloc, row[1], dt2str(date_from_webkit(row[2], 5.5))))
    conn.commit()
    conn.close()


def delete_vists():
    cursor, conn = create_connection()
    test = cursor.execute('''
        Delete from browser_history
    ''').fetchall()
    conn.commit()
    for t in test:
        print(t)


data_to_insert = [('https://web.whatsapp.com/', '(4) WhatsApp', 13347276360792631),
                  ('https://chat.openai.com/', 'ChatGPT', 13347271142274210),
                  ('https://skyfoundry.com/', 'Home – SkyFoundry', 13347269453670045),
                  ('https://chat.openai.com/c/5979cade-9b1c-46e9-bea6-90b5fe4daf3c', 'View Greengrass Logs',
                   13347271016460708), (
                      'https://nagarro.sharepoint.com/sites/iotcoe/_layouts/15/stream.aspx?id=%2Fsites%2Fiotcoe%2FShared%20Documents%2FIoT%2FWork%20%2D%202023%2FPlatform%2FRecordings%2FBMS%5FHoneywell%5FTechWalkthrough%2FMeeting%20with%20BMS%20technical%20team%2D20231110%5F121204%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview',
                      'Meeting with BMS technical team-20231110_121204-Meeting Recording.mp4', 13347271013455521), (
                      'https://www.google.com/search?q=hello&rlz=1C1JJTC_enIN971IN971&oq=Hello&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMg0IARAuGLEDGMkDGIAEMgcIAhAAGIAEMgoIAxAuGLEDGIAEMg0IBBAAGIMBGLEDGIAEMg0IBRAuGIMBGLEDGIAEMg0IBhAAGIMBGLEDGIAEMgcIBxAuGIAEMgcICBAAGIAEMgoICRAAGLEDGIAE0gEHODczajBqN6gCALACAA&sourceid=chrome&ie=UTF-8',
                      'hello - Google Search', 13347269451834166),
                  ('https://chat.openai.com/#pricing', 'ChatGPT', 13347271119228787),
                  ('https://chat.openai.com/c/763060a8-aa2a-4c34-af10-ab7e054de084', 'ChatGPT', 13347271306874524)]
