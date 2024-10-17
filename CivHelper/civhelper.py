import tkinter as tk
from tkinter import ttk

# Define the notes for each civilization
civ_notes = {}

america_notes = """
Start bias: None.

Uniques

Unique Ability: Manifest Destiny

- Tiles cost 50% less gold to buy.
- Military land units have +1 sight.

Unique Unit I: Minuteman (Replaces the Musketman)

- Ignores terrain movement costs (keeps on upgrade).
- Gives Golden Age points on a kill equal to the opposing unit's strength, or ranged strength if it's higher (keeps on upgrade).
- Drill I - 15% combat bonus in rough terrain (keeps on upgrade).

Unique Unit II: B17 (Replaces the Bomber)

- 70 ranged strength, up from 65.
- Siege I - +33% attack vs. cities (keeps on upgrade).
- Evasion - -50% damage from being intercepted (keeps on upgrade).

Strategy

America does best at domination victories.

America's sight advantage makes them excellent at scouting out terrain early on to find ancient ruins, city locations, natural wonders, and other Civs. Once you've got some cash, you can cheaply buy high-yield tiles near your cities to get them growing, or try settling near another Civ and buying tiles to block them from expanding.

Try to get Minutemen going as soon as possible, backed with either Trebuchets, Crossbows, or Cannons. With just an Armoury, Minutemen can start with Siege to do decent damage to cities, or Cover II to stay defended against them. Ignoring terrain costs means they can easily slip through and flank enemies.

If one round of war isn't enough, America can go again in the Atomic era with their powerful B17s. A Military Academy and either Autocracy's Total War tenet or the Brandenburg Gate will let you build new B17s immediately with Logistics, letting them attack twice in one turn. Fill some Carriers with B17s, bring some Destroyers and Battleships to escort them and you'll have a very deadly end-game navy.

Social Policy trees: 1. Liberty, 2. Commerce or Exploration, 3. Rationalism

Ideology: Autocracy, Order

Religion: Pantheon: Faith Pantheons or Faith Healers, Founder: Tithe or Church Property, Follower: Any happiness bonuses, Enhancer: Messiah if you have Faith Healers, Religious Texts or Itinerant Preachers otherwise.

Key wonders: Statue of Zeus, Angkor Wat, Notre Dame, Brandenburg Gate, Kremlin or Prora, Pentagon

Summary of key strengths:

- Early exploration.
- Combat in rough terrain.
- End-game warfare.
"""

arabia_notes = """
Start bias: Desert.

Uniques

Unique Ability: Ships of the Desert

- Caravans have a 50% increased range.
- Trade routes spread the home city's religion (the majority religion in the city the trade route was sent from) twice as effectively.
- Oil resources you're personally producing provide double their normal quantities.
- Resources from trading or from allied City-States are not doubled in quantity.
- This stacks with the Third Alternative tenet from the Autocracy ideology to create quadruple quantities of oil.

Unique Unit: Camel Archer (Replaces the Knight)

- Classified as a ranged unit rather than a mounted unit, therefore is built faster with the Temple of Artemis and has no vulnerability to Pikemen.
- Instead of a melee attack, has a ranged attack with 21 strength and a range of 2 tiles.
- 17 melee strength, down from 20.
- No city attack penalty.

Unique Building: Bazaar (Replaces the Market)

- Provides 1 extra copy of every improved luxury resource near the city (in your land and within a three-tile radius).
- 2 gold generated per turn, up from 1.
- Increases gold yield by 2 for every oasis or oil tile worked by the city.

Strategy

Arabia does best at diplomatic or domination victories.

Arabia begins peacefully. Expand fairly quickly and get a faith and trade route infrastructure going. Your Caravans can travel further than those of other Civs, and therefore will make more money. Once you have a religion, stack pressure bonuses (e.g. Religious Texts) and the spread of your faith will be hard to stop.

Before you convert the world, however, you have a strong opportunity to conquer it with the Camel Archer. Camel Archers can move in range of cities, fire at them, and move out of range of their attacks, allowing them to do a great deal of damage without being harmed themselves. They cannot capture cities themselves, so use a couple of unpromoted Horsemen to get the last hit.

If war isn't for you, Arabia's huge oil quantities and the Bazaar's doubling of luxury resources puts you in a good position as a trader. Trade other Civs for gold, and you can use that money to bribe City-States for delegates at the United Nations, and from there get diplomatic victory.

Social Policy trees: 1. Liberty, 2. Piety, Patronage (diplomacy) or Commerce (domination), 3. Commerce (diplomacy) or Rationalism (domination)

Ideology: Freedom (diplomacy), Autocracy (domination)

Religion: Pantheon: Desert Folklore or other faith Pantheons, Founder: Tithe or Church Property or Papal Primacy (diplomacy), Follower: Any happiness bonuses, Enhancer: Religious Texts, Reformation: Jesuit Education or To the Glory of God or Charitable Missions (diplomacy)

Key wonders: Petra, Great Mosque of Djenne, Notre Dame (domination), Forbidden Palace (diplomacy), Big Ben (domination), Neuschwanstein

Summary of key strengths:

- Reasonable gold output.
- Fast religious spread, especially if using the start bias with Desert Folklore.
- Very effective mid-game warfare.
"""

assyria_notes = """
Start bias: Avoid tundra.

Uniques

Unique Ability: Treasures of Nineveh

- When you conquer an enemy city, whether from a full Civ or City-State, you gain a random technology.
- You can only gain technologies the respective enemy has and you don't.
- This can only happen once per enemy city (so losing and recapturing a city won't work and you can't get technologies out of recapturing your own cities you lost).
- Cities captured by other means don't count (e.g. trade deals).

Unique Unit: Siege Tower (Replaces the Catapult)

- No ranged attack, attacks by melee instead.
- Can only attack cities.
- Does not need to set up to attack.
- 12 strength, up from 7.
- 3 sight, up from 1.
- When adjacent to an enemy city, friendly land units within 2 tiles gain a 50% bonus against that city.
- This works even if the Siege Tower is embarked, though embarked and naval units themselves do not receive the 50% bonus.

Unique Building: Royal Library (Replaces the Library)

- +1 Great Writing slot.
- +10XP to units built in the city with the slot filled.

Strategy

Assyria's best at domination and scientific victories, and isn't bad at culture either.

Assyria's a fun Civ that thrives in unusual playstyles. With the powerful Siege Tower UU, it's one of the few Civs which has a real edge to early-game conquests. Work towards getting Mathematics early along with Construction for Composite Bowmen, followed by building a couple of Siege Towers along with about four Composite Bowmen. Don't waste time building wonders at this point, and Barracks are likely to be not worth the cost. Siege Towers do massive damage against cities, and cities they're next to will be vulnerable to your other units.

For most Civs, going to war often means your infrastructure (and hence your science) lags behind, but as Assyria gains technologies from conquest, they can just keep pushing for military technologies to keep their armed forces ahead, using war to catch up with the more peaceful technologies you missed.

The Royal Library is the odd one out of Assyria's uniques. Although filling the Great Writing slot gives +10XP for all units built in the city, that won't ever be worth an extra starting promotion unless the city has no other XP boosts. Instead, its main advantage is the slot itself - Great Writing slots get quite scarce by the end of the game relative to the number of Great Works you may have generated. This can be helpful for maximizing your culture or tourism potential.

So, you have three routes. Either just carry on with war to a domination victory, use the science advantage to a scientific victory, or use your extra slots and conquered Great Works to a cultural victory.

Social Policy trees: 1. Honour, 2. Aesthetics (culture) or Commerce (diplomacy and domination), 3. Exploration (culture) or Rationalism

Ideology: Autocracy (culture and domination), Order (science)

Religion: Pantheon: Faith Pantheons or God of Craftsmen, Founder: Tithe or Church Property, Follower: Any happiness bonuses, Enhancer: Religious Texts or Itinerant Preachers

Key wonders: Any theming bonus wonder (culture), Leaning Tower of Pisa (culture and science), Brandenburg Gate, Eiffel Tower (culture), Kremlin or Prora, Neuschwanstein (domination), Hubble Space Telescope (science)

Summary of key strengths:

- Powerful early warfare.
- Can recover effectively from a weak position.
- Able to pursue a military focus without neglecting infrastructural technology.
"""

aztec_notes = """
Start bias: Jungle.

Uniques

Unique Ability: Sacrificial Captives

- When killing any enemy unit, gain culture equal to the unit's strength, or ranged strength if it's higher.
- This works in a similar way to the Honour opener (but for all units instead of just Barbarians) and stacks with it.

Unique Unit: Jaguar (Replaces the Warrior)

- 33% extra strength in forest and jungle (keeps on upgrade).
- Woodsman - Double movement rate through forest and jungle (keeps on upgrade).
- 25 health restored on a kill (keeps on upgrade).

Unique Building: Floating Gardens (Replaces the Water Mill)

- Can be built in cities adjacent to lakes as well as rivers.
- 1 maintenance cost, down from 2.
- +15% food bonus.
- +2 food to every lake tile worked by the city.
- Does not affect the Lake Victoria natural wonder.

Strategy

The Aztecs are best at domination and scientific victories.

Start by taking the Honour opener and killing Barbarians with your Jaguars. The culture you'll get allows you to push ahead through the Tradition tree quickly, which nicely complements the Floating Gardens. Floating Gardens offer a considerable food bonus (unlike a growth bonus, it applies to all food output in the city, not just surplus) making it easy to build tall. Together with your jungle start bias, you can get quite an edge on science.

For the rest of the game, the key is to balance war with science. Don't neglect one when going for the other, or you won't get the full potential out of your uniques. Take some time to build up a tech advantage, then go to war. If you're playing scientifically, it's best not to take too many cities to avoid the diplomatic penalties associated with it (and hence the loss of potential research agreements.) If you're going for domination, make sure you can handle what you take and raze what you can't manage.

Social Policy trees: 1. Honour Opener and Tradition, 2. Honour, 3. Rationalism

Ideology: Order (domination), Freedom (science)

Religion: Pantheon: Faith Pantheons or food Pantheons or Sacred Path, Founder: Tithe or World Church, Follower: Swords into Plowshares or Feed the World and Religious Community, Enhancer: Religious Texts or Defender of the Faith

Key wonders: Great Library, Temple of Artemis, Hanging Gardens, Leaning Tower of Pisa, Porcelain Tower, Kremlin or Statue of Liberty, Great Firewall, Hubble Space Telescope (science)

Summary of key strengths:

- Strong, early UU minimises the threat of Barbarians and offers decent exploration potential.
- Fast city growth.
- UA ensures you can salvage rewards out of a war in stalemate.
"""

babylon_notes = """
Start bias: Avoid tundra.

Uniques

Unique Ability: Ingenuity

- Receive a free Great Scientist with the Writing technology.
- This does not increase the cost of future Great Scientists, Engineers or Merchants.
- 50% bonus to Great Scientist generation.
- This stacks additively with other bonuses, so if you had just this and a Garden in a city, it would have a 75% bonus to Great Scientist generation.

Unique Unit: Bowman (Replaces the Archer)

- 7 strength, up from 5.
- 9 ranged strength, up from 7.

Unique Building: Walls of Babylon (Replaces Walls)

- Costs 65 production, down from 75.
- Provides 6 city strength, up from 5.
- Provides 100 city HP, up from 50.

Strategy

Babylon is best at scientific victories.

Get Writing immediately. Then, use the Great Scientist to place an Academy (preferably adjacent to your capital so it can't easily be pillaged.) This will give you a huge science bonus over anyone else for quite some time, allowing you to rush through the early eras. After you've cleaned up your Worker technologies, push on towards Education so you can get Universities and their scientist slots filled. Keep creating Academies with the Great Scientists you gain until the modern era. Then, hang on to them until 8 turns after you've built Research Labs, and start using them to rush technologies instead. The 8 turn gap seems strange, but the amount of science you get from Great Scientists is based on the output of the last 8 turns.

If all this science is worrying your neighbors, your other uniques can help defend yourself. Walls of Babylon give your cities two-thirds more health rather than a third making them much harder to take over, while Bowmen are roughly mid-way between Archers and Composite Bowmen, allowing you to have an adequate defense without having to take a diversion to Construction.

For a change of strategy, Bowmen also make good early rushing units. Take a few along with a couple of Warriors or Spearmen, and you may be able to take out an unprepared rival. An early captured capital is a significant advantage which will make eventual scientific victory even easier.

Social Policy trees: 1. Tradition, 2. Commerce, 3. Rationalism

Ideology: Freedom

Religion: Pantheon: Faith Pantheons or food Pantheons, Founder: Tithe or Interfaith Dialogue, Follower: Swords into Plowshares or Feed the World and Religious Community or Guruship, Enhancer: Religious Texts or Reliquary

Key wonders: Great Library, Mausoleum of Halicarnassus, Temple of Artemis, Hanging Gardens, Leaning Tower of Pisa, Porcelain Tower, Red Fort, Statue of Liberty, Great Firewall, Hubble Space Telescope

Summary of key strengths:

- Strongest early-game science.
- Extremely strong early-game defensive potential, combined with early scientific advantages, this makes Babylon very hard to attack.
"""

# Add the new civ notes to the dictionary
civ_notes["Aztec"] = aztec_notes
civ_notes["Babylon"] = babylon_notes

# Function to show civilization notes
def show_civ_notes(civ):
    return civ_notes.get(civ, "No notes available for this civilization.")

# Set up the GUI
root = tk.Tk()
root.title("Civ Helper")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Drop-down menu for selecting a civilization
civ_var = tk.StringVar()
civ_menu = ttk.Combobox(mainframe, textvariable=civ_var)
civ_menu['values'] = list(civ_notes.keys())
civ_menu.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Text box to display the notes
notes_text = tk.Text(mainframe, width=80, height=30, wrap="word")
notes_text.grid(column=1, row=2, sticky=(tk.W, tk.E))

# Function to update the notes display
def update_notes(*args):
    civ = civ_var.get()
    notes_text.delete(1.0, tk.END)
    notes_text.insert(tk.END, show_civ_notes(civ))

civ_var.trace('w', update_notes)

# Padding for all child elements of the mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()