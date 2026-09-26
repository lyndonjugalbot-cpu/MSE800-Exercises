from travelpackage import TravelPackageBuilder

# Fluent chaining — each call returns self, so calls can stack:
package = (
    TravelPackageBuilder()
    .set_destination("Melbourne")
    .set_hotel("4-star")
    .set_transport("Train")
    .set_meal_plan("Breakfast")
    .add_activity("Museum")
    .add_activity("City Tour")
    .add_activity("Beach")
    .set_insurance(True)
    .build()
)
package.show_package()