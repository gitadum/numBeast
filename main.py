from func import calculationSerie, multiplicationTables

def main():
    calculationSerie(n=5, operator="onlyAdditionOrSubstaction")
    calculationSerie(n=5, nTerms=2, rangeTerm=(1,100),
                     operator="onlyMultiplicationOrDivision")
    multiplicationTables()

if __name__ == "__main__":
    main()