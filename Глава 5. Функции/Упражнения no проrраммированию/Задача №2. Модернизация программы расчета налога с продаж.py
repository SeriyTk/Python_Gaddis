import Mod2
FEDERAL_TAX = 0.05
REGIONAL_TAX = 0.025
TOTAL = 0


def Sales_tax():
    total = Mod2.condition(TOTAL)
    federal_tax, regional_tax, total_tax, total_sum = Mod2.result(total, FEDERAL_TAX, REGIONAL_TAX)
    Mod2.printo(total, federal_tax, regional_tax, total_tax, total_sum)

if __name__ == '__main__': Sales_tax()
