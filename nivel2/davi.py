n1= int(input())
str1 = input()
n2= int(input())
str2 = input()

minimo = len(min(str1,str2))
prefixo = 0
for i in range(minimo):
    if str1[i] == str2[i]:
        prefixo+=1
    else:
        break
print(prefixo)