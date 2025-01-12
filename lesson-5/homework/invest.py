def invest(amount, rate, years):
    print(rate)
    for i in range(1,years+1):
        amount*=1+rate
        print(f"year {i}: ${round(amount,2)}")
amount=float(input('Enter the initial amount: '))
rate=float(input("Enter the annual rate: "))
years=int(input('Enter the period: '))

invest(amount,rate,years)