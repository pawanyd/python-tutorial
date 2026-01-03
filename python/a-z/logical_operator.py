good_credit_score = True
has_creminal_record = True

if good_credit_score and not has_creminal_record:
    print(f"you are elegiable for loan")
elif good_credit_score and has_creminal_record:
    print("your are not elegiable for not")


# comparition operators 

tempature = 20
if tempature >= 30:
    print("day is hot")
elif tempature < 30:
    print("Day is cold")
