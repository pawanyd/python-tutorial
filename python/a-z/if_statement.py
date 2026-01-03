credit_score = False
bad_credit = True
amount = 1000000
if credit_score:
    downpayment = (10 / 100) * amount
    print("you need to make downpayment of 10% that is =>", downpayment)
elif bad_credit:
    downpayment = (20 / 100) * amount
    print("you need to make downpayment of 20% that is =>" , downpayment)