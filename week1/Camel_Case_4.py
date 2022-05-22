import re


def split(splitstring):
    splitedList = re.split('(?=[A-Z])', splitstring)
    listToStr = ' '.join([str(elem).lower() for elem in splitedList if elem])
    return listToStr


def combine(splitstring):
    splitedList = splitstring.split()
    listToStr = ''.join([str(elem).capitalize()
                        for elem in splitedList if elem])
    return listToStr


def camelCase(s):
    # s = str
    output = ''
    splitedString = s.split(";")

    if s[0] == 'S':
        if splitedString[1] == 'M':
            output = split(splitedString[2][:-2])

        elif splitedString[1] == 'C' or splitedString[1] == 'V':
            output = split(splitedString[2])

    elif s[0] == 'C':
        if splitedString[1] == 'M':
            temp = combine(splitedString[2])
            if len(temp) >= 2:
                output = temp[0].lower() + temp[1:]+'()'
            else:
                output = temp+'()'

        elif splitedString[1] == 'C':
            output = combine(splitedString[2])

        elif splitedString[1] == 'V':
            temp = combine(splitedString[2])
            if len(temp) >= 2:
                output = temp[0].lower() + temp[1:]

    return print(output)


if __name__ == '__main__':

    while True:
        try:
            s = input().rstrip()
            camelCase(s)

        except EOFError:
            break
