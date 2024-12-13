import streamlit as st
st.title("Welcome to ABC Bank")
class Bank:
    def __init__(self):
        if 'acbal' not in st.session_state:
            st.session_state.acbal = 10000
        if 'count' not in st.session_state:
            st.session_state.count = 0

    def deposit(self):
        dep = st.number_input("Enter the amount to be deposited", min_value=1, step=1)
        if dep < 100:
            st.error("Minimum deposit amount should be 100")
        elif dep % 100 != 0:
            st.error("Amount should be a multiple of 100")
        elif dep > 50000:
            st.error("Maximum deposit amount is 50000")
        else:
            st.session_state.acbal += dep
            st.success(f"Your balance after deposit is {st.session_state.acbal}")

    def withdraw(self):
        if st.session_state.count >= 3:
            st.error("Transaction limit is 3 times")
            return
        wit = st.number_input("Enter the amount to withdraw", min_value=1, step=1)
        if st.session_state.acbal < 500:
            st.error("Insufficient balance")
        elif wit < 100:
            st.error("Minimum amount to withdraw is 100")
        elif wit % 100 != 0:
            st.error("Amount should be a multiple of 100")
        elif wit > st.session_state.acbal:
            st.error("Withdraw amount should be less than account balance")
        elif wit > 20000:
            st.error("Transaction amount limit is 20000")
        else:
            st.session_state.acbal -= wit
            st.session_state.count += 1
            st.success(f"Your balance after withdrawal is {st.session_state.acbal}")

    def balance(self):
        st.success(f"Your current balance is {st.session_state.acbal}")

    def validate(self):
        for i in range(3, 0, -1):
            pin = st.number_input("Enter your PIN number", min_value=1, step=1)
            if st.button("enter"):
                if pin == 1234:
                    self.view_options()
                    break
                else:
                    if i == 1:
                        st.error("Card blocked")
                    else:
                        st.error(f"Invalid pin number. Attempts left: {i - 1}")

    def view_options(self):
        # Show buttons for different options
        if st.button("Deposit"):
            self.deposit()
        if st.button("Withdraw"):
            self.withdraw()
        if st.button("Balance"):
            self.balance()
        if st.button("Exit"):
            st.success("Exiting")
            st.stop()

# Create an object of Bank class
obj = Bank()
obj.validate()
