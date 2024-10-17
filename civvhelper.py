import tkinter as tk
from tkinter import ttk
import webbrowser

# Define the notes for each civilization
civ_notes = {
    "America": """
Start bias
None.

Unique Ability: Manifest Destiny
Tiles cost 50% less gold to buy
Military land units have +1 sight

Unique Unit I: Minuteman (Replaces the Musketman)
Ignores terrain movement costs (keeps on upgrade)
Gives Golden Age points on a kill equal to the opposing unit's strength, or ranged strength if it's higher (keeps on upgrade)
Drill I - 15% combat bonus in rough terrain (keeps on upgrade)

Unique Unit II: B17 (Replaces the Bomber)
70 ranged strength, up from 65
Siege I - +33% attack vs. cities (keeps on upgrade)
Evasion - -50% damage from being intercepted (keeps on upgrade)

Strategy

America does best at domination victories.

America's sight advantage makes them excellent at scouting out terrain early on to find ancient ruins, city locations, natural wonders and other Civs. Once you've got some cash, you can cheaply buy high-yield tiles near your cities to get them growing, or try settling near another Civ and buying tiles to block them from expanding.

Try to get Minutemen going as soon as possible, backed with either Trebuchets, Crossbows or Cannons. With just an Armoury, Minutemen can start with Siege to do decent damage to cities, or Cover II to stay defended against them. Ignoring terrain costs means they can easily slip through and flank enemies.

If one round of war isn't enough, America can go again in the Atomic era with their powerful B17s. A Military Academy and either Autocracy's Total War tenet or the Brandenburg Gate will let you build new B17s immediately with Logistics, letting them attack twice in one turn. Fill some Carriers with B17s, bring some Destroyers and Battleships to escort them and you'll have a very deadly end-game navy.

Social Policy trees	
1. Liberty
2. Commerce or Exploration
3. Rationalism

Ideology	Autocracy or Order
Religion	Pantheon: Faith Pantheons or Faith Healers
Founder:    Tithe or Church Property
Follower:   Any happiness bonuses
Enhancer:   Messiah if you have Faith Healers, Religious Texts or Itinerant Preachers otherwise.

Key wonders	
Statue of Zeus
Angkor Wat
Notre Dame
Brandenburg Gate
Kremlin or Prora
Pentagon

Summary of key strengths
Early exploration
Combat in rough terrain
End-game warfare
""",

    "Arabia": """
Start bias
Desert.

Unique Ability: 
Ships of the Desert
Caravans have a 50% increased range
Trade routes spread the home city's religion (the majority religion in the city the trade route was sent from) twice as effectively
Oil resources you're personally producing provide double their normal quantities
Resources from trading or from allied City-States are not doubled in quantity.
This stacks with the Third Alternative tenet from the Autocracy ideology to create quadruple quantities of oil.

Unique Unit: 
Camel Archer (Replaces the Knight)
Classified as a ranged unit rather than a mounted unit, therefore is built faster with the Temple of Artemis and has no vulnerability to Pikemen
Instead of a melee attack, has a ranged attack with 21 strength and a range of 2 tiles.
17 melee strength, down from 20
No city attack penalty

Unique Building: 
Bazaar (Replaces the Market)
Provides 1 extra copy of every improved luxury resource near the city (in your land and within a three tile radius)
2 gold generated per turn, up from 1
Increases gold yield by 2 for every oasis or oil tile worked by the city

Strategy

Arabia does best at diplomatic or domination victories.

Arabia begins peacefully. Expand fairly quickly and get a faith and trade route infrastructure going. Your Caravans can travel further than those of other Civs, and therefore will make more money. Once you have a religion, stack pressure bonuses (e.g. Religious Texts) and the spread of your faith will be hard to stop.

Before you convert the world, however, you have a strong opportunity to conquer it with the Camel Archer. Camel Archers can move in range of cities, fire at them and move out of range of their attacks, allowing them to do a great deal of damage without being harmed themselves. They cannot capture cities themselves, so use a couple of unpromoted Horsemen to get the last hit.

If war isn't for you, Arabia's huge oil quantities and the Bazaar's doubling of luxury resources puts you in a good position as a trader. Trade other Civs for gold, and you can use that money to bribe City-States for delegates at the United Nations, and from there get diplomatic victory.

Social Policy trees	
1. Liberty
2. Piety, Patronage (diplomacy) or Commerce (domination)
3. Commerce (diplomacy) or Rationalism (domination)
Ideology	Freedom (diplomacy) or Autocracy (domination)
Religion	Pantheon: Desert Folklore or other faith Pantheons
Founder: Tithe or Church Property or Papal Primacy (diplomacy)
Follower: Any happiness bonuses
Enhancer: Religious Texts
Reformation: Jesuit Education or To the Glory of God or Charitable Missions (diplomacy)

Key wonders	
Petra
Great Mosque of Djenne
Notre Dame (domination)
Forbidden Palace (diplomacy)
Big Ben (domination)
Neuschwanstein

Summary of key strengths
Reasonable gold output
Fast religious spread, especially if using the start bias with Desert Folklore
Very effective mid-game warfare

""",

    "Assyria": """
Start bias:
Avoid tundra.

Unique Ability: Treasures of Nineveh
- Gain a random technology when conquering enemy cities.
- Can only gain technologies the enemy has but you don't.

Unique Unit: Siege Tower (Replaces the Catapult)
- Melee unit that can only attack cities.
- Grants a 50% attack bonus to friendly units within 2 tiles.

Unique Building: Royal Library (Replaces the Library)
- +1 Great Writing slot.
- +10XP to units built in the city with the slot filled.

Strategy:
Assyria's best at domination and scientific victories, and isn't bad at culture either.

Assyria's a fun Civ that thrives in unusual playstyles. With the powerful Siege Tower UU, it's one of the few Civs which has a real edge to early-game conquests. Work towards getting Mathematics early along with Construction for Composite Bowmen, followed by building a couple of Siege Towers along with about four Composite Bowmen. Don't waste time building wonders at this point, and Barracks are likely to be not worth the cost. Siege Towers do massive damage against cities, and cities they're next to will be vulnerable to your other units.

For most Civs, going to war often means your infrastructure (and hence your science) lags behind, but as Assyria gains technologies from conquest, they can just keep pushing for military technologies to keep their armed forces ahead, using war to catch up with the more peaceful technologies you missed.

The Royal Library is the odd one out of Assyria's uniques. Although filling the Great Writing slot gives +10XP for all units built in the city, that won't ever be worth an extra starting promotion unless the city has no other XP boosts. Instead, its main advantage is the slot itself - Great Writing slots get quite scarce by the end of the game relative to the number of Great Works you may have generated. This can be helpful for maximising your culture or tourism potential.

So, you have three routes. Either just carry on with war to a domination victory, use the science advantage to a scientific victory, or use your extra slots and conquered Great Works to a cultural victory.

Social Policy Trees:
1. Honour
2. Aesthetics or Commerce
3. Rationalism

Ideology: Autocracy or Order
""",

    "Austria": """
Start bias
Hills.

Unique Ability: 
Diplomatic Marriage
If a City-State is allied to you and has been for 5 consecutive turns, you may spend gold to annex or puppet it into your empire.
The turn you first allied with the City-States does not count as one of the 5 consecutive turns.
The cost of the City-State scales with the number of units they control (starting at 500 gold with no units in normal-speed games.) All the units controlled by the City-State (including ones outside their own lands) become under your control. If the City-State has more than one city, you will gain them all.
All buildings present in the City-State are retained on puppeting or annexation.
Annexed City-States do not count as occupied, and as such creates no more unhappiness than puppeting the city.
The annexed or puppeted City-State loses its original capital status, and hence is able to be razed by rivals and is unable to become a City-State once more. The number of delegates needed to win diplomatic victory is adjusted accordingly.
Annexing or puppeting a mercantile City-State destroys their unique luxuries.

Unique Unit: Hussar (Replaces Cavalry)
5 movement points, up from 4
3 sight, up from 2
+50% flanking bonus - +15% instead of +10% strength bonus for every friendly unit adjacent to the enemy your unit is fighting (keeps on upgrade)
Does not affect the flanking bonus received by other units, such as an adjacent Rifleman.

Unique Building: Coffee House (Replaces the Windmill)
10% production bonus for buildings removed
5% production bonus for all uses
Can be built in any city, not just those on flat land
25% Great Person Points bonus

Strategy

Austria does best at domination victories, but is very capable at science and culture as well.

It takes some time to get Austria's uniques going, but starting off by building tall (and taking the Tradition tree) isn't a bad idea. Generally, you should aim to get the National College up before turn 100 (and before you start annexing City-States) so you can get your science off to a good start - it'll be useful no matter your eventual victory path. On the road to Coffee Houses, make a diversion first to Education for Universities, and be sure to pick up a couple of policies from the Patronage tree - you'll need to hold alliances if you want to annex City-States, and Patronage makes that much easier.

Coffee Houses are nice for acting like a second Garden, but perhaps even more useful is their lack of restriction as to where you can build them. This means you can more easily exploit their production bonuses ready for Hussars and Artillery. The flanking bonuses of Hussars makes them able to deal with most same-era units if they can surround them, while Artillery deal with city defences. Even if you want to just focus on your Great Person bonuses towards culture or science, it's worth going to war to bring rivals down a peg.

Once Airports are up, you can invade other continents without even needing much of a navy whatsoever - saving you a lot of gold, production and oil. Simply ally with a City-State on the new continent, annex it, and start airlifting your units in. Upgraded Hussars may lose their speed and sight bonuses, but Autocracy's Lightning Warfare makes flanking bonuses even easier to attain due to the fact they can ignore zone of control. Bring some anti-air units and some kind of siege weapon and you'll be hard to stop.

Social Policy trees	
1. Tradition
2. Mix of Patronage and Commerce
3. Rationalism
Ideology	Autocracy (culture and domination) or Freedom (culture and science)
Order (science)
Religion	Pantheon: Faith Pantheons or Sacred Waters
Founder: Tithe or Church Property or Papal Primacy
Follower: Divine Inspiration and Religious Community (culture and science), any happiness bonus (domination)
Enhancer: Reliquary or Religious Unity

Key wonders	
Any theming bonus wonder (culture)
Mausoleum of Halicarnassus
Temple of Artemis
Hanging Gardens
Alhambra
Machu Picchu
Notre Dame (domination)
Leaning Tower of Pisa
Big Ben
Brandenburg Gate
Eiffel Tower (culture)
Kremlin or Prora or Statue of Liberty
Neuschwanstein (domination)
Pentagon (domination)

Summary of key strengths

Flexible - can pursue any victory route except diplomacy effectively
Consistent late-game production
Can reduce the contribution of City-States in the World Congress, setting back diplomatic Civs in the long-run
Can pull off late-game intercontinental warfare without a navy
""",

    "Aztec": """
Start bias
Jungle.

Unique Ability: Sacrificial Captives

When killing any enemy unit, gain culture equal to the unit's strength, or ranged strength if it's higher
This works in a similar way to the Honour opener (but for all units instead of just Barbarians) and stacks with it.

Unique Unit: 
Jaguar (Replaces the Warrior)
33% extra strength in forest and jungle (keeps on upgrade)
Woodsman - Double movement rate through forest and jungle (keeps on upgrade)
25 health restored on a kill (keeps on upgrade)

Unique Building: 
Floating Gardens (Replaces the Water Mill)
Can be built in cities adjacent to lakes as well as rivers
1 maintenance cost, down from 2
+15% food bonus
+2 food to every lake tile worked by the city
Does not affect the Lake Victoria natural wonder

Strategy

The Aztecs are best at domination and scientific victories.

Start by taking the Honour opener and killing Barbarians with your Jaguars. The culture you'll get allows you to push ahead through the Tradition tree quickly, which nicely complements the Floating Gardens. Floating Gardens offer a considerable food bonus (unlike a growth bonus, it applies to all food output in the city, not just surplus) making it easy to build tall. Together with your jungle start bias, you can get quite an edge on science.

For the rest of the game, the key is to balance war with science. Don't neglect one when going for the other, or you won't get the full potential out of your uniques. Take some time to build up a tech advantage, then go to war. If you're playing scientifically, it's best not to take too many cities to avoid the diplomatic penalties associated with it (and hence the loss of potential research agreements.) If you're going for domination, make sure you can handle what you take and raze what you can't manage.

Social Policy trees	
1. Honour Opener and Tradition
2. Honour
3. Rationalism
Ideology	Order (domination) or Freedom (science)
Religion	Pantheon: Faith Pantheons or food Pantheons or Sacred Path
Founder: Tithe or World Church
Follower: Swords into Plowshares or Feed the World and Religious Community
Enhancer: Religious Texts or Defender of the Faith

Key wonders	
Great Library
Temple of Artemis
Hanging Gardens
Leaning Tower of Pisa
Porcelain Tower
Kremlin or Statue of Liberty
Great Firewall
Hubble Space Telescope (science)

Summary of key strengths
Strong, early UU minimises the threat of Barbarians and offers decent exploration potential
Fast city growth
UA ensures you can salvage rewards out of a war in stalemate
""",

    "Babylon": """
Start bias
Avoid tundra.

Unique Ability: 
Ingenuity
Receive a free Great Scientist with the Writing technology
This does not increase the cost of future Great Scientists, Engineers or Merchants.
50% bonus to Great Scientist generation
This stacks additively with other bonuses, so if you had just this and a Garden in a city, it would have a 75% bonus to Great Scientist generation.

Unique Unit: 
Bowman (Replaces the Archer)
7 strength, up from 5
9 ranged strength, up from 7

Unique Building: 
Walls of Babylon (Replaces Walls)
Costs 65 production, down from 75
Provides 6 city strength, up from 5
Provides 100 city HP, up from 50

Strategy

Babylon is best at scientific victories.

Get Writing immediately. Then, use the Great Scientist to place an Academy (preferably adjacent to your capital so it can't easily be pillaged.) This will give you a huge science bonus over anyone else for quite some time, allowing you to rush through the early eras. After you've cleaned up your Worker technologies, push on towards Education so you can get Universities and their scientist slots filled. Keep creating Academies with the Great Scientists you gain until the modern era. Then, hang on to them until 8 turns after you've built Research Labs, and start using them to rush technologies instead. The 8 turn gap seems strange, but the amount of science you get from Great Scientists is based on the output of the last 8 turns.

If all this science is worrying your neighbours, your other uniques can help defend yourself. Walls of Babylon give your cities two-thirds more health rather than a third making them much harder to take over, while Bowmen are roughly mid-way between Archers and Composite Bowmen, allowing you to have an adequate defence without having to take a diversion to Construction.

For a change of strategy, Bowmen also make good early rushing units. Take a few along with a couple of Warriors or Spearmen, and you may be able to take out an unprepared rival. An early captured capital is a significant advantage which will make eventual scientific victory even easier.

Social Policy trees	
1. Tradition
2. Commerce
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or food Pantheons
Founder: Tithe or Interfaith Dialogue
Follower: Swords into Plowshares or Feed the World and Religious Community or Guruship
Enhancer: Religious Texts or Reliquary

Key wonders	
Great Library
Mausoleum of Halicarnassus
Temple of Artemis
Hanging Gardens
Leaning Tower of Pisa
Porcelain Tower
Red Fort
Statue of Liberty
Great Firewall
Hubble Space Telescope

Summary of key strengths
Strongest early-game science
Extremely strong early-game defensive potential, combined with early scientific advantages, this makes Babylon very hard to attack
""",

 "Brazil": """
Start bias:
Jungle.

Unique Ability: Carnival
- +100% Tourism during Golden Ages (stacks multiplicatively with other bonuses).
- +50% Great Person Points for Writers, Artists, and Musicians during Golden Ages.

Unique Unit: Pracinha (Replaces Infantry)
- Gives Golden Age points on a kill equal to the unit's strength.

Unique Improvement: Brazilwood Camp (Requires Machinery)
- Can only be built on resourceless jungles.
- Yields 2 gold.
- +2 culture with Acoustics.

Strategy:
Brazil excels at cultural victories. Focus on infrastructure early on, build guilds, and time Golden Ages with tourism boosts for maximum impact.

Social Policy Trees:
1. Tradition
2. Aesthetics
3. Rationalism

Ideology: Freedom
Religion: Faith Pantheons, Sacred Path, Tithe, Religious Community.
""",

    "Byzantium": """
Start bias:
Coastal.

Unique Ability: Patriarchate of Constantinople
- Choose an extra belief when founding a religion (not including Reformation beliefs).
- Gain +20 points towards founding a religion.

Unique Unit I: Dromon (Replaces Trireme)
- Ranged naval unit with 10 strength and 2-tile range.
- +50% bonus vs naval units.

Unique Unit II: Cataphract (Replaces Horseman)
- 3 moves, down from 4.
- 15 strength, up from 12.
- Can receive defensive bonuses.

Strategy:
Byzantium is highly flexible. Focus on founding a religion early and build your strategy around the chosen belief bonuses.

Social Policy Trees:
1. Piety or Honour (domination)
2. Aesthetics or Commerce
3. Rationalism

Ideology: Autocracy (domination) or Order
Religion: Papal Primacy, Tithe, Mosques, Religious Texts.
""",

    "Carthage": """
Start bias:
Coastal.

Unique Ability: Phoenician Heritage
- All coastal cities get free Harbours.
- Land units can walk on mountains after gaining a Great General (take 50 HP damage if ending turn on a mountain).

Unique Unit I: Quinquereme (Replaces Trireme)
- 13 strength, up from 10.

Unique Unit II: African Forest Elephant (Replaces Horseman)
- 14 strength, up from 12.
- Feared Elephant: -10% combat penalty for adjacent enemy units.

Strategy:
Carthage is best at diplomatic and domination victories. Use free Harbours for early economic boosts and explore the map aggressively.

Social Policy Trees:
1. Liberty or Honour
2. Patronage (diplomacy) or Exploration (domination)
3. Rationalism

Ideology: Autocracy or Order
Religion: Messenger of the Gods, Religious Texts.
""",

    "Celts": """
Start bias:
Forest.

Unique Ability: Druidic Lore
- +1 faith for cities with at least one adjacent unimproved forest.
- +2 faith for cities with three or more adjacent unimproved forests.

Unique Unit: Pictish Warrior (Replaces Spearman)
- Gains faith on kills equal to half the enemy unit's strength.
- +20% combat bonus outside your territory.

Unique Building: Ceilidh Hall (Replaces Opera House)
- +3 local happiness.

Strategy:
The Celts excel at cultural victories but can pursue multiple victory paths thanks to early religious bonuses. Build wide and focus on faith generation.

Social Policy Trees:
1. Liberty or Piety
2. Aesthetics or Rationalism
3. Piety or Aesthetics

Ideology: Order
Religion: God-King, Pilgrimage, Religious Art, Sacred Sites.
""",

    "China": """
Start bias
None.

Unique Ability: 
Art of War
Great Generals contribute a 30% bonus to combat for land units within 2 tiles, up from 15%
Experience from land-based combat contributes 50% more towards the generation of Great Generals

Unique Unit: 
Chu-Ko-Nu (Replaces the Crossbowman)
14 ranged strength, down from 18 (-22%)
May attack twice (keeps on upgrade)

Unique Building: 
Paper Maker (Replaces the Library)
0 maintenance cost, down from 1
+2 gold

Strategy

China is best at domination victories.

Arguably the easiest Civ in the game to pick up and play, China has simple but effective (and fun) uniques to get you to world conquest. At first, work towards the Writing technology and the Liberty Social Policy tree for your Paper Makers and to help with early expansion respectively. Aside from Libraries being important buildings anyway for their contribution to science, Paper Makers also offer a valuable source of early gold, ready for supporting Chu-Ko-Nu-led armies later on.

You'll want to get the Machinery technology quickly, but you'll also need something with a melee attack to go with your Chu-Ko-Nu, seeing as they can't capture cities. Knights, Pikemen or even Horsemen will do. Even if you don't have a Great General to begin with, Chu-Ko-Nu can rapidly earn them as attacking twice in a turn gives double the usual XP, and hence double the usual Great General contribution (in addition to the 50% bonus from China's UA.) The 30% bonus they'll be contributing works on cities letting you rapidly tear down those walls. Any excess Great Generals can be used to create Citadels, which are great for cutting into enemy land, giving you a safer point to attack their cities from.

Try to promote as many Chu-Ko-Nu as possible with the Range promotion, so they'll remain effective when upgraded to Gatling Guns. Your other uniques will continue to be useful, so you can have essentially continuous warfare all the way to the end of the game - so long as your happiness can handle it.

Social Policy trees	
1. Liberty
2. Commerce or Honour
3. Rationalism
Ideology	Autocracy
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Tithe or Church Property
Follower: Any happiness beliefs or Guruship
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Statue of Zeus
Alhambra
Notre Dame
Big Ben
Brandenburg Gate
Neuschwanstein
Prora

Summary of key strengths
Uniques build on top of already important gameplay features; no need for an odd technology path
Good early gold output without having to depend on trade routes
Powerful medieval-era warfare
""",

    "Denmark":"""
Start bias
Coastal.

Unique Ability: 
Viking Fury
Embarked units have +1 movement point (making 3 total at first, 4 with Astronomy and 5 with Steam Power)
Disembarking a unit uses up 1 movement point rather than depleting all its moves
The disembarked unit will have movement points equal to how many it had prior to disembarking, minus one. This means it can have more movement points remaining than its normal maximum.
Standard melee and melee mounted units pay no movement cost to pillage. This ability carries over on upgrade.
All civilian naval units (Work Boats, Great Admirals) have +1 movement point

Unique Unit I: 
Berserker (Replaces the Longswordsman)
Costs 550 gold to purchase in normal-speed games, up from 460
Requires the Metal Casting technology rather than Steel
Obsoletes with the Metallurgy technology instead of Gunpowder
3 moves, up from 2
Amphibious - No combat penalty from attacking across rivers or from the sea (keeps on upgrade)

Unique Unit II: 
Norwegian Ski Infantry (Replaces the Rifleman)
Bonuses in Snow, Tundra and Hills - Double movement in hill, tundra and snow tiles and +25% strength in those tiles if forest and jungle are not present (keeps on upgrade)

Strategy

Denmark is best at domination victories.

The Danish Civ is all about war. There's not really any bonuses that aren't focused on it, but the ones they do have can be surprisingly effective if played well. Start your game by picking up Bronze Working to discover where iron spots are, then Writing to keep your tech rate up, followed by Worker technologies, Optics and finally push towards Metal Casting. Gold, happiness and iron should be your prioirities at the early stage of the game ready for mid-game warfare. Build a good number of Catapults or Trebuchets to accompany your Berserkers, and you'll have a lethal force that'll remain a threat for quite some time - Berserkers have quite a wide window of usage.

Bring your army to the coast of another Civ, then you can disembark the whole lot onto land. Siege units can disembark, set up and fire in a single turn, allowing them to deal vast amounts of damage before enemies can even respond. Berserkers meanwhile can heal up rapidly with free pillaging, and can easily re-position to protect your Catapults and Trebuchets. The key to Danish warfare is the speed - no other Civ can flood a new landmass like Denmark can. Rush in, take cities and burn what you don't need, then move along.

If unhappiness becomes a major issue, you can take a break to fix your economy and get back into the fight with Norwegian Ski Infantry. Berserkers promote into them (via Musketmen) so you can make good use of all your old veteran units again. Like Berserkers, they're more mobile than normal front-line units, and unlike them they fight more effectively in hills, tundra and snow. Although tundra and snow bonuses may seem to be very situational, it is a good way to take cities on the most vulnerable parts of new continents. Bring along some Artillery as well, and you can finish off your world conquests.

Social Policy trees	
1. Honour or Liberty
2. Exploration or Liberty
3. Rationalism
Ideology	Autocracy
Religion	Pantheon: Faith Pantheons or God of the Sea or Messenger of the Gods
Founder: Tithe or Initiation Rites
Follower: Any happiness bonus
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Pyramids
Statue of Zeus
Colossus
Great Lighthouse
Alhambra
Notre Dame
Brandenburg Gate
Neuschwanstein
Prora
Pentagon

Summary of key strengths
Particularly strong in the first turn of warfare
Strongest pillager in the game - can quickly ruin the lands around an enemy city, or rapidly recover during sieges from the health granted
One UU upgrades into the other, so it's easier to have a highly-promoted army
Can be effective even at a technological disadvantage; Berserkers arrive earlier than regular Longswordsmen
""",

    "Egypt":"""
Start bias
Avoid jungle and forest.

Unique Ability: 
Monument Builders
+20% production bonus when building wonders (both national and world wonders)

Unique Unit: 
War Chariot (Replaces the Chariot Archer)
5 moves, up from 4
Does not require Horse resources

Unique Building: 
Burial Tomb (Replaces the Temple)
Enemies that capture this city receive twice as much gold as normal
This stacks with Songhai's Unique Ability or the double-gold-on-city-capture ability of Landsknechte (those two bonuses do not stack with each other)
0 maintenance cost, down from 2
+2 local city happiness

Strategy

Egypt is best at cultural victories.

Unlike most other Civs, Egypt can play three different ways based on which unique they want to emphasis, with the same eventual target of a cultural victory:

Focusing on the Unique Ability is the standard, lowest-risk option, involving building tall and going for a cultural victory via theming bonus wonders, wonders with high culture yields and wonders with direct tourism yields.

Focusing on the War Chariot is slightly riskier than purely focusing on the UA, but can reward you with a defeated rival early in the game (and hence one less player to influence with tourism.) Build a small force of War Chariots and a couple of melee units (Spearmen are reasonably strong and affordable, but Warriors can work, too) to invade an opponent before they have proper defences. Then, switch into one of the other playstyles for the rest of the game.

Focusing on the Burial Tomb is the highest risk/highest reward option. It involves building cities in huge numbers, getting faith buildings in your religion and taking the Sacred Sites Reformation belief. High happiness and faith outputs are crucial. War Chariots can act as decent defensive units for quite some time in case your mass city-settling starts to anger other Civs. It's much harder than the other routes, but can result in a mid-game cultural victory.

Social Policy trees	
1. Tradition (UA emphasis) or Liberty (UB emphasis)
2. Aesthetics (UA emphasis) or Piety (UB emphasis)
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or Messenger of the Gods (UB emphasis) or Sacred Waters (UB emphasis)
Founder: Tithe (UA emphasis) or Pilgrimage (UB emphasis)
Follower: Divine Inspiration and Religious Community (UA emphasis) or any religious buildings (UB emphasis)
Enhancer: Religious Texts or Itinerant Preachers
Reformation: Sacred Sites (UB emphasis)

Key wonders	
Any theming bonus wonder
Pyramids (UB emphasis)
Stonehenge (UA emphasis)
Temple of Artemis (UA emphasis)
Hanging Gardens (UA emphasis)
Any Theology wonder
Notre Dame (UB emphasis)
Leaning Tower of Pisa (UA emphasis)
Eiffel Tower
Statue of Liberty
CN Tower (UB emphasis)

Summary of key strengths
Some degree of early-game flexibility regarding the choice of unique to favour
Best wonder-builder for most of the game, can win a wonder race even if somewhat late to a technology
Strong at cultural victories
""",

    "England":"""
Start bias
Coastal.

Unique Ability: 
Sun Never Sets
+2 movement points to all naval units (both military and civilian) and embarked units
When any Civ enters the renaissance era, gain 2 Spies instead of 1.

Unique Unit I: 
Longbowman (Replaces the Crossbowman)
Range - +1 range (keeps on upgrade)

Unique Unit II: 
Ship of the Line (Replaces the Frigate)
Upgrade cost of 420 rather than 390 in normal speed games
30 strength, up from 25
35 ranged strength, up from 28
Costs 170 production, down from 185
Costs 720 gold, down from 770
Costs 80 gold to upgrade to, down from 180
3 sight, up from 2

Strategy

England is best at domination victories.

Although many Civs can pull off mid-game domination effectively, England can dominate by both the land and by the sea thanks to their two very effective unique units. What England doesn't have is much in the way of economic support, so it's important to get to Machinery quickly for Longbowmen followed by Navigation for Ships of the Line. Don't neglect science or infrastructure along the way, and don't be afraid to start a war before your Ships of the Line are ready - even just one of your UUs will still be effective.

Longbowmen are almost like medieval-era artillery - they can out-range cities, attacking them without risking being attacked themselves. Meanwhile, Ships of the Line completely dominate the seas until Ironclads roll around (and even then they can stand up to them reasonably effectively.) Bring Knights or Horsemen with your Longbowmen and Caravels or Privateers with your Ships of the Line as neither UUs can take cities themselves.

Aside from the power of England's UUs, their naval units in general are much faster than normal making it easier to respond to coastal threats or reach new lands quickly, and you'll also get an extra Spy. With one more Spy than anyone else, you can steal more technologies from other Civs than the other way around, helping you keep up even if your science infrastructure has fallen behind. Although Ships of the Line will lose their unique strengths once you're into the last few eras, the range Longbowmen have will continue to be useful as you upgrade them to Gatling Guns, Machine Guns and Bazookas.

Social Policy trees 
1. Liberty
2. Exploration
3. Rationalism
Ideology	Autocracy
Religion	Pantheon: Faith Pantheons or God of the Sea or Faith Healers
Founder: Tithe or Church Property
Follower: Any happiness bonuses
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Colossus
Great Lighthouse
Notre Dame
Neuschwanstein
Prora
Great Firewall
Pentagon

Summary of key strengths
Powerful mid-game warfare
Fastest navy in the game, making coastal warfare quicker and retreats safe
Renaissance-era naval supremacy via the Ship of the Line
Longbowmen can damage cities without being at risk of injury themselves
""",

    "Ethiopia":"""
Start bias
None.

Unique Ability: 
Spirit of Adwa
All your units receive a 20% combat bonus against the units of Civs or City-States with more cities than you
Puppeted cities and cities in the process of being razed count, so if you had 4 cities, and your rival had 2 regular and 3 puppet cities, you'd still receive the 20% bonus against their units.
City ranged attacks are not affected by the 20% combat bonus.

Unique Unit: 
Mehal Sefari (Replaces the Rifleman)
Costs 250 gold to upgrade in normal speed games, up from 200
Costs 200 production in normal speed games, down from 225
Costs 680 gold in normal speed games, down from 740
Costs 110 gold to upgrade to in normal speed games, down from 160
Drill I - 15% combat bonus in rough terrain (keeps on upgrade)
30% combat bonus in your capital, bonus reduces the further from it this unit is (keeps on upgrade)
Every tile away from the capital reduces the bonus by 3%
10 or more tiles away from the capital, this bonus has no effect

Unique Building: 
Stele (Replaces the Monument)
+2 faith

Strategy

Ethiopia is a flexible Civ that can pull off any victory route, but I'd advise culture or science if you want to make the most of all your uniques.

You can usually secure a religion before any other Civ as Ethiopia thanks to Steles, giving you the first pick of the best beliefs. For the wonder-building cultural players among us, that's a great opportunity to pick up things like Religious Community and Divine Inspiration. For a science-centred game, things like Tithe for research agreement gold can be effective. Of course, a religion is nothing without followers, and spreading your religion needs faith. This is the tricky bit - do you build wide to maximise faith output, or build tall to make the most use of your defensive UA? You'll have to judge that for yourself.

Once all your early key decisions are done, Ethiopia settles down into something more straightforward - just play for your chosen victory route like you would for any other Civ. You'll have a higher faith output than most Civs and some defensive advantages, but you don't need to greatly adjust how you play to accomodate those differences.

Alternatively, it's perfectly viable to play a war-centred Ethiopian game. If you raze most of the cities you capture, you can ensure the 20% combat bonus from your UA stays active. With the Brandenburg Gate and a Military Academy, new Mehal Sefari can start with March, making them excellent at survival.

Social Policy trees	
1. Tradition or Liberty
2. Piety or Aesthetics (culture)
3. Rationalism
Ideology	Freedom (culture and science)
Religion	Pantheon: Faith Pantheons or God-King
Founder: Tithe or Church Property or Pilgrimage
Follower: Religious Community (culture and science), Divine Inspiration (culture), Swords into Plowshares
Enhancer: Any boost to religious spread
Reformation: Jesuit Education (science) or Unity of the Prophets

Key wonders	
Any theming bonus wonder (culture)
Temple of Artemis (tall-building)
Hanging Gardens (tall-building)
Any Theology wonder
Leaning Tower of Pisa
Porcelain Tower (science)
Brandenburg Gate
Eiffel Tower (culture)
Statue of Liberty (culture and science)
Great Firewall
Hubble Space Telescope (science)

Summary of key strengths
Frequently first to a religion
Strong defence
Reasonably flexible regarding a favoured victory route
""",

    "France":"""
Start bias
None.

Unique Ability: 
City of Light
Great Work theming bonuses are doubled in the capital

Unique Unit: 
Musketeer (Replaces the Musketman)
28 strength, up from 24

Unique Improvement:
Chateau (Requires Chivalry)
Can only be built on a resourceless tile in your own territory, next to a luxury resource and not another Chateau.
The luxury resource can be on the land or in the sea. Indonesia's unique luxuries count.
Yields 2 culture and 1 gold
+50% defence to units on the tile
+1 culture and +2 gold with Flight

Strategy

France is best at cultural victories.

One of a handful of capital-centric Civs, France needs to start by building its capital tall ready to handle the mid-game theming bonus wonders; the Tradition tree will help here. Don't neglect expansion, but don't over-do it; you don't want unhappiness pressures when you're trying to win wonder races. Get Philosophy fairly quickly so you can get the science bonus from the National College up and running, and dedicate a city aside from your capital to generating GWAMs.

Come the mid-game, picking up as many theming bonus wonders as possible is the key priority. Make use of Great Engineers to rush the trickier ones; restricted wonders like the Louvre and Uffizi tend to be much less competitive and can be built the conventional way. Even if you manage few or none at all, your UA isn't useless; you can still build a Museum, the Hermitage and Oxford University in your capital. If wonder-building has made other Civs angry, Musketeers are reasonable defensive units due to having no particular counters - even against other UUs. Still, their awkward placement on the technology tree means they're more of an emergency unit than anything else.

This leaves Chateaux. Although you can build them at Chivalry, and they provide a useful source of culture for rushing through Social Policies quicker, you shouldn't be building or working very many until you've got Hotels and Airports up and running - at which point they're worth 3 tourism each. Stacked on top of your theming bonuses, you'll have plenty of tourism ready to become influential with the world and achieve cultural victory.

Social Policy trees	
1. Tradition
2. Aesthetics (and Exploration Opener)
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or God of Craftsmen
Founder: Tithe or Church Property
Follower: Religious Community, Cathedrals, Divine Inspiration, Religious Art
Enhancer: Religious Texts or Reliquary

Key wonders	
Any theming bonus wonder
Temple of Artemis
Hanging Gardens
Leaning Tower of Pisa
Eiffel Tower
Statue of Liberty
Great Firewall

Summary of key strengths
Strongest mid-game tourism output
Reasonable mid-game defence; Musketeers have no counters in their era
Poor expansion potential is less of a setback than it is to most Civs
""",
    "Germany":"""
Start bias
None.

Unique Ability: 
Furor Teutonicus
When defeating a Barbarian unit inside an encampment, there is a 67% chance they will join your side and you will receive 25 gold.
Most early captured Barbarian units don't need strategic resources (though they're still needed to upgrade them.)
Unique Barbarian units (including the captured units that don't require strategic resources) count separately for the purpose of the Terracotta Army wonder.
-25% maintenance cost for all land units

Unique Unit: 
Panzer (Replaces the Tank)
80 strength, up from 70
6 moves, up from 5

Unique Building: 
Hanse (Replaces the Bank)
+5% production for every trade route your empire has with City-States
The source of the trade route doesn't matter; every trade route you have with a City-State is worth a 5% production boost in all your cities with Hanses.

Strategy

Germany is best at domination victories but is fine at diplomacy as well.

Germany plays best as a "sledgehammer" Civ - that is to say, play peacefully until late in the game, where you can use your powerful infrastructure to raise a very strong army capable of taking over the world. You can use your UA to build up a decent defensive army without having to spare production towards it, letting you build up a good infrastructure early on. Emphasise science output, and once you have Education, work towards Banking for Hanses.

Hanses offer incredible production bonuses so long as you trade extensively with City-States. Every trade route with them is worth a 5% production boost, so even without Petra and the Colossus, you can have a 25% production bonus in all Hanse cities as soon as the UB is first available. Waiting until Panzers to start your first wars is a little risky considering how late they come, so try building up an industrial-era Artillery-heavy army instead.

Panzers with Autocracy's Lightning Warfare are one of the fastest things on land, and are strong enough to stand up to pretty much everything of the same era. Helicopter Gunships will still peel them apart, but thankfully most Civs will be on the other side of the tech tree focusing on more peaceful technologies. Bring some Rocket Artillery or Bombers and some kind of anti-air, and you've got yourself a swift way to end the game in your favour.

Alternatively, Germany's high amount of city-state trading due to the nature of Hanses make them work well with Freedom's Treaty Organisation tenet, and their cheaply-maintained armies that can be mass-produced thanks to Hanse production suits Autocracy's Gunboat Diplomacy tenet well. Both tenets offer strong influence bonuses which make diplomatic victories easier.

Social Policy trees	
1. Honour's Opener and Liberty or Tradition
2. Patronage (diplomacy) or Commerce
3. Rationalism or Commerce (diplomacy)
Ideology	Autocracy
Freedom (diplomacy)
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Tithe or Church Property
Follower: Any happiness bonus or Religious Community
Enhancer: Religious Texts or Itinerant Preachers or Just War (domination)

Key wonders	
Statue of Zeus
Colossus
Petra
Terracotta Army
Alhambra (domination)
Machu Picchu (diplomacy)
Notre Dame (domination)
Forbidden Palace
Big Ben
Brandenburg Gate (diplomacy)
Neuschwanstein
Prora
Pentagon

Summary of key strengths
Can acquire an early army without neglecting infrastructure, providing a good early defence
Strongest production output in the game in the later eras
Synergy with every ideology
Can easily switch between diplomatic and domination focus, even late in the game
""",

    "Greece":"""
Start bias
Greece has no starting bias.

Unique Ability: 
Hellenic League
Halved City-State influence decay when the level of influence is above the resting point
Doubled City-State influence regain rate when the level of influence is below the resting point
These per-turn changes don't directly affect the tenets Gunboat Diplomacy or Treaty Organisation, but do stack with them
Can enter City-State territory without losing influence even without friendship
Units can heal in City-State territory as if the City-State is friendly, even when at war with it

Unique Unit I: 
Hoplite (Replaces the Spearman)
13 strength, up from 11

Unique Unit II: 
Companion Cavalry (Replaces the Horseman)
14 strength, up from 12
5 moves, up from 4
Great Generals I - 50% increased contribution to Great General generation (keeps on upgrade)

Strategy

Greece is best at diplomatic victories.

Greece is an incredibly effective diplomatic Civ, which has an unrivalled ability to hold on to City-State alliances, but lacks advantages regarding actually gaining influence (with the exception of if you're below the equilibrium point)

Early in the game, you can use the ability to regain influence twice as fast to bully City-States for gold and workers. You can take that advantage to an early war if you like, but be sure to take Composite Bowmen and/or Catapults with you for dealing with cities as both Greece's UUs are melee-based. Hoplites are basically Swordsmen and Spearmen rolled into one unit, while Companion Cavalry build on the advantages of regular Horsemen.

Once the World Congress rolls around, though, your focus should be City-State alliances. You can't gain influence as rapidly as other diplomatic Civs, so beware of diplomatic rivals who are saving up their gold or placing Spies in your allied City-States - they might just overturn your alliances just before a World Congress vote before you can react.

Enter ideologies, however, and it all gets much easier. Whether you prefer Gunboat Diplomacy or Treaty Organisation, you'll be gaining more influence per turn than other Civs as less will be subtracted via influence decay. This end-game advantage will really help out with winning a world leader vote, and with it, diplomatic victory.

Social Policy trees	
1. Liberty
2. Patronage
3. Commerce
Ideology	Freedom or Autocracy
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Papal Primacy or Tithe or Church Property
Follower: Any happiness bonus
Enhancer: Religious Unity or Religious Texts

Key wonders	
Pyramids
Petra
Machu Picchu
Notre Dame
Forbidden Palace
Neuschwanstein
Prora

Summary of key strengths
Reasonable early-game warfare, no need for iron until the medieval era
Low decay for City-State influence ensures long-lasting bonuses
Very effective at diplomatic victory
""",

    "Huns":"""
Start bias
Avoid forest and jungle.

Unique Ability: 
Scourge of God
Start with the Animal Husbandry technology in addition to the normal Agriculture.
+1 production per pasture improvement
Raze cities at double speed (2 population killed per turn rather than 1)
Cities founded besides the capital will come from city lists of other Civs (including defeated Civs) in your game, regardless of whether or not you have discovered them

Unique Unit I: 
Battering Ram (Replaces the Spearman)
Costs 75 production, up from 56
Costs 320 gold, up from 260
10 strength, down from 11
Sight of 1, down from 2
50% bonus vs. mounted units removed
33% penalty while defending
Does not recieve defensive bonuses
Can only attack cities, but can still deal damage in defence
300% bonus vs. cities
Cover I - +33% defence vs. ranged attacks (keeps on upgrade)
Upgrades to Trebuchet instead of Pikeman
Obsoletes with Physics instead of Civil Service

Unique Unit II: 
Horse Archer (Replaces the Chariot Archer)
7 strength, up from 6
Does not use up all movement points to enter rough terrain
Does not require Horse resources
Accuracy I - 15% bonus when attacking units on open terrain (keeps on upgrade)

Strategy

The Huns are best at domination victories.

With a free starting technology, early production bonuses and two effective early UUs, the Huns are the ultimate rusher Civ. Start by building a Scout so you can search for any potential targets, then a Worker so you can make use of your production bonus for pastures, while you research your way to The Wheel for Horse Archers. Build at least a couple before you get to Bronze Working, and you can use them to fight Barbarians to train until you've got a couple of Battering Rams ready. Don't waste time building Barracks or wonders - they'll cost you more than they gain you at this point in the game.

Now, take at least two Battering Rams together with your Horse Archers towards enemy lands and get the war started. Two Battering Rams can take most cities in a couple of turns, while Horse Archers can deal with any defending units. You can easily wipe a Civ out of the game, taking a valuable city (in the form of their capital) in the process. On smaller maps, you can win the game extremely early on this way.

The Huns mostly depend on a good early war to get them through the game, but that's not to say they're powerless later on. Extra pasture production will still be helpful in raising new armies, while double-speed razing means you only need to deal with the unhappiness associated with it for half as long allowing your conquests to continue unhindered.

Social Policy trees	
1. Honour or Liberty
2. Commerce
3. Rationalism
Ideology	Autocracy or Order
Religion	Pantheon: Faith Pantheons or God of Craftsmen or God of the Open Sky
Founder: Tithe or Church Property
Follower: Any happiness bonus
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Notre Dame
Brandenburg Gate
Neuschwanstein
Prora
Pentagon

Summary of key strengths
Best Civ in the game at an early rush
Good early production
Less prone to persistent unhappiness in warfare thanks to fast razing
""",

    "Inca":"""
Start bias
Hills.

Unique Ability: 
Great Andean Road
All land units (both civilian or military types) moving into hill tiles only use one movement point.
Hills with forest or jungle also only use one movement point for units to enter.
This does not affect crossing rivers onto hill tiles.
Roads and railroads built on hill tiles have no maintenance cost.
Roads and railroads built on tiles without hills have half the normal maintenance cost.
With the Wagon Trains Social Policy from the Commerce tree, roads and railroads are maintenance-free regardless of location.

Unique Unit: 
Slinger (Replaces the Archer)
4 strength, down from 5
Withdraw Before Melee - Chance to withdraw rather than deal and receive damage if attacked by melee (keeps on upgrade)
Being attacked by faster units decreases the withdrawal odds
Mountains, lakes and seas behind the Slinger can negatively impact its withdrawal chance
High base strength relative to the attacking unit increases withdrawal chance, low base strength reduces it

Unique Improvement: 
Terrace Farm (Requires Construction)
Can only be built on resourceless hills within your own territory
Yields 1 food
+1 food for every adjacent mountain
+1 food with Civil Service (if adjacent to fresh water) or Fertiliser (if not.)

Strategy

The Inca are best at scientific victories and are reasonably effective at domination.

If the Iroquois are the Civ for a very forest and jungle-centric game, the Inca are the Civ for hill-heavy gameplay. Immediately, the Inca can move quickly through hill tiles making early-game exploration quite a bit easier - you'll need that advantage to track down mountain-heavy areas for your Terrace Farms later on. Slingers make particularly good scouting units (especially Scouts promoted into Slingers via ancient ruins) due to their ability to retreat from melee attacks, but they're awful at escorting civilian units for the same reason.

Once you've found a good mountain-rich area, settle cities next to those mountains and build up Terrace Farms. The city growth rate will be incredible, allowing you to maximise your science output. Enter Observatories and your advantage will only grow. Meanwhile, your cheap roads can save you money which you can pour into research agreements. Add some good science wonders in the mix (after all, the hills your Terrace Farms are on still offer production) and you've got a good recipe for scientific victory.

Alternatively, mobility in hills, gold from cheap roads and a technological advantage makes an excellent set-up for domination. Mountainous areas are typically surrounded by lots of hills making the most lucrative spots for Terrace Farms you don't own easier places to take than would be the case for most other Civs.

Social Policy trees	
1. Tradition
2. Commerce
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Tithe or Church Property or Interfaith Dialogue
Follower: Swords into Plowshares, Religious Community, Feed the World
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Great Library
Temple of Artemis
Hanging Gardens
Petra
Machu Picchu
Leaning Tower of Pisa
Porcelain Tower
Statue of Liberty
Great Firewall
Hubble Space Telescope

Summary of key strengths
Decent early-game exploration due to easy hill movement
Reasonable early economy thanks to cheap roads
Very good food output; can grow huge cities
Incentive to settle near mountains delivers large science outputs in the second half of the game
""",

    "India":"""
Start bias
Grassland.

Unique Ability: 
Population Growth
Unhappiness from number of cities doubled
Unhappiness from number of citizens halved
Local city happiness in a city is capped at 67% of the population of the city, rounded down to the nearest unit, instead of the normal 100%.

Unique Unit: 
War Elephant (Replaces the Chariot Archer)
Costs 70 production, up from 56
Costs 310 gold, up from 260
3 moves, down from 4
9 strength, up from 6
11 ranged strength, up from 10
Does not use up all movement points to enter rough terrain
Does not require Horse resources
Costs 110 gold to upgrade in normal-speed games, down from 135

Unique Building: 
Mughal Fort (Replaces the Castle)
Costs 150 production, down from 160
Costs 680 gold, down from 720
+2 culture
+2 tourism with Flight

Strategy

India is best at cultural victories and is almost as effective at scientific victories.

An unusual and often misunderstood Civ, India if well-played can throw a general convention that you must build tall or wide out the window. Although India's new cities start with more unhappiness, once they hit size 7 (on standard-sized or smaller maps - it's size 5 on large and size 4 on huge maps) they'll generate less unhappiness than those of other Civs. The difference becomes more substantial the more they grow - by size 21, cities of other Civs generate about 50% more unhappiness than those of Indian cities. More tall cities means more potential to build wonders and more science output.

The challenge, however, is getting over the early unhappiness hurdles. It's important for India to track down as many luxury resources as possible early on so they can afford the unhappiness penalty of founding new cities. Alternatively, try using your strong, resourceless War Elephants to war - enemy capitals are guarenteed to have two different kinds of luxury resources nearby on most kinds of randomly-generated maps, so capturing one will give you quite an advantage.

Once you've established all the cities you need, you can settle down and concentrate on a peaceful cultural or scientific victory route. While most Civs struggle with happiness in the mid-game (as cities are growing fast but new sources of happiness are limited) India avoids that issue, letting you grow huge cities unhindered.

Finally, the role of Mughal Forts in India's strategy is minor compared to their UA, but a maintenance-free culture bonus is nonetheless useful for getting through Social Policies (and securing good tiles) faster. The tourism bonus at Flight doesn't make a huge difference, but at least you don't have to make any major detours to unlock it.

Social Policy trees	
1. Tradition
2. Aesthetics (culture) or Commerce (science)
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or Goddess of Love
Founder: Tithe or Church Property or Interfaith Dialogue
Follower: Divine Inspiration, Religious Community, Feed the World, Swords into Plowshares
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Any theming bonus wonder (culture)
Temple of Artemis
Hanging Gardens
Chichen Itza
Leaning Tower of Pisa
Porcelain Tower
Eiffel Tower
Statue of Liberty
Great Firewall
Hubble Space Telescope (science)

Summary of key strengths
Reasonable potential for an early-game rush
Can manage multiple large cities without slipping into unhappiness
Happiness and culture advantages provides reasonable defence against cultural Civs
""",

    "Indonesia":"""
Start bias
Coastal.

Unique Ability: 
Spice Islanders
The first three cities you found on different landmasses besides the one your capital is in...
Can never be razed
Provide two copies of a unique luxury (Nutmeg, Cloves and Pepper)
The landmasses may be of any size
The cities must also be founded on separate landmasses to each other, so for the maximum effect you need at least four landmasses
Capturing cities on other continents won't allow you access to the luxuries, nor will getting the cities via trading
Placing one of those cities on a resource will displace the old resource.
If those cities are captured, the capturing Civ gets the luxuries
Tiles these cities are on generate an additional 2 gold

Unique Unit: 
Kris Swordsman (Replaces the Swordsman)
Mystic Blade - After a unit with this promotion attacks or is attacked for the first time, this promotion is replaced by a random special one in the following list. All of them, including the Mystic Blade promotion, are kept on upgrade.
Enemy Blade - -20HP/turn in enemy territory
Evil Spirits - -10% attack, -30% defence
Ambition - +50% attack, -20% defence
Heroism - Gives a 15% strength bonus to all land units within 2 tiles, does not stack with a Great General's bonus
Invulnerability - +30% defence, recover 20HP more a turn while healing.
Recruitment - Heal 50HP after killing a non-Barbarian military unit.
Restlessness - +1 movement point, +1 attack, can move after attacking.
Sneak Attack - +50% flanking bonus (15% bonus to combat per friendly unit adjacent to the enemy rather than 10%)

Unique Building: 
Candi (Replaces the Garden)
Can be built in any city, not just ones with an adjacent lake or river
+2 faith
+2 faith for every religion with at least one follower in the city

Strategy

Indonesia is best at diplomatic and domination victories.

What Indonesia lacks in simplicity it makes up for in potential. It can have a huge empire early in the game without falling into unhappiness, an army of essentially six UUs in one and the game's strongest faith output - but you'll have to work hard to earn all this.

The challenge early on is balancing out the colonisation encouraged by your UA with the different techological requirements of your other uniques. A good move is to take Bronze Working right away to find iron for your future Kris Swordsmen, then work towards Optics so you can set up colonies on offshore islands before other Civs can. The happiness offered by your unique luxuries is enough to cover the unhappiness cost of settling those cities, and if you trade one of the two away in exchange for another luxury, you can grow it to size 5 without any trouble.

If you can build wide early on (even if you can't find offshore islands to settle) and build plenty of Shrines, you should be able to secure a faith Pantheon and through it a religion without having to rush to Theology for Candi. This gives you the breathing space you need to prepare a Kris Swordsman-led army. As you build them, send the ones you already have to fight Barbarians so you can reveal their random promotion prior to starting a war. Bring some Composite Bowmen or Catapults to deal with cities, and you can dominate classical-era warfare.

What makes Kris Swordsmen distinct from other front-line UUs is the wide range of roles the random promotions allows them to fill. Heroism lets you start a war with a Great General without needing to have fought before, Ambition and Restlessness allows the units to be used aggressively, Recruitment makes the unit exceptionally good at soaking up damage, Recruitment enables attacks which would otherwise be extremely risky while Sneak Attack helps speed up battles you're already doing well at.

After Kris Swordsman wars, it's time to build plenty of Candi and exploit the huge amount of faith they generate. In areas where your own religion is in competition with another Civ, you can get 6 faith or more generated per turn from just one building. To make things even better, Candi aren't restricted to any particular city location unlike regular Gardens, making the Peace Gardens belief a very powerful source of happiness and a good alternative to picking a religious building as one of your Follower beliefs. This frees up faith you can use to spread your religion further for Founder bonuses, for buying Great People with later in the game, or for use with a strong Reformation belief. What you shouldn't be doing is buying lots of Great Prophets - they'll remove followers of other religions hence reducing your faith output.

So, what's left is to wrap this up into a victory. You can use your happiness advantages together with promoted Kris Swordsmen and siege units to continue a path to world domination, or make your huge empire concentrate on gold output to help with bribing City-States and with that, win the world leader vote.

Social Policy trees	
1. Liberty
2. Piety or Patronage (diplomacy)
3. Commerce or Exploration or Rationalism (domination)
Ideology	Order (domination)
Autocracy (diplomacy)
Religion	Pantheon: Faith Pantheons or God of the Sea
Founder: Tithe or Papal Primacy (diplomacy) or Interfaith Dialogue
Follower: Peace Gardens, Pagodas, Mosques, Asceticism
Enhancer: Itinerant Preachers or Just War (domination) or Religious Unity (diplomacy) or Holy Order
Reformation: Charitable Missions (diplomacy) or Jesuit Education or Religious Fervour (domination) or To the Glory of God

Key wonders	
Borobudur
Great Mosque of Djenne
Machu Picchu
Notre Dame
Forbidden Palace (diplomacy)
Leaning Tower of Pisa
Kremlin (domination)
Neuschwanstein
Prora
Pentagon
CN Tower

Summary of key strengths
Highest faith potential in the game
Decent happiness bonuses
Monopoly of up to three resources provides an edge in diplomacy with other Civs
Reasonable early-to-mid-game warfare potential
""",

    "Iroquois":"""
Start bias
Forest.

Unique Ability: 
The Great Warpath
Units can move through forests and jungles in friendly territory as if they were roads (and rivers between forests can be crossed as if there's a bridge there, even without Engineering)
Forests and jungles in friendly territory can be used as roads for purposes of City Connections after researching The Wheel
Caravans move through forest and jungle tiles as if they were roads
With Railroad, forests and jungles in friendly territory will act as railroads for the purpose of the 25% production boost.
Note that forests and jungles do not act as railroads for movement purposes; you'll have to build those to get that advantage.

Unique Unit: 
Mohawk Warrior (Replaces the Swordsman)
Does not require Iron resources
Obsoletes with Gunpowder instead of Steel
33% extra strength in forest and jungle (keeps on upgrade)

Unique Building: 
Longhouse (Replaces the Workshop)
10% production bonus removed
Costs 100 production, down from 120
+1 production to every forest worked by the city

Strategy

The Iroquois are best at domination victories and are reasonable at science.

No Civ is as tied to a particular terrain type as the Iroquois. Without forests or jungles, they lose nearly all of their unique advantages, and without forests their Longhouse UB actually becomes worse than generic Workshops. It's important to expand fast to take good forest spots before another Civ moves in and chops the trees down, so be prepared to get Settlers built early on. Thankfully, you won't need so many Workers - forests within your own lands basically act as roads, reducing the amount of work they need to do (and saving you maintenance.)

Mohawk Warriors have all the advantages of Swordsmen, without the biggest downside - the need for iron. Their strength bonus in forests and jungles is more than enough to overcome the defensive bonuses of enemies fortifying there, making it much more viable to take forested cities than would otherwise be the case. Don't just bring Mohawk Warriors on their own - bring some Composite Bowmen, too.

Founding and capturing forest-rich cities will reward you with high production for the rest of the game. While the loss of the 10% production modifier is a shame, you can more than make up for it by working plenty of lumber mills. You can then use it to build up a new army to conquer the world, or perhaps to rapidly build up a food/science infrastructure towards a scientific victory.

Social Policy trees	
1. Tradition (strong start) or Liberty or Honour (weak enemy/other Civs have forest)
2. Commerce
3. Rationalism
Ideology	Order
Religion	Pantheon: Faith Pantheons or Sacred Path
Founder: Tithe or Church Property
Follower: Religious Community and/or any happiness bonuses
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Statue of Zeus (domination)
Hanging Gardens (science)
Alhambra (domination)
Machu Picchu
Notre Dame (domination)
Porcelain Tower
Brandenburg Gate (domination)
Kremlin
Neuschwanstein
Great Firewall (science)
Pentagon
Hubble Space Telescope (science)

Summary of key strengths
Better in forested land than any other Civ, and good in jungles
Strong early defence
""",

    "Japan":"""
Start bias
Coastal.

Unique Ability: 
Bushido
All units fight as if they are at full health even when wounded.
This does not prevent the Charge promotion (+33% damage against wounded units) from working against your units.
The Elite Forces tenet from the Autocracy ideology (closing the gap between wounded and full-health units by 25%) does not stack with this, and therefore has no effect when playing as Japan.
+1 culture from fishing boats and +2 culture from atolls
The former can be added to tourism with a Hotel, Airport or National Visitor Centre; the latter cannot.

Unique Unit I: 
Samurai (Replaces the Longswordsman)
While embarked, can construct fishing boats. This depletes the unit's remaining moves, but does not consume the unit.
Shock I - 15% combat bonus in open terrain (keeps on upgrade)
Great Generals II - 100% increased contribution to Great General generation (keeps on upgrade)
Upgrades to the Rifleman, rather than the Musketman
Samurai can therefore be built until Rifling, rather than Gunpowder
Normally, promoting a unit from a Longswordsman to a Rifleman would cost a combined total of 230 gold. For Samurai, it's 220

Unique Unit II: 
Zero (Replaces the Fighter)
Does not require oil resources
+33% strength vs. fighter-class aircraft (keeps on upgrade)

Strategy

Japan is best at domination victories.

The skew of Japan towards warfare is obvious, but it's easy to overlook their advantage to coastal development. Sea resources can be a surprisingly good early source of culture, and atolls are particularly strong - not even requiring development to reach their full effectiveness. This can get you through your first Social Policy tree quickly, ready to give you an edge at producing Samurai (and Trebuchets to support them.)

Samurai have a long window of usage and backed by an Armoury, can get straight to the Siege promotion or just one promotion from March. Keep a few Samurai around even past their obsoletion as they can build fishing boats improvements for free while embarked - saving you a considerable amount of production or gold that would go towards Work Boats.

Late in the game, you have Zeroes. Instead of using them as you would Fighters, use them more like Bombers. Although they won't deal as much damage, their bonus against Fighter-class aircraft makes them stronger in the event of interception, and the fact you can build them without oil allows you to construct vast quantities of them. Try filling a Carrier with Zeroes to make a pseudo-Battleship.

Backing your wars up is your ability to fight at full strength even with injured units. This makes your units roughly 20% stronger than they usually would be at 50% health, which doesn't sound like a lot, but remember that it stacks multiplicatively with promotions unlike other unique combat bonuses. For ranged units, this bonus is particularly effective as, so long as they're protected from being targeted, you don't need to bother healing them up. And for air units, this becomes even stronger - when set to sleep, they can't be directly attacked meaning it's safe to keep them fighting until they're on very low health.

Social Policy trees	
1. Liberty (situationally, Tradition or Honour can work well)
2. Exploration or Commerce
3. Rationalism
Ideology	Order or Autocracy (do not take Elite Forces)
Religion	Pantheon: Faith Pantheons or God of the Sea or Messenger of the Gods or Faith Healers
Founder: Tithe or Church Property
Follower: Any happiness bonuses
Enhancer: Religious Texts or Itinerant Preachers or Just War

Key wonders	
Statue of Zeus
Colossus
Terracotta Army
Alhambra
Machu Picchu
Notre Dame
Brandenburg Gate
Kremlin or Prora
Neuschwanstein
Pentagon

Summary of key strengths
Good at warfare at any point in the game
Strong at wars of attrition
Potential for strong early-game culture
Cheap to develop coastal cities
""",

    "Korea":"""
Start bias
Coastal.

Unique Ability: 
Scholars of the Jade Hall
+2 science for every specialist
+2 science on every Great Tile Improvement and on every Landmark within your lands.
Building a Library, University, Public School, Research Lab, Observatory or the National College, Oxford University or Great Library in the capital grants a one-off science boost equal to that of a research agreement.
Like research agreements, this gives science equal to 50% of the median cost of technologies you can currently research and is affected by the boost offered by the Porcelain Tower and the Scientific Revolution Social Policy in the Rationalism tree.

Unique Unit I: 
Hwach'a (Replaces the Trebuchet)
11 strength, down from 12
200% bonus vs cities removed
26 ranged strength, up from 14
2 sight, up from 1
If you upgrade a Catapult to a Hwach'a, it will still retain the sight penalty.

Unique Unit II: 
Turtle Ship (Replaces the Caravel)
Loses "Withdraw Before Melee" promotion, meaning it doesn't have a chance to retreat a tile instead of being attacked when hit by melee.
This bonus would normally be retained on upgrade, but as Korea's Turtle Ships lack it, they can't have Ironclads with it either.
Cannot enter ocean tiles unless in friendly territory
2 sight, down from 3
36 strength, up from 20
Obsoletes with Replaceable Parts instead of Steam Power

Strategy

Korea is best at scientific victories.

While Babylon dominates early-game science, Korea tends to have the biggest science output later on. Before the bulk of scientific bonuses arrive, Korea has to make do with the science bonuses from completing buildings in their capital, making it important to grab Writing (for Libraries), Philosophy (for the National College) and Education (for Universities) early. Once you have Libraries, you can start filling lots of scientist slots and really get your bonuses up and running. Be wary of filling too many engineer or merchant slots - producing a Great Person of either type will raise the cost of future Great Scientists - but otherwise such slots provide useful additional science. Filling Artist, Musician and Writer slots won't cause any such trouble.

Ultimately, Korea's UA allows an enhanced version of normal scientific gameplay with the only real difference being the capital emphasis. However, Korea's UUs diverge quite a bit from standard practice. Both lose a key advantage in exchange for a huge amount of strength, making them near-unstoppable defensive units (and not bad on the offensive, either, if you feel like diverging from the typical scientific path.)

Hwach'a have a ranged strength only slightly below Gatling Guns, with double their range (although you'll need to set up unlike Gatling Guns.) While having only 11 points of melee strength may make Hwach'a appear vulnerable, remember that if they're taking ranged damage, they'll use their ranged strength to defend. This makes Hwach'a suprisingly good against cities despite their lower damage output.

Turtle Ships lose the crucial scouting utility of Caravels in exchange for acting like a Trireme with more strength than anything else prior to Ironclads. With Coastal Raider promotions, they can deal a lot of damage to cities, but as Turtle Ships can't enter oceans, that city needs to be very exposed to the coast.

Social Policy trees	
1. Tradition
2. Exploration
3. Rationalism
Ideology	Freedom or Order
Religion	Pantheon: Faith Pantheons or production Pantheons
Founder: Tithe or Church Property
Follower: Swords into Plowshares, Religious Community, Feed the World
Enhancer: Religious Texts or Itinerant Preachers or Reliquary

Key wonders	
Great Library
Hanging Gardens
Oracle
Leaning Tower of Pisa
Porcelain Tower
Statue of Liberty
Great Firewall
Hubble Space Telescope

Summary of key strengths
Core bonus (the UA) doesn't require too much deviation from typical scientific play to use
Highest late-game scientific potential in the game
Very powerful mid-game defense
""",

    "Maya":"""
Start bias
None.

Unique Ability: The Long Count
Ability unlocks after discovering Theology, which replaces the standard calendar with a Mayan Long Count calendar.
At the start of every b'ak'tun (when the leftmost number on the calendar increases on a 394-year cycle) you recieve a free Great Person of your choice
Once a Great Person has been selected, it cannot be picked again until all other Great People have been chosen.
All Great People generated this way except for Great Admirals and Generals increase the cost of the next Great Person of their respective type (for Great Engineers, Merchants and Scientists, generating one will raise the costs for all three.)

Unique Unit: 
Atlatlist (Replaces the Archer)
Upgrade cost of 85 rather than 80 in normal speed games
Requires the Agriculture technology rather than Archery (in other words, unlocked at the start of the game)
Costs 36 production, down from 40
Costs 180 gold, down from 200

Unique Building: 
Pyramid (Replaces the Shrine)
Generates 2 faith, up from 1
+2 science

Strategy

The Mayans are best at scientific victories.

A gloriously unconventional Civ, the Mayans are distinctive at having strengths in both science and religion - both of which come with the powerful Pyramid UB. Aside from providing a good boost to science early on, it also really helps out in overcoming the higher technology costs associated with having lots of cities. For that reason, the Mayans work best as a wide-building scientific empire. A well-developed wide empire can exceed a tall one in science potential (although it's trickier to do) and will have a huge faith advantage (even before taking into account Pyramids' doubled faith ouput compared to Shrines.)

A boost to science early on is necessary to get to Theology quickly, so you can make good use of your UA. Helpfully, you don't need to make a diversion to Archery for early defensive units seeing as Atlatlists come with no technology requirement. Furthermore, Philosophy is on the way to Theology, so you can get your National College built early.

The Mayan UA helps make up somewhat for the lack of specialists wide empires tend to have by essentially giving you a repeating version of Liberty's finisher. Great Engineers, Prophets and especially Scientists are your best first choices of Great People. Work towards scientific technologies and the Jesuit Education Reformation belief (one of the best ways of turning your faith advantage into a scientific advantage) and you'll have all the scientific infrastructure you need to get spaceship technologies quickly. Although building wide means you'll be slow to build spaceship parts, having lots of cities means you can build many at once.

Social Policy trees	
1. Liberty
2. Piety or Commerce
3. Rationalism
Ideology	Order
Religion	Pantheon: Faith Pantheons or Messenger of the Gods or Ancestor Worship
Founder: Tithe or Church Property or Interfaith Dialogue
Follower: Asceticism, other happiness bonuses, Feed the World
Enhancer: Religious Texts or Itinerant Preachers or Holy Order
Reformation: Jesuit Education or To the Glory of God

Key wonders	
Great Library
Any Theology wonder
Machu Picchu
Notre Dame
Porcelain Tower
Great Firewall
CN Tower
Hubble Telescope

Summary of key strengths
Ideal for a wide-building scientific victory
Excellent early-game science
Good at founding a religion
Above-average early rushing potential
""",

    "Mongolia":"""
Start bias
Plains.

Unique Ability: 
Mongol Terror
All melee mounted units recieve +1 movement point
All military units gain +30% strength versus City-State cities and units controlled by them

Unique Unit: 
Keshik (Replaces the Knight)
Classified as a ranged unit rather than a mounted unit, therefore is built faster with the Temple of Artemis and has no vulnerability to Pikemen
Instead of a melee attack, has a ranged attack with 16 strength and a range of 2 tiles.
15 strength, down from 20
5 moves, up from 4
No city attack penalty
Quick Study - +50% XP gain (keeps on upgrade)
Great Generals I - 50% increased contribution to Great General generation (keeps on upgrade)

Unique Great Person:
Khan (Replaces the Great General)
5 moves, up from 2
While healing, regains 15HP more per turn
While healing, adjacent land or air units regain 15HP more per turn. Does not affect units sharing a tile with the Khan.

Strategy

Mongolia is best at domination victories.

Almost to the extent the Zulus are focused on their Impis, Mongolia is focused on their Keshiks. A fast ranged unit that can move before attacking, they can safely tear down city defences by moving in range of the city, firing, then moving out of range again. Fast XP gain means they can get to Logistics faster than most other ranged units can, doubling their damage output. The one thing they can't do is capture cities - keep a couple of Horsemen around for that role. Your UA helpfully gives Horsemen extra mobility, so you can keep them safe from harm until you need to rush in to finish off a city.

If your targets decide to enlist the help of City-State allies, your UA will make mincemeat of them. You'll not only do vastly more damage against City-State units, but also the cities themselves - handy if one's in a good location, such as near a natural wonder. Keep in mind that directly declaring war on more than one City-State in quick succession will give you a lower influence equilibrium resting point and faster influence decay with others; declare war on full Civs with City-State alliances to avoid this.

While Mongolia's UA is pretty niche in usage and their UU won't be around for ever, their Unique Great People - Khans - will be useful throughout the game. They're fast enough to keep up with your mounted units (Keshiks boosted by Khans are stronger than Crossbowmen as well as faster) and provide a bigger bonus to the healing rate of adjacent units than the Medic II promotion does, although those two bonuses do not stack. This really becomes powerful once air units enter the battlefield; place a Khan next to a city full of air units with Air Repair, and they'll heal 40HP every turn. This gives a considerable advantage in late-game wars to finish off what your Keshiks started.

Social Policy trees	
1. Liberty
2. Commerce
3. Rationalism
Ideology	Autocracy or Order
Religion	Pantheon: Faith Pantheons or Faith Healers
Founder: Tithe or Church Property
Follower: Any happiness bonuses
Enhancer: Messiah if you have Faith Healers, Religious Texts or Itinerant Preachers otherwise.

Key wonders	
Statue of Zeus
Temple of Artemis
Alhambra
Machu Picchu
Notre Dame
Brandenburg Gate
Kremlin or Prora
Neuschwanstein
Pentagon

Summary of key strengths
Strong mid-game warfare, especially in reasonably open terrain, with a particularly hard to kill army
Reasonable late-game warfare due to the synergy between Khans and air units
Effective against diplomatic Civs
""",

    "Morocco":"""
Start bias
Desert.

Unique Ability: 
Gateway to Africa
Each international trade route with a different Civilization or City-State gives you a bonus 3 gold and 1 culture.
The gold and culture is separate from the displayed trade route yield, so some trade routes may be better than they appear.
Trade routes from other Civs to Morocco can still award the bonus.
More than one trade route involving the same Civ (whether to or from them) will only award the bonus once, not multiple times.
Internal routes (delivering food or production to another of your own cities) will not award this bonus.
Other Civs gain +2 for every international trade route sent to Morocco. This stacks.

Unique Unit: 
Berber Cavalry (Replaces Cavalry)
Homeland Guardian - 25% combat bonus in friendly territory (keeps on upgrade)
Desert Warrior - 50% combat bonus in desert (keeps on upgrade)

Unique Improvement: 
Kasbah (Requires Chivalry)
Can only be built on a resourceless desert tile (including flood plains) within your own territory
Yields 1 food, 1 production and 1 gold
+50% defence to units on the tile

Strategy

Morocco is best at diplomatic victories.

Perhaps the diplomatic Civ with the best defensive capabilities, Morocco is excellent at playing a peaceful game of maintaining friendships - and making sure you continue to receive plenty of trade routes (and hence gold) from other Civs. Morocco's UA gives you more gold (and culture, to a lesser extent) the more different Civs have a trade route with you, so to maximise this bonus, trade with a range of City-States and let the trade routes of other full Civs come to you. Get routes set up quickly, and you won't have to worry about the early-game money issues many other Civs face.

A desert start bias makes the powerful Desert Folklore Pantheon a distinct possibilty and through it a strong religion, but the main attraction of deserts is Morocco's Kasbahs. Kasbahs make settling in desert areas much more viable, although flat desert tiles are still weak; keep to flood plain or desert hill-heavy areas. You can try completing the Liberty Social Policy tree quickly to grab a free Great Engineer and rush Petra in a desert hill city for very high yields, but this isn't a completely reliable strategy. A more consistent way to get more from Kasbahs is to emphasise Golden Ages, which doubles their gold outputs.

If being friendly to other Civs to ensure their continued trading and settling in lands that are unattractive to other Civs isn't enough to keep invasions away, the industrial era brings Berber Cavalry, which are perhaps the most powerful defensive unit in the game. In deserts within your own lands, the unit's strength increases by 75%, allowing them to take on even technologically-advanced armies. The high power of each unit means you can keep a smaller military in the late-game, saving you money that otherwise would go towards maintenance. Saved maintenance along with UA and Kasbah gold should be enough to secure plenty of City-State allies and hence win a World Leader vote.

Social Policy trees	
1. Liberty
2. Patronage
3. Commerce or Piety
Ideology	Freedom
Religion	Pantheon: Desert Folklore or other faith Pantheons
Founder: Tithe or Papal Primacy or Church Property
Follower: Any happiness bonuses
Enhancer: Religious Texts or Religious Unity
Reformation: Charitable Missions or To the Glory of God

Key wonders	
Colossus
Petra
Chichen Itza
Machu Picchu
Notre Dame
Forbidden Palace
Taj Mahal
Big Ben
Statue of Liberty

Summary of key strengths
Encourages inward trade routes which can provide a strong boost to early science on higher difficulties
Strong defence, especially relative to other diplomatic Civs
Can make good use of desert which is otherwise marginal terrain
""",

    "Netherlands":"""
Start bias
Grassland.

Unique Ability: 
Dutch East India Company
Trading your last copy of a luxury resource away still provides you with half its happiness
This bonus is affected by the Protectionism Social Policy in the Commerce tree, meaning 4 happiness rather than 2 when traded away.

Unique Unit: 
Sea Beggar (Replaces the Privateer)
Coastal Raider II - 20% bonus against cities and steals gold equivalent to 33% of damage when attacking them (keeps on upgrade)
Supply - Can heal outside friendly territory (keeps on upgrade)

Unique Improvement: 
Polder (Requires Guilds)
Can only be built on marshes and flood plains within your own territory. Does not remove marshlands when built upon them.
Yields 3 food
+1 production and +2 gold with Economics

Strategy

The Dutch are best at diplomatic victories but can situationally be strong at domination or science.

No matter your eventual victory route, the Dutch ability to rapidly expand in the early-game thanks to their UA will be useful. Rather than just trading excess luxuries, you can viably trade them all for luxuries you don't have giving you more happiness than most Civs at this stage of the game. This allows you to handle more cities earlier on, which gives them more time to develop.

Where should those cities go? Marsh or especially floodplain-heavy regions, so you can build Polders later on. At first, Polders are equal to or superior to farms in food yields - if you have a good marsh/floodplain start, sticking to a low number of cities, building tall with this food and seeking a scientific victory is an option. Once you've got the renaissance-era Economics technology, they also gain a point of production and two points of gold, making them tiles that you'll pretty much always want to work.

Privateers are excellent units already; they can capture enemy ships and deal decent damage to cities, but Sea Beggars takes that even further. They can heal outside friendly lands, making them much more viable on prolonged campaigns, and they start with Coastal Raider II in addition to the default Coastal Raider I. With just an Armoury, you can get to Logistics - aside from increasing per-turn damage output, it also lets you move Sea Beggars after attacking to keep them safe from city attacks and let more Sea Beggars move in to attack the cities. If you can't get a good war going during their main window of use, don't worry - they keep more promotions when upgraded than any other unit in the game.

So, good Polder spots can lead towards scientific victory and Sea Beggars could lead to a domination victory on a water-heavy map, but diplomacy is what the Netherlands do best at. Trading luxuries, working Polders and attacking cities with Sea Beggars all can get you gold, which means more potential for bribing City-States for their delegates.

Social Policy trees	
1. Liberty
2. Patronage (diplomacy) or Exploration (domination) or Commerce (science)
3. Exploration (diplomacy) or Commerce (diplomacy) or Rationalism (domination or science)
Ideology	Freedom (diplomacy or science) or Order (domination or science)
Religion	Pantheon: Faith Pantheons or Messenger of the Gods or God of the Sea
Founder: Tithe or Church Property or Papal Primacy (diplomacy)
Follower: Any happiness bonuses (diplomacy or domination), Religious Community (science), Swords into Plowshares (science)
Enhancer: Religious Unity (diplomacy), Religious Texts or Itinerant Preachers

Key wonders	
Temple of Artemis (science)
Colossus
Great Lighthouse
Petra
Chichen Itza
Machu Picchu
Notre Dame
Forbidden Palace (diplomacy)
Leaning Tower of Pisa (science)
Porcelain Tower (science)
Big Ben
Kremlin or Statue of Liberty
Great Firewall (science)
Pentagon (domination)
CN Tower (diplomacy or domination)
Hubble Space Telescope (science)

Summary of key strengths
Highly flexible - uniques can suit most playstyles
Early happiness boost makes early expansion easier
Strong economy; all three uniques can help provide gold
""",

    "Ottomans":"""
Start bias
Coastal.


Unique Ability: 
Barbary Corsairs
-67% naval unit maintenance cost
All naval melee units recieve the Prize Ships promotion which allows them to capture enemy ships on a decisive victory
Captured ships will become in your control with 50 HP, but unable to perform any action until the turn after capture
The chance of capturing a ship can be as high as 80% against much weaker ships or as low as 20% on stronger ones

Unique Unit I: 
Janissary (Replaces the Musketman)
25% strength bonus when attacking (keeps on upgrade)
50 health restored on a non-Barbarian kill (keeps on upgrade)

Unique Unit II: 
Sipahi (Replaces the Lancer)
5 moves, up from 4
3 sight, up from 2
No movement cost to pillage (keeps on upgrade)

Strategy

The Ottomans are best at domination victories.

Along with England, the Ottomans are powerful at mid-game warfare both by land and by sea. Like England, their naval-based UA has its uses throughout the game - in this case, you can build a couple of Triremes to pick off Barbarian naval units and build a free, easily-maintained navy out of it. Interestingly, you can even steal unique naval units off other Civs this way, but on the whole you shouldn't dive into war until your Janissaries are ready.

Janissaries are one of the most effective UUs around owing to their high damage output and ability to make risky attacks safe in the knowledge the health-on-kills attribute will stop them from getting destroyed immediately afterwards. Your early-game should be mostly dedicated to preparing for Janissary-led wars, so be sure to emphasise science generation and production before beelining Gunpowder. Like most non-ranged UUs, Janissaries will need ranged backup to deal with cities - Cannons or Frigates are fine for this purpose.

Complementing Janissaries are Sipahi, which make decent support units. Don't hold off your Janissary wars until Sipahi are ready; instead, bring Sipahi in when you're already at war. They can pillage enough in a turn that they're pretty hard to kill, as well as getting you a bit of gold along the way and ruining the lands of enemy cities. You can rush in a few Sipahi to ruin a city's infrastructure prior to bringing your slower units in, making it hard for them to respond.

Social Policy trees	
1. Liberty or Honour
2. Exploration
3. Rationalism
Ideology	Autocracy
Religion	Pantheon: Faith Pantheons or Messenger of the Gods or God of the Sea
Founder: Tithe or Church Property
Follower: Any happiness bonus
Enhancer: Religious Texts or Itinerant Preachers or Just War

Key wonders	
Statue of Zeus
Colossus
Great Lighthouse
Machu Picchu
Notre Dame
Neuschwanstein
Prora
Pentagon

Summary of key strengths
Effective at renaissance-era warfare at both sea and on land
UUs can play more aggressively without the risk of dying; Janissaries receive 50HP from kills and Sipahi can recover health rapidly via pillaging
Can assemble a navy with minimal effort from cities, allowing them to dedicate more time to land forces or infrastructure
""",

    "Persia":"""
Start bias
None.

Unique Ability: 
Achaemenid Legacy
Golden Ages last 50% longer
This stacks additively with other bonuses, so with the Chichen Itza wonder and Universal Suffrage tenet, Golden Ages are 150% longer than their base length.
During a Golden Age, all units gain a 10% strength bonus and +1 movement point
The strength bonus applies to land, naval and air units alike, and works against cities.
The movement point bonus works on land, naval and civilian units, but not embarked units.

Unique Unit: 
Immortal (Replaces the Spearman)
12 strength, up from 11
Double Heal Rate - While healing, heals 10HP per turn more (keeps on upgrade)

Unique Building: 
Satrap's Court (Replaces the Bank)
3 gold generated per turn, up from 2
+2 local city happiness

Strategy

Persia is best at domination victories, is good at diplomacy and is reasonable at other routes.

If you want war without the little annoyances, Persia is the Civ for you. Their UU, the Immortal, heals much faster than normal Spearmen and are slightly stronger, giving you and excellent unit to take damage on behalf of an early Composite Bowman army. That's powerful enough already to take out another Civ early on, but add Liberty's Representation (typically the earliest way of getting a Golden Age) and you've got a highly mobile force with a 10% strength bonus that even works against cities!

Immortal/Composite Bowmen armies will only get you so far on their own, so settle down with your early conquests, accumulate some excess happiness (both for the Golden Age potential and to get you ready for future conquests) and build up a Golden Age infrastructure. By that, I mean emphasising things that might lead to more or longer Golden Ages in future - the Chichen Itza wonder (if someone else takes it, well, you know who your next target is), bonuses to Great Artist generation, that kind of thing. By the middle of the game, you may be able to start an indefinite Golden Age, popularly known as "Forever Golden".

Once the state of Forever Golden is achieved, Persia becomes an incredibly deadly warmonger for other Civs to face. Rough terrain and the Great Wall don't slow you down as much as other Civs. You eat up Social Policies more rapidly than most Civs, and with all the culture, make life hard for cultural Civs. You have plenty of production to churn out new units, which are automatically stronger than the new units made by other Civs. And you have masses of cash. And conquests won't slow you down as much as they would for other Civs, because you can get extra happiness via your UB.

There's a slight catch to this, however. In order to maximise Golden Age potential, Persia takes quite an unusual Social Policy path. They're the only non-cultural Civ that should consistently take the Aesthetics tree, and the only warmonger that should go for the Freedom ideology. Aesthetics takes a bit of time for its effects to really kick in, unlike Commerce (the usual pick for warmongers at this point) and taking Freedom means giving up a war-centric level three tenet, but Persia's powerful Golden Ages are worth the sacrifice.

Social Policy trees	
1. Liberty
2. Aesthetics
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or Faith Healers or Messenger of the Gods
Founder: Tithe or Church Property
Follower: Any happiness bonus
Enhancer: Religious Texts or Itinerant Preachers or Reliquary

Key wonders	
Statue of Zeus
Alhambra
Chichen Itza
Machu Picchu
Notre Dame
Leaning Tower of Pisa
Sistine Chapel
Taj Mahal
Uffizi
Brandenburg Gate
Louvre
Cristo Redentor
Statue of Liberty
Pentagon

Summary of key strengths
Strong at war at any point in the game, assuming a Golden Age can be started
Very strong economic support for war - bonuses via Golden Ages and happiness via Satraps' Courts
Good resistance to rival ideologies via happiness and Golden Age culture but can go to war effectively with any ideology in case the pressure is overwhelming
""",

    "Poland":"""
Start bias
Plains.

Unique Ability: 
Solidarity
At the start of every era (besides the Ancient era) recieve one free Social Policy.
The free Social Policy does not raise the cost of future policies or remove stored culture

Unique Unit: 
Winged Hussar (Replaces the Lancer)
28 strength, up from 25
5 moves, up from 4
Heavy Charge - When attacking, if the defending unit deals less damage than the Winged Hussar it retreats one tile, favouring the direction opposite the Winged Hussar. If the unit can't manage that, it takes extra damage. (keeps on upgrade)
Shock I - 15% combat bonus in open terrain (keeps on upgrade)

Unique Building: 
Ducal Stable (Replaces the Stable)
Costs 75 production in normal speed games, down from 100
Costs 400 gold, down from 500
0 maintenance cost, down from 1
Provides 15XP to mounted units built in the respective city
+1 gold for pasture resources (horses, sheep, cattle)

Strategy

Poland is best at domination victories but can viably go for any victory path.

Every era, Poland receives a completely free Social Policy or ideological tenet. By the end of the game, this is more than enough to get an entire Social Policy tree for free, and you'll have a huge advantage to development throughout the game. Additionally, you can open Social Policy trees as soon as they become available (especially powerful for ones with strong openers like Rationalism.)

Although the UA works well for any victory route, your other uniques complement renaissance-era warfare nicely and as such domination makes your most reliable path. Make sure you settle your cities near horses for the sake of future Winged Hussars, or at least cows or sheep for Ducal Stables. Ducal Stables, in addition to helping you build mounted units (including your UU) quickly, also give you gold so you can support more of them, and lets them start with more XP.

Winged Hussars are the strongest and fastest renaissance land unit, but that's not all - they also start with Shock I (with a Military Academy and a Ducal Stable, you can get them straight to March or Blitz) and have the unique ability to knock back enemies they hit. You can knock enemies off favourable terrain this way, or you can try moving around enemy units and knocking them towards you. If the unit's cornered (such as against mountains or the sea,) you'll deal even more damage! Winged Hussars struggle against cities, however - bring Cannons (and later, Artillery) to deal with them. Although your UU can be used throughout the industrial era, it doesn't upgrade very well, so you need to be prepared to shift towards a more conventional end-game army, but that shouldn't pose too much of a problem thanks to the developmental advantages your UA gave you.

Social Policy trees	
1. Liberty and/or Tradition
2. Commerce
3. Rationalism
Ideology	Autocracy or Order
Religion	Pantheon: Faith Pantheons or God of the Open Sky or Messenger of the Gods
Founder: Tithe or Church Property or World Church
Follower: Any happiness or production bonus
Enhancer: Religious Texts or Itinerant Preachers or Just War

Key wonders	
Pyramids
Statue of Zeus
Oracle
Alhambra
Machu Picchu
Notre Dame
Brandenburg Gate
Kremlin or Prora
Neuschwanstein
Pentagon

Summary of key strengths
Highly flexible - can pursue any victory route effectively
Can open Social Policy trees as soon as they're available, providing a reasonable head start
Has the strongest land unit of the renaissance era
""",

    "Polynesia":"""
Start bias
Coastal.

Unique Ability: 
Wayfinding
Can embark land units from the start of the game with no technology requirement
Any embarked or naval unit (including Galleasses and Triremes) can immediately cross oceans with no technology requirement
Cargo Ships are an exception. They can be relocated between continents, but their Trade Routes cannot cross oceans until Astronomy is researched.
Units recieve +1 sight when embarked (2 instead of 1.)
All units within 2 tiles of a Moai improvement recieve a 10% strength boost
This applies to land, sea and air units alike. The bonus is based on where the unit is situated/based when attacking, not where the target is.
This works even on Moai outside your lands

Unique Unit: 
Maori Warrior (Replaces the Warrior)
Haka War Dance - 10% penalty to adjacent enemy land units' strength (keeps on upgrade)
This promotion's effect does not stack
This has no effect if you're using a ranged attack on an enemy unit in the promotion's range

Unique Improvement: 
Moai (Requires Construction)
Can only be built on a coastal tile within your own territory
May be built on tiles containing resources
If constructed on marshland, does not remove the marsh.
+1 culture
+1 culture for every adjacent Moai
+1 gold with Flight

Strategy

Polynesia is best at cultural victories.

The only pure-cultural Civ with a maritime emphasis, Polynesia offers quite distinctive gameplay - but first, let's start with the simplest unique: The Maori Warrior, which replaces your Warriors (so as such, you start with one.) They make adjacent enemy units 10% weaker, which is handy for clearing out Barbarians faster. As the bonus carries over on upgrade, it'll provide a nice little edge in combat if another Civ aims to invade.

A bonus that can help deal with Barbarians is nice for the early-game, but what really gives Polynesia an edge early on is the ability to embark and even cross oceans immediately. This can help you to discover every Civ in the game very early on (hence giving you great trading opportunities) as well as allowing you to access islands (and therefore Ancient Ruins) no-one else can get to. With two sight rather than one, embarked units are also decent coastal explorers before you can get Triremes up and running.

Being able to discover Civs early and accumulate tourism against them is a small bonus towards cultural victory, but Polynesia's key advantage is the Moai Unique Improvement. Having lots of them clustered together creates large culture yields, and with a Hotel and Airport in a nearby city, good sums of tourism. Look for two-tile-thick landmasses for the maximum possible output, but be careful you don't work too many early on at the expense of production or city growth - you'll need at least one decent city for building theming bonus wonders. If the offer of faster cultural victories via Moai tourism isn't enough, they'll also generate gold with Flight (particularly powerful during a Golden Age) which is good for holding a presence in the World Congress to get things like the International Games or Arts Funding passed. Furthermore, your UA also gives your units 10% extra strength if they're within two tiles of a Moai, giving you quite strong defences when combined with Maori Warriors' Haka War Dance promotion.

So, Polynesia's key advantages are early-game exploration, defence and (eventually) tourism. They make an excellent choice for players who like to know what's going on in the world without having to fight it.

Social Policy trees	
1. Tradition or Liberty
2. Aesthetics
3. Exploration
4. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or God of the Sea
Founder: Tithe or Church Property
Follower: Swords into Plowshares (tall-building), Religious Community (tall-building), any happiness bonus (wide-building)
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Any theming bonus wonder
Temple of Artemis (tall-building)
Hanging Gardens (tall-building)
Parthenon
Leaning Tower of Pisa
Cristo Redentor
Eiffel Tower
Statue of Liberty
Great Firewall
CN Tower (wide-building)

Summary of key strengths
Extremely effective early exploration, especially on water-heavy maps; usually can take more Ancient Ruins than most Civs
Usually the first to discover all nations and, if the first to Printing Press, is generally guarenteed to be the first host of the World Congress
Good early defence, and on water-heavy maps, can be immune from elimination for as much as the first half of the game by settling overseas
Reasonable tourism potential
""",

    "Portugal":"""
Start bias
Coastal.

Unique Ability: 
Mare Clausum
Resource diversity bonuses (having cities with different resources to each other on other ends of an international trade route) are doubled for Portugal.
This means 1 gold instead of 0.5 per different resource for land trade routes, and 2 gold instead of 1 for naval trade routes.
This has no effect on international trade routes not set up by Portugal.

Unique Unit: 
Nau (Replaces the Caravel)
5 moves, up from 4
One-time-use ability to generate a lump sum of gold as well as experience when adjacent to or within a foreign tile
The further from the capital the Nau is, the more money and experience it generates

Unique Improvement: 
Feitoria (Requires Navigation)
Can only be built in coastal resourceless tiles in City-State territory (may replace existing improvements)
+50% defence to units on the tile
Provides one untradable copy of each luxury resource type the City-State owns

Strategy

Portugal is best at diplomatic victories.

While not quite as rich as Venice, Portugal is nonetheless one of the game's best Civs for generating gold. The Unique Ability affects quite an obscure mechanic, but all you really need to know is that your international trading (particulary with mercantile City-States) will give you more gold than normal, and settling coastal areas near lots of resources will make the best use of that. Build wide so you have a good range of cities to trade from and to maximise the number of luxury tiles you can work later in the game for gold. Because of Portugal's heavy use of international trading, try not to get involved in wars - you don't want to lose all those Cargo Ships.

Naus have more movement than Caravels, making them excellent at exploring the oceans, but more to the point, they can perform a one-use action akin to Great Merchants' Trade Missions. The yields are lower, but it doesn't consume the unit and grants it experience. This offers an interesting way to convert production to gold at a more efficient ratio than is offered by the conventional option on the city screen.

Finally, building Feitorias gives you vast amounts of happiness allowing you to grow your wide empire and from there work plenty of gold tiles. All these vast sums of cash can be used to bribe City-States for alliances, and you can use their delegates to win a World Leader vote.

Social Policy trees	
1. Liberty
2. Patronage
3. Exploration
Ideology	Freedom
Autocracy
Religion	Pantheon: Faith Pantheons or God of the Sea
Founder: Papal Primacy or Tithe or Church Property
Follower: Any happiness bonuses
Enhancer: Religious Texts or Itinerant Preachers or Religious Unity

Key wonders	
Colossus
Great Lighthouse
Petra
Forbidden Palace
Neuschwanstein
Prora or Statue of Liberty
CN Tower

Summary of key strengths
Second to Venice in gold potential, without the no-Settler restriction
Very strong happiness bonus via Feitorias
Can create a midgame navy cheaply via the Exotic Goods ability of Naus
""",

    "Rome":"""
Start bias
None.

Unique Ability: 
The Glory of Rome
+25% production in all cities towards buildings that already exist your current capital
This bonus applies to all your cities besides your capital - puppet and regular alike.

Unique Unit I: 
Legion (Replaces the Swordsman)
17 strength, up from 14
Can construct roads and forts like a Worker (with the respective technologies; cannot remove them)
Obsoletes with Gunpowder instead of Steel

Unique Unit II: 
Ballista (Replaces the Catapult)
8 strength, up from 7 (+14%)
10 ranged strength, up from 8 (+25%)

Strategy

Rome is best at domination victories, but can go for any other victory route reasonably effectively.

With very straightforward bonuses, Rome is an excellent choice for someone wanting to play a wide-building Civ for the first time. Their UA makes setting up in new cities considerably faster; great for getting cities ready to raise an army. Grab Bronze Working early so you can find iron spots, and settle them before anyone else - you'll need it for Legions.

Legions are the classical era's most powerful unit and are even slightly stronger than Pikemen, for a lower cost. You don't need to worry about bringing Spearmen along for the ride - Legions are actually better against mounted units than them. They can also build forts and roads; the latter of which gives Legions a very helpful role in peacetime. However, don't fall into the trap of rushing Iron Working straight away to churn them out; basic development technologies like Writing are more important to grab first.

Complementing Legions are Ballistae. With a nice strength boost, you can both tear city defences down more easily and take less damage doing so, letting you recover sooner. Your two UUs together make Rome the strongest classical-era warmonger around - use that advantage to secure a wide empire so you can make good further use of your UA. You can continue along the warpath, upgrading your UUs to better units in later eras, or perhaps shift course to a different victory route - all victory routes have quite a few buildings tied to them that need constructing, and the faster you can do that, the better your odds at winning.

Social Policy trees	
1. Liberty or Honour
2. Commerce
3. Rationalism
Ideology	Order
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Tithe or Church Property
Follower: Any happiness bonuses
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Pyramids
Alhambra
Angkor Wat
Machu Picchu
Notre Dame
Big Ben
Brandenburg Gate
Kremlin
Neuschwanstein
Pentagon
CN Tower

Summary of key strengths
Effective at early warfare
Strong at developing new cities in a wide empire
Reasonably flexible; UA helps towards any victory path
""",

    "Russia":"""
Start bias
Tundra.

Unique Ability: 
Siberian Riches
All tiles with strategic resources (Horses, Iron, Coal, Oil, Aluminium or Uranium) gain +1 production
Improved horse, iron and uranium resources within your territory provide double their normal quantities
This stacks with the Third Alternative tenet from the Autocracy ideology to create quadruple quantities of the respective resources.
Resources from trading or from allied City-States are not doubled in quantity.

Unique Unit: 
Cossack (Replaces the Cavalry)
33% combat bonus against wounded units (keeps on upgrade)

Unique Building: 
Krepost (Replaces the Barracks)
Reduces the gold and culture costs of acquiring new tiles in the respective city by 25%

Strategy

Russia is best at domination victories.

Russia is one of a handful of Civs built around the "sledgehammer" playstyle; develop peacefully at first, then build up a strong infrastructure ready for assembling a huge army later in the game capable of taking all the world's capitals without needing substantial reinforcement. Doubled quantities of certain strategic resources increases the potential size of your army, while extra production allows you to build up to that larger size without taking a much greater length of time.

Helping you in the task of securing strategic resources is the Krepost UB, which allows your cities to accumulate tiles more rapidly both via culture and via gold. Combined with a wide empire, you should be able to secure plenty of oil; a crucial resource your UA doesn't double the quantities of and one that will be necessary to upgrade your Cossacks.

Cossacks signal the point where you need to switch from peaceful development to preparing for war. They're very effective unit killers, which start with a promotion identical to Charge, but can be stacked with it for a 66% bonus against wounded units! Build plenty and bring some Artillery along with them to deal with city defences. The promotion Cossacks have carries over on upgrade, which combined with Autocracy's Lightning Warfare, gives you armoured units that can easily flank enemy units and deal massive damage to them.

Finally, if conventional warfare doesn't quite work out, Russia is the only Civ with a direct advantage in nuclear warfare - they receive double uranium resources (quadruple with Autocracy's Third Alternative.) Don't count on waiting until Atomic Bombs come along before starting a war (uranium is rare, so there's quite a chance you won't have any in your settled lands); think of this more as a backup strategy.

Social Policy trees	
1. Liberty
2. Commerce
3. Rationalism
Ideology	Autocracy
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Tithe or Church Property
Follower: Any happiness bonuses, Religious Community
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Alhambra
Angkor Wat
Machu Picchu
Notre Dame
Brandenburg Gate
Neuschwanstein
Prora
Pentagon

Summary of key strengths
Strong at late-game warfare, and is the only Civ with a direct advantage to nuclear warfare
Unlikely to suffer strategic resource penalties in the first half of the game
Above-average production, useful for any victory route
""",

    "Shoshane":"""
Start bias
None.

Unique Ability: 
Great Expanse
Start the game with a Pathfinder (the Shoshone Scout UU) instead of a Warrior
Founded cities receive 8 additional tiles, on top of the default 7
These tiles are typically those which would have been favoured by the city gaining those tiles via culture
These tiles do not raise the culture or gold cost of the next tiles (so the first tile the city gains through culture will cost the same as it does for any other Civ.)
Military land units receive a 15% bonus to combat within friendly territory
Air and naval units do not gain this bonus. Helicopter Gunships don't get the bonus unless they've been upgraded to from an Anti-Tank Gun.

Unique Unit I: 
Pathfinder (Replaces the Scout)
Costs 45 production in normal-speed games, up from 25
Costs 220 gold in normal-speed games, up from 140
8 strength, up from 5
Upgrades to a Composite Bowman rather than an Archer via Ancient Ruins
Native Tongue - Can choose benefit when entering Ancient Ruins (keeps on upgrade)
Options include gaining culture, gold, faith, a technology, a point of population in one of your cities, revealing part of the map, revealing nearby Barbarian encampments and upgrading the unit. On Settler difficulty, you have the two additional options of a free Worker or a free Settler.
Has a "cooldown" - must explore two ruins between each choice of the same option. (e.g. Technology -> Culture -> Population bonus -> Technology.)
The faith option cannot be chosen until turn 20 (on normal speed games.) Once you've founded a Pantheon, the faith offered by it triples, and its cooldown resets. Once you've founded a religion, you can no longer choose the option.
You cannot choose to upgrade a unit via Ancient Ruins if it has already received an upgrade from them.
The technology option only works for ancient-era technologies, and as such, cannot be picked once you have all of them.

Unique Unit II: 
Comanche Riders (Replaces the Cavalry)
Costs 310 gold to upgrade in normal-speed games, up from 260
Costs 200 production in normal-speed games, down from 225
Costs 680 gold in normal-speed games, down from 740
Costs 170 gold to upgrade to in normal-speed games, down from 220
Full Moon Striker - +1 movement point (keeps on upgrade)

Strategy

The Shoshone are best at domination and scientific victories.

While Brazil makes the late-game more complicated, the Shoshone are all about the early-game. Immediately, you have a significant advantage to exploration with a free super-Scout, while your UA gives your capital access to lots of good tiles immediately, helping it to grow faster even before you have any Workers. Put that growth to good use - build a couple of extra Pathfinders to complement your first so you can track down lots of Ancient Ruins. Choosing the population point option first gives you several turns' head start in development, and the culture boost, free technology and free faith are also powerful choices.

As Ancient Ruins disappear from the map, it's time to consider expansion. Getting lots of tiles when founding a city is actually good for both wide-building strategies (cutting off lots of land chokes the potential of other Civs and stops them competing for space) and tall-building approaches (again, getting good tiles early gives a head start to development.) Building wide as the Shoshone best-suits a domination victory, while building tall is generally better for science. If anyone seeks to take your vast lands in warfare, you've got a 15% friendly lands bonus on all your land units to make things harder for them.

Compared to Pathfinders, Comanche Riders are the lesser UU, but they still have their uses. With a speed bonus that keeps on upgrade, you'll have fast armoured units which are great with Autocracy's Lightning Warfare for surrounding enemies and maximising flanking bonuses. Even if you're not going to war with them, they're still helpful for covering your vast lands quickly to repel would-be attackers.

Social Policy trees	
1. Liberty or Tradition
2. Commerce
3. Rationalism
Ideology	Autocracy (domination)
Freedom (science)
Order
Religion	Pantheon: Faith Pantheons or Messenger of the Gods
Founder: Tithe or Church Property
Follower: Any happiness bonus (domination), Religious Community (science), Swords into Plowshares (science)
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Great Library
Pyramids
Temple of Artemis (science)
Hanging Gardens (science)
Alhambra (domination)
Machu Picchu
Notre Dame (domination)
Leaning Tower of Pisa (science)
Porcelain Tower (science)
Brandenburg Gate (domination)
Kremlin or Prora or Statue of Liberty
Neuschwanstein (domination)
Great Firewall (science)
Pentagon (domination)
CN Tower (domination)
Hubble Space Telescope (science)

Summary of key strengths
Very strong start
Effective at seizing lots of land early, indirectly weakening other players
Reasonable defense
""",

    "Siam":"""
    Start bias
Avoid forest.

Unique Ability: 
Father Governs Children
Cultural, maritime and religious City-States gift 50% more culture, food and faith respectively when befriended or allied
Unit gifts from militaristic City-States start with 10 more experience than normal
Mercantile City-States are not affected.

Unique Unit: 
Naresuan's Elephant (Replaces the Knight)
3 moves, down from 4
25 strength, up from 20
Does not require Horse resources
50% bonus vs. mounted units

Unique Building: 
Wat (Replaces the University)
+3 culture

Strategy

Siam is best at scientific victories but can shift to diplomacy as a back-up.

A typical game as Siam is a sort of mash-up between a tall-building scientific Civ and a diplomatic Civ. Because they have no advantages to gold or holding influence, Siam will struggle to compete in a World Leader vote, but before then, they can get an awful lot out of City-State friendships and alliances. Just killing a few Barbarians early on for a religious City-State can secure you a good faith Pantheon and with it a religion, while befriended maritime City-States can make your capital huge. Generally, religious City-States should be your main priority at first, followed by maritime City-States. Once your domestic faith generation has got off the ground, that order switches.

In the medieval era, Siam's culture generation really takes off. Cultural City-States are amazing sources of culture, as are Wats. Being a University replacement, you'll be building lots of Wats anyway, so enjoy eating Social Policies up faster than pretty much any other non-cultural Civ. That edge will get you through the Rationalism tree quickly, and with it, a scientific edge. Later on, you'll be able to take both Treaty Organisation and Space Procurements from the Freedom ideology so you can both secure your City-State friendships/alliances and build the spaceship faster.

Not far from Wats on the technology tree are Naresuan's Elephants. With high strength and a bonus against other mounted units, they're essentially slow, cheap Lancers available an era early. Their purpose is to defend you throughout the medieval and renaissance eras so you can focus on the peaceful technologies in the top half of the technology tree and not get distracted from the pursuit of science.

Social Policy trees	
1. Tradition
2. Patronage
3. Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or food Pantheons
Founder: Papal Primacy or Tithe or Church Property
Follower: Swords into Plowshares, Religious Community, Divine Inspiration, Feed the World
Enhancer: Religious Unity or Missionary Zeal or Holy Order

Key wonders	
Great Library
Stonehenge
Temple of Artemis
Hanging Gardens
Oracle
Borobudur or Hagia Sophia
Forbidden Palace
Leaning Tower of Pisa
Porcelain Tower
Sistine Chapel
Cristo Redentor
Great Firewall
Hubble Space Telescope

Summary of key strengths
Very high culture output, particularly useful for slowing down cultural Civs
Good mid-game defence
Easy to make use of all uniques without making difficult detours on the technology tree
Emphasis on City-States makes it easy to switch to diplomacy if other victory routes don't work out
""",

    "Songhai":"""
Start bias
Avoid tundra.

Unique Ability: 
River Warlord
Destroying Barbarian encampments grants triple the normal amount of gold (75 rather than 25 in normal speed games of Prince difficulty and above)
Capturing cities grants triple the normal amount of gold
This stacks with Egyptian Burial Tombs to grant six times the normal amount of gold, but doesn't stack with the double gold Landsknechte get from capturing cities.
All military land units have a free Amphibious promotion (can attack across rivers or from the sea with no combat penalty)
Military embarked units (civilian units including Great Generals aren't affected) have double defence and +1 sight

Unique Unit: 
Mandekalu Cavalry (Replaces the Knight)
Costs 240 gold to upgrade in normal speed games, up from 220
Costs 110 production in normal speed games, down from 120
Costs 430 gold in normal speed games, down from 460
Costs 80 gold to upgrade to from a Chariot Archer in normal speed games, down from 135
Costs 55 gold to upgrade to from a Horseman in normal speed games, down from 100
No city attack penalty

Unique Building: 
Mud Pyramid Mosque (Replaces the Temple)
0 maintenance cost, down from 2
+2 culture

Strategy

Songhai is best at domination victories.

An underrated warmongering Civ, Songhai comes with all sorts of little bonuses. Destroying Barbarian encampments early on can make quite a sum of gold - use it to help with expansion; you'll want to grab a good number of horse resources ready for Mandekalu Cavalry. Although not as effective as Keshiks or Camel Archers, they can perform hit-and-run attacks on cities reasonably well, and can be built cheaply. Bring some Crossbows and you've got quite an effective mid-game army going. If you need to cross the sea to invade, don't worry - double embarkment defence means you can keep a minimal number of escort units, and the free Amphibious promotion makes attacking coasts much easier.

Where Songhai really comes into its own is the aftermath of combat. Triple gold from capturing cities covers maintenance costs and then some - you can use the excess to buy more units or happiness buildings to support conquest. Choose to puppet rather than annex cities you want to keep; they won't raise Social Policy costs that way, so you can exploit the culture bonus of Mud Pyramid Mosques effectively. If you fall into severe unhappiness, finish up your wars quickly to allow time to recover, but otherwise, keep the wars going until victory.

Social Policy trees	 
1. Honour (opener) and Liberty
2. Commerce or Piety
3. Rationalism
Ideology	Autocracy or Order
Religion	Pantheon: Faith Pantheons or Messenger of the Gods or Ancestor Worship
Founder: Tithe or Church Property
Follower: Any happiness bonus and/or Choral Music
Enhancer: Religious Texts or Itinerant Preachers
Reformation: To the Glory of God or Religious Fervour

Key wonders	
Pyramids
Statue of Zeus
Alhambra
Angkor Wat
Any Theology wonder
Machu Picchu
Notre Dame
Sistine Chapel
Big Ben
Brandenburg Gate
Kremlin or Prora
Neuschwanstein
Pentagon

Summary of key strengths
Decent economy early on thanks to encampment gold
Strong gold income during war thanks to tripled gold from capturing cities
Good at building a wide, religion-heavy puppet empire
Double embarkment defence and free amphibious promotion allows armies to be used for amphibious invasions much more effectively than other Civs, saving time and money on building a navy
""",

    "Spain":"""
Start bias
Coastal.

Unique Ability: 
Seven Cities of Gold
Discovering natural wonders gives a gold bonus (typically 100 gold in normal-speed games)
The gold bonus is higher if you're the first to discover the natural wonder (typically 500 gold in normal-speed games)
Happiness from discovering natural wonders or having certain natural wonders (e.g. Fountain of Youth) within your land is doubled
Tile yields from natural wonders are doubled
Double tile yields also affects the One With Nature Pantheon and the Natural Heritage Sites resolution from the World Congress

Unique Unit I: 
Conquistador (Replaces the Knight)
Costs 135 production in normal-speed games, up from 120
Costs 500 gold In normal-speed games, up from 460
Costs 165 gold to upgrade to from a Chariot Archer In normal-speed games, up from 135
Costs 130 gold to upgrade to from a Horseman In normal-speed games, up from 100
Upgrade cost of 190 rather than 220 in normal speed games
4 sight, up from 2
No penalty when attacking cities
Can found a city on a landmass not containing your capital, using up the unit
Double embarkment defence and may embark without the Optics technology (keeps on upgrade)

Unique Unit II: 
Tercio (Replaces the Musketman)
Counts as a standard melee unit rather than gunpowder melee, meaning...
Tercios can be built 15% faster with the Warrior Code Social Policy
The 25% bonus against gunpowder Impis (the Zulu UU) have doesn't work against Tercios
Costs 160 production in normal-speed games, up from 150
Costs 570 gold in normal-speed games, up from 540
Costs 90 gold to upgrade to in normal-speed games, up from 70
Upgrade cost of 140 rather than 160 in normal speed games
26 strength, up from 24
50% bonus vs. mounted units

Strategy

Spain is best at cultural and domination victories.

The common perception of Spain as a very luck-based Civ has truth, but is also overrated. Being first to discover a natural wonder early on gives you enough gold to buy a Settler to found a city there, but that infrequently happens and isn't necessary for a good game as Spain. What is necessary is taking a natural wonder as soon as you can - even if that entails capturing a City-State near one. The exact natural wonder you take doesn't matter; so long as you can get one quickly and set up the One With Nature Pantheon, you'll generate enough faith on the tile to secure yourself a religion.

Whether you have a strong start or even one without any natural wonders, it's important to make use of your UUs. Conquistadors make excellent support units - they can perform hit-and-run attacks against cities reasonably effectively and cross seas without needing to be escorted (similar advantages to Songhai's Mandekalu Cavalry) but on top of that, they also have the highest sight of any land unit (making them worth keeping even into the industrial era to provide a line of sight for Artillery) and can, on landmasses not containing your capital, found cities. You can use them to explore new landmasses rapidly, and quickly settle if you find new natural wonders. Unlike Settlers, they can be purchased with faith via the Holy Warriors belief making an interesting use of excess faith from One With Nature.

While Conquistadors offer a support role, Tercios are all-round unit-killers (although they'll need help with cities.) They'll win against pretty much any other unit in their era or earlier. Because they're classed as standard melee units rather than gunpowder, you can eliminate their higher cost disadvantage with Honour's Warrior Code.

Once the World Congress is created, get Natural Heritage Sites passed. It'll add 10 culture to every natural wonder you own, which can be added to tourism with a Hotel, Airport and/or the National Visitor Centre. Just a Hotel and an Airport makes a natural wonder worth almost as much tourism as the Eiffel Tower (and that's assuming the wonder doesn't have any culture of its own!) You can use this to complement other sources of tourism towards a cultural victory, or enjoy having more happiness available due to having a stronger ideology, hence having more to support conquests.

Social Policy trees	
1. Liberty (up to Collective Rule)
1.5. Liberty (rest of tree), Piety (up to Reformation) or Honour (up to Warrior Code)
2. Exploration or Piety or Aesthetics (culture)
3. Rationalism
Ideology	Freedom (culture)
Autocracy (culture or domination)
Order (domination)
Religion	Pantheon: One With Nature or other faith Pantheons
Founder: Tithe or Church Property or Pilgrimage
Follower: Holy Warriors or any happiness bonuses or Divine Inspiration (culture) and Religious Community (culture)
Enhancer: Just War or Religious Texts or Itinerant Preachers
Reformation: Religious Fervour (domination) or Sacred Sites (culture) or Jesuit Education

Key wonders	
Any theming bonus wonder (culture)
Alhambra
Borobudur or Hagia Sophia
Machu Picchu
Notre Dame
Leaning Tower of Pisa (culture)
Brandenburg Gate (domination)
Eiffel Tower
Kremlin or Prora or Statue of Liberty
Neuschwanstein
Great Firewall (culture)
CN Tower

Summary of key strengths
Very strong early faith potential
Effective at overseas exploration and expansion
Potential for very strong individual cities due to doubled natural wonder yields
Reasonable mid-game warfare; Tercios have no real weaknesses until the industrial era
""",

    "Sweden":"""
Start bias
Tundra.

Unique Ability: 
Nobel Prize
+10% Great Person Points in all cities for every declaration of friendship active
This bonus affects Great Artists, Engineers, Merchants, Musicians, Scientists and Writers, but not Great Prophets, Generals or Admirals.
Being "friends" with City-States does not count
This bonus stacks, meaning two DoFs gives a 20% bonus
The befriended nation also gains +10% Great Person Points in all cities
Gain 90 influence with a City-State when gifting a Great Person to them
As with any unit, there's a three turn delay between gifting the Great Person and you gaining the influence, unless you move the unit into the City-State's territory and gift it directly.
This 90 influence does not stack with the 5 from gifting military units or the Freedom ideology's Arsenal of Democracy tenet's 15 Influence bonus.

Unique Unit I: 
Hakkapeliita (Replaces the Lancer)
15% combat bonus when sharing a tile with a Great General (keeps on upgrade)
If both this unit and a Great General start a turn on the same tile, the Great General can move as much as the Hakkapeliitta can for that turn (keeps on upgrade)

Unique Unit II: 
Carolean (Replaces the Rifleman)
March - Heals every turn, even when performing an action (keeps on upgrade)

Strategy

Sweden is best at diplomatic victories, is almost as good at domination victories and can perform reasonably well at science and culture.

An oddity among diplomatic Civs, Sweden works best building tall rather than wide due to their Great Person-focused UA. Don't get involved in early wars - instead, try to make as many friends as possible. 5 declarations of friendship is a 50% bonus; enough to match Babylon's UA but for every type of Great Person. No Great Person is useless for Sweden - you can gift the ones you don't need to City-States for 90 influence, the equivalent to an alliance and a half. Honour's Warrior Code offers the earliest Great Person in the game - a Great General - which can be gifted to a religious City-State to help secure you an early religon, but be aware that comes at the cost of a couple of early developmental Social Policies from the Tradition tree.

Interesting choices of Social Policies are quite important to Sweden's game. Finishing the Patronage tree allows you to receive Great People from allied City-States. Aside from this creating a feedback loop, (you ally with a City-State, it gives you a Great Person, you can give it back for more influence,) it also offers you a chance of getting a Khan, normally restricted to Mongolia. Completing Piety up to Reformation lets you take To the Glory of God and essentially turn faith into influence.

In the industrial era, it's time to prepare for war. Hakkapeliitta get winning odds against Cavalry when both are backed by Great Generals, but you don't need to build many - Caroleans and Artillery are more useful. If you received a Khan from an allied City-State, adjacent Caroleans will heal at least a quarter of their health every single turn making your forces incredibly hard to stop. You can either attempt world domination this way, or try killing lots of units to farm Great Generals. Keep those Great Generals and other excess Great People around until about 4-5 turns before a World Leader vote, then you can gift them all at once for a huge boost to influence that will be incredibly hard to overturn.

Social Policy trees	
1. Tradition and/or Honour (up to Warrior Code)
2. Patronage
3. Piety (diplomacy) or Rationalism (domination)
4. Any Great Person generation bonuses
Ideology	Autocracy (diplomacy or domination)
Freedom (diplomacy)
Religion	Pantheon: Faith Pantheons or Faith Healers
Founder: Papal Primacy or Tithe or Church Property
Follower: Swords into Plowshares, Religious Community, Divine Inspiration
Enhancer: Religious Unity or Just War or Religious Texts or Itinerant Preachers
Reformation: To the Glory of God or Charitable Missions or Religious Fervour

Key wonders	
Temple of Artemis
Great Wall
Hanging Gardens
Alhambra
Machu Picchu
Notre Dame (domination)
Forbidden Palace
Porcelain Tower
Leaning Tower of Pisa
Brandenburg Gate
Neuschwanstein
Prora or Statue of Liberty
Pentagon

Summary of key strengths
Strong Great Person output, especially on maps with high numbers of Civs
Alternative use for all Great People ensures all are useful
Good at industrial-era warfare
Great at pulling off unexpected diplomatic victories by well-timed Great Person gifts
Ideal for a tall-building diplomatic playstyle
""",

    "Venice":"""
Start bias
Coastal. Venice is placed before all other Civs, increasing their odds of a coastal start even further, but it is still not a certainty.

Unique Ability: 
Serenissima
Can never acquire Settlers by any means (except for the starting Settler to found your capital with)
Can never annex cities (all captured cities must be either puppeted or razed)
Free Merchant of Venice (Venice's Great Merchant replacement) when researching Optics
Taking the Collective Rule policy in the Liberty tree grants a Merchant of Venice instead of a Settler
Can purchase units and buildings (including faith purchases and spaceship parts with the Space Procurements tenet in the Freedom tree) in puppeted cities
Trade Route limit doubled

Unique Unit: 
Great Galleass (Replaces the Galleass)
Costs 110 production, up from 100
Costs 430 gold, up from 400
18 strength, up from 16
20 ranged strength, up from 17
Upgrade cost of 160 rather than 180 in normal speed games

Unique Great Person: 
Merchant of Venice (Replaces the Great Merchant)
+2 moves while embarked
Double gold and influence from Trade Missions
Can expend in City-State territory to turn it into a puppet in your control. Does not require an alliance or even friendship. The city can never be turned back into a City-State.
If the City-State owns multiple cities, they will all be taken as puppets under your control at once.

Strategy

Venice is best at diplomatic victories.

The oddest Civ in the game, Venice plays unlike anyone else. You can't choose where to build cities aside from your capital - you have to either capture others or use Merchants of Venice to convert more. Additionally, all cities aside from your capital will be puppets, so while it gives you an edge to Social Policy acquisition, your science will suffer if you expand to too many cities (puppets raise technology costs like normal cities, but have a 25% penalty to science output.) What you do have, however, is the strongest economy in the game and the ability to purchase items in puppeted cities. You'll have 16-20 trade routes by the end of the game, giving you so much cash that you'll dominate the World Congress/United Nations and still have money to spare for developing your cities' infrastructures.

Merchants of Venice provide you with a peaceful means of expansion; they can instantly and irreversibly annex City-States. Don't overdo it - although the delegate requirement for World Leader votes is adjusted to compensate for the loss of the City-State, every City-State you annex increases the relative value of non-City-State delegates, making the World Congress more competitive. Instead, use later Merchants of Venice for Trade Missions - they're twice as effective as they are for normal Great Merchants.

Finally, Great Galleasses have a small window of usage, but during that time they're the strongest ship in the sea and will help keep your naval trade routes safe from Barbarians or other pillagers.

Social Policy trees	
1. Tradition
2. Patronage
3. Commerce or Exploration or Rationalism
Ideology	Freedom
Religion	Pantheon: Faith Pantheons or God of the Sea
Founder: Tithe or Interfaith Dialogue
Follower: Religious Community, Swords into Plowshares, Feed the World
Enhancer: Religious Texts or Itinerant Preachers or Religious Unity or Defender of the Faith

Key wonders	
Stonehenge
Temple of Artemis
Colossus
Hanging Gardens
Angkor Wat
Forbidden Palace
Leaning Tower of Pisa
Red Fort
Big Ben
Statue of Liberty

Summary of key strengths
Strongest economy in the game bar none
Strong versus other diplomatic Civs; if an alliance can't be easily overturned with great wealth, the city can simply be annexed via a Merchant of Venice to set back the opposing Civ.
Ability to purchase in puppets means puppet cities are considerably more useful at war
No pressure to seek out good spots to settle
Strongest navy in the late-medieval to early-renaissance eras
""",

    "Zulu":"""
Start bias
Avoid jungle.

Unique Ability: 
Iklwa
Standard melee units cost half the normal maintenance
Each promotion costs 25% less XP than normal
The experience cap for fighting Barbarians (30 XP) is unaffected.

Unique Unit: 
Impi (Replaces the Pikeman)
Upgrade cost of 280 rather than 200 in normal speed games (+40%)
When attacking units, Impis first perform a special ranged-like attack, dealing damage without receiving any before immediately before going into normal melee combat.
The ranged attack counts separately for XP purposes (2 for the ranged attack, 5 for the melee)
The attack does take effect if the Impi is attacking while embarked.
25% bonus vs. gunpowder units
Upgrades to Riflemen, rather than Lancers and as such Impis can be built until Rifling, rather than Metallurgy.

Unique Building: 
Ikanda (Replaces the Barracks)
Standard melee units receive the Buffalo Horns promotion for free (+1 movement, +25% flanking bonus, +10% defence against ranged attacks)
These units then have access to the Buffalo Chest promotion (+10% open terrain combat strength, +25% flanking bonus, +10% ranged defence) which is obtained like any other promotion
Units with the Buffalo Chest promotion can then obtain the Buffalo Loins promotion (+10% combat strength, +25% flanking bonus, +10% ranged defence)

Strategy

The Zulus are best at domination victories.

For a Civ with a huge military power spike, look to the Zulus. Their Impi UU can be complemented by both their Unique Ability and the Ikanda alike, making them an incredibly tough opponent in the medieval and renaissance eras. There's a catch, however - most bonuses obsolete by the industrial era, so it's crucial you get a good war going. Along with basic Worker technologies and Writing, pick up Bronze Working early for Ikandas, then beeline Civil Service so you can get Impis quickly.

Ikandas give standard melee units access to a unique set of promotions including large flanking bonuses, and more importantly, a +1 movement speed bonus! High mobility makes it easier to scout new locations, catch enemies and position your units into a strong formation (i.e. surrounding enemies.) As only units which were first built/bought as standard melee units can have these promotions, the only way of getting new units with them in the late-game is to get Commerce's Mercenary Army and buy Landsknechte, which have an awkward upgrade path. Your UA's reduced maintenance cost similarly only works on standard melee units.

Even without Ikandas offering extra mobility and flanking bonuses, Impis are powerful units. They can deal damage without receiving any before starting combat - unlike any other melee unit. This gives them a good enough damage output to be competitive with Longswordsmen, helps the unit to take less damage from combat and even gives the Impi more XP when attacking! Furthermore, Impis have a hidden 25% bonus against gunpowder units, which together with their 50% bonus against mounted units, allows them to take on pretty much anything prior to the industrial era. They'll still struggle somewhat against cities, so bring some ranged or siege units to help out.

Finally, the reduced XP cost of promotions offered by your UA complements the fast XP gain of Impis beautifully, but more to the point, it's the one bonus you have that isn't tied to any particular point in the game. Autocracy's Total War along with the Brandenburg Gate and a Military Academy in the same city (which isn't as hard to do as it sounds) can give you new units of any kind with instant top-tier promotions (March, Blitz, Logistics, etc.) to help mop up the last few Civs that didn't fall to your Impi wars.

Social Policy trees	
1. Honour
2. Commerce
3. Rationalism
Ideology	Autocracy
Religion	Pantheon: Faith Pantheons or Messenger of the Gods or God of Craftsmen or Faith Healers
Founder: Tithe or Church Property or Ceremonial Burial
Follower: Any happiness bonuses
Enhancer: Religious Texts or Itinerant Preachers

Key wonders	
Statue of Zeus
Terracotta Army
Alhambra
Notre Dame
Brandenburg Gate
Pentagon

Summary of key strengths
Very strong mid-game land warfare, especially on the offensive against units, even more so against mounted units
Can still be effective even with a technological disadvantage thanks to stacked bonuses on Impis (including +25% vs. gunpowder)
Low melee maintenance and fast promotions makes it easy to move from one opponent to the next with less of a need to rebuild the economy
""",
}

   


# Function to update the notes display
def update_notes(*args):
    civ = civ_var.get()
    notes_text.delete(1.0, tk.END)
    notes_text.insert(tk.END, civ_notes.get(civ, "No notes available for this civilization."))

# Function to open the hyperlink
def open_link(event):
    webbrowser.open_new("https://steamcommunity.com/sharedfiles/filedetails/?id=506298426")

# Set up the main GUI window
root = tk.Tk()
root.title("Civ Helper")
root.geometry("800x600")

# Mainframe setup
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Civilization dropdown menu
civ_var = tk.StringVar()
civ_menu = ttk.Combobox(mainframe, textvariable=civ_var, width=30)
civ_menu['values'] = list(civ_notes.keys())
civ_menu.grid(column=0, row=0, sticky=tk.W)

# Text widget to display the notes
notes_text = tk.Text(mainframe, wrap="word", width=80, height=30)
notes_text.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

# Always on top checkbox
always_on_top_var = tk.BooleanVar()
always_on_top_checkbox = ttk.Checkbutton(
    mainframe, text="Always on Top", variable=always_on_top_var,
    command=lambda: root.attributes("-topmost", always_on_top_var.get())
)
always_on_top_checkbox.grid(column=0, row=2, sticky=tk.W)

# Hyperlink label
link_label = tk.Label(mainframe, text="Information formatted from Zigzagzigal's Civ Summaries (BNW)", 
                      fg="blue", cursor="hand2")
link_label.grid(column=0, row=3, sticky=tk.S)
link_label.bind("<Button-1>", open_link)

# Event handling for the dropdown menu
civ_var.trace('w', update_notes)

# Padding for all elements
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Initialize the application
root.mainloop()
