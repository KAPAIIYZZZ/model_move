class Field:
    def __init__(self):
        self.massive = []
    def render(self, size, character):
        self.massive = [[0] * size for i in range(size)]
        self.massive[character.point.x][character.point.y] = 1
        for i in range(0, len(self.massive)):
            for j in range(0, len(self.massive[i])):
                print(self.massive[i][j], end=' ')
            print()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Character:
    def __init__(self, point):
        self.point = point
    def move(self, direction, size):
        if direction == 'w':
            if self.point.x - 1 < 0:
                print('Игрок выходит за пределы поля')
            else:
                self.point.x -= 1
        elif direction == 'd':
            if self.point.y + 1 >= size:
                print('Игрок выходит за пределы поля')
            else:
                self.point.y += 1
        elif direction == 's':
            if self.point.x + 1 >= size:
                print('Игрок выходит за пределы поля')
            else:
               self.point.x += 1
        elif direction == 'a':
            if self.point.y - 1 < 0:
                print('Игрок выходит за пределы поля')
            else:
               self.point.y -= 1
        else:
            print('Неверная команда')
def main():
    size = int(input('Введите размер поля: '))
    field = Field()
    print('Введите координаты игрока')
    y = int(input('x: '))
    x = int(input('y: '))
    if x < 0 or y < 0 or x >=size or y >= size:
        print('Неверные координаты')
    else:
        character = Character(Point(x,y))
        field.render(size, character)
        while True:
            stop = input('Введите + если хотите передвинуть персонажа, - если хотите завершить ')
            if stop == '+':
                direction = input('Введите направление движения:\nw - вверх, d - вправо, s - вниз, a - влево\n')
                character.move(direction, size)
                field.render(size, character)
            elif stop == '-':
                break
            else:
                print('Erorr')
main()