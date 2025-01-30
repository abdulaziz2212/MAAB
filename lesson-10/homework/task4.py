import json
import csv

def load_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)
    
def json_to_csv(tasks):
    with open('tasks.csv', 'w',newline='') as file:
        fieldnames=['id','task','completed','priority']
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(tasks)

    print(f"JSON data has been successfully converted to tasks.csv")

tasks= load_json('tasks.json')
json_to_csv(tasks)