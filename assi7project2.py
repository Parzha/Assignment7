class math:
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def multi(self):
        result_sorat = self.x * self.z
        result_makhraj = self.y * self.w

        print(f'Your answer is {result_sorat}/{result_makhraj}\n')


    def divi(self):
        result_sorat = self.x * self.w
        result_makhraj = self.y * self.z

        print(f'Your answer is {result_sorat}/{result_makhraj}\n')
    def sub(self):

        result1 = self.x * self.w
        result2 = self.y * self.z
        result_sorat = result1 - result2
        result_makhraj = self.y * self.w

        print(f'Your asnwer is {result_sorat}/{result_makhraj}\n')

    def add(self):
        result1 = self.x * self.w
        result2 = self.y * self.z
        result_sorat = result1 + result2
        result_makhraj = self.y * self.w
        if (self.y == 0 or self.w == 0):
            print("invalid fraction number/0 ")
        else:
            print(f'Your answer is {result_sorat}/{result_makhraj}\n')



print('''What operaterions you want to do with your fractions
        1- Addition  
        2- Subtraction
        3- Multiplication
        4- Division ''')

while(True):
    user_input_menu =int(input("Enter your choice from the list->"))

    if user_input_menu == 1:

        sorat1_str , makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
            fraction = math(sorat1,makhraj1,sorat2,makhraj2)
            fraction.add()


    elif user_input_menu == 2:
        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
            fraction = math(sorat1, makhraj1, sorat2, makhraj2)
            fraction.sub()


    elif user_input_menu == 3:
        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
            fraction = math(sorat1, makhraj1, sorat2, makhraj2)
            fraction.multi()


    elif user_input_menu == 4:
        sorat1_str, makhraj1_str = input("Please enter the first numerator and first denominator").split()
        sorat2_str, makhraj2_str = input("Please enter the second numerator and second denominator").split()

        sorat1 = int(sorat1_str)
        sorat2 = int(sorat2_str)
        makhraj1 = int(makhraj1_str)
        makhraj2 = int(makhraj2_str)
        if makhraj1 == 0 or makhraj2 == 0:
            print("Invalid fraction --> Number/0 Try again \n")
        else:
            fraction = math(sorat1, makhraj1, sorat2, makhraj2)
            fraction.divi()


    elif user_input_menu == 5:
        print("BYE BYE")
        break

    else:
        print("Invalid input please try again")



