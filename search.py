import sqlite3
from database import DB_NAME

# search for keyword in the database and return matching chunks
def search_keyword(keyword):
    # create a new database connection
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # execute search query
    cursor.execute("""
        SELECT source_file, content
        FROM text_chunks
        WHERE content LIKE ?
    """, (f"%{keyword}%",))

    # fetch all matching results
    results = cursor.fetchall()
    # close the connection and return results
    conn.close()
    return results
