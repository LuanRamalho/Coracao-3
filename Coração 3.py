import turtle
import random

def draw_heart(x, y, size, color):
    """Desenha um coração em uma posição específica."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size * 0.4, 180)
    turtle.right(90)
    turtle.circle(size * 0.4, 180)
    turtle.forward(size)
    turtle.left(130)  # Volta à posição inicial

    turtle.end_fill()

def random_color():
    """Gera uma cor aleatória no formato hexadecimal."""
    return random.choice(["red", "pink", "blue", "purple", "orange", "yellow", "green"])

def main():
    """Função principal que desenha corações aleatórios."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Corações Aleatórios")

    turtle.speed(0)
    turtle.hideturtle()

    # Gera uma quantidade aleatória de corações
    number_of_hearts = random.randint(5, 20)

    for _ in range(number_of_hearts):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        size = random.randint(20, 50)
        color = random_color()
        draw_heart(x, y, size, color)

    # Aguarda o usuário fechar a janela
    screen.mainloop()

if __name__ == "__main__":
    main()
