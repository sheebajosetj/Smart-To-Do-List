from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime, date
from datetime import datetime, date, timedelta

app = Flask(__name__)

TASKS_FILE = 'tasks.json'

# Load or initialize tasks
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def update_overdue(tasks):
    today = date.today().isoformat()
    for task in tasks:
        if task['status'] == 'Pending' and task['due_date'] < today:
            task['status'] = 'Overdue'
def sort_tasks(tasks):
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    return sorted(tasks, key=lambda t: (t['status'] != 'Overdue', priority_order[t['priority']]))            

@app.route('/')
def index():
    tasks = load_tasks()
    update_overdue(tasks)
    save_tasks(tasks)
    tasks = sort_tasks(tasks)
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = {
        'id': get_next_id(tasks),
        'title': request.form['title'],
        'description': request.form['description'],
        'due_date': request.form['due_date'],
        'priority': request.form['priority'],
        'status': 'Pending',
        'created_at': datetime.now().isoformat(),
        'completed_at': ''
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            task['completed_at'] = datetime.now().isoformat()
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/sort/priority')
def sort_by_priority():
    tasks = load_tasks()
    update_overdue(tasks)
    pending_tasks = [t for t in tasks if t['status'] != 'Completed']
    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
    sorted_tasks = sorted(pending_tasks, key=lambda x: priority_order[x['priority']])
    return render_template('index.html', tasks=sorted_tasks)


@app.route('/filter/<status>')
def filter_status(status):
    tasks = load_tasks()
    update_overdue(tasks)
    today = date.today()
    if status == "pending":
        filtered = [t for t in tasks if t['status'] == 'Pending']
    elif status == "completed":
        filtered = [t for t in tasks if t['status'] == 'Completed']
    elif status == "overdue":
        filtered = [t for t in tasks if t['status'] == 'Overdue']
    elif status == "today":
        filtered = [t for t in tasks if t['due_date'] == today.isoformat()]
    elif status == "tomorrow":
        tomorrow = (today + timedelta(days=1)).isoformat()
        filtered = [t for t in tasks if t['due_date'] == tomorrow]
    else:
        filtered = tasks
    return render_template('index.html', tasks=filtered)


if __name__ == '__main__':
    app.run(debug=True)