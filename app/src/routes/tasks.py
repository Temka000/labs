# app/src/routes/tasks.py
from flask import Blueprint, request, jsonify
from utils import execute_query
from models import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    rows = execute_query('SELECT id, title, description, priority, status FROM tasks;', fetch_all=True)
    tasks = [Task.from_db_row(row).to_dict() for row in rows]
    return jsonify(tasks)

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    row = execute_query('SELECT id, title, description, priority, status FROM tasks WHERE id = %s;', 
                        (task_id,), fetch_one=True)
    if row:
        return jsonify(Task.from_db_row(row).to_dict())
    return jsonify({'error': 'Task not found'}), 404

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    task_id = execute_query(
        'INSERT INTO tasks (title, description, priority, status) VALUES (%s, %s, %s, %s) RETURNING id;',
        (data['title'], data.get('description', ''), data.get('priority', 'medium'), data.get('status', 'pending')),
        fetch_one=True
    )[0]
    return jsonify({'id': task_id, 'message': 'Task created'}), 201

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    execute_query(
        'UPDATE tasks SET title = %s, description = %s, priority = %s, status = %s WHERE id = %s;',
        (data['title'], data.get('description', ''), data.get('priority', 'medium'), data.get('status', 'pending'), task_id)
    )
    return jsonify({'message': 'Task updated'})

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    execute_query('DELETE FROM tasks WHERE id = %s;', (task_id,))
    return jsonify({'message': 'Task deleted'})
