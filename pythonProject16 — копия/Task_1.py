num_1, num_2 = map(int, input('Enter two digits: ').split())
if num_1 > num_2:
    c = num_1
    num_1 = num_2
    num_2 = c
sum_multiple_nine = 0
sum_pairs = 0
sum_odd = 0
avarage_multiple_nine = 0
avarage_pairs = 0
avarage_odd = 0
count = 0
for i in range(num_1, num_2 + 1):
    if i % 9 == 0:
        sum_multiple_nine += i
        result_sum_multiple_nine = f'The sum of all numbers is ' \
                                   f'multiple of 9 in the range from {num_1} to {num_2} = {sum_multiple_nine}'
    if i % 2 == 0:
        sum_pairs += i
        result_sum_pairs = f'The sum of all pairs numbers in the range from {num_1} to {num_2} = {sum_pairs}'
    if i % 2 != 0:
        sum_odd += i
        result_sum_odd = f'The sum of all odd numbers in the range from {num_1} to {num_2} = {sum_odd}'
    count += 1
avarage_multiple_nine = sum_multiple_nine / count
avarage_multiple_nine = round(avarage_multiple_nine, 2)
avarage_pairs = sum_pairs / count
avarage_pairs = round(avarage_pairs, 2)
avarage_odd = sum_odd / count
avarage_odd = round(avarage_odd, 2)
result_avarage_multiple_nine = f'The avarage of all numbers is ' \
                                   f'multiple of 9 in the range from {num_1} to {num_2} = {avarage_multiple_nine}'
result_avarage_pairs = f'The avarage of all pairs numbers in the range from {num_1} to {num_2} = {avarage_pairs}'
result_avarage_odd = f'The avarage of all odd numbers in the range from {num_1} to {num_2} = {avarage_odd}'
print(count)
print(result_sum_pairs)
print(result_avarage_pairs)
print(result_sum_odd)
print(result_avarage_odd)
print(result_sum_multiple_nine)
print(result_avarage_multiple_nine)

