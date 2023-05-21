from typing import List, Tuple

TEST_DATA: List[Tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    return current_rep + (rep_points * BONUS if buf_effect else rep_points)


def remove_rep(current_rep: float, rep_points: int,
               debuf_effect: bool) -> float:
    return current_rep - (rep_points * ANTIBONUS if debuf_effect else rep_points)


def main(duel_res: List[Tuple[int, str, bool]]) -> str:
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        elif result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (
    f'После {len(duel_res)} поединков, '
    f'репутация персонажа — {current_rep:.3f} очков.'
)

# Тестовый вызов функции main.
print(main(TEST_DATA))