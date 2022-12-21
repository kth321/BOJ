for i in range(int(input())):
    _, *grade = list(map(int, input().split()))
    grade.sort()
    diff = []
    for j in range(len(grade) - 1):
        diff.append(grade[j + 1] - grade[j])
    print(f'Class {i + 1}')
    print(f'Max {grade[-1]}, Min {grade[0]}, Largest gap {max(diff)}')