
def crRow(user, i):
    row = str(i)+(' '*(3-len(str(i))))
    row += user[0]+(' '*(5-len(user[0])))
    row += user[1]+(' '*(10-len(user[1])))
    row += user[2]+(' '*(12-len(user[2])))
    row += user[3]+(' '*(10-len(user[3])))
    row += user[4]+(' '*(12-len(user[4])))
    row += user[5]+(' '*(16-len(user[5])))
    if len(user) == 7:
        row += user[6]+(' '*(16-len(user[6])))
    return row

    