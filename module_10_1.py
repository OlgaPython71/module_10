import time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time = time.time()
print(f'Работа потоков {(finish_time - start_time)}')
start_time = time.time()
thread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread.start()
thread2.start()
thread3.start()
thread4.start()
thread3.join()
finish_time = time.time()
print(f'Работа потоков {(finish_time - start_time)}')
