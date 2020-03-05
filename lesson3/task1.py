import sys

if __name__ == '__main__':
    sample_str = sys.argv
    if len(sample_str[1]) > 2:
        print(sample_str[1][:2] + sample_str[1][-2:])
    if len(sample_str[1]) == 2:
        print(sample_str[1][:2] + sample_str[1][-2:])
    if len(sample_str[1]) < 2:
        print('EMPTY STRING')
