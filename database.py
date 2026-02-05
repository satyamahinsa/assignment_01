import os, sqlite3

# get the directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# name of the local database file
DB_NAME = os.path.join(BASE_DIR, "chunks.db")

# create the database and table if they don't exist
def init_db():
    # create a new database connection
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # create a table to store text chunks if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS text_chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file TEXT,
            content TEXT
        )
    """)
    
    # commit changes and close the connection
    conn.commit()
    conn.close()

# insert a text chunk into the database
def insert_chunk(source_file, content):
    # create a new database connection
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # insert a single text chunk into the table
    cursor.execute(
        "INSERT INTO text_chunks (source_file, content) VALUES (?, ?)",
        (source_file, content)
    )
    
    # commit changes and close the connection
    conn.commit()
    conn.close()
