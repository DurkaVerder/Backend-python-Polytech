from module2 import show_summary, list_greetings
from module3 import distance_and_sqrt_example


def top_level_function(seed: int) -> None:
    show_summary(seed)


def demo_imports_depth(seed: int) -> dict:
    greetings = list_greetings(seed)
    stats = distance_and_sqrt_example(16, 12)
    return {'greetings': greetings, 'stats': stats}


def collect_all_names(seed: int) -> list[str]:
    return greetings if (greetings := list_greetings(seed)) else []