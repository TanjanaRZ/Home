import csv

def load(lst):
    with open('users.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            lst.append(row)
    f.close()
    return 'Список загружен'
    
def save(users):
    if len(users) == 0:
        return 'Нечего сохранять'
    else:
        with open('users.csv', 'w') as f:
            writer = csv.writer(f, lineterminator="\r")
            for i in range(len(users)):
                
                writer.writerow(users[i])
        return 'Список сохранён'
        f.close()