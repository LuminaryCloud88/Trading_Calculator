# A Trading Calculator That Takes Inputs from the User 
# Such as Capital, Fees, Entry, Exit Prices, Direction, Risk and Leverage
# Returns PnL % and $ and also R:R ratios
# Adds to list or Key-Value pair to show total calculations at the end
from user_inputs import inputs
from calculations import *
def main():
    calculate_pnl(*inputs())

if __name__ == "__main__":
    main()