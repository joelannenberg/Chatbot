from yahoo_finance import Share

prompt = "Please enter: <ticker> <command>"

# Conversation
while (True):
    # Grab user input and prompt
    inputstr = raw_input(prompt+"\n")
    #inputstr = "What is the largest company by market cap?"
    strArray = inputstr.split()
    ticker = strArray[0]
    command = strArray[1]

    # Keep record of input
    pastArray = []
    pastArray.append(inputstr)

    # Debugging
    #print strArray
    #print pastArray
    stock = Share(str(ticker))
    if (command == "price"):
        print "The share price is currently $" + stock.get_price()
    elif (command == "marketcap"):
        print "The market capitalization is $" + stock.get_market_cap()
    elif (command == "PEratio"):
        print "The P/E ratio is " + stock.get_price_earnings_ratio()
    elif (command == "ebitda"):
        print "The EBITDA is " + stock.get_ebitda()
    else:
        print "I do not recognize that command"
    print "------------------------------------------------------------"
