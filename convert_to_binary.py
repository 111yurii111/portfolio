number = int(input("Number under 255: "))



No_of_places = 7
options = ["0", "0", "0" ,"0", "0", "0", "0", "0"]

#if the input == 256 the output should be 10000000 insted of 11111111
if number == 2 ** (No_of_places + 1):
    options[0] = '1'
    print(''.join(options))
    exit()

Loop_num = 0
for i in range(len(options)):
    if number <= 2 ** No_of_places:
        options[Loop_num] = "0"
    else:
        options[Loop_num] = "1"
        number -= 2 ** No_of_places

    Loop_num += 1
    No_of_places -= 1

print(''.join(options))
