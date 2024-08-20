import sqlite3

con = sqlite3.connect('articles.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE IF NOT EXISTS item(id integer PRIMARY KEY, title text NOT NULL, price integer NOT NULL check (price > 0), category text NOT NULL, state text NOT NULL, type text, option text, description text NOT NULL, path text NOT NULL, groups text, label text)")
cursorObj.execute("CREATE TABLE IF NOT EXISTS settings(user_email_login TEXT PRIMARY KEY,user_password_login TEXT NOT NULL,'language' TEXT NOT NULL,images_path TEXT NOT NULL,time_to_sleep REAL NOT NULL CHECK (time_to_sleep > 0),browser TEXT NOT NULL)")
con.commit()
con.close()
