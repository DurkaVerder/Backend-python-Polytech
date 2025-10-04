from module1 import demo_imports_depth, top_level_function, collect_all_names
from other import (
    random_distribution_example,
    random_sample_vs_choice,
    math_trig_and_log,
    locale_sort_strings,
    decimal_compute_with_context,
    decimal_quantize_example,
    create_order_from_params,
    process_order_list,
    order_dict_map,
    modify_order_item_qty,
    sum_prices_and_modify,
)


# Шаг 2
def demonstrate_imports_and_run_all() -> None:
    res = demo_imports_depth(42)
    print("Demo imports result:", res)

    # Шаг 4
    print("Random distribution:", random_distribution_example(5))
    print("Random sample vs choice:", random_sample_vs_choice([1, 2, 3, 4], 2))

    # Шаг 5
    print("Math trig/log:", math_trig_and_log(0.5))

    # Шаг 6
    print("Locale sorted:", locale_sort_strings(["яблоко", "банан", "апельсин"]))

    # Шаг 7
    print("Decimal div:", decimal_compute_with_context("10", "3"))
    print("Decimal quantize:", decimal_quantize_example("2.3456"))

    # Шаг 8 и 9: работа с data-классами
    o1 = create_order_from_params(1, [(1, "Кофе", "3.50", 2), (2, "Чай", "2.25", 1)])
    o2 = create_order_from_params(2, [(3, "Булочка", "1.10", 5)])
    orders = [o1, o2]

    print("Process order list totals:", process_order_list(orders))
    od = order_dict_map(orders)
    print("Order dict keys:", list(od.keys()))
    modified = modify_order_item_qty(o1, 1, 5)
    print("Modified order qty first item:", modified.items[0].qty)
    print("Sum prices and modify:", sum_prices_and_modify(orders, 1, 3))


# Шаг 10
if __name__ == "__main__":
    demonstrate_imports_and_run_all()
