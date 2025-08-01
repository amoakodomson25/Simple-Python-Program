def sort_asc():
    print()
    print("chi square test of homogenity")
    print("_______________________________________")


    def chisquare():
            while True:
                try:
                    probabilities = list(map(float, input("Enter probabilities of categories: ").split()))
                    frequncies = list(map(float, input("Enter frequencies of categories: ").split()))

                    if len(probabilities) == len(frequncies):
                        E = []
                        for i in range(len(probabilities)):
                            E.append(probabilities[i] * sum(frequncies))
                        print(E)
                        

                        SUM = []
                        for i in range(len(frequncies)):
                            SUM.append(((frequncies[i] - E[i])**2) / E[i])

                        result = round(sum(SUM), 2)
                        print(result)
                    elif len(probabilities) != len(frequncies):
                        print("The lengths of probabilities and frequencies are not the same")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number")    
    chisquare()
sort_asc()
