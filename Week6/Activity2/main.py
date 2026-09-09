"""Employee Access Management System.

Several functions can only be used by authorised (logged-in) employees.
Instead of repeating the same authentication check inside every function,
a single @login_required decorator handles the access control.
"""

employee = {
    "name": "Lyndon Jugalbot",
    "logged_in": False,
}



#decorator to check if the employee is logged in before allowing access to certain functions
def login_required(func):
    """Only run the wrapped function when the current employee is logged in."""

    def wrapper(*args, **kwargs):
        if not employee.get("logged_in"):
            print(f"Access denied: '{func.__name__}' requires you to log in first.")
            return None  # Stop the original function from executing.
        
        return func(*args, **kwargs)
    return wrapper


#functions with deecorators to restrict access to logged-in employees
@login_required
def view_salary():
    print("Salary: $75,000 per year.")


@login_required
def view_personal_details():
    print(f"Name: {employee['name']} | Phone: 02904312345 | Address: 7/150 Victoria St, Onehunga, Auckland 1061")


@login_required
def download_report():
    print("Downloading annual_report.pdf ... completed.")


def login(employee):
    employee["logged_in"] = True
    print(f"{employee['name']} is now logged in.")


def logout(employee):
    employee["logged_in"] = False
    print(f"{employee['name']} is now logged out.")



#main program to demonstrate the login_required decorator in action
def main():
    print("--- Attempting access while logged OUT ---")
    view_salary()
    view_personal_details()
    download_report()

    print("\n--- Employee logs in ---")
    login(employee)

    print("\n--- Attempting access while logged IN ---")
    view_salary()
    view_personal_details()
    download_report()

    print("\n--- Employee logs out ---")
    logout(employee)
    view_salary()
    view_personal_details()
    download_report()


if __name__ == "__main__":
    main()
