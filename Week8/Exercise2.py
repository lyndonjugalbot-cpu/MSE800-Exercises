from abc import ABC, abstractmethod

# Abstract
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

#The Notifications
class Email(Notification):
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMS(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class Push(Notification):
    def send(self, message):
        print(f"Sending PUSH notification: {message}")

#Abstract Factory
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

#The Factories
class EmailFactory(NotificationFactory):
    def create_notification(self):
        return Email()

class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMS()

class PushFactory(NotificationFactory):
    def create_notification(self):
        return Push()

def notify(factory: NotificationFactory, message: str):
    notification = factory.create_notification()
    notification.send(message)


#client
message = "Your booking is confirmed."
notify(EmailFactory(), f"{message}")
notify(SMSFactory(), f"{message}")
notify(PushFactory(), f"{message}")