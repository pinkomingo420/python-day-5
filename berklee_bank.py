bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

def welcome():
    """
    Task: Display the welcome message for Berklee Bank.
    Name: welcome.
    Input: None.
    Side Effects: Displays a welcome message.
    Return: None.
    """
    pass


def login(user's_name,PIN):
    """
    Task: Ask the user for their name and PIN and verify their account.
    Name: login.
    Input: The user's name and PIN.
    Side Effects: Prompts the user to enter their name and PIN.
    Return: The account name if login is successful, otherwise None.
    """
    pass


def check_balance(account_name):
    """
    Task: Display the user's current account balance.
    Name: check_balance.
    Input: The user's account name.
    Side Effects: Displays the account balance.
    Return: None.
    """
    pass


def deposit(account_name,deposit_amount):
    """
    Task: Add money to the user's account.
    Name: deposit.
    Input: The user's account name and the deposit amount.
    Side Effects: Updates the account balance and displays a message.
    Return: None.
    """
    pass


def withdraw(account_name, withdrawal_amount):
    """
    Task: Withdraw money if the account has sufficient funds.
    Name: withdraw.
    Input: The user's account name and the withdrawal amount.
    Side Effects: Updates the account balance if the withdrawal is valid and displays a message.
    Return: None.
    """
    pass


def main_menu(user's_menu_choice):
    """
    Task: Display the ATM menu and let the user choose an action.
    Name: main_menu.
    Input: The user's menu choice.
    Side Effects: Displays the menu and prompts the user for a choice.
    Return: The user's selected menu option.
    """
    pass


def exit_atm():
    """
    Task: End the ATM session.
    Name: exit_atm.
    Input: None.
    Side Effects: Displays a goodbye message.
    Return: None.
    """
    pass


def run_tests():
    # Test welcome()
    print(welcome())  # Expecting None

    # Test login()
    print(login(Amira,0000))  # Expecting a valid account name or None

    # Test check_balance()
    print(check_balance("Priya"))  # Expecting None

    # Test deposit()
    print(deposit("Priya",100))  # Expecting None

    # Test withdraw()
    print(withdraw("Carlos",100))  # Expecting None

    # Test main_menu()
    print(main_menu(deposit))  # Expecting a menu option

    # Test exit_atm()
    print(exit_atm())  # Expecting None