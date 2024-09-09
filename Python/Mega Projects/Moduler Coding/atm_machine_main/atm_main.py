class Atm:

  #constructor(special function) - superpower
  def __init__(self):
    self.pin = ""
    self.balance = 0
    # self.menu()


  def menu(self):
    user_input = input(
        """
        Hi how can i help you?

        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balence
        4. Press 4 to withdraw
        5. Anything to exit
        """
    )

    if user_input == '1':
      #create a pin
      self.create_pin()

    elif user_input == '2':
      #change pin
      self.change_pin()

    elif user_input == '3':
      #check balnce
      self.check_balance()

    elif user_input == '4':
      #withdraw
      self.withdraw()

    else:
      exit()


  def create_pin(self):
    user_pin = input("Enter your pin: ")
    self.pin = user_pin

    user_balance = int(input("Enter Balance: "))
    self.balance = user_balance

    print("Pin Created Successfully!")
    # self.menu()


  def change_pin(self):
    old_pin = input("Enter old pin: ")

    if old_pin == self.pin:
      #Let change the pin
      new_pin = input("Enter new pin: ")
      self.pin = new_pin
      print("Pin changed Successfully!")
      # self.menu()

    else:
      print("Sorry you entered wrong pin.")
      # self.menu()




  def check_balance(self):
    user_pin = input("Enter your pin: ")
    if user_pin == self.pin:
      print(f"Your balance is {self.balance}")
    else:
      print("Your pin is correct, please try again")
    # self.menu()



  def withdraw(self):
    user_pin = input("Enter your pin: ")
    if user_pin == self.pin:
      # Allow to withdraw
      amount = int(input("Enter the amount: "))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print(f"withdraw successfull and the current balance is {self.balance}")

      else:
        print("You have insufficient balance")


    else:
      print("Your pin is wrong!")
    # self.menu()
