def vote(votes):
    # your code
    quantity = set(votes)
    max = 0
    number = None
    for q in quantity:
        repetition = 0
        for i in votes:
            if q == i:
                repetition += 1
        if repetition > max:
            max = repetition
            number = q
    return number


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))