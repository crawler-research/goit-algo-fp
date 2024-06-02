import turtle

def draw_tree(t, branch_len, angle, level):
    if level > 0:
        t.forward(branch_len)
        t.left(angle)
        draw_tree(t, branch_len - 15, angle, level - 1)
        t.right(2 * angle)
        draw_tree(t, branch_len - 15, angle, level - 1)
        t.left(angle)
        t.backward(branch_len)

def main(level):
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_tree(t, 100, 30, level)

if __name__ == "__main__":
    level = int(input("Вкажіть рівень рекурсії: "))
    main(level)