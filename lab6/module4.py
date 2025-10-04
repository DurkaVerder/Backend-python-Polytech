from module5 import pick_random_products
from decimal import Decimal, getcontext
import random



def assemble_cart(seed: int) -> list:
    pool = [
    (1, 'Кофе', '3.50'),
    (2, 'Чай', '2.25'),
    (3, 'Булочка', '1.10'),
    (4, 'Молоко', '1.80'),
    ]
    return pick_random_products(seed, pool, 3)



def decimal_average_prices(items: list) -> Decimal:
    getcontext().prec = 10
    s = sum((it.product.price for it in items), Decimal('0'))
    return (s / Decimal(len(items))) if items else Decimal('0')


def random_shuffle_ids(items: list) -> list:
    ids = [it.product.id for it in items]
    random.shuffle(ids)
    return ids