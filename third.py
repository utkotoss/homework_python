dictionary = {}

tasks_num = int(input())

for q in range(tasks_num) :
    task = input()
    temp_task = task.split()

    if (temp_task[0] == "ADD") :
        temp_task[1] = temp_task[1].lower()
        temp_task[2] = temp_task[2].lower()

        already_exist = False
        for syn1,syn2 in dictionary.items() :
            if (temp_task[1] == syn1 and temp_task[2] == syn2) or (temp_task[2] == syn1 and temp_task[1] == syn2) :
                already_exist = True
        if (already_exist == False) :
            dictionary[temp_task[1]] = temp_task[2]
        

    if (temp_task[0] == "COUNT") :
        temp_task[1] = temp_task[1].lower()
        counter = 0

        for syn1,syn2 in dictionary.items() :
            if (syn1 == temp_task[1]) or (syn2 == temp_task[1]) :
                counter += 1
        print(counter)

    if (temp_task[0] == "CHECK") :
        temp_task[1] = temp_task[1].lower()
        temp_task[2] = temp_task[2].lower()

        ans = False
        for syn1,syn2 in dictionary.items() :
            if (syn1 == temp_task[1] and syn2 == temp_task[2]) or (syn1 == temp_task[2] and syn2 == temp_task[1]) :
                ans = True
                break
        if (ans) :
            print("YES")
        else :
            print("NO")




