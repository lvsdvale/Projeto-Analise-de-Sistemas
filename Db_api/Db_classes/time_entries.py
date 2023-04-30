import psycopg2
import datetime

class Time_entries:

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def get_time_entries(self, id):

        self.cursor.execute(f"""
        select *
        from time_entries
        where time_entrie_id = {id}
        """)

        data = self.cursor.fetchall()
        return data

    def delete_time_entries(self, id):
        self.cursor.execute(f"""
        delete
        from time_entries
        where time_entrie_id = {id}
        """)

    def post_time_entries(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        insert into time_entries (time_entrie_id, time_entrie_user, time_entrie_start, time_entrie_duration, time_entrie_task, _created_at, _updated_at)
        values (%s, %s, %s, %s, %s, %s, %s)
        """,
        (  
         json_data.get("time_entrie_id"),
         json_data.get("time_entrie_user"),
         json_data.get("time_entrie_start"),
         json_data.get("time_entrie_duration"),
         json_data.get("time_entrie_task"),
         now,
         now))
        
        self.conn.commit()

    
    def update_time_entries(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        update time_entries set
        time_entrie_user = '{json_data.get("time_entrie_user")}',
        time_entrie_start = '{json_data.get("time_entrie_start")}',
        time_entrie_duration = '{json_data.get("time_entrie_duration")}',
        time_entrie_task = '{json_data.get("time_entrie_task")}',
        _updated_at = '{now}'
        where
        time_entrie_id = {json_data.get("time_entrie_id")}
        """)
        
        self.conn.commit()
        