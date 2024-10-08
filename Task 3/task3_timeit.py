# Завдання 3. Порівняти ефективність алгоритмів пошуку підрядка: 
# Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів 
# (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання кожного алгоритму 
# для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого. 
# На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.
import timeit
import matplotlib.pyplot as plt
import numpy as np
from models import kmp_search, boyer_moore_search, rabin_karp_search

def get_min(d: dict, index: int):
    return min(d.values(), key=lambda x: x[index])[index] 

def get_max(d: dict, index: int):
    return max(d.values(), key=lambda x: x[index])[index]

def compare_minmax(d, index, minmax:str):
    for k in d:
        for k_ in d:
            if k!=k_:
                yield f"Різниця {minmax} часу пошуку між алоритмами {k} та {k_} складає {d[k][index] - d[k_][index]:.8f}"


"""1. Збір даних"""
        
words_to_search = ['ВИКОРИСТАННЯ', 'ВИКОРИСТАННЯ АЛГОРИТМІВ', 'наприклад', 
                   'наприклад, сортування: товари в магазині сортують', 'інтерполяції', 
                   'використовує формули інтерполяції', 'знаннями',
                   'потрібно володіти фундаментальними знаннями', 'html',
                   'https://dl.sumdu.edu.ua/textbooks/95351/522264/index.html', 'no-word-test']

words_to_search2 = ['методи', 'методи та структури', 'автор', 'системи соціальної мережі',  'можливим', 
                    'розв’язувати багато проблем', 'генерації', 'при традиційних представленнях', 'комбинато',
                    'искусство программирования, том 4а. комбинато', 'test-test']


data1 = {} # зберігання часів пошуку у першому тексті
data2 = {} # зберігання часів пошуку у першому тексті

filename = "стаття_1.txt"
filename2 = "стаття_2.txt"

with open(filename, 'r', encoding="utf-8") as f:
    ft = f.read().lower()

with open(filename2, 'r', encoding="utf-8") as fn:
    fp = fn.read().lower()

n = 10

"""Підрахунок часу пошуку"""

for i, j in zip(words_to_search, words_to_search2):
    word = i.lower()
    word2 = j.lower()
    data1[word] = [timeit.timeit(stmt=f'kmp_search(ft, word)', globals=globals(), number=n)/n]
    data2[word2] = [timeit.timeit(stmt=f'kmp_search(fp, word2)', globals=globals(), number=n)/n]
    data1[word].append(timeit.timeit(stmt=f'boyer_moore_search(ft, word)', globals=globals(), number=n)/n)
    data2[word2].append(timeit.timeit(stmt=f'boyer_moore_search(fp, word2)', globals=globals(), number=n)/n)
    data1[word].append(timeit.timeit(stmt=f'rabin_karp_search(ft, word)', globals=globals(), number=n)/n)
    data2[word2].append(timeit.timeit(stmt=f'rabin_karp_search(fp, word2)', globals=globals(), number=n)/n)


"""3. Аналіз мінімального та максимального значень часу"""

stats1 = {'KMP': [get_min(data1, 0), get_max(data1,0)],
          'Boyer-Moore': [get_min(data1, 1), get_max(data1,1)],
          'Rabin-Karp': [get_min(data1, 2), get_max(data1,2)]
         }

stats2 = {'KMP': [get_min(data2, 0), get_max(data2,0)],
          'Boyer-Moore': [get_min(data2, 1), get_max(data2,1)],
          'Rabin-Karp': [get_min(data2, 2), get_max(data2,2)]
         }

"""3.1. Мінімальний час у двох текстах"""

print("*****TEXT 1*****")
for n in compare_minmax(stats1, 0, 'мінімального'):
    print(n)

print("*****TEXT 2*****")
for m in compare_minmax(stats2, 0, 'мінімального'):
    print(m)
 
"""3.2. Максимальний час у двох текстах"""

for n in compare_minmax(stats1, 1, 'максимального'):
    print(n)

print("*****TEXT 2*****")

for m in compare_minmax(stats2, 1, 'максимального'):
    print(m)
 

"""-----------------------------------------------------------------------------"""
"""VISUALIZATIONS"""

all_kmp = [i[0] for i in data1.values()] #список значень часу, отриманих для алгоритму КМП
all_boyer = [i[1] for i in data1.values()] #список значень часу, отриманих для алгоритму Бойера-Мура
all_karp = [i[2] for i in data1.values()] #список значень часу, отриманих для алгоритму Рабіна-Карпа

"""TEXT 1"""
fig1, axs = plt.subplots(2,2, figsize = (8,5))
axs[0,0].plot(range(len(data1)), all_kmp, label='KMP')
axs[0,1].plot(range(len(data1)), all_boyer, label='Boyer-Moore', color='orange')
axs[1,0].plot(range(len(data1)), all_karp, label = 'Rabin-Karp', color='green')

axs[1,1].plot(range(len(data1)), all_kmp, label='KMP')
axs[1,1].plot(range(len(data1)), all_boyer, label='Boyer-Moore')
axs[1,1].plot(range(len(data1)), all_karp, label = 'Rabin-Karp')
axs[0,0].grid(alpha=0.3)
axs[0,1].grid(alpha=0.3)
axs[1,0].grid(alpha=0.3)
axs[1,1].grid(alpha=0.3)
axs[0,0].legend()
axs[0,1].legend()
axs[1,0].legend()
axs[1,1].legend()
axs[0,0].set_xticks(np.arange(0, len(data1)+1, 1))
axs[0,1].set_xticks(np.arange(0, len(data1)+1, 1))
axs[1,0].set_xticks(np.arange(0, len(data1)+1, 1))
axs[1,1].set_xticks(np.arange(0, len(data1)+1, 1))

plt.tight_layout()

# plt.savefig('graphs/dataoverview')
# plt.show()
"""TEXT 2"""

fig2, axs = plt.subplots(2,2, figsize = (8,5))
axs[0,0].plot(range(len(data2)), all_kmp, label='KMP')
axs[0,1].plot(range(len(data2)), all_boyer, label='Boyer-Moore', color='orange')
axs[1,0].plot(range(len(data2)), all_karp, label = 'Rabin-Karp', color='green')

axs[1,1].plot(range(len(data2)), all_kmp, label='KMP')
axs[1,1].plot(range(len(data2)), all_boyer, label='Boyer-Moore')
axs[1,1].plot(range(len(data2)), all_karp, label = 'Rabin-Karp')
axs[0,0].grid(alpha=0.3)
axs[0,1].grid(alpha=0.3)
axs[1,0].grid(alpha=0.3)
axs[1,1].grid(alpha=0.3)
axs[0,0].legend()
axs[0,1].legend()
axs[1,0].legend()
axs[1,1].legend()
axs[0,0].set_xticks(np.arange(0, len(data2)+1, 1))
axs[0,1].set_xticks(np.arange(0, len(data2)+1, 1))
axs[1,0].set_xticks(np.arange(0, len(data2)+1, 1))
axs[1,1].set_xticks(np.arange(0, len(data2)+1, 1))

plt.tight_layout()

# plt.show()


"""MINMAX"""

"""Порівняння мінімальних значень"""

fig4, axs = plt.subplots()
axs.bar([k for k in stats1], [round(float(stats1[k][0]), 6) for k in stats1], label="Text 1")
axs.bar([k for k in stats2], [round(float(stats2[k][0]), 6) for k in stats2], label="Text 2")
plt.legend()
axs.grid(alpha=0.3)
axs.set_ylabel("Seconds")
# plt.show()

"""Порівняння максимальних значень"""

fig5, axs = plt.subplots()

axs.bar([k for k in stats2], [round(float(stats2[k][1]), 6) for k in stats2], label="Text 2")
axs.bar([k for k in stats1], [round(float(stats1[k][1]), 6) for k in stats1], label="Text 1")
plt.legend()
axs.grid(alpha=0.3)
axs.set_ylabel("Seconds")
# plt.show()
