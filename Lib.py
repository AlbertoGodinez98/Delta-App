from dataclasses import dataclass, field
from datetime import date
from logging import raiseExceptions


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
            case "remove" | "-":
                self.current_quantity -= quantity
            case _:
                raiseExceptions("Action can only be 'Add' or 'Remove'")

    def info(self) -> str:
        """Inv.info()
        Returns relevant information."""
        print(
            f"Created \"{self.name}\" on {self.day}. Current quantity is {self.current_quantity}")
