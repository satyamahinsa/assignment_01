import os
import sqlite3
from database import DB_NAME

# read a text file and return its content
def read_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# chunk text into smaller pieces based on word count
def chunk_text(text, min_words=300, max_words=500):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + max_words
        chunk_words = words[start:end]

        # only include the chunk if it meets the word count requirement
        if min_words <= len(chunk_words) <= max_words:
            chunks.append(" ".join(chunk_words))

        start = end

    return chunks

# get list of already processed files from database
def get_processed_files():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # fetch distinct source files
    cursor.execute("SELECT DISTINCT source_file FROM text_chunks")
    files = {row[0] for row in cursor.fetchall()}

    conn.close()
    return files

# load and chunk text files from a directory
def load_and_chunk_files(directory):
    processed_files = get_processed_files()
    
    # iterate over all text files in the directory
    for filename in os.listdir(directory):
        if not filename.endswith(".txt"):
            continue

        # skip file if it has already been processed
        if filename in processed_files:
            continue
        
        # read and chunk the file
        path = os.path.join(directory, filename)
        text = read_text_file(path)
        yield filename, chunk_text(text)
