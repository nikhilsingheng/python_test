from collections import Counter

simple_case = input(input("Enter the nimber of  case"))
simple_count = 0
simple_names = []

while simple_case < simple_count:

    num = int(input("Enter the nimber of each case"))
    count = 0
    while count < num:
        name = str(input("Enter the name by Twitter ID case"))
        simple_names.append(name)
        count += 1

    simple_count += 1

uniq_names = [pref_name.split()[0] for pref_name in simple_names]
times = Counter(uniq_names)

required = times.values()

for element in set(required):
    num1 = ([(key, value)
            for key, value in sorted(times.items()) if value == element])

    if len(num1) > 1:
        for(key, value) in num1:
            print(key, '', value)
    max_value = max(times.values())
    tem_max_result = [(key, value) for key, value in sorted(
        times.items()) if value == max_value]

    if tem_max_result != num1:
        for (key, value) in tem_max_result:
            print(key, '', value)
