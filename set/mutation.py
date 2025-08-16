def mutate_string(string, position, character):
    string= s
    pos= int(i) 
    l = list(string)
    l[pos] = c
    string = "".join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

''' input would be first string like  abracadabra then the position and character like - 5,k'''
# another way to do this is
'''>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra'''