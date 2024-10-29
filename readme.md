# Flask TODO Application

This is a simple Flask web application for managing a TODO list. Users can add, delete, and prioritize tasks, with all data stored in a MongoDB database.

## Features

- **Add TODO Items:** Users can input new tasks along with their priority level.
- **Delete TODO Items:** Each task can be removed from the list.
- **Prioritization:** Users can assign a priority level (Important, Unimportant, Normal, Very Important) to each task.
- **Persistent Storage:** All tasks are stored in a MongoDB database for persistence.

## Tech Stack

- **Flask:** A lightweight WSGI web application framework in Python.
- **MongoDB:** A NoSQL database for storing TODO items.
- **HTML/CSS:** For front-end templates and styling.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mrochelle23/ACS-1710-Final-Assessment.git
   cd flask-todo-app
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install flask pymongo certifi
   ```

4. **Set Up MongoDB:**
   - Ensure you have a MongoDB instance running and update the `uri` variable in `app.py` with your MongoDB connection string.

5. **Run the Application:**
   ```bash
   python app.py
   ```
   Open your browser and go to `http://127.0.0.1:5000` to access the application.

## File Structure

- **app.py:** Main application file containing the Flask app and MongoDB logic.
- **requirements.txt:** Lists the dependencies for the application.
- **.gitignore:** Specifies files and directories to ignore in Git.
- **templates/**: Contains HTML templates used for rendering pages.
  - **index.html**: The main page where users can add and manage TODO items.
- **static/**: Contains static files such as CSS.
  - **styles.css**: Styles for the application.

## Usage

1. On the main page, enter a new TODO item in the text field and select its priority.
2. Click the "Submit" button to add the item to your list.
3. To delete a TODO item, click the "Delete Todo" button next to the item.
4. Tasks can be marked as complete (the completion functionality can be implemented further).

## Acknowledgements

- Developed by Make School students © 2020.
- MongoDB and Flask for their robust frameworks.
