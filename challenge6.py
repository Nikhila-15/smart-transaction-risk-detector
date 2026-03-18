n=int(input('enter number of transactions:'))
s=[0]*n
for i in range(n):
    s[i]=int(input())
print(s)
d={
    "normal":[],
    "large":[],
    "high risk":[],
    "invalid":[]
}
for i in range(n):
    if s[i]<=0:
        d["invalid"].append(s[i])
    elif s[i]>1 and s[i]<=500:
        d["normal"].append(s[i])
    elif s[i]>=501 and s[i]<=2000:
        d["large"].append(s[i])
    else:
        d["high risk"].append(s[i])

valid_transactions=[t for t in s if t>0 ]
print("valid transactions=",valid_transactions)

count=len(valid_transactions)
total=sum(valid_transactions)
summary = (total, count)

frequent=count>5
large_spending=total>5000
suspicious_spending=len(d["high risk"])>=3
if suspicious_spending and frequent and large_spending:
    risk = "high risk"
elif suspicious_spending or large_spending:
    risk = "moderate risk"
else:
    risk = "low risk"
print("\nFINANCIAL RISK REPORT:")
print("categorized transactions:", d)
print("transaction summary:", summary)
print("total transaction value:", total)
print("number of transactions:", count)
print("final risk classification:", risk)