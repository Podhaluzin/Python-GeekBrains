with open('file_6.txt', 'r', encoding='utf-8') as f:
    dict_subjects = {}
    for line in f:
        list_subjects = line.split(' ')
        sum_lessons = 0
        for lessons in list_subjects[1:]:
            for i in range(len(lessons)):
                if lessons[:-i].isdigit():
                    sum_lessons += int(lessons[:-i])
                    break
            dict_subjects.update({list_subjects[0][0: -1]: sum_lessons})
print(dict_subjects)
