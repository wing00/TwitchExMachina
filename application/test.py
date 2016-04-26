import re

string = "[{'game': 'League of Legends'}, {'game': 'Counter-Strike: Global Offensive'}, {'game': 'Dota 2'}, {'game': 'Hearthstone: Heroes of Warcraft'}, {'game': 'Dark Souls III'}, {'game': 'Call of Duty: Black Ops III'}, {'game': 'Minecraft'}, {'game': 'Tom Clancy's The Division'}, {'game': 'World of Warcraft'}, {'game': 'Gaming Talk Shows'}, {'game': 'World of Tanks'}, {'game': 'Destiny'}, {'game': 'RuneScape'}, {'game': 'Street Fighter V'}, {'game': 'Overwatch'}, {'game': 'StarCraft II'}, {'game': 'FIFA 16'}, {'game': 'Creative'}, {'game': 'H1Z1: King of the Kill'}, {'game': 'Smite'}]"



print re.sub("'", '"', string)

[{"game": "League of Legends"}, {"game": "Counter-Strike: Global Offensive"}, {"game": "Dota 2"}, {"game": "Hearthstone: Heroes of Warcraft"}, {"game": "Dark Souls III"}, {"game": "Call of Duty: Black Ops III"}, {"game": "Minecraft"}, {"game": "Tom Clancy's The Division"}, {"game": "World of Warcraft"}, {"game": "Gaming Talk Shows"}, {"game": "World of Tanks"}, {"game": "Destiny"}, {"game": "RuneScape"}, {"game": "Street Fighter V"}, {"game": "Overwatch"}, {"game": "StarCraft II"}, {"game": "FIFA 16"}, {"game": "Creative"}, {"game": "H1Z1: King of the Kill"}, {"game": "Smite"}]
