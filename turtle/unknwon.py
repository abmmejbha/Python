import turtle as t

# screen settings
width, height = 1600, 900
screen = t.Screen()
s = screen
s.setup(width,height)
s.screensize(3 * width, 3 * height)
s.bgcolor('black')
s.delay(0)

# turtle settings
leo = t.Turtle()
leo.pensize(3)
leo.speed(0)
leo.color('orange')
# l-system settings

gens = 20
axiom ='A'
chr_1, rule_1 = 'A', 'AB'
chr_2, rule_2 = 'B', 'A'
step = 50 
angle = 60 

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else rule_2 for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


for gen in range(gens):
    t.pencolor('white')
    t.goto(-width // 2 + 60, -height // 2 + 60 )
    t.clear()
    t.write(f'generation: {gen}', font=("Arial", 60, "normal"))

    leo.setheading(0)
    leo.goto(0, 0)
    leo.clear()

    for chr in axiom:
        if chr == chr_1: 
            leo.left(60)
            leo.forward(step)
        elif chr == chr_2:
            leo.right(60)
            leo.forward(step)
    axiom = apply_rules(axiom)
    
t.Screen().exitonclick()