from Db_classes.companies import Companies
from Db_classes.projects import Projects
from Db_classes.tasks import Tasks
from Db_classes.time_entries import Time_entries
from Db_classes.users import Users
from os import getenv
from fastapi import FastAPI, Request
import psycopg2
import uvicorn

conn = psycopg2.connect(
                database='postgres',
                user='admin',
                password='admin',
                host='localhost',
                port=5432
            )

cursor = conn.cursor()

companies = Companies(cursor, conn)
projects = Projects(cursor, conn)
users = Users(cursor, conn)
tasks = Tasks(cursor, conn)
time_entries = Time_entries(cursor, conn)
app = FastAPI()

#Companies
@app.get("/get_companies/{id}")
async def get_companies(id):
    return companies.get_companies(id)

@app.post("/post_companies")
async def post_companies(info : Request):
    json = await info.json()
    companies.post_companies(json)

@app.post("/update_companies")
async def update_companies(info : Request):
    json = await info.json()
    companies.update_companies(json)
    
@app.delete("/delete_companies/{id}")
async def delete_companies(id):
    companies.delete_companies(id)

#Projects
@app.get("/get_projects/{id}")
async def get_projects(id):
    return projects.get_projects(id)

@app.post("/post_projects")
async def post_projects(info : Request):
    json = await info.json()
    projects.post_projects(json)

@app.post("/update_projects")
async def update_projects(info : Request):
    json = await info.json()
    projects.update_projects(json)
    
@app.delete("/delete_projects/{id}")
async def delete_projects(id):
    projects.delete_projects(id)

#Tasks
@app.get("/get_tasks/{id}")
async def get_tasks(id):
    return tasks.get_tasks(id)

@app.post("/post_tasks")
async def post_tasks(info : Request):
    json = await info.json()
    tasks.post_tasks(json)

@app.post("/update_tasks")
async def update_tasks(info : Request):
    json = await info.json()
    tasks.update_tasks(json)
    
@app.delete("/delete_tasks/{id}")
async def delete_tasks(id):
    tasks.delete_tasks(id)

#Time_entries
@app.get("/get_time_entries/{id}")
async def get_time_entries(id):
    return time_entries.get_time_entries(id)

@app.post("/post_time_entries")
async def post_time_entries(info : Request):
    json = await info.json()
    time_entries.post_time_entries(json)

@app.post("/update_time_entries")
async def update_time_entries(info : Request):
    json = await info.json()
    time_entries.update_time_entries(json)
    
@app.delete("/delete_time_entries/{id}")
async def delete_time_entries(id):
    time_entries.delete_time_entries(id)

#Users

@app.get("/get_users/{id}")
async def get_users(id):
    return users.get_users(id)

@app.post("/post_users")
async def post_users(info : Request):
    json = await info.json()
    users.post_users(json)

@app.post("/update_users")
async def update_users(info : Request):
    json = await info.json()
    users.update_users(json)
    
@app.delete("/delete_users/{id}")
async def delete_users(id):
    users.delete_users(id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)