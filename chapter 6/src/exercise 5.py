str = "X-DSPAM-Confidence: 0.8475 "
x = str.find(":")
y = str[x+1:]
print(y)
y = float(y)
y+=1
print(y)

