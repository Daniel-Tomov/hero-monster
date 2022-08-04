# hero-monster
Classes and Objects practice for SANS Foundations course

# Instructions

Create a game that uses 2 classes: Hero() and Monster().

The hero:
<ul>
<li>Has a weapon that does an amount of damage</li>
<li>Has an amount of health</li>
<li>Can attack with their weapon and cause damage</li>
<li>Can lose health if attacked</li>
<li>Will die if they have 0 health</li>
<li>Has 1 healing potion that they can drink to get back 5 health, but the potion can only be used once.</li>
</ul>
The monster:
<ul>
<li>Has an attack strength and can do an amount of damage</li>
<li>Has an amount of health</li>
<li>Can roar</li>
<li>Can attack and cause damage</li>
<li>Can lose health if attacked</li>
<li>Will automatically run away if it gets down to 1 health remaining</li>
</ul>


Once you have your classes and objects working, create constructors for each one so you can build them anytime you want with damage strength and starting health points that you choose.

Allow your program to accept user input so you can specify the stats of your hero, then have the program randomly assign values to the monster and have them fight, trading attacks back and forth, until the hero dies or the monster runs away.


# Example of Monster dying
Specify how much damage you want your hero to do: 10000000

Specify how much health you want your hero to have: 10000000

Attacking

The Hero has attacked and the Monster has -9999913 health remaining

The Monster has died

# Example of Hero dying

Specify how much damage you want your hero to do: 15

Specify how much health you want your hero to have: 50 

Attacking

The Hero has attacked and the Monster has 82 health remaining

Attacking

RRROOOOAAAAARRR

The Monster has attacked and the Hero has 22 health remaining

Attacking

RRROOOOAAAAARRR

The Hero has healed

The Monster has attacked and the Hero has -1 health remaining

The Hero has died
