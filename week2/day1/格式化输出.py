#__author:iruyi
#date:2018/9/11

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

if salary.isdigit():
    salary = int(salary)
else:
    exit("salary must be digit.")

msg = '''
------------------format---------------
name:%s
age:%s
job:%s
salary:%f
------------------end------------------
''' % (name,age,job,salary)

print(msg)