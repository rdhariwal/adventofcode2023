from pathlib import Path

def compute(input = "input"):
    sum = 0
    p = Path(__file__).with_name(input)
    with p.open('r') as file_in:
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
    return sum

def enhanced_compute(input = "input"):
    sum = 0
    p = Path(__file__).with_name(input)
    with p.open('r') as file_in:
        for line in file_in:
            line = line.rstrip('\n')
            slength = len(line)
            # SET DEFAULT VALUES
            fd = "0"
            ld = "0"
            for i in range(slength):
                if line[i].isnumeric() and fd == "0":
                    fd = line[i]
                tld = line[slength - i - 1]
                if tld.isnumeric() and ld == "0":
                    ld = tld
                if fd != "0" and ld != "0":
                    break
            print(line)
            cal = fd+ld
            print(cal)
            cali = int(cal)
            sum = sum + cali
            print(sum)
    return sum