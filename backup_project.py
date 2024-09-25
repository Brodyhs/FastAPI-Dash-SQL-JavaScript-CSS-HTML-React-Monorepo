import os

# Define the root directory of your project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the output file path
OUTPUT_FILE = os.path.join(ROOT_DIR, 'project_backup.txt')

# Define the file extensions you care about
RELEVANT_EXTENSIONS = ['.py', '.js', '.jsx', '.css', '.html']

# Define folders to exclude
EXCLUDE_FOLDERS = ['venv', '__pycache__', '.git', 'node_modules']

# Define setup instructions
SETUP_INSTRUCTIONS = """
# Project Backup Instructions

## Setting Up the Virtual Environment

1. **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - **Windows:**
        ```bash
        venv\\Scripts\\activate
        ```
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

## Installing Dependencies

1. **Upgrade pip:**
    ```bash
    pip install --upgrade pip
    ```

2. **Install FastAPI, Uvicorn, and other dependencies:**
    ```bash
    pip install fastapi uvicorn pymongo pymssql
    ```

3. **For the React frontend, navigate to the frontend directory and install npm packages:**
    ```bash
    cd ../my-website
    npm install
    ```

## Starting the Backend and Frontend

1. **Start the FastAPI backend:**
    ```bash
    cd backend
    venv\\Scripts\\activate  # Activate the virtual environment if not already activated
    uvicorn main:app --reload
    ```
    - The backend will be running at `http://127.0.0.1:8000`

2. **Start the React frontend:**
    ```bash
    cd ../my-website
    npm start
    ```
    - The frontend will open in your default browser at `http://localhost:3000`

## Accessing the Application

- **Empty Locations Page (API Endpoint):**
    - URL: [http://127.0.0.1:8000/empty-locations](http://127.0.0.1:8000/empty-locations)

- **React Frontend Homepage:**
    - URL: [http://localhost:3000](http://localhost:3000)

- **Other Pages:**
    - **Vanilla Tool:** [http://localhost:3000/vanilla-tool](http://localhost:3000/vanilla-tool)
    - **Dash Tool:** [http://127.0.0.1:8000/dash-tool](http://127.0.0.1:8000/dash-tool)
    - **User Tool:** [http://localhost:3000/user-tool](http://localhost:3000/user-tool)

## Restarting the Services

- **To restart the backend or frontend, simply stop the running process (Ctrl+C in the terminal) and start them again using the commands above.**

---

"""

def is_relevant_file(filename):
    _, ext = os.path.splitext(filename)
    return ext in RELEVANT_EXTENSIONS

def should_exclude_folder(folder_name):
    return folder_name in EXCLUDE_FOLDERS

def collect_files(root_dir):
    collected_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modify dirnames in-place to skip excluded folders
        dirnames[:] = [d for d in dirnames if not should_exclude_folder(d)]
        for filename in filenames:
            if is_relevant_file(filename):
                filepath = os.path.join(dirpath, filename)
                collected_files.append(filepath)
    return collected_files

def write_backup_file(files, output_path, instructions):
    with open(output_path, 'w', encoding='utf-8') as f:
        # Write setup instructions
        f.write(instructions)
        f.write("\n\n")
        
        # Write each file's path and content
        for file_path in files:
            relative_path = os.path.relpath(file_path, ROOT_DIR)
            f.write(f"=== File: {relative_path} ===\n\n")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                f.write(content)
            except Exception as e:
                f.write(f"Error reading file: {e}\n")
            f.write("\n\n")  # Add space between files

def main():
    print("Scanning project directory for relevant files...")
    files = collect_files(ROOT_DIR)
    print(f"Found {len(files)} relevant files.")
    
    print(f"Writing to {OUTPUT_FILE}...")
    write_backup_file(files, OUTPUT_FILE, SETUP_INSTRUCTIONS)
    print("Backup complete!")

if __name__ == "__main__":
    main()
