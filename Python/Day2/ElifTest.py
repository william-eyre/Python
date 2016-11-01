A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
def main():
    # Get a test score from the user
    score = int(input('Enter your test score:'))
    if score >= A_SCORE:
        print('Well done you clever cloggs you got an A ')
    elif score >= B_SCORE:
        print("Not bad, you're smart, but you're also not a nerd")
    elif score >= C_SCORE:
        print('Average')
    elif score >= D_SCORE:
        print('Nearly')
    else:
        print('you gon damn messed up')

main()
