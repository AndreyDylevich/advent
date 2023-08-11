with open('advent.txt.txt') as f:

 calories = []
 for group in f:
   calories.append(group.strip())
max_calories = []
counter = 0
for i in calories:
    if i != '':
        counter = counter + int(i)
    else:
        max_calories.append(counter)
        counter = 0

print(max(max_calories))

# part 2
calories2 = []
calories_elf2 = []
with open('advent.txt.txt') as f:
  for group2 in f:
    if group2.strip():
      calories_elf2.append(int(group2))
    else:
      calories2.append(calories_elf2)
      calories_elf2 = []

if calories_elf2:
  calories2.append(calories_elf2)

  calories2 = sorted(calories2, key=sum, reverse=True)

  top_three_calories = calories2[:3]

  all_calories = sum(sum(elf_calories) for elf_calories in top_three_calories)

  print(all_calories)

































