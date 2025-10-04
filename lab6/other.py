from decimal import Decimal, getcontext
import random
import math
import locale
from module7 import Product, OrderItem, Order
from dataclasses import replace


# Шаг 4
def random_distribution_example(n: int) -> dict:
    a = [random.random() for _ in range(n)]
    b = random.uniform(0, 1)
    return {'list_randoms_len': len(a), 'one_uniform': b}


def random_sample_vs_choice(seq: list, k: int):
    return {'sample': random.sample(seq, min(k, len(seq))), 'choice': random.choice(seq) if seq else None}


# Шаг 5
def math_trig_and_log(x: float) -> dict:
    return {'sin': math.sin(x), 'log1p': math.log1p(x), 'ceil': math.ceil(x)}


# Шаг 6
def locale_sort_strings(strings: list[str]) -> list[str]:
    locale.setlocale(locale.LC_COLLATE, '')
    return sorted(strings, key=locale.strxfrm)


# Шаг 7
def decimal_compute_with_context(a: str, b: str) -> Decimal:
    getcontext().prec = 10
    return Decimal(a) / Decimal(b)


def decimal_quantize_example(val: str) -> Decimal:
    d = Decimal(val)
    return d.quantize(Decimal('0.01'))


# Шаг 8
def create_order_from_params(order_id: int, items_params: list[tuple[int,str,str,int]]) -> Order:
    items = [OrderItem(Product(pid, name, Decimal(price)), qty) for pid, name, price, qty in items_params]
    return Order(order_id, items)


# Шаг 9
def process_order_list(orders: list[Order]) -> list[Decimal]:
    return [sum((it.product.price * it.qty for it in o.items), Decimal('0')) for o in orders]


def order_dict_map(orders: list[Order]) -> dict:
    return {o.id: o for o in orders}


def modify_order_item_qty(order: Order, product_id: int, new_qty: int) -> Order:
    for i, it in enumerate(order.items):
        if it.product.id == product_id:
            order.items[i] = replace(it, qty=new_qty)
            break
    return order


def sum_prices_and_modify(orders: list[Order], order_id: int, new_qty: int) -> Decimal:
    od = order_dict_map(orders)
    if order_id in od:
        order = modify_order_item_qty(od[order_id], od[order_id].items[0].product.id, new_qty)
        return sum((it.product.price * it.qty for it in order.items), Decimal('0'))
    return Decimal('0')