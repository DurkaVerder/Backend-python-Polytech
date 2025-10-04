import re
import unicodedata
from typing import List, Tuple

# Шаг 1
def format_report(name: str, base: float, times: int) -> str:
    template = "Отчёт для: {name}. Итоговая сумма: {total} (расчёт: {base} * {times}). Дополнительно: {note}"
    def helper_note(x: float) -> str:
        return f"среднее на итерацию {x / max(times,1):.2f}"
    total = base * times 
    note = helper_note(total) 
    return template.format(name=name, base=base, times=times, total=total, note=note)

# Шаг 2
def repeat_combo_and_print(prefix: str, infix: str, count: int) -> None:
    out = "\n".join((f"{i+1}. {prefix}{infix}{i+1}" for i in range(max(0,count))))
    print(out)

# Шаг 3
def count_substring_ignore_case(text: str, sub: str) -> int:
    t = text.lower()
    s = sub.lower()
    if not s:
        return 0
    return sum(1 for i in range(len(t)-len(s)+1) if t[i:i+len(s)] == s)

# Шаг 4
def substring_between(s: str, i: int, j: int) -> str:
    return s[i:j] if 0 < i < j < len(s)-1 else ""

# Шаг 5
def detect_latin_in_words(*texts: str) -> Tuple[List[str], int]:
    latin_words_found = []
    words_with_latin = 0
    for txt in texts:
        words = re.findall(r"[\w\-]+", txt, flags=re.UNICODE)
        found_in_text = False
        for w in words:
            if any(('LATIN' in unicodedata.name(ch) if ch.strip() else False) for ch in w):
                latin_words_found.append(w)
                found_in_text = True
        if found_in_text:
            words_with_latin += 1
    return latin_words_found, words_with_latin

# Шаг 6
def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch for ch in s.lower() if ch.isalnum())
    return cleaned == cleaned[::-1]

# Шаг 7
def normalize_spaces_and_length(s: str) -> int:
    normalized = re.sub(r"\s+", " ", s.strip())
    return len(normalized)

# Шаг 8
def sentences_to_lines(text: str) -> str:
    return re.sub(r"[\.\!\?]+", "\n", text)

# Шаг 9
def initials(fullname: str) -> str:
    parts = [p for p in fullname.strip().split() if p]
    return '.'.join(p[0].upper() for p in parts) + ('.' if parts else '')


def longest_word(text: str) -> str:
    words = re.findall(r"[\w]+", text)
    return max(words, key=len) if words else ''


def extract_numbers(text: str) -> List[int]:
    nums = re.findall(r"[-+]?\d+", text)
    return [int(n) for n in nums]

