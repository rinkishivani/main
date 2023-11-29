people = [[1, 'rinki', 'F', 23], [2, 'yash', 'M', 19]]


def show_person():
    ''' show person's data '''
    for i in range(len(people)):
        srno = people[i][0]
        name = people[i][1]
        gender = people[i][2]
        print('Sr No.: ', srno, ' Name: ', name, ' Gender: ', gender, '\n')


def age_filter():
    ''' filter age '''
    for i in range(len(people)):
        if people[i][3] < 20:
            srno = people[i][0]
            name = people[i][1]
            gender = people[i][2]
            print('Sr No.: ', srno, ' Name: ', name, ' Gender: ', gender, '\n')


show_person()
age_filter()
# print(len(people))
