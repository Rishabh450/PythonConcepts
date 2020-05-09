accounts = {
    'current': 1958.00,
    'saving': 15
}


# default args must follow non default values
def add_roll(amount: float, name: str = 'current') -> float:
    accounts[name] += amount
    return accounts[name]


print(add_roll(1000.00, 'saving'), 'saving', 'here')
