import os

def count_occ(lst1:list,target):
    if len(lst1) == 0:
        return 0
    plus1 = 0
    if lst1[0] == target:
        plus1 = 1

    return plus1 + count_occ(lst1[1:],target)
#print(count_occ([1,2,9,4,9,6,7,8,9],9))

def arrange(path, entries):
    # arrange folder last and ignore folders starts with .
    entry_list = []
    for entry in entries:
        if os.path.isdir(os.path.join(path, entry)):
            if entry[0] != '.':
                entry_list.append(entry)
        else:
            entry_list.insert(0, entry)

    return entry_list

def list_and_size(path, indent):
    print(' ' * indent, f"{path}")

    entries = os.listdir(path)

    entry_list = arrange(path, entries)

    for entry in entry_list:
        if os.path.isdir(os.path.join(path, entry)):
            print(' ' * (indent + 4) + f"[{entry}]")
            full_path = os.path.join(path, entry)
            list_and_size(full_path, indent + 4) # The path of the current dir

        else:
            print(' ' * (indent + 4) + entry) # Print the files

list_and_size(r'C:\Users\User\Desktop\Study_Pro\General_Projects_git', 0)