# A Trading Calculator That Takes Inputs from the User 
# Such as Capital, Fees, Entry, Exit Prices, Direction, Risk and Leverage
# Returns PnL % and $ and also R:R ratios
# Adds to list or Key-Value pair to show total calculations at the end

def inputs():
    while True:
        capital = float(input("Enter amount used to trade: $"))
        fees = float(input("Enter your maker or taker fees (as %): ")) * 2
        entry = round(float(input("Enter your entry price: ")), 2)
        exit = round(float(input("Enter your exit price: ")), 2)
        direction = input("Enter either long or short: ").lower()
        leverage = float(input("Enter leverage here. If none was used, simply type 1: "))

        print("\n --- Your Trade Summary ---")
        print(f">Capitial: ${capital}")
        print(f">Fees: {fees}%. Calculated for entry and exit.")
        print(f">Entry Price: {entry}")
        print(f">Exit Price: {exit}")
        print(f">Direction of Trade: {direction}")
        print(f">Leverage: {leverage}x")

        final = input("\n Does this look correct? (yes/no)").strip().lower()
        
        if final in ["yes", "y"]:
            return capital, fees, entry, exit, direction, leverage
        elif final in ["no", "n"]:
            print("\nLet's try again...\n")
            continue
        else:
            print("\nInvalid response. Please type 'yes' or 'no'.\n")