from .models import Buyer, Game

buyer1 = Buyer.objects.create(name="Olya", balance=999.00, age=20)
buyer2 = Buyer.objects.create(name="Kolya", balance=888.00, age=16)
buyer3 = Buyer.objects.create(name="Tim", balance=900.00, age=19)

game1 = Game.objects.create(title="Game A", cost=59.99, size=5.5, description="The walker game.", age_limited=False)
game2 = Game.objects.create(title="Game B", cost=49.99, size=5.0, description="The adventure game.", age_limited=True)
game3 = Game.objects.create(title="Game C", cost=39.99, size=4.5, description="The maze game.", age_limited=True)

game1.buyers.set([buyer1, buyer2, buyer3])
game2.buyers.set([buyer1, buyer3])
game3.buyers.set([buyer1, buyer3])