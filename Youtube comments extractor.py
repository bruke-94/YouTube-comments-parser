import json
import os

# Path to your input JSON file
input_directory= r'D:\Useful python programs\Youtube comment extractor\Raw comments (unparsed)'
# Prompt user for input file name (without extension)
input_filename = input("Input File name: ")  
# Construct the full input file path
input_json_file= os.path.join(input_directory, input_filename + '.json')
# Directory path where you want to save the output JSON file
output_directory = r'D:\Useful python programs\Youtube comment extractor\Final (parsed)'

# Prompt user for output file name (without extension)
output_filename = input("Output file name: ")

# Construct the full output file path
output_json_file = os.path.join(output_directory, output_filename + '.json')

# List to store extracted data
extracted_data = []

# Read input JSON file
try:
    with open(input_json_file, 'r', encoding='utf-8') as f:
        # Read each line in the file
        for line in f:
            # Try to parse each line as JSON
            try:
                entry = json.loads(line.strip())

                # Extract text and author fields if they exist
                if 'text' in entry and 'author' in entry:
                    extracted_entry = {
                        'text': entry['text'],
                        'author': entry['author']
                    }
                    extracted_data.append(extracted_entry)

            except json.JSONDecodeError as e:
                print(f'Error decoding JSON: {str(e)}')
                continue  # Skip this line if JSON decoding fails
        # Count number of comments extracted
    num_comments = len(extracted_data)

    # Prepend count as the first entry in extracted_data
    extracted_data.insert(0, {'comment_count': num_comments})


    # Write extracted data to output JSON file
    with open(output_json_file, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)

    print(f'Extracted data saved to {output_json_file}')
    # Count number of comments extracted
    num_comments = len(extracted_data)
    num_comments -= 1
    print(f'{num_comments} comments counted')


except FileNotFoundError:
    print(f'Error: File {input_json_file} not found.')

except Exception as e:
    print(f'An error occurred: {str(e)}')
