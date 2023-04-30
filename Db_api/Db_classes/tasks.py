import psycopg2
import datetime

class Tasks:

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def get_tasks(self, id):

        self.cursor.execute(f"""
        select *
        from tasks
        where task_id = {id}
        """)

        data = self.cursor.fetchall()
        return data

    def delete_tasks(self, id):
        self.cursor.execute(f"""
        delete
        from tasks
        where task_id = {id}
        """)

    def post_tasks(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        insert into tasks (task_id, task_name, task_project, task_user, task_priority, task_deadline, _created_at, _updated_at)
        values (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (  
         json_data.get("task_id"),
         json_data.get("task_name"),
         json_data.get("task_project"),
         json_data.get("task_user"),
         json_data.get("task_priority"),
         json_data.get("task_deadline"), 
         now,
         now))
        
        self.conn.commit()

    
    def update_tasks(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        update tasks set
        task_name = '{json_data.get("task_name")}',
        task_project = '{json_data.get("task_project")}',
        task_user = '{json_data.get("task_user")}',
        task_priority = '{json_data.get("task_priority")}',
        task_deadline = '{json_data.get("task_deadline")}', 
        _updated_at = '{now}'
        where
        task_id = {json_data.get("task_id")}
        """)
        
        self.conn.commit()
        