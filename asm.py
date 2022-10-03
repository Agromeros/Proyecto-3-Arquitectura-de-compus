"""instr = {'MOV': 
{'AB': 0000000},
{'BA'}}"""


def ReadAsmy():
    file_name = "assembly.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()
    l_lines_str = []
    code_lines = []
    for i in range(len(lines)):
        l = lines[i].strip()  # .split()
        # for j in range(len(l)):
        #   l[j] = int(l[j])
        l_lines_str.append(l)
    if 'CODE:' in l_lines_str:
        for i in range(l_lines_str.index('CODE:'), len(l_lines_str), 1):
            code_lines.append(l_lines_str[i])
    # print(l_lines_str)
    return code_lines


ReadAsmy()


def AsmyVerification():
    pass
