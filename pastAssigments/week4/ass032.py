hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
   h = float(hrs)
   r = float(rate)
except:
    print("Error")
    quit()
if h > 40:
  overTime = h - 40
  overTimePay= overTime * (r*1.5)
  grossPay= (r*40) + overTimePay
else:
	grossPay= r * h
print(grossPay)
