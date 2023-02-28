def iteration(seed, iterations):
    for i in range(iterations):
        raisee=seed**3
        last_five = int(str(raisee)[-5:])
        seed=last_five
    print(last_five)

iteration(5245, 7037)