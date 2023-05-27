# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то
# они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

poem = input('Что сочинил Винни: ').split()

res_list = []

for i in range(len(poem)):
    res_list.append(list(filter(lambda x: x in "аеёиоуыэюяАЕЁИОУЫЭЮЯ", poem[i])))

res_list = list([len(i) for i in res_list])

# Можно заменить строчки 13-16 этой конструкцией, мне она нравится больше, но не использует фильтр
# for i in poem:
#     count_vowels = len([char for char in i if char in "аеёиоуыэюяАЕЁИОУЫЭЮЯ"])
#     res_list.append(count_vowels)

if len(set(res_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
    