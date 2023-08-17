# Read input
E, M, D = map(int, input().split())
preferences = [tuple(map(int, input().split())) for _ in range(M)]
dislikes = [tuple(map(int, input().split())) for _ in range(D)]
groups = [list(map(int, input().split())) for _ in range(E // 3)]
preference_sets = [set(pair) for pair in preferences]
dislike_sets = [set(pair) for pair in dislikes]
group_students = [set(group) for group in groups]
violations = 0
for preference in preference_sets:
    found = any(all(student in group for student in preference) for group in group_students)
    if not found:
        violations += 1
for dislike in dislike_sets:
    found = any(any(student in group for student in dislike) for group in group_students)
    if found:
        violations += 1
print(violations)
