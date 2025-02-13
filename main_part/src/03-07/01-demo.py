# 占位符
sName = "Mary"
fPrice = 125.75
n = 5
sText = "%s has %d lambs, each lamb worth $%.2f. So, these lambs worth $%.1f in total." % (sName, n, fPrice, n * fPrice)
print(sText)