first_name = input("first :")
last_name =  input("last :")
count = len(first_name+ last_name)
initials = first_name[0]+last_name[0]
doublefirstname= first_name[0]*2+first_name[1]*2+first_name[2]*2 + first_name[3]*2 + first_name[4]*2+first_name[5]*2
spelledbackward=last_name[9]+last_name[8]+last_name[7]+last_name[6]+last_name[5]+last_name[4]+last_name[3]+last_name[2]+last_name[1]
print (f"Hello {last_name},{first_name} ! Your name has {count} letters, and your initials are {initials}. {doublefirstname} is repeated, your name spelled backward is {spelledbackward}")
