def hitung_bobot_konsonan(string):
    vowel=('a','i','u','e','o')
    tot=0
    for i in range(0,len(string)):
        if string[i].lower() not in vowel and string[i].isalpha():
            tot+=ord(string[i].lower())-96
    return tot
