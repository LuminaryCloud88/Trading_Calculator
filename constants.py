from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Trade:
    capital: float
    fees: float
    entry: float
    exit: float
    direction: str
    leverage: float
    risk: float
    subscribed: bool = False
    symbol: Optional[str] = field(default=None, repr=False)
    date: Optional[str] = field(default=None, repr=False)
    units: Optional[float] = field(default=None, repr=False)
    pnl_percentage: Optional[float] = field(default=None, repr=False)

    position_size: float = 0.0
    pnl: float = 0.0
    r_multiple: float = 0.0


help_text = """
--- Welcome to the help page ---
This page is to clarify what you should be inputing.

For capital, entry, exit, leverage, and risk;
just input the numbers in a decimal format (i.e. '2001.56').
Do not include symbols or any other characters besides the numbers and "." .

The risk/stop field currently only supports a number, NOT a percentage. 
If this field is left blank, the program will use your position size instead.

For fees, just type what maker or taker fees your trading platform has.
If the maker fees are .0012%, just type .0012. 
The percent sign is added automagically to the calculations. 

For direction just pick one of the options availiable.

"""