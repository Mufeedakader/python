def check_password():
    password=input('enter your paasword')
    lowercount,uppercount,digitcount,specialkey=0,0,0,0
    if len(password)>=8:
        for letter in password:
            # print(letter)
            if letter.islower():
                lowercount+=1
            elif letter.isupper():
                uppercount+=1
            elif letter.isdigit():
                digitcount+=1
            elif letter in ["@","#","$"]:
                specialkey+=1
        if lowercount>=1 and uppercount>=1 and digitcount>=1 and specialkey>=1:
            print('valid password')
    else:
        print("password is invalid")
check_password()