#     if x == "q" or "Q":
#         break
    # balcon.exe -n "Microsoft David Desktop" -t "hello there"
# print(cmd)

import os
print("Wellcome to Text To Speech ")
print('if want to quit type "q"')
while True:
    x = input("Enter text to convert into speech: ")
    if x == "q":
        break
    cmd= "balcon.exe -n" +" "+ '"Microsoft David Desktop"'+" "+f'-t "{x}"'
    os.system(cmd)
