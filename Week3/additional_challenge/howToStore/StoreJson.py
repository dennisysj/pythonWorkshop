import json

tasks = ["buy milk", "study", "exercise"]

with open("tasks.json", "w") as file:
    json.dump(tasks, file)
