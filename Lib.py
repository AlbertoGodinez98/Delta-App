from cmath import log
from dataclasses import dataclass, field
from datetime import date
import logging


logging.basicConfig(level=logging.INFO, filename="logging.log",
                    filemode="a", format="%(asctime)s - %(message)s")


@dataclass
class Inv():
    """Inv(name: str, current_quantity: int, day = date.today())"""
    name: str
    current_quantity: int = 0
    day: str = date.today()

    def operation(self, quantity: int = 0, action: str = "+") -> None:
        """Inv.operation(quantity: int, action: str)
        Admitted actions are: "Add", "Remove", "+", "-\""""
        match action.lower():
            case "add" | "+":
                self.current_quantity += quantity
                logging.info(
                    f"Added   {quantity}. Current quantity is {self.current_quantity}")
            case "remove" | "-":
                self.current_quantity -= quantity
                logging.info(
                    f"Removed {quantity}. Current quantity is {self.current_quantity}")
            case _:
                logging.raiseExceptions("Action can only be 'Add' or 'Remove'")
                logging.error("Error - Invalid action")

    def info(self) -> str:
        """Inv.info()
        Returns relevant information."""
        print(
            f"Created \"{self.name}\" on {self.day}. Current quantity is {self.current_quantity}")
        logging.info(
            f"Created \"{self.name}\" on {self.day}. Current quantity is {self.current_quantity}")
