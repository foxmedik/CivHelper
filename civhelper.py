import tkinter as tk
from tkinter import ttk

# Civilization notes
civ_notes = {
    "America": """Start bias: None
Uniques:
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

Strategy:
America does best at domination victories.

America's sight advantage makes them excellent at scouting out terrain early on to find ancient ruins, city locations, natural wonders and other Civs. Once you've got some cash, you can cheaply buy high-yield tiles near your cities to get them growing, or try settling near another Civ and buying tiles to block them from expanding.

Try to get Minutemen going as soon as possible, backed with either Trebuchets, Crossbows or Cannons. With just an Armoury, Minutemen can start with Siege to do decent damage to cities, or Cover II to stay defended against them. Ignoring terrain costs means they can easily slip through and flank enemies.

If one round of war isn't enough, America can go again in the Atomic era with their powerful B17s. A Military Academy and either Autocracy's Total War tenet or the Brandenburg Gate will let you build new B17s immediately with Logistics, letting them attack twice in one turn. Fill some Carriers with B17s, bring some Destroyers and Battleships to escort them and you'll have a very deadly end-game navy.

Social Policy trees:
1. Liberty
2. Commerce or Exploration
3. Rationalism

Ideology:
Autocracy
Order

Religion:
Pantheon: Faith Pantheons or Faith Healers
Founder: Tithe or Church Property
Follower: Any happiness bonuses
Enhancer: Messiah if you have Faith Healers, Religious Texts or Itinerant Preachers otherwise.

Key wonders:
Statue of Zeus
Angkor Wat
Notre Dame
Brandenburg Gate
Kremlin or Prora
Pentagon

Summary of key strengths:
Early exploration
Combat in rough terrain
End-game warfare
""",
    # Add other civilizations similarly...
}

def show_notes(*args):
    civ = civ_var.get()
    notes_var.set(civ_notes.get(civ, "No notes available."))

# Create the main window
root = tk.Tk()
root.title("Civ V Quick Reference Guide")

# Create a variable to hold the selected civilization
civ_var = tk.StringVar()
civ_var.set("Select a civilization")

# Create a dropdown menu
civ_dropdown = ttk.OptionMenu(root, civ_var, *civ_notes.keys(), command=show_notes)
civ_dropdown.pack(pady=10)

# Create a text widget to display the notes
notes_var = tk.StringVar()
notes_label = tk.Label(root, textvariable=notes_var, wraplength=500, justify="left")
notes_label.pack(pady=10)

# Start the main event loop
root.mainloop()
