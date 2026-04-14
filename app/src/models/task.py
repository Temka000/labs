# app/src/models/task.py
class Task:
    def __init__(self, id=None, title=None, description=None, priority=None, status=None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status
        }

    @staticmethod
    def from_db_row(row):
        return Task(id=row[0], title=row[1], description=row[2], priority=row[3], status=row[4])
