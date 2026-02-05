# Text Chunking and Keyword Search Program

## Overview

This project is a simple Python program that processes text files in a structured and reproducible way. The program reads one or more text files, splits each file into sequential text chunks based on word count (300-500 words), stores the chunks in a local SQLite database, and allows users to search for text chunks using a keyword.

---

## Features

- Reads one or more `.txt` files from a local directory
- Splits text sequentially into chunks of **300–500 words**
- Stores valid chunks in a local **SQLite database**
- Skips files that have already been processed to avoid duplication
- Provides an interactive **keyword-based search** using terminal
- Runs locally using only standard Python libraries

---

## Project Structure

```bash
project_root/
│
├── main.py # entry point
├── database.py # database initialization and insert logic
├── text_processor.py # file reading, chunking, and file-check logic
├── search.py # keyword search functionality
├── chunks.db # SQLite database (auto-generated)
├── data/
│ └── article_1.txt # example of text files
│ └── article_2.txt # example of text files
│ └── article_2.txt # example of text files
└── README.md # project documentation
```

---

## Program Workflow

### File Retrieval

The program scans the `data/` directory and reads all files with the `.txt` extension using UTF-8 encoding.

Before processing a file, the program checks the database to determine whether the file name already exists in the `source_file` column. If the file has already been processed, it is skipped to prevent duplicate data insertion.

---

### Text Chunking

Each text file is split **sequentially from beginning to end** into contiguous chunks based on word count:

- Minimum chunk size: **300 words**
- Maximum chunk size: **500 words**

Any remaining text at the end of the file that does not meet the minimum word requirement is intentionally excluded. This ensures that all stored chunks strictly follow the task specification.

---

### Database Storage

Valid chunks are stored in a local SQLite database named `chunks.db`, located in the same directory as the program code.

The database table structure is as follows:

| Column Name  | Description                           |
|-------------|---------------------------------------|
| id          | Auto-incremented primary key           |
| source_file | Name of the original text file         |
| content     | Text content of the chunk              |

The database and table are created automatically if they do not already exist.

---

### Keyword Search

After processing the text files, the program enters an interactive search mode using terminal. Users can enter a keyword, and the program will display all text chunks that contain that keyword.

The search uses simple substring matching and returns:
- The source file name
- A short preview of the matching text chunk

Users can exit the search mode by typing `exit`.

---

## How to Run the Program

### Step 1 - Requirements

- Python **3.10 or later**
- No external libraries are required

Verify Python installation:

```bash
python --version
```

### Step 2 - Prepare Input Data

1. Place one or more `.txt` files inside the folder named `data`.

Example:
```bash
data/
├── article1.txt
├── article2.txt
```


### Step 3 - Execute the Program

From the project root directory, run:

```bash
python main.py
```

The program will:
1. Initialize the database
2. Process new text files
3. Store valid chunks in the database
4. Enter keyword search mode

### Step 4 - Search Text Chunks

When prompted:

```bash
Enter a keyword (or type 'exit'):
```

- Enter any keyword to search for matching chunks
- Type exit to terminate the program

!['Result Output'](/01_assignment/img/results.png)

---

## AI Tool Usage

AI tools were used as a development assistant to:

- Assisting with code structuring and modularization 
- Helping refine text chunking and validation logic in line with the task requirements
- Generate clear technical documentation

---

## Conclusion

This project implements a complete and functional **text-processing pipeline**, **from file retrieval and validation to data storage and retrieval**. The solution is intentionally simple, readable, and easy to explain, aligning with the objectives of the technical assignment.