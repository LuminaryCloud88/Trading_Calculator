# A Trading Calculator That Takes Inputs from the User 
# Such as Capital, Fees, Entry, Exit Prices, Direction, Risk and Leverage
# Returns PnL % and $ and also R:R ratios
# Add Units held (capital/entry)
from user_inputs import inputs
from constants import Trade

def basic_metrics(trade: Trade) -> Trade:
    
    position_size = float(trade.capital * trade.leverage)
    calculated_fees = float(position_size * trade.fees)
    if trade.direction == "long":
        pnl = float((trade.exit - trade.entry)*(position_size / trade.entry))
    elif trade.direction == "short":
        pnl = float((trade.entry - trade.exit)*(position_size / trade.entry))
    
    pnl -= calculated_fees
    r_multiple = calculate_r_multiples(pnl, trade.risk)

    trade.position_size = position_size
    trade.pnl = pnl
    trade.r_multiple = r_multiple

    if trade.subscribed == True:
        calculate_premium_metrics(trade)

    return trade

def calculate_r_multiples(pnl: float, risk: float) -> float:
    return pnl / risk

# Basic metrics with units and pnl ratio
# def calculate_premium_metrics(trade: Trade):
