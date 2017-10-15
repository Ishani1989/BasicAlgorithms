

class Solution(object):
    def reverse(self, x):
        l = len(str(x))
        j = 1
        while(j<l):
            q = x/10
            r = x%10
            x = q
            print r
            if(q<10):
                print q
            j = j + 1

if __name__ == '__main__':
    Solution().reverse(3456)

