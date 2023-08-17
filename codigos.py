repetitions = int(input())
input_string = input()
current_char = input_string[0]
char_count = 0
for char in input_string:
    if char == current_char:
        char_count += 1
    else:
        print(f"{char_count} {current_char}", end=" ")
        current_char = char
        char_count = 1
print(f"{char_count} {current_char}", end=" ")
