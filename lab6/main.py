from other import (
    format_report,
    repeat_combo_and_print,
    count_substring_ignore_case,
    substring_between,
    detect_latin_in_words,
    is_palindrome,
    normalize_spaces_and_length,
    sentences_to_lines,
    initials,
    longest_word,
    extract_numbers,
)


def run_all() -> None:
    # 1
    s1 = format_report("Отдел продаж", 1234.56, 3)
    print(s1)

    # 2 
    repeat_combo_and_print("Продукт-", "-версия-", 3)

    # 3
    text = "Абба абба ABba abBa"
    c = count_substring_ignore_case(text, "abba")
    print("count=", c)

    # 4
    s = "Это тестовая строка"
    sub = substring_between(s, 4, 11)
    print(sub)

    # 5
    a, b = detect_latin_in_words("Пример: Рострал, СТАНДАРТ, Роst")
    print("найдено слова=", a, "количество строк с латинскими буквами=", b)

    # 6
    print(is_palindrome("А роза упала на лапу Азора"))

    # 7
    print("length:", normalize_spaces_and_length("  слово   ещё   слово  "))

    # 8
    paragraph = "Первое предложение. Второе! Третье? И четвёртое..."
    print(sentences_to_lines(paragraph))

    # 9
    print("initials:", initials("иванов иван сергеевич"))
    print("longest:", longest_word("Короткое длиннейшееСлово среднее"))
    print("numbers:", extract_numbers("Текст с числами: 10, -5 и 42"))


if __name__ == "__main__":
    run_all()
