import itertools as it
with open('studygroup.txt', 'r') as file:
    students = file.readline().split()
combinations = list(it.combinations(students, 3))
for i, combo in enumerate(combinations):
    print(f"1: {combo[0]} 2: {combo[1]} 3: {combo[2]}")