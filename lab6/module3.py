import math
from module4 import assemble_cart
from module6 import locale_grouping_example



def summary_cart_prices(seed: int) -> dict:
    items = assemble_cart(seed)
    total = sum(float(it.product.price) * it.qty for it in items)
    formatted = locale_grouping_example(total)
    return {'total': total, 'formatted': formatted, 'count': len(items)}



def distance_and_sqrt_example(a: float, b: float) -> dict:
    return {'sqrt_a': math.sqrt(a), 'hypot_ab': math.hypot(a, b), 'floor_a': math.floor(a)}



def greet_products(seed: int) -> list[str]:
    items = assemble_cart(seed)
    return [f"Товар: {it.product.name} x{it.qty}" for it in items]