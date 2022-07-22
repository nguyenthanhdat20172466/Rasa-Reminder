# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,AllSlotsReset, ReminderScheduled, ReminderCancelled

class ActionUpdatePhoneNumber(Action):

    def name(self) -> Text:
        return "action_update_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone_number = tracker.get_slot('phone_number')
        email_address = tracker.get_slot('email_address')
        print("phone_number=",phone_number)
        print("email_address=",email_address)
        text=tracker.latest_message['text']
        print("action_update_information.text=",text)
        dispatcher.utter_message(text=f"Hello Your information is up to date Phone={phone_number}; Email={email_address}")
        return [SlotSet("phone_number",None),SlotSet("email_address",None)]
#        return [AllSlotsReset()]      

class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message("I will remind you in 0.5 minutes.")

        date = datetime.datetime.now() + datetime.timedelta(seconds=30)
        entities = tracker.latest_message.get("entities")

        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=True,
        )
        return [reminder]
class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        #name = tracker.get_slot("name")
        dispatcher.utter_message("Bạn còn cần gì ko?")

        return [AllSlotsReset()]
# class ActionCancelReminder(Action):
#     """Cancels all reminders."""

#     def name(self) -> Text:
#         return "action_forget_reminders"

#     async def run(
#         self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:

#         #dispatcher.utter_message(f"Okay, I'll cancel all your reminders.")

#         # Cancel all reminders
#         return [ReminderCancelled()]