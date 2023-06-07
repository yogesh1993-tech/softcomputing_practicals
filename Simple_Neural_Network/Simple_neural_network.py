
x = float(input("Enter value of x: "))
w = float(input("Enter value of Weight (w): "))
b = float(input("Enter value of bias (b): "))

net = float(w*x + b)

if net<0:
        out = 0

elif 0 <= net <= 1:
        out = net
else:
        out=1

print(f'Net	: {net}')
print(f'Output : {out}')

