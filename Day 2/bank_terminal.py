'''
gaakete banki functiebis mixedvit
sadac shegedzleba sheitano tanxa gamoitano tanxa da naxo sakutari angarishi
'''

balance = 30

term_menu = int(input("romeli operaciis shesruleba gsurt '\n'balansis shesamowmeblad airchiet 1 \ntanxis shesatanad airchiet 2 \ntanxis gasatanad airchiet 3 \n"))

def inputt():
    global balance
    inp = int(input("Sheitanet tanxa: "))
    print(balance + inp)

def out():
    global balance
    out = int(input("chaweret tanxis raodenoba: "))
    if out > balance:
        print("balansze arasakmarisi tanxaa")
    else:
        print("miiget tanxa: ",out, "\n" "balansi: ", balance - out)    



if term_menu == 1:
    print(balance)
    
elif term_menu == 2:
    inputt()
    
elif term_menu == 3:
    out()