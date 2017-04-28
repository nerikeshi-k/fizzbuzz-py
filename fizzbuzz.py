# python3

print("\n".join(["fizz"+(lambda x:" buzz"if not x%5 else"")(x)if not x%3 else"buzz"if not x%5 else str(x)for x in range(1,int(input()))]))
