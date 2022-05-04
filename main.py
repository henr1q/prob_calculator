import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, ball in balls.items():
            self.contents.extend([color] * ball)

        # print(self.contents)

    def draw(self, draw_ball):
        drawed = []
        if draw_ball < len(self.contents):
            draw = random.sample(self.contents, draw_ball)
            for i in draw:
                self.contents.pop()
                drawed.append(i)
        else:
            drawed = self.contents

        return drawed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    cases = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        balls_exp = sum([1 for color, ball in expected_balls.items() if balls_drawn.count(color) >= ball])

        cases += 1 if balls_exp == len(expected_balls) else 0


    chance = cases / num_experiments
    return print(chance)


hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=10, num_experiments=2000)

