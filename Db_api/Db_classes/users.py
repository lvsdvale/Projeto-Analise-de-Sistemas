import psycopg2
import datetime

class Users:

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def get_users(self, id):

        self.cursor.execute(f"""
        select *
        from users
        where user_id = {id}
        """)

        data = self.cursor.fetchall()
        return data

    def delete_users(self, id):
        self.cursor.execute(f"""
        delete
        from users
        where user_id = {id}
        """)

    def post_users(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        insert into users (user_id, user_email, user_password, user_name, user_company_id, user_adm, user_type, _created_at, _updated_at)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (  
         json_data.get("user_id"),
         json_data.get("user_email"),
         json_data.get("user_password"),
         json_data.get("user_name"),
         json_data.get("user_company_id"),
         json_data.get("user_adm"), 
         json_data.get("user_type"), 
         now,
         now))
        
        self.conn.commit()

    
    def update_users(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        update users set
        user_email = '{json_data.get("user_email")}',
        user_password = '{json_data.get("user_password")}',
        user_name = '{json_data.get("user_name")}',
        user_company_id = '{json_data.get("user_company_id")}',
        user_adm = '{json_data.get("user_adm")}', 
        user_type = '{json_data.get("user_type")}', 
        _updated_at = '{now}'
        where
        user_id = {json_data.get("user_id")}
        """)
        
        self.conn.commit()
        