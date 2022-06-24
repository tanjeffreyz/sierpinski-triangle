import math
import random
from matplotlib import pyplot as plt


def plot_point(x, y):
    plt.plot(x, y, color='blue', linestyle=None, marker='.', markersize=1)


STYLE = 'g.'
WIDTH = 1
HEIGHT = WIDTH * math.sqrt(3) / 2
ANCHORS = [
    (0, 0),
    (WIDTH, 0),
    (WIDTH / 2, HEIGHT)
]

padding = 0.1
additional_height_padding = (WIDTH - HEIGHT) / 2
plt.xlim(-padding, WIDTH + padding)
plt.ylim(
    -padding - additional_height_padding,
    HEIGHT + additional_height_padding + padding
)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

for anchor in ANCHORS:
    plot_point(anchor[0], anchor[1])

# Pick a random starting point within the outer triangle,
# but either inside or outside the center inner triangle
MODE = 'in'
assert MODE in {'in', 'out'}

if MODE == 'in':
    # Linearly more chance near top of inner triangle (b/c it's upside-down)
    start_y = random.triangular(0, HEIGHT / 2, HEIGHT / 2)
    inner_width = WIDTH * start_y / HEIGHT
    start_x = random.uniform(
        (WIDTH - inner_width) / 2,
        (WIDTH + inner_width) / 2
    )
else:
    top_half = random.uniform(0, 1) < 1 / 3     # 2x valid area in bottom half than top half
    if top_half:
        # Linearly more chance near bottom (0) of top-most inner triangle
        start_y = random.triangular(HEIGHT / 2, HEIGHT, HEIGHT / 2)
        outer_width = (HEIGHT - start_y) / HEIGHT * WIDTH
        # Width of horizontal cross-section of outer triangle at height START_Y
        start_x = random.uniform(
            (WIDTH - outer_width) / 2,
            (WIDTH + outer_width) / 2
        )
    else:
        start_y = random.triangular(0, HEIGHT / 2, 0)
        outer_width = (HEIGHT - start_y) / HEIGHT * WIDTH
        delta_width = (WIDTH - outer_width) / 2
        start_x = random.choice([
            random.uniform(
                delta_width,
                outer_width / 2
            ),
            random.uniform(
                WIDTH - outer_width / 2,
                WIDTH - delta_width
            )
        ])
plot_point(start_x, start_y)
point = (start_x, start_y)

# Start drawing the Sierpinski triangle
for _ in range(25_000):
    selected_anchor = random.choice(ANCHORS)
    new_x = (point[0] + selected_anchor[0]) / 2
    new_y = (point[1] + selected_anchor[1]) / 2
    plot_point(new_x, new_y)
    point = (new_x, new_y)

plt.savefig('output', dpi=200)
plt.show()
