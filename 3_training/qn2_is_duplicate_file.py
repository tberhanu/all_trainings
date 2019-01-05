#!/usr/bin/evn python3

def give_duplicated_files(files):
    s = set()
    for file1 in files:
        for file2 in files:
            if file1 != file2 and is_duplicated(file1, file2) and (file2, file1) not in s:
                s.add((file1, file2))
                break

    return list(s)
def is_duplicated(file1, file2):
    with open(file1, 'r') as rf1:
        with open(file2, 'r') as rf2:
            for line1, line2 in zip(rf1, rf2):
                if line1 != line2:
                    return False

            return True



if __name__ == "__main__":
    print(give_duplicated_files(["file.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt"]))