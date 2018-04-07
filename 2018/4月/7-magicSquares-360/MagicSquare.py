#!/usr/bin/env python3
# coding=utf8


def check_rows(Squares):

    sum_ = sum(Squares[0])
    for row in Squares[1:]:
        temp = sum(row)
        if sum_ != temp:
            return 0, sum_

    return 1, sum_


def check_cols(Squares):

    leng = len(Squares)

    col = []
    for i in range(leng):
        col.append(Squares[i][0])
    sum_ = sum(col)

    for i in range(leng-1):

        col = []

        for row in Squares:
            col.append(row[i+1])
        temp = sum(col)

        if sum_ != temp:
            return 0, sum_

    return 1, sum_


def check_diag(Squares):

    leng = len(Squares)

    d = []
    for i in range(leng):
        d.append(Squares[i][i])
    sum_ = sum(d)

    temp = []
    for i in range(leng):
        temp.append(Squares[i][leng-1-i])

    if sum_ != sum(temp):
        return 0, sum_

    return 1, sum_


def check(Squares):

    check_r = check_rows(Squares)
    check_c = check_cols(Squares)
    check_d = check_diag(Squares)

    if check_r[0] == 0 or check_c[0] == 0 or check_d[0] == 0:
        return 0

    if check_d[1] != check_r[1] != check_c[1]:
        return 0

    return 1


def isMagic(name1, name2):

    file_in = open(name1, 'r')
    file_out = open(name2, 'w')

    num = file_in.readline()
    file_out.writelines(num+'\n')

    num = int(num.strip())

    while num > 0:

        N = file_in.readline().strip()
        while N is '':
            N = file_in.readline().strip()
        N = int(N)

        Squares = []
        for i in range(N):
            temp = file_in.readline().strip().split()
            temp_int = [int(x) for x in temp]
            Squares.append(temp_int)

        flg = check(Squares)

        if flg == 0:
            file_out.writelines(str(N) + ' invalid\n')
            print('invliad')
        else:
            file_out.writelines(str(N) + ' valid\n')
            print('valid')

        for line in Squares:
            str_ = '  '.join([str(x).rjust(len(str(N*N)), ' ') for x in line])
            file_out.writelines(str_+'\n')
        file_out.writelines('\n')

        num -= 1


def main():

    name1 = input("Enter name of input file:")
    name2 = input("Enter name of output file:")
    if name1 == name2:
        print("The names are the same")
    else:
        isMagic(name1, name2)
        print("The output has been written to results.txt")


if __name__ == "__main__":
    main()








