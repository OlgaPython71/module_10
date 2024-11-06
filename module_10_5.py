import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for file in filenames:
    read_info(file)
finish_time = time.time()
print(finish_time - start_time)
# Многопроцессный
if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    finish_time = time.time()
    print(finish_time - start_time)
