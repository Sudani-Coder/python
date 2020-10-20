class BankAccount:
    def __init__(self, AccountID, AccountName, AccountBalance, AccountPassword):
        self.__AccountID = AccountID
        self.__AccountName = AccountName
        self.__AccountBalance = AccountBalance
        self.__AccountPassword = AccountPassword

    def get_account_info(self):
        print(f'The Account Number  => {self.__AccountID}')
        print(f'The Account Name    => {self.__AccountName}')
        print(f'The Account Balance => {self.__AccountBalance}')


if __name__ == "__main__":
    myAccount = BankAccount('SD01', 'Sudani Coder', 100500000, '09321')
    myAccount.get_account_info()
