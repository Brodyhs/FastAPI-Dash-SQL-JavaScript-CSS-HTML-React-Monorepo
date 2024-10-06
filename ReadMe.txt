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