#Ez egy blackjack magyarul, 21 python kódja
import random
player = []
dealer = []

for i in range(2):
    player.append(random.randint(1, 11))
print("te lapjaid", sum(player),player)

for i in range(2):
    dealer.append(random.randint(1, 11))
print("Dealernek van (x) és",dealer[1])


if sum(dealer) == 21:
    print("Dealernek 21-e van pontosan, ezért vesztettél")
elif sum(dealer) > 21:
    print("Dealernek többet érnek a lapjai mint 21 ezért vesztett")

while sum(player) < 21:
        player_input = str(input("Válassz,kérsz lapot vagy megállsz?(kerek/megallok)"))
        if player_input == "kerek":
                player.append(random.randint(1, 11))
                print("te lapjaid", sum(player),player)
        else:
                print("a lapjaid:",player,sum(player))
                print("a dealer lapjai:",dealer,sum(dealer))
                if sum(dealer) > sum(player):
                    print("Dealer lapja többet ér ezért nyert")
                else:
                    print("Nyertél, lapjaid többet érnek mint a dealernek")
                    break
if sum(player) > 21:
    print("Vesztettél többet ér a lapod mint 21")
elif sum(player) == 21:
    print("pontosan 21-ed van nyertél")
elif sum(player) == sum(dealer):
    print("döntetlen")