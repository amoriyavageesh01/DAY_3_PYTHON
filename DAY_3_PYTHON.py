# command to enter any word as per the interest of user
s=input('enter any word of your choice: ')
# initially dictionary is empty
d={}
for i in s:
    # command to store the word entered by the user in the dictionary
    d[i]=d.get(i,0)+1
print(d)
# command to extract the Key whose Value is maximum in the dictionary
max_key_value=max(d,key=d.get)
print(max_key_value)
