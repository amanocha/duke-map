import server

db = server.get_db()

def write_project_info(username, name, introduction, department, topic, course, collaborators, keywords):
    user = db.users.find({"username": username})