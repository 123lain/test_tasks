import re

example_grades = [
    'Иванов: 85',
    'Петров: 42',
    'Сидоров: abc',
    'Козлов: 90',
    ': 55',
    'Иванов: 70'
]

def process_grades(records: list[str]) -> dict:
    valid_count = 0
    valid_sum = 0
    skipped_count = 0
    passed = []

    for grade in records:
        match = re.match(r'(?P<name>\w+):\s(?P<grade>\d+)', grade)
        if match:
            valid_count += 1

            grade = float(match.group('grade'))
            valid_sum += grade
            if match.group('name') not in passed and grade > 60:
                passed.append(match.group('name'))
        else:
            skipped_count += 1

    return {
        'valid_count': valid_count,
        'average': round(valid_sum / valid_count, 1) if valid_count != 0 else 0.0,
        'passed': sorted(passed),
        'skipped': skipped_count
    }

if __name__ == '__main__':
    print(process_grades(example_grades))