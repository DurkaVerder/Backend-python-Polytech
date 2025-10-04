import random
import math
from module6 import math_stats_on_prices
from module7 import create_product, OrderItem


def pick_random_products(seed: int, pool: list[tuple[int,str,str]], k: int) -> list[OrderItem]:
    random.seed(seed)
    chosen = random.sample(pool, k)
    return [OrderItem(create_product(pid, name, price_s), 1) for pid, name, price_s in chosen]


def random_choice_and_randint_example(items: list) -> tuple:
    a = random.choice(items)
    b = random.randint(1, 10)
    return a, b


def math_compute_discount(price: float, percent: float) -> float:
    return price - math.floor(price * percent / 100)