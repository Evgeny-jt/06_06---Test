def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм

def solution(a, b, c):
    minus = -1
    discriminant = b**2-4*a*c
    # функция для нахождения корней уравнения
    if discriminant < 0:
        return 'корней нет'
    elif discriminant == 0:
        answer = (-1*b)/(2*a)
        return answer
    else:
        answer1 = (-1*b+discriminant**0.5)/2*a
        answer2 = (-1*b-discriminant**0.5)/2*a
        return answer1, answer2

if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))