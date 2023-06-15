def func(s):
    s.replace(" ","")
    s = ''.join(letter for letter in s if letter.isalnum())
    s = s.lower()
    # print(s)
    return s == s[::-1]
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
    
    
string = "Ga*'riMa"
string[::-1]
print(string[::-1])