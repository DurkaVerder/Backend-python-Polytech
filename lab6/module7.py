from dataclasses import dataclass, replace
from decimal import Decimal, getcontext
import locale


@dataclass
class Product:
    id: int
    name: str
    price: Decimal



@dataclass
class OrderItem:
    product: Product
    qty: int



@dataclass
class Order:
    id: int
    items: list[OrderItem]



def decimal_sum_prices(items: list[OrderItem]) -> Decimal:
    getcontext().prec = 28
    return sum((it.product.price * it.qty for it in items), Decimal('0'))


def _module7_helper_format_currency(value: Decimal) -> str:
    locale.setlocale(locale.LC_ALL, '')
    conv = locale.localeconv()
    q = value.quantize(Decimal('0.01'))
    return f"{q}"


def create_product(pid: int, name: str, price_str: str) -> Product:
    return Product(pid, name, Decimal(price_str))