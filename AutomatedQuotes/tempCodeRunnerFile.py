for x in wl:
        if (x == d[0]):
            index = wl.index(d[0])
            tictosend = tickers[index]
    for x in tictosend:
        price = str(finnhub_client.quote(x)['c'])
        percent_change = str(finnhub_client.quote(x)['dp'])
        change = str(finnhub_client.quote(x)['d'])
        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
        wl_result.append(end)

    wl_result_str ="".join(map(str,wl_result))