import os

def arrange(path, entries)->list:
    # arrange folder last and ignot folder starts with .
    entry_list = []
    for entry in entries:
        if os.path.isdir(os.path.join(path, entry)):
            if entry[0] != '.':
                entry_list.append(entry)
        else:
            entry_list.insert(0, entry)

    return entry_list

def find_the_file(path, filename):
    entries = os.listdir(path)

    entry_list = arrange(path, entries)

    for entry in entry_list:
        if entry == filename:
            full_path = os.path.join(path, entry)
            return f"True, Full Path : {full_path.replace("C:\\","-> ")}"


        if os.path.isdir(os.path.join(path, entry)):
            full_path = os.path.join(path, entry)
            return find_the_file(full_path,filename)

    return "False,File not found"

# change to folder on your computer
print(find_the_file(r"C:\Users\User\Desktop\Study_Pro\General_Projects_git", '02_webhook_few_q.py'))







