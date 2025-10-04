from module3 import summary_cart_prices, greet_products
import locale



def show_summary(seed: int) -> None:
    s = summary_cart_prices(seed)
    print(f"Итого: {s['formatted']} (raw={s['total']})")



def locale_example_set_and_conv():
    locale.setlocale(locale.LC_ALL, '')
    return locale.localeconv()


def list_greetings(seed: int) -> list[str]:
    return greet_products(seed)