import csv
with  open('D:\GajulaPavanKumar\devops_projects_2024\PythonProgrammers\Projects\sample.csv',mode='r') as file:
    csvfile = csv.reader(file)

    for lines in csvfile:
        print(lines)