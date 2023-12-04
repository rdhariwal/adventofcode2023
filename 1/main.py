sum = 0
with open("/Users/rd/code/adventofcode2023/1/input") as file_in:
    for line in file_in:
        line = line.rstrip('\n')
        slength = len(line)
        # SET DEFAULT VALUES
        fd = ""
        ld = ""
        for i in range(slength):
            if line[i].isnumeric() and fd == "":
                fd = line[i]
            tld = line[slength - i - 1]
            if tld.isnumeric() and ld == "":
                ld = tld
            if fd != "" and ld != "":
                break
        print(line)
        cal = fd+ld
        print(cal)
        cali = int(cal)
        sum = sum + cali
        print(sum)