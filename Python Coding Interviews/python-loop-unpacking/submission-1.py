from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    # curr_max = 0
    # for name, score in scores:
    #     curr_max = max(curr_max, score)
    # for name, score in scores:
    #     if curr_max == score:
    #         return name
    best_score, best_student_name = 0, ''
    for name, score in scores:
        if score > best_score:
            best_score = score
            best_student_name = name
    return best_student_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
