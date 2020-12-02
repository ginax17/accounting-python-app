import sys


from user.authentication import authenticate_user
from transactions.journal import receive_income, pay_expense
import banking
# from banking import reconciliation
# from banking.fvb import reconciliation as newfvb
# from banking.ubsa import reconciliation as newubsa
# from banking.online import reconciliation as newonline


# newfvb.do_reconciliation()
# newubsa.do_reconciliation()
# newonline.do_reconciliation()


if __name__ == "__main__":
    #help("modules")
    if len(sys.argv) > 1:
        i = 1
        for b in range(len(sys.argv)-1):
            print(sys.argv[i])
            i += 1

authenticate_user()
receive_income(float(100))
pay_expense(float(100))

banking.reconciliation.do_reconciliation()



