def palindrome(x):
    data = str(x)
    print data

    i = 0
    j = len(data)-1
    print '-------------'

    ret = True
    while i<j:
        if data[i] != data[j]:
            ret = False
            print data[i], data[j]
            break
        i=i+1
        j=j-1
    return ret

if __name__ == '__main__':
    print palindrome(123211)
