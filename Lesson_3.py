class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Вы внесли {amount} Br.\nНовый баланс: {self.__balance} Br')
        else:
            print("Сумма должна быть положительной!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Вы сняли {amount }Br.\nНовый баланс: {self.__balance} Br')
            return True
        else:
            print("Недостаточно средств!")
            return False

    def get_balance(self):
        return self.__balance


def atm_interface():
    account = BankAccount(1000)  # Начальный баланс 1000
    while True:
        print("\nДобро пожаловать в банкомат!")
        print("1. Проверить баланс")
        print("2. Внести средства")
        print("3. Снять средства")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            print(f'Ваш текущий баланс: {account.get_balance()} Br')
        elif choice == '2':
            amount = float(input("Введите сумму для внесения: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Спасибо за использование банкомата!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

        # Запуск интерфейса банкомата


atm_interface()