def longestCommonPrefix(strs):
    result = ""
    temp = ""
    if len(strs) == 1:
        return strs[0]
    if len(strs) > 1:
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in xrange(1, len(strs)):
                temp = ""
                if len(strs[j]) < 1:
                    return ""
                elif i >= len(strs[j]):
                    break
                elif strs[j][i] == letter:
                    #print "haha", j, i, letter, strs[j][i]
                    continue
                else:
                   temp=strs[0][0:i]
                result = result + temp
    return result


if __name__ == '__main__':
    strs = ["a", "a"]
    print longestCommonPrefix(strs)
