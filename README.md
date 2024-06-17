# YouTube Comment Extractor

This Python script extracts comments and commenter usernames from a JSON file and saves the extracted data to another JSON file. It is designed to organize the raw comment data obtained from the [YouTube Comment Downloader](https://github.com/egbertbouman/youtube-comment-downloader) if you are only interested in the comment text and the commenter.

## Features

- Reads a JSON file containing raw YouTube comments.
- Extracts the `text` (comment) and `author` (commenter username) fields from each comment.
- Counts the total number of comments.
- Saves the extracted comments and usernames to a new JSON file.

## Requirements

- Python 3.x
- No additional libraries required beyond the Python standard library

## Usage

1. Ensure you have Python 3 installed on your machine.
2. Save the script to a `.py` file, for example, `youtube_comment_extractor.py`.
3. Place your raw comments JSON files in an input directory, for example, `input_comments`.
4. Run the script from a terminal or command prompt.

### Steps to Run the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the script using the command:

   ```sh
   python youtube_comment_extractor.py
