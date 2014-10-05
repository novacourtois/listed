import requests
from datetime import datetime
import psycopg2



hostname = 'http://localhost:5000'

def create_user(username, password):
	url = '/user'
	r = requests.post(url, auth=(username, password))

	print(r.json())
	return 'success'

def add_task(username, password, description, due_date, category, priority):
	url = '/tasks'
	payload = {'username':'', 'password':''}
	r = requests.post(url, auth=(username, password), data = payload)
	print(r.text)


def get_tasks(username, password):
	url = '/tasks'
	r = requests.post(url, auth=(username, password))
	return r.json()

def set_completed(username, password, task_id):
	pass

if __name__ == '__main__':
	create_user('novacourtois', 'thisisapass')
	add_task('novacourtois','thisisapass', 'do work', datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'school', 5 )
	tasks = get_tasks('novacourtois','thisisapass')
	for task in tasks:
		print(task['description'])
