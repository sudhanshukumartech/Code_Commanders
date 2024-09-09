import google.generativeai as genai

class NLPModel:

    def get_model(self):
        GOOGLE_API_KEY = "AIzaSyCaHhqYXaaJGk1WD23xxznOp4lOrCr46i8"
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-pro")
            return model
        except Exception as e:
            print(e)
    

class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()

    def first_menu(self):
        first_input = input("""
        Hi! How would you like to proceed?

            1. Not a member? Register
            2. Already a member? Login
            3. Bhai galti se aa gaya kia? Exit
                            
            """)
        
        if first_input == "1":
            #register
            self.__register()

        elif first_input == "2":
            #login
            self.__login()

        else:
            exit()

    
    def second_menu(self):
        second_input = input("""
        Hi! How would you like to proceed?

        1. Sentiment Analysis
        2. Language Transilation
        3. Language Detection
        """)

        if second_input == '1':
            #Sentiment Analysis
            self.__sentiment_analysis()

        elif second_input == '2':
            # Language Transilation
            self.__language_transilation()

        elif second_input == '3':
            # Language Detection
            self.__language_detection()

        else:
            exit()

    
    def __register(self):
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")

        if email in self.__database:
            print("Email already exists.")
        
        else:
            self.__database[email] = [name, password]
            print("Registration successful. Now you can login!")
            # print(self.__database)
            self.first_menu()


    def __login(self):
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")

        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login Successfull")
                self.second_menu()

            else:
                print("Incorrect Password")
                self.__login()

        else:
            print("Email not found. Please register first.")
            self.first_menu()

    
    def __sentiment_analysis(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()


    def __language_transilation(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        response = model.generate_content(f"Give me hindi transilation of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    
    def __language_detection(self):
        user_text = input("Enter your text: ")
        model = super().get_model()
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()




        






if __name__ == '__main__':
    nlp = NLPApp()