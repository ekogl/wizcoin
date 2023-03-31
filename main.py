print("hello, wizards", end="\n\n")


accounts = {
    "Harry": 4,
    "Hermione": 2,
    "Ron": 1
}

for name in accounts:
    print(f"balance for {name}: {accounts[name] * 10}")