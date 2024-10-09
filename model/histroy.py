import os
import json

# Function to save a query and its results to history
def save_to_history(query_text, results):
    # Get the current directory of this file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path for the query history file
    history_path = os.path.join(current_dir, 'query_history.txt')

    # Prepare data for storing
    history_data = {
        'query': query_text,
        'results': results['documents']  # Assuming 'documents' contains the relevant results
    }

    # Write the query and results to a file as JSON
    with open(history_path, 'a') as history_file:
        history_file.write(json.dumps(history_data) + '\n')  # Write each entry in a new line

# Function to load the query history from a file
def load_history():
    # Get the current directory of this file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path for the query history file
    history_path = os.path.join(current_dir, 'query_history.txt')

    # Read and return the history from the file
    history = []
    if os.path.exists(history_path):
        with open(history_path, 'r') as history_file:
            for line in history_file:
                history.append(json.loads(line))
    
    return history
