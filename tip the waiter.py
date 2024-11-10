def calculatetotbill(billamo, tipper) :
    #calculate the total bill amount to pay
    total=billamo + (billamo * 0.01 * tipper)
    total=round(total, 2)
    print(f"please pay ${total} because this is a very fancy hotel :)")

calculatetotbill(500, 20)