# A Trading Calculator That Takes Inputs from the User 
# Such as Capital, Fees, Entry, Exit Prices, Direction, Risk and Leverage
# Returns PnL % and $ and also R:R ratios
# Adds to list or Key-Value pair to show total calculations at the end
from user_inputs import inputs

def calculate_pnl(capital, fees, entry, exit, direction, leverage):
    controlled_capital = float(capital * leverage)
    calculated_fees = float(controlled_capital * fees)
    if direction == "long":
        pnl = float((exit - entry)*(controlled_capital / entry))
    elif direction == "short":
        pnl = float((entry - exit)*(controlled_capital / entry))
    
    pnl -= calculated_fees

    print(f" PnL: ${pnl:.2f}")

    return pnl, controlled_capital

#def r_multiples(entry, exit, controlled_capital, direction):
#    r_multiple = exit