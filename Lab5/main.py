from others import run_all


if __name__ == '__main__':
    results = run_all()
    # Компактный вывод результатов
    for k, v in results.items():
        print(f"{k}: {v}")

