def anBisect(an):
    if ((an % 4 == 0 and an % 100 != 0)) or an % 400 == 0:
        return 1
    return 0

def validateInput(input):
    an = input[1] + input[2]
    luna = input[3] + input[4]
    zi = input[5] + input[6]
    judet = input[7] + input[8]

    if int(judet) == 47 or int(judet) == 48 or int(judet) == 49 or int(judet) == 50 or int(judet) < 1 or int(judet) > 52:
        return 0

    max_zile = 0

    if (int(luna) % 2 == 0):
        max_zile = 30
    else:
        max_zile = 31

    if int(luna) == 2:
        if anBisect(int(an)):
            max_zile = 28
        else:
            max_zile = 29

    if int(luna) > 12 or int(luna) == 0 or int(zi) > max_zile:
        print("CNP invalid\n")
        return 0
    return 1

cnp = input("Introduce-ti CNP-ul: ")

while (len(cnp) != 13 or validateInput(cnp) == 0):
    cnp = input("Introduce-ti CNP-ul: ")

validator = "279146358279"

sum = 0

cnp = list(cnp)
for i in range(0, len(cnp) - 1):
    sum += int(cnp[i]) * int(validator[i])

print(sum)
control_digit = sum % 11
if control_digit == 10:
    control_digit = 1

if control_digit == int(cnp[-1]):
    print("Valid cnp")
else:
    print("Invalid cnp")

print(control_digit)
