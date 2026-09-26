class TravelPackage:
    def __init__(self, destination, hotel, transport, meal_plan, activities, insurance):
        self.destination = destination
        self.hotel = hotel
        self.transport = transport
        self.meal_plan = meal_plan
        self.activities = activities
        self.insurance = insurance

    def show_package(self):
        print("Destination:", self.destination)
        print("Hotel:", self.hotel)
        print("Transport:", self.transport)
        print("Meal Plan:", self.meal_plan)
        print("Activities:", ", ".join(self.activities) if self.activities else "None")
        print("Insurance:", "Yes" if self.insurance else "No")


class TravelPackageBuilder:
    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.meal_plan = "None"
        self.activities = []
        self.insurance = False

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_hotel(self, hotel):
        self.hotel = hotel
        return self

    def set_transport(self, transport):
        self.transport = transport
        return self

    def set_meal_plan(self, meal_plan):
        self.meal_plan = meal_plan
        return self

    def add_activity(self, activity):
        self.activities.append(activity)
        return self

    def set_insurance(self, insurance):
        self.insurance = insurance
        return self

    def build(self):
        return TravelPackage(
            self.destination, self.hotel, self.transport,
            self.meal_plan, self.activities, self.insurance
        )
