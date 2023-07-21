from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('htask.html')
cont = "Домашнее задание выполнено!!!"
msg = tm.render(foot=cont)
print(msg)
