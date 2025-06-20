# Smart To-Do List Manager

A clean and simple task manager built using **Flask (Python)** for the backend and **HTML + CSS** for the frontend. It helps you create, filter, sort, and manage daily tasks efficiently — with features like priority sorting, overdue detection, and status tracking.

---

##  Features

- **Add New Tasks** (with title, description, due date, and priority)
- **Auto-incremented Task ID**
- **Overdue Detection** based on current date
- **Filter Tasks** by:
  - Pending
  - Completed
  - Overdue
  - Due Today / Tomorrow
- **Sort by Priority** (High → Low) for incomplete tasks
- **Delete Tasks**
- **Mark Tasks as Completed** with timestamp

---

## How It Works

- The backend is powered by `Flask`, and all tasks are saved locally in `tasks.json`.
- Each task is assigned a unique ID automatically.
- When loading tasks, the app automatically marks old tasks (past due date) as **Overdue** if they’re not completed.
- The UI is built with HTML and inline CSS for quick rendering in the browser.

---

##  How to run?

### 1.Clone the Repository
```bash
git clone https://github.com/yourusername/smart-todo-flask.git
cd smart-todo-flask
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```
### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the App
```bash
python app.py
```
Then open your browser and visit:
http://127.0.0.1:5000










