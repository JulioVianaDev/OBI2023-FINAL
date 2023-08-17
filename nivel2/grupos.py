E, M, D = map(int, input().split())
preferences = [tuple(map(int, input().split())) for _ in range(M)]
print(preferences)
dislikes = [tuple(map(int, input().split())) for _ in range(D)]
groups = [list(map(int, input().split())) for _ in range(E // 3)]
group_sets = [set(group) for group in groups]
student_group_map = {student: group_index for group_index, group in enumerate(group_sets) for student in group}
violations = 0
violations += sum(1 for x, y in preferences if student_group_map.get(x) != student_group_map.get(y))
violations += sum(1 for u, v in dislikes if student_group_map.get(u) == student_group_map.get(v))
# print(violations)
