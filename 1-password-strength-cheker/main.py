# password should be 8 digit - done
# one capital lettar -done
# must include minimum 1 number - done
# must include @#$^&*! - done

password = input("Enter password: ")
special_chars = "@#$^&*!"

if len(password) < 8:
    print("weak password")
    print("tip to improve:- Make it of 8 charectors")
elif not any(char.isupper() for char in password):
    print("weak password")
    print("tip to improve:- add atleast 1 uppercase letter")
elif not any(digi.isdigit() for digi in password):
    print("weak password")
    print("tip to improve:- add atleast 1 digit")
elif not any(special in special_chars for special in password):
    print("weak password")
    print("tip to improve:-add special charectors such as @#$^&*!")
else:
    print("strong password")