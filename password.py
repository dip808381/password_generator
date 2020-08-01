dic1 = {'a': '@','b': 'B','c': 'C','d': 'D','e': '3','f': 'F','g': 'G','h': '#','i': '!','j': 'J','k': 'K','l': 'L','m': 'M','n': 'N','o': 'O','p': 'P','q': 'Q','r': 'R','s': '$','t': 'T','u': 'U','v': 'V','w': 'W','x': 'X','y': 'Y','z': 'Z'}
def pwrd(inp):
    #inp = input('Enter Your Password Hint:') 
    lis = []
    for i in inp:
        if i == ' ':continue
        if i not in dic1:
            dic1[i]=i
        lis.append(dic1[i.lower()])
    org = "".join(lis)
    return org
if __name__ == "__main__":
    print(pwrd('dipesh@1234'))
