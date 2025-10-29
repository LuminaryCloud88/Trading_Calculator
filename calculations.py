# A Trading Calculator That Takes Inputs from the User 
# Such as Capital, Fees, Entry, Exit Prices, Direction, Risk and Leverage
# Returns PnL % and $ and also R:R ratios
# Adds to list or Key-Value pair to show total calculations at the end
# Add Units held (capital/entry)
from user_inputs import inputs

def calculate_pnl(capital, fees, entry, exit, direction, leverage, risk):
    position_size = float(capital * leverage)
    calculated_fees = float(position_size * fees)
    if direction == "long":
        pnl = float((exit - entry)*(position_size / entry))
    elif direction == "short":
        pnl = float((entry - exit)*(position_size / entry))
    
    pnl -= calculated_fees
    r_multiple = calculate_r_multiples(pnl, risk)

    print("\n --- Your Trade Summary ---")
    print(f" Your position size is: {position_size:.2f}")
    print(f" PnL: ${pnl:.2f}")
    print(f" Risk:Reward Ratio is: {r_multiple:.2f}")

    return pnl, position_size, r_multiple

def calculate_r_multiples(pnl, risk):
    r_multiple = pnl / risk
    return r_multiple