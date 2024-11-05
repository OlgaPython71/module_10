import random
import time
import threading


class Bank:
    def __init__(self, balance, lock=threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            count_deposit = random.randint(50, 500)
            self.balance += count_deposit
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {count_deposit}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            count_take = random.randint(50, 500)
            print(f'Запрос на {count_take}')
            if count_take <= self.balance:
                self.balance -= count_take
                print(f'Снятие: {count_take}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank(0)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
