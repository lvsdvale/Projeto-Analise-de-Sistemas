import psycopg2
import datetime

class Projects:

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def get_projects(self, id):

        self.cursor.execute(f"""
        select *
        from projects
        where project_id = {id}
        """)

        data = self.cursor.fetchall()
        return data

    def delete_projects(self, id):
        self.cursor.execute(f"""
        delete
        from projects
        where project_id = {id}
        """)

    def post_projects(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        insert into projects (project_id, project_name, project_owner, project_deadline, _created_at, _updated_at)
        values (%s, %s, %s, %s, %s, %s)
        """,
        (  
         json_data.get("project_id"),
         json_data.get("project_name"),
         json_data.get("project_owner"),
         json_data.get("project_deadline"),
         now,
         now))
        
        self.conn.commit()

    
    def update_projects(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        update projects set
        project_name = '{json_data.get("project_name")}',
        project_owner = '{json_data.get("project_owner")}',
        project_deadline = '{json_data.get("project_deadline")}',
        _updated_at = '{now}'
        where
        project_id = {json_data.get("project_id")}
        """)
        
        self.conn.commit()
        