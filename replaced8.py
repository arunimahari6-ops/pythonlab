def change_char(str1):
    char = str1[0]
    str1=str1.replace(char,"$")
    srt1=char+str1[1:]
    return srt1
print(change_char("restart"))