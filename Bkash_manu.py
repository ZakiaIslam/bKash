import random


def creat_account():
    #account_Number = int(input("Enter Account Number....."))
    PIN = int(input("Enter your PIN number: "))
    return PIN
def main_manu():
    print("bKash\n"
          "1 Send Money\n"
          "2 Mobile Recharge\n"
          "3 Payment\n"
          "4 Cash Out\n"
          "5 Pay Bill\n"
          "6 App Registration for 25 Bonus\n"
          "7 My bKash\n"
          "8 Helpline\n"
    )
    return (int(input("___")))

def Send_Money_1():
    global account_balance
    global PIN
    print("Enter Receive bKash Account No:...")
    receive_account_number = int(input())
    print("Enter Amount:...")
    amount = int(input())
    print("Enter Reference:...")
    reference = input()
    print("Send Money.\nTo: {} \nAmount: {} \nReference: {}".format(receive_account_number,amount,reference))
    print("Enter Menu PIN to confirm: ")
    PIN_check = int(input())
    if PIN_check == PIN:
        if account_balance < amount:
            print("Unsufficient Balance")
        else:
            account_balance -= amount
            print("Successfully Send Money")
    else:
        print("PIN Number is Not Correct")

    #pass
def Mobile_Recharge_2():
    global account_balance
    global PIN
    print("bKash\n"
          "1 Robi\n"
          "2 Airtel\n"
          "3 Banglalimk\n"
          "4 Grameenphone\n"
          "5 Teletalk\n"
          "0 Main Menu\n")

    sim_number = int(input())
    if sim_number == 1:
        select_number = int(input(("bKash\n"
              "1 Prepaid\n"
              "2 Postpaid\n"
              "3 Prepaid Internet packs\n"
              "4 Prepaind Voice packs\n"
              "5 Prepaid Bundle packs\n"
              "0 Main Menu\n"
              )))
        if select_number == 0:
            main_manu()
        else:
            account_number = input("Enter Robi Mobile No:....")
            if account_number[:3] != "018":
                print("Please Enter Correct Robi Number")
            else:
                recharge_amount = int(input(("Enter Recharge Amount")))
                print("Mobile Recharge.\nTo: {} \nRecharge Amount: {} \n".format(account_number,recharge_amount))
                print("Enter Menu PIN to confirm: ")
                PIN_check = int(input())
                if PIN_check == PIN:
                    if account_balance < recharge_amount:
                        print("Unsufficient Balance")
                    else:
                        account_balance -= recharge_amount
                        print("Successfully Recharged")
                else:

                    print("PIN Number is Not Correct")

    elif sim_number == 2:
        select_number = int(input(("bKash\n"
              "1 Prepaid\n"
              "2 Postpaid\n"
              "3 Prepaid Internet packs\n"
              "4 Prepaind Voice packs\n"
              "5 Prepaid Bundle packs\n"
              "0 Main Menu\n"
              )))
        if select_number == 0:
            main_manu()
        else:
            account_number = input("Enter Airtel Mobile No:....")
            if account_number[:3] != "016":
                print("Please Enter Correct Airtel Number")
            else:
                recharge_amount = int(input(("Enter Recharge Amount")))
                print("Mobile Recharge.\nTo: {} \nRecharge Amount: {} \n".format(account_number,recharge_amount))
                print("Enter Menu PIN to confirm: ")
                PIN_check = int(input())
                if PIN_check == PIN:
                    if account_balance < recharge_amount:
                        print("Unsufficient Balance")
                    else:
                        account_balance -= recharge_amount
                        print("Successfully Recharged")
                else:
                    print("PIN Number is Not Correct")

    elif sim_number == 3:
        select_number = int(input(("bKash\n"
              "1 Prepaid\n"
              "2 Postpaid\n"
              "3 Prepaid Internet packs\n"
              "4 Prepaind Voice packs\n"
              "5 Prepaid Bundle packs\n"
              "0 Main Menu\n"
              )))
        if select_number == 0:
            main_manu()
        else:
            account_number = input("Enter Banglalimk Mobile No:....")
            if account_number[:3] != "019":
                print("Please Enter Correct Banglalimk Number")
            else:
                recharge_amount = int(input(("Enter Recharge Amount")))
                print("Mobile Recharge.\nTo: {} \nRecharge Amount: {} \n".format(account_number,recharge_amount))
                print("Enter Menu PIN to confirm: ")
                PIN_check = int(input())
                if PIN_check == PIN:
                    if account_balance < recharge_amount:
                        print("Unsufficient Balance")
                    else:
                        account_balance -= recharge_amount
                        print("Successfully Recharged")
                else:
                    print("PIN Number is Not Correct")


    elif sim_number == 4:
        select_number = int(input(("bKash\n"
              "1 Prepaid\n"
              "2 Postpaid\n"
              "3 siktto\n"
              "0 Main Menu\n"
              )))
        if select_number == 0:
            main_manu()
        else:
            account_number = input("Enter Grameenphone Mobile No:....")
            if account_number[:3] != "017":
                print("Please Enter Correct Grameenphone Number")
            else:
                recharge_amount = int(input(("Enter Recharge Amount")))
                print("Mobile Recharge.\nTo: {} \nRecharge Amount: {} \n".format(account_number,recharge_amount))
                print("Enter Menu PIN to confirm: ")
                PIN_check = int(input())
                if PIN_check == PIN:
                    if account_balance < recharge_amount:
                        print("Unsufficient Balance")
                    else:
                        account_balance -= recharge_amount
                        print("Successfully Recharged")
                else:
                    print("PIN Number is Not Correct")

    elif sim_number == 5:
        select_number = int(input(("bKash\n"
                                   "1 Prepaid\n"
                                   "2 Postpaid\n"
                                   "0 Main Menu\n"
                                   )))
        if select_number == 0:
            main_manu()
        else:
            account_number = input("Enter Teletalk Mobile No:....")
            if account_number[:3] != "015":
                print("Please Enter Correct Teletalk Number")
            else:
                recharge_amount = int(input(("Enter Recharge Amount")))
                print("Mobile Recharge.\nTo: {} \nRecharge Amount: {} \n".format(account_number, recharge_amount))
                print("Enter Menu PIN to confirm: ")
                PIN_check = int(input())
                if PIN_check == PIN:
                    if account_balance < recharge_amount:
                        print("Unsufficient Balance")
                    else:
                        account_balance -= recharge_amount
                        print("Successfully Recharged your ammount is ",account_balance)
                else:
                    print("PIN Number is Not Correct")
    elif sim_number == 0:
        main_manu()

    # print("Enter Receive bKash Account No:...")
    # receive_account_number = int(input())
    # print("Enter Amount:...")
    # amount = int(input())
    # print("Enter Reference:...")
    # reference = input()



    #pass

def Payment_3():
    global PIN
    global account_balance
    merchant_accout = int(input("Enter Merchant bKash Account No: "))
    amount = int(input("Enter Amount: "))
    reference = input("Enter Reference: ")
    counter = int(input("Enter Counter No: "))
    print("Payment\nTo: {} \nAmount: {} \nReference: {} \nCounter: {} \n".format(merchant_accout,amount,reference,counter))
    check_pin = int(input("Enter Menu PIN to comfirm: "))
    #check_pin = int(input())
    if check_pin == PIN:
        if account_balance < amount:
            print("Unsufficient Balance")
        else:
            account_balance -= amount
            print("Successfully Payment Completed")
    else:
        print("PIN Number is Not Correct")

    #pass
def Cash_Out_4():
    global PIN
    global account_balance
    print("bKash\n"
          "1 From Agent\n"
          "2 From ATM\n"
          "0 Main Menu")
    selected_number = int(input("..."))
    if selected_number == 0:
        main_manu()
    elif selected_number == 1:
        agent_number = int(input("Enter Agent bKash Account No: "))
        amount = int(input("Enter Amount: "))
        print("Cash out: \nTo: {} \nAmount: {} \nEnter Menu PIN to comfirm: ".format(agent_number,amount))
        check_pin = int(input())
        if check_pin == PIN:
            if account_balance < amount:
                print("Unsufficient Balance")
            else:
                account_balance -= amount
                print("Successfully Cash Out tk{}".format(amount))
        else:
            print("PIN Number is Not Correct")

    elif selected_number == 2:
        check_pin = int(input("Enter Menu PIN to request ATM Cash Out: "))
        if check_pin == PIN:
            print("You Secuity Code is",random.randint(00000,99999),".Go to a bKash enabled ATM booth within 5 minutes.\nUse this code on ATM screen")
        else:
            print("Invalid PIN Number")

    #pass
def Pay_Bill_5():
    print("bKash\n"
          "1 Electricity(Prepaid)\n"
          "2 Electricity(Postpaid)\n"
          "3 Gas\n"
          "4 Water\n"
          "5 Internet,TV and Phone\n"
          "6 Education\n"
          "7 Holding Tax\n"
          "8 Financial Services\n"
          "9 Other\n"
          "0 Main Menu")
    selected_number = int(input("...."))
    if selected_number == 0:
        main_manu()
    else:
        print("Sorry..!!!Service is not available Right now!!")


    #pass
def App_Registration_for_25_Bonus_6():
    global PIN
    print("bKash App Registration.\n")
    chack_pin = int(input("Enter Menu PIN to confirm:"))
    if chack_pin == PIN:
        print("Registration Complete")
    else:
        print("Invalid PIN number")
    #pass
def My_bKash_7():
    global account_balance
    global PIN
    print("bKash\n"
          "1 Check Balance\n"
          "2 Request Statement\n"
          "3 Change Mobile Menu PIN\n"
          "4 Manage Beneficiary\n"
          "5 Update MNP info\n"
          "0 Main Menu\n")
    dial_number = int(input())
    if dial_number == 0:
        main_manu()
    elif dial_number == 1:
        check_pin = int(input())
        if check_pin == PIN:
            print("Your current bKash Account balance is Tk {}\nApp diye balance check simple!".format(account_balance))
        else:
            print("Invalid PIN Number")
    elif dial_number == 2:
        check_pin = int(input())
        if check_pin == PIN:
            print("Your request has been processed.Wait few minutes for sms")
        else:
            print("Invalid PIN Number")
    elif dial_number == 3:
        check_pin = int(input("Enter Old PIN"))
        if check_pin != PIN:
            print("Invalid PIN Number")
        else:
            PIN = int(input("Enter a 5 digit New PIN"))

    elif dial_number == 4:
        print("bKash\n"
              "1 Electricity(Prepaid)\n"
              "2 Electricity(Postpaid)\n"
              "3 Gas\n"
              "4 Water\n"
              "5 Internet,TV and Phone\n"
              "6 Education\n"
              "7 Holding Tax\n"
              "8 Financial Services\n"
              "9 Other\n"
              "0 Main Menu")
        selected_number = int(input("...."))
        if selected_number==0:
            main_manu()
        else:
            print("Sorry..!!!Service is not available Right now!!")
    elif dial_number == 5:
        print("bKash\n"
              "1 GP\n"
              "2 Robi/Airtel\n"
              "3 Banglalink\n"
              "4 Teletalk\n"
              "0 Main Menu")
        selected_number = int(input("...."))
        if selected_number == 0:
            main_manu()
        elif ((selected_number == 1) or (selected_number == 2) or (selected_number == 3) or (selected_number == 4)):
            check_pin = int(input("Enter PIN"))
            if check_pin != PIN :
                print("Invalid PIN Number")
            else:
                print("Thank You.Your information has been update successfully")
        else:
            print("Please Enter Correct Number")

    #pass
def Helpline_8():
    print("bKash\n"
          "1 Call 16247 or Visit www.bkash.com for more info.\n"
          "0 Main Menu\n")
    dial_number = int(input())
    if dial_number == 0:
        main_manu()
    elif dial_number == 1:
        print("Open phone App And dial number by yourself or goto google and visit the site !!!!")
    else:
        print("Please Dial the correct Number!!!")

### Start
account_balance = 20000
number = input("Dial *247# for bKash: ")
if number == "*247#":
    PIN = creat_account()
    serial_number = main_manu()
    if serial_number == 1:
        Send_Money_1()

    elif serial_number ==2:
        Mobile_Recharge_2()

    elif serial_number == 3:
        Payment_3()

    elif serial_number == 4:
        Cash_Out_4()

    elif serial_number == 5:
        Pay_Bill_5()

    elif serial_number == 6:
        App_Registration_for_25_Bonus_6()

    elif serial_number == 7:
        My_bKash_7()

    elif serial_number == 8:
        Helpline_8()


else:
    print("Please Dial the correct Number!!!")