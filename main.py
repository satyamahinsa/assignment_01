import os

from database import init_db, insert_chunk
from text_processor import load_and_chunk_files
from search import search_keyword

# define data directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def main():
    # initialize the database
    init_db()

    # load and process text files, then insert chunks into the database
    for filename, chunks in load_and_chunk_files(DATA_DIR):
        for chunk in chunks:
            insert_chunk(filename, chunk)

    print("Data has been processed and inserted into the database\n")

    # keyword-based search loop
    while True:
        keyword = input("Enter a keyword (or type 'exit'): ")
        if keyword.lower() == "exit":
            break

        # search for matching text chunks
        results = search_keyword(keyword)
        print(f"\nFound {len(results)} results\n")

        # display search results with a short preview
        for i, (source, content) in enumerate(results, 1):
            print(f"Result {i} | Source file: {source}")
            print(content[:300] + "...\n")  # show only the first 300 characters

if __name__ == "__main__":
    # entry point of the program
    main()