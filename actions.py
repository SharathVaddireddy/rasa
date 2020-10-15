# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
import requests


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print(f"Link >>>> {tracker.slots.get('LINK')}")
#         print(tracker.latest_message)
#         dispatcher.utter_message(text="Hello World updated!")
#
#         return []


class ActionInfo(Action):
    def name(self) -> Text:
        return "action_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(f"Slot acc number >> {tracker.slots.get('ACCOUNT')}")
        response = requests.get(f'http://localhost:8000/cus/get/{tracker.slots.get("ACCOUNT")}').json()
        print(response)
        if response['success']:
            data = response['data']
            account = data['account']
            balance = account['balance']
            dispatcher.utter_message(text=f"Your balance is: {balance}")
        else:
            dispatcher.utter_message(text="Account number is invalid")
        return []