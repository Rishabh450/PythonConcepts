def create(name: str, holder: str, account_holders: list = None):
    if account_holders is None:
        account_holders = []
    account_holders.append(holder)
    return {
        'name': name,
        'main_holder': holder,
        'accnt_holders': account_holders
    }


a1 = create('checking', 'Rolf')
a2 = create('checking', 'Jen')
print(a2)
# set omits repeated elements
a = set([1, 2, 3, 3, 3, 4, 4, 5])
# update method can append anything
a.update([10, "Sajal", 12, 12, "Rishabh", 13])
b = set()
b.add(10)
print("Sajal" in a)
print(a)
print(b.issubset(a))

# be careful with dictionaries, lists, sets userdefined objects
