import sys

if __name__ == '__main__':
    tel_num = sys.argv

    if tel_num[1].isdigit() and len(tel_num[1]) == 10:
        print('This telephone number is legit!')
    elif tel_num[1].isdigit() and len(tel_num[1]) != 10:
        print('This telephone number contains more or less than 10 digits')
    else:
        print('This telephone number contains letter, please repeat(')