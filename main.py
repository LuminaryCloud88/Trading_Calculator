# A Trading Calculator That Takes Inputs from the User 
# Such as Capital, Fees, Entry, Exit Prices, Direction, Risk and Leverage
# Returns PnL % and $ and also R:R ratios
# Adds to list or Key-Value pair to show total calculations at the end
# Free version uses user input shown above to show you your pnl and r multiples
# Pro version will let you save trades to a database to track your w/l ratio and keep track of multiple trades
# Run if, else statement in main loop to check if subscribed and if not only give access to the free version
from interface_layout import free_metrics_window

def main():
    free_metrics_window()

if __name__ == "__main__":
    main()