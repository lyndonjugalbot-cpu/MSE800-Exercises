"""
Admin menu module.

Provides the menu shown to an administrator after logging in, giving
access to car and booking management features via CarService and
BookingService.
"""

import sys
from cli import booking_management_menu, car_management_menu
from cli.messages import GOODBYE, INVALID_OPTION

def run(admin, car_service, booking_service):
        """Show the admin menu in a loop until they log out or exit."""

        while True:
            print(f"\n=== Welcome, {admin.full_name}! (Admin) ===")
            print("1. Manage Cars")
            print("2. Manage Bookings")
            print("3. Logout")
            print("4. Exit")
            choice = input("Choose an option").strip()

            if choice == "1":
                car_management_menu.run(admin, car_service)
            elif choice == "2":
                booking_management_menu.run(admin, booking_service)
            elif choice == "3":
                return
            elif choice == "4":
                print(GOODBYE)
                sys.exit(0)
            else:
                print(INVALID_OPTION)
                