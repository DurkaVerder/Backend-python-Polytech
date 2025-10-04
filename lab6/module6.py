import math
import locale
from decimal import Decimal
from module7 import Product, OrderItem, Order, decimal_sum_prices


def calc_order_total(order: Order) -> Decimal:
    return decimal_sum_prices(order.items)


def math_stats_on_prices(items: list[OrderItem]) -> dict:
    prices = [float(it.product.price) for it in items]
    return {
    'max': max(prices) if prices else 0,
    'ceil_first': math.ceil(prices[0]) if prices else 0,
    'hypot_example': math.hypot(*prices[:2]) if len(prices) >= 2 else 0,
    }


def locale_grouping_example(number: float) -> str:
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string('%.2f', number, grouping=True)