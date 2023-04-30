import psycopg2
import datetime

class Companies:

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def get_companies(self, id):

        self.cursor.execute(f"""
        select *
        from companies
        where company_id = {id}
        """)

        data = self.cursor.fetchall()
        return data

    def delete_companies(self, id):
        self.cursor.execute(f"""
        delete
        from companies
        where company_id = {id}
        """)

    def post_companies(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        insert into companies (company_id, company_name, company_city, company_state, company_email, created_by_user,  _created_at, _updated_at)
        values (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (  
         json_data.get("company_id"),
         json_data.get("company_name"),
         json_data.get("company_city"),
         json_data.get("company_state"),
         json_data.get("company_email"),
         json_data.get("created_by_user"), 
         now,
         now))
        
        self.conn.commit()

    
    def update_companies(self, json_data):
        now = datetime.datetime.now()
        self.cursor.execute(f"""
        update companies set
        company_name = '{json_data.get("company_name")}',
        company_city = '{json_data.get("company_city")}',
        company_state = '{json_data.get("company_state")}',
        company_email = '{json_data.get("company_email")}',
        created_by_user = {json_data.get("created_by_user")}, 
        _updated_at = '{now}'
        where
        company_id = {json_data.get("company_id")}
        """)
        
        self.conn.commit()
        