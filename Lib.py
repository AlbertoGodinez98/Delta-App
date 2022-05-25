from dataclasses import dataclass, field
from datetime import date
import logging
import PySimpleGUI as sg

logging.basicConfig(level=logging.INFO, filename="logging.log",
                    filemode="w", format="%(asctime)s - %(message)s")


@dataclass
class Inv():
    """Inv(name: str, current_quantity: int, day = date.today())"""
    name: str
    current_quantity: int = field(default=0)
    day: str = field(default=date.today())

    def __post_init__(self) -> None:
        return f"Created \"{self.name}\" on {self.day}"

    def operation(self, quantity: int = 0, action: str = "+") -> None:
        """Inv.operation(quantity: int, action: str)
        Admitted actions are: "Add", "Remove", "+", "-\""""
        match action.lower():
            case "add" | "+":
                self.current_quantity += quantity
                logging.info(
                    f"Added   {quantity} to   \"{self.name}\". Current quantity is {self.current_quantity}")
            case "remove" | "-":
                self.current_quantity -= quantity
                logging.info(
                    f"Removed {quantity} from \"{self.name}\". Current quantity is {self.current_quantity}")
            case _:
                logging.raiseExceptions("Action can only be 'Add' or 'Remove'")
                logging.error("Error - Invalid action")

    def info(self) -> str:
        """Inv.info()
        Returns relevant information."""
        print(
            f"Created \"{self.name}\" on {self.day}. Current quantity is {self.current_quantity}")

    def show(self) -> None:
        sg.Window(title="Hello world", layout=[[]], margins=(100, 50)).read()
