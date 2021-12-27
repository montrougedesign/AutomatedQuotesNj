                if receivedticker_up == 'WL1':
                    ABR_P = str(finnhub_client.quote('ABR')['c'])
                    ABR_PC = str(finnhub_client.quote('ABR')['dp'])
                    ABR_PRC = str(finnhub_client.quote('ABR')['pc']) 
                    ABR_C = str(finnhub_client.quote('ABR')['d'])

                    ABR_ALL = 'ABR' + "\n" + "Price  " + "$" + ABR_P + "\n" + "Change  " + "$" +ABR_PC + "\n" + "Percent Change  " + ABR_PRC + "%" "\n" + "Previos close  " + "$"+ ABR_C

                    print(time.asctime() + '\n' +From_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', From_ ,ABR_ALL)

                    print(ABR_ALL)



                else: 
                    print()