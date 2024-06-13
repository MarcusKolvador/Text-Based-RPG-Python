import sys
import os
import time

screen_width = 100
global debug
debug = False


# Player initialization
class Player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mana = 0
        self.stamina = 0
        self.status_effects = []
        self.location = "b2"
        self.game_finished = False
        self.gender = ""
        self.archetype = ""
        self.weapon = ""


Player = Player()


# Dragon initialization

class Dragon:
    def __init__(self):
        self.name = "Maevnussut"
        self.hp = 10000
        self.mana = 5000
        self.stamina = 1000


Dragon = Dragon()


# Debug options
def debug():
    global debug
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        debug = True

    else:
        debug = False


# Title Screen #
def main():
    debug()
    intro = """
You stand in front of the giant stone doors... touching them, brings a still coolness to your skin.

Your eyes catch sight of faint, weathered, and enigmatic markings within the stone.
As you observe them, they light up with a faint blue glow. Suddenly, understanding dawns upon you...

Say - Enter - to embrace fate.
Say - Help - for assistance.
If you wish to abandon this journey, utter the word - Quit -.

"""
    os.system("clear")
    print(
        "###################################################################################################"
    )
    writer(intro)
    print(
        "###################################################################################################\n"
    )
    while True:
        option = input("> ")
        if option.lower() == ("enter"):
            char_create()
            sys.exit()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        else:
            writer(
                "The doors do not resonate. The cold stone only stares back into you.\n"
            )


# Help menu
def help_menu():
    os.system("clear")
    help = """
Main menu functionality:

Type - Enter - to start.
Type - Help - for this menu.
Type - Quit - to exit this game.

Runtime arguments:

Run with - -d - for debugging mode

In game controls:

Type - move - to enable movement controls, followed by:
Type    - up/north -, - down/south -, - left/west -, -right/east -
Type - examine - to examine said location
Type - quit - to quit the game

Please wait for the - > - indicator, to input text or commands.

"""
    print(
        "###################################################################################################"
    )
    writer(help)
    print(
        "###################################################################################################\n"
    )


ZONE_NAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

zones = {
    "a1": {
        ZONE_NAME: "stalagmite formation",
        DESCRIPTION: """You encounter a formation of rocks, boulders and stalagmites... there is something peculiar about this area, as if some essence imbues the very wind, whispering to you

As you venture into the midst of the rocky formation, a symphony of textures surrounds you—rough boulders, jagged rocks, and delicate stalagmites standing like ancient sentinels.
The air carries an otherworldly essence, as if some ethereal force imbues the very wind that sweeps through the stones, whispering secrets known only to the land.

Perhaps there is a hidden meaning to the symbols. The play of light and shadow dances on the surfaces, creating an ever-shifting tapestry of colors.
You feel an intangible connection to the place, as if the rocks themselves hold the echoes of stories untold.

A gentle breeze carries with it a soft, melodic hum, stirring your senses and inviting you to listen closely to the murmurs of the ancient stones.

Should you choose to head on from here, the northern and western paths appear daunting, almost impassable.
You quickly rule them out, realizing the need to focus on the more accessible routes.
Turning your attention east and south, you weigh the possibilities, deciding that one of these directions holds the key to continuing your journey through the mysterious landscape.

With a determined stride, you set forth on your next step, eager to uncover the secrets that await.""",
        EXAMINATION: """As focus your ears on the faint murmurs within the wind, a slow, rhythmic passage seems to fill your ears:

'I'm born in the silence, yet I speak with grace,
In the open embrace, my presence takes place.
Whispers I mimic, as if in a trance,
In rocky chambers, you might get a chance.'

You rub your head in confusion, the riddle echoing in your mind like the very essence of the wind.
The words resonate with the surroundings, leaving you with a sense that the rocks themselves hold the key to unraveling the mystery.
The rhythmic cadence lingers, inviting you to ponder the enigma concealed within the ancient stones.""",
        SOLVED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2",
    },
    "a2": {
        ZONE_NAME: "rocky plateau",
        DESCRIPTION: """As your feet touch the rocky expanse, the ground feels uneven and cool beneath your boots.

To the west, a gathering of rocks forms a rugged formation, resembling a silent forest in stone.

Turning east, the rocky expanse gradually yields to a grassy plain, a stark contrast in textures.

Even as you sense the transition beneath your steps, the southern stretch echoes the familiar mix of rocks and greenery.

You hesitate at the prospect of heading north, a lingering uncertainty pulling at your instincts. The rocks stand like sentinels, and the unknown awaits in that direction.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3",
    },
    "a3": {
        ZONE_NAME: "grassy area",
        DESCRIPTION: """As you venture further across the grassy plain, the landscape unfolds in a symphony of contrasts.
To the east and south, your eyes are drawn to the inviting sandy coast, where the gentle waves of a glimmering lake lap against the shore.

In stark opposition to the serene waters, the western horizon reveals a rocky wasteland. Towering formations of jagged rocks and rugged cliffs create an imposing barrier.
The ground beneath your feet transitions from the soft grass to a more unforgiving terrain, signaling the challenging journey that awaits in that direction.

You pause, contemplating the northern path. A subtle intuition nudges you, whispering that your journey here is not yet complete.
The landscape holds untold mysteries, and you decide to press on, guided by an unseen force that beckons you to explore further.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "",
        DOWN: "a4",
        LEFT: "a2",
        RIGHT: "a4",
    },
    "a4": {
        ZONE_NAME: "sandy coast",
        DESCRIPTION: """Standing on the sandy coast, you reflect on your journey, still uncertain about the why and how of your arrival.
Yet, a strange familiarity and a comforting sense of home linger in this mystical area.
A glimmer in the lake captures your attention, sparking curiosity. The waters appear serene and inviting, tempting you to explore further.

To the west, the path leads to a grassy plain, evoking a nostalgic aura.
However, the northern and eastern paths seem to discourage your advance, as if an unseen force urges caution.
The choices before you hold the promise of discovery and the potential for unraveling the mysteries that shroud your existence in this enigmatic realm.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: "",
    },
    "b1": {
        ZONE_NAME: "rocky wasteland",
        DESCRIPTION: """Your feet tread upon a harsh wasteland of rock and sand, the whispering wind carrying secrets from the northern rocky formations.
To the east, the familiar greenery marks the place where your journey began.
Down south, the wasteland stretches, growing more unforgiving with each step.

Despite the allure of the unknown, you decide that the west path is not the direction to continue your adventure.
The rocky formations to the north and the changing landscape to the south beckon, offering divergent paths for exploration.
With a determined choice, you set your course, eager to uncover the mysteries that lie ahead.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "a1",
        DOWN: "c2",
        LEFT: "",
        RIGHT: "b2",
    },
    "b2": {
        ZONE_NAME: "green plains",
        DESCRIPTION: """Returning to the green plains where your journey began, a curious sense of familiarity and calm envelops you.
Despite the uncertainty of your location, a peculiar reassurance prevents fear from taking hold.
The vibrant greenery seems to embrace you, and the whispering wind carries echoes of the mysteries you've encountered.

As you stand on the familiar ground, a realization dawns that this place holds a unique significance in your unfolding adventure.
The questions about your origin and purpose persist, but for now, a serene acceptance settles within you, encouraging you to continue your exploration with a newfound courage.
North or south or west, rocky platitudes stretch wide, while your eastern path transforms into a lakeshore of serenity.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3",
    },
    "b3": {
        ZONE_NAME: "sandy coast",
        DESCRIPTION: """The sandy coast beneath your feet feels warm as you stand there, embraced by a cool and refreshing breeze that gently caresses your face.
The air carries a hint of salt from the nearby lake. To the east, the glistening waters of the lake extend an inviting allure, reflecting the sunlight in a captivating dance.

South, a small, glimmering pond catches your eyes in the distance, among the spreading marshland.

In both other directions, a carpet of soft green growth unfolds, creating a lush and vibrant landscape.
The gentle rustle of leaves accompanies the breeze, adding a soothing soundtrack to the natural beauty that surrounds you.

Now, you have the choice to explore the inviting lake to the east or venture into the lush greenery in other directions. What will you decide?.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4",
    },
    "b4": {
        ZONE_NAME: "lake's edge",
        DESCRIPTION: """At the lake's edge, the water sparkles and gleams under the sunlight. A gentle hum of the wind envelops the air, bringing a sense of warmth.
Intrigued, your gaze is drawn to something within the water, captivating you as you approach, feeling no sense of threat.

The eastern edge of the lake presents an impassable barrier, veiled by an impenetrable thicket of thick reeds.""",
        EXAMINATION: """Entering the soft waters, they embrace your ankles and rise gently to your hips, providing a cooling and refreshing sensation.
Wading deeper, your attention is drawn to something nestled in the sand at the lake's floor, glistening mysteriously.

Your hand brushes aside the sand, unveiling a small, silver lamp, its surface gleaming in the soft light.""",
        SOLVED: False,
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: "",
    },
    "c1": {
        ZONE_NAME: "smoldering, grassy plain...",
        DESCRIPTION: """A sense of dread fills your heart. The grass here seems scorched, burned in places. You feel a deep sense of unease.

To the north and east, the rocky plains unfold, offering a somehow more inviting terrain.
Westward, the looming mountains appear nearly impassable.

As you consider the south, it appears passable, but a subtle unease tugs at your instincts, urging caution.
It would be wise to explore all other areas and address any lingering uncertainties before venturing into this region.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "b1",
        DOWN: "d1",
        LEFT: "",
        RIGHT: "c2",
    },
    "c2": {
        ZONE_NAME: "rocky wasteland",
        DESCRIPTION: """A rocky wasteland stretches as far as the eye can see, marred by the remnants of a lost village.
The air is heavy with the scent of ash, and the ground beneath your feet is uneven and harsh. Jagged rocks and rubble are scattered across the desolate landscape.
Venturing south and west, the terrain becomes increasingly rugged.
Large boulders and sharp rocks impede progress, and the ruins of ancient structures stand as silent witnesses to a once-thriving community now reduced to decay.

The northern and eastern areas seamlessly transition into vast, grassy fields, marking a stark contrast to the rocky wasteland.
This shift from desolation to greenery suggests a renewal and a flourishing of nature in these regions, and fills your heart with hope.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3",
    },
    "c3": {
        ZONE_NAME: "grassy plain",
        DESCRIPTION: """Before you, a tranquil scene unfolds as a grassy expanse stretches as far as the eye can see.
The blades of grass sway gently in the wind, creating a rhythmic dance that brings a sense of calmness to the surroundings.

To the east and north, your gaze meets a sandy coast, where the grassy terrain meets the shoreline.

Venturing southward, the grassy landscape transforms into a moist environment, giving way to a sprawling swamp.
The air becomes denser, and the ground softens underfoot as you navigate this wetland.

To the west, the serene grassy expanse abruptly transitions into a rugged and rocky terrain.
The jagged rocks and uneven ground form a stark contrast to the peacefulness of the grassy fields, adding an element of challenge and exploration to the landscape.

Each direction beckons with its own unique character, offering a diverse range of environments to explore.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4",
    },
    "c4": {
        ZONE_NAME: "sandy coast",
        DESCRIPTION: """The sun beats down on the sandy coast as you stand at the water's edge, gazing at the glimmering lake to the north.
The midday sun's reflection dances on the water's surface, momentarily blinding you.

To your east, the lake seems to deepen, and the terrain becomes impassable. The waters stretch out into the distance.

Turning your attention southward, you notice a marshy swamp extending before you. The ground becomes soggy, and the air carries a distinct earthy scent.
In the distance, you spot a small hut nestled among the vegetation, surrounded by the murky waters of the swamp.

Looking west, a vast grassy plain unfolds. The landscape is dotted with occasional wildflowers, and the plain extends as far as the eye can see.
It seems like a serene and open expanse.

Now, it's up to you to decide where your adventure takes you. What direction will you explore: north towards the glimmering lake,
south into the marshy swamp with the distant hut, or west across the expansive grassy plain?""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: "",
    },
    "d1": {
        ZONE_NAME: "burned, harrowing wasteland",
        DESCRIPTION: """Before you stands a harrowing scene of destruction. To the south and west, imposing mountains serve as impassable barriers.
The ruins of a once-thriving temple lie in disarray, a testament to a chaotic past.
In front of the desolation, a colossal red dragon, as tall as the temple spire, rests peacefully, seemingly basking in its own creation.
The rhythmic breath of the dragon sends shudders through your heart.

A voice within warns of the danger ahead, urging you to turn back unless your heart and soul are steeled for the challenge.
What will you decide? Will you face the slumbering dragon, or heed the warning and retreat from this ominous sight?""",
        EXAMINATION: """As you take a cautious step forward, the colossal red dragon stirs.
With a slow and deliberate motion, it opens one eye, fixing its gaze upon you.
The very ground beneath you trembles with each step of the massive creature.
A deafening roar reverberates through the air, shaking your surroundings. The dragon's heavy breathing seems to vibrate your very soul.""",
        SOLVED: False,
        UP: "c1",
        DOWN: "",
        LEFT: "",
        RIGHT: "d2",
    },
    "d2": {
        ZONE_NAME: "smoldered, grassy plain",
        DESCRIPTION: """The burned and smoldered grass underfoot adds a somber note to the atmosphere, instilling a sense of unease and dread.
It feels as though something destructive has passed through this area recently.
The west, where the scorched land lies, seems to hold an ominous energy, and an instinct tells you to proceed with caution.

Turning your attention to the north, the grass softens beneath your steps, transitioning into a healthier green hue.
A peaceful plain stretches out before you, inviting you with a sense of tranquility. The contrast between the charred west and the serene north is stark.

In the east, you find a small pond filled with strangely glowing fish. The ethereal glow adds a magical touch to its surroundings.

South, a harsh mountain range forbids your venture. You choose not to go there.

Considering the foreboding feeling from the west, you might decide to explore other directions.""",
        EXAMINATION: "examine",
        SOLVED: True,
        UP: "c2",
        DOWN: "",
        LEFT: "d1",
        RIGHT: "d3",
    },
    "d3": {
        ZONE_NAME: "marshy area with a swamp",
        DESCRIPTION: """You find yourself in front of a small pond, its deep waters illuminated by the gentle glow of a few fish.
The aquatic creatures swim in intriguing circling patterns, their bioluminescence cutting through the darkness.
Their odd behavior sparks your curiosity, inviting you to delve deeper into the mystery of this enchanting pond.

Facing north, you observe a sandy coast hugging the lake's edge. To the west, the smoldered plain extends, bearing the scars of a recent blaze.
The south path is blocked by imposing mountains, their harsh peaks dissuading easy passage.
In the east, the marsh gradually transforms into a swamp. Amidst the intrigue, a mysterious small hut stands alone.
The choices lie before you—where will your journey take you?""",
        EXAMINATION: """You approach the pond closer. Observing it further, you see them circling, but exchanging their positions in intricate patterns
Somehow, they always group into pools of three. Three...""",
        SOLVED: False,
        UP: "c3",
        DOWN: "",
        LEFT: "d2",
        RIGHT: "d4",
    },
    "d4": {
        ZONE_NAME: "swamp with a hut",
        DESCRIPTION: """Before you stands a small hut, its foundations sinking into the swamp.
The boards show signs of decay, weathered by the persistent moisture in the air. The door hangs loose, leaving a small crack inviting you to peer inside.

Facing the small hut, you observe the surroundings: to the north, the swamp gradually transitions into the sandy shores of a lake; eastward, the swamp eases into a marshy terrain.
However, both the south and west directions are impassable, blocked by imposing mountains. The choice is yours—will you venture north toward the lake or east into the marsh?""",
        EXAMINATION: """You decide to peer through the crack, however it's too dark to see exactly. You notice some sort of case standing on the table.
Trying to pry it open, you find yourself blocked by a metal chain, held together with a combination lock.""",
        SOLVED: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: "",
    },
}


# Game interaction
def show_location():
    print("\n" + ("#" * (4 + len(Player.location))))
    print("# " + Player.location.upper() + " #")
    print("#" * (4 + len(Player.location)))
    print("\n")
    print(zones[Player.location][DESCRIPTION])


def prompt():
    print("\n" + "======================")
    writer("What action shall you partake?\n\n")
    action = input("> ")
    actions = ["move", "quit", "examine", "help", "lamp"]
    while action.lower() not in actions:
        writer("\nYou stumble in confusion... Partake in an appropriate action.\n\n")
        action = input("> ")
    if action.lower() == "move":
        player_move(action.lower())
    elif action.lower() == "quit":
        sys.exit()
    elif action.lower() == "examine":
        examine(action.lower())
    elif action.lower() == "help":
        help_menu()
    elif action.lower() == "lamp" and "genie's lamp" in Player.status_effects:
        lamp_action()


def player_move(action):
    while True:
        writer("\nWhich direction calls you?\n\n")
        direction = input("> ")

        directions = {
            "up": UP,
            "down": DOWN,
            "left": LEFT,
            "right": RIGHT,
            "north": UP,
            "south": DOWN,
            "west": LEFT,
            "east": RIGHT,
        }

        if direction in directions:
            destination = zones[Player.location][directions[direction]]
            if destination:
                movement(destination)
                break
            else:
                writer("\nThis doesn't seem quite possible...\n")
        else:
            writer("\nWhich direction calls you?\n\n")


def movement(destination):
    os.system("clear")
    writer("\nYou move to a " + zones[destination][ZONE_NAME] + ".\n\n")
    Player.location = destination
    time.sleep(0.5)
    show_location()


def examine(action):
    if zones[Player.location][SOLVED]:
        writer("\nThere is nothing to do here...\n\n")
    else:
        writer("\n# " + zones[Player.location][EXAMINATION] + " #\n\n")
        if Player.location == "b4":
            lamp_accquire()
            zones[Player.location][SOLVED] = True
        elif Player.location == "d4":
            hut_lock()
        elif Player.location == "d1":
            dragon_fight()


# Progression functions
def lamp_accquire():
    writer("\nACCQUIRED A GENIE'S LAMP\n\n")
    writer("\nUse the action - lamp - to prompt its action\n\n")
    Player.status_effects.append("genie's lamp")


def lamp_action():
    if "lamp_guess_failed" not in Player.status_effects:
        writer(
            """
As you rub the silver lamp, a cloud of smoke billows forth, and with a resounding mystical echo, a faint genie... or so you expected...
A semi-translucent man in a black, vertically striped suit with white lines, square glasses and sharp eyes with pale red irises and pure white hair,
falling down to his brows appears in front of you.

He grunts and looks at you, with an interested look.

'You have freed me...
that is what you'd like to hear, isn't it.
But what if I did not want to be freed?
Hm.
Never mind.
Riddle me this.
Up north east, the stones shimmer...
what is their answer?'\n\n"""
        )

    else:
        writer("\n'So... got a different answer? The stones still shimmer...'\n\n")

    if input("> ").lower() == "echo":
        writer(
            """\n'Yess... You guessed it. Congratulations""")
        time.sleep(0.5)
        writer("\nNow...'")
        time.sleep(1)
        writer("\nHe claps his hands")

        writer("\n'The stones should stop shimmering, and...")
        time.sleep(1)
        writer("\n- Z -... let me tell you that... - Z -...'")
        time.sleep(0.5)
        writer("""\nWith a mysterious smile, he turns away from you and... fades away
The lamp cracks, and shatters into a thousand pieces... you are left thinking about this mysterious encounter...\n"""
            )
        zones["a1"][SOLVED] = True
        Player.status_effects.remove("genie's lamp")
    else:
        writer("\n'Not quite... Try again another time'\n\n")
        Player.status_effects.append("lamp_guess_failed")


def hut_lock():
    if "lock_failed" not in Player.status_effects:
        writer(
            """\nThe lock on the chain barring your entry has two rotating elements, marked with a series of letters and numbers.
You decide that you ought to input a combination of them, and see if the lock pries open.
What combination will you try?\n\n"""
        )
        answer = input("> ")
        if lock_mechanism(answer) == True:
            hut_enter()
    else:
        writer(
            """You choose to retry the lock...
What combination will you try?\n\n"""
        )
        answer = input("> ")
        if lock_mechanism(answer) == True:
            hut_enter()


def lock_mechanism(answer):
    if answer == "Z3":
        writer("\nThe lock clicks open, freeing the chain and dropping to the floor.")
        return True
    else:
        writer(
            "\nYou tug on the lock, but nothing hapens. You decide to try another combination or explore more and ponder this puzzle.\n\n"
        )
        Player.status_effects.append("lock_failed")
        return False


def hut_enter():
    if Player.archetype == "rogue":
        Player.weapon = "dagger"
    elif Player.archetype == "mage":
        Player.weapon = "grimoire"
    else:
        Player.weapon = "sword"

    if Player.weapon == "dagger":
        description = """\nThe curved blade glistens at you with a razor sharp edge. The hilt adorned with a black, leather-wrapped handle.
The dagger feels cold to the touch, and its weight is balanced to perfection, suggesting a level of craftsmanship that goes beyond mere functionality.
As you examine it, the room seems to take on a different atmosphere. The once shabby hut seems not so much desolate, nor weak, but akin a home.
Perhaps, you feel the memories of its prior owner, merging with yours.
As if his dark cloak had been pulled over your shoulders, you take your next strides with a newfound fire filling your heart."""
    elif Player.weapon == "grimoire":
        description = """\nThe leather-bound book lays upon the velvet, its cover marked with mysterious writings in a language you cannot understand.
As you run your fingers over the textured surface, a faint energy pulses from the pages, illuminating the room.
A sense of wonder and purpose fills the room. You get a feeling, akin to a curiosity of a child you once felt.
Everything seems interesting, fresh, new... filled with purpose.

The book appears ancient, and its pages feel delicate beneath touch, yet you're not afraid that it will crumble.
Perhaps, it's guided many in the past. Perhaps, it will too guide you..."""
    else:
        description = """\nThe cool, metal blade lays on the velvet, its polished surface reflecting your own image back at you.
The gleaming alloy, akin to that of steel, straight along its length seems to hold an immeasurable strength.
The hilt is simple, wrapped in a soft black leather, for added comfort.
Your eyes trace down. At the base of the sword lies a green zircon, embedded into the pommel.
The gemstone radiates a deep green, fiery hue, contrasting sharply with the cold, metallic sheen of the sword.

As you hold the sword, a sense of reassurance and tranquility washes over you.
The before bleak room seems to bask in the gentle glow of the gemstone, and a feeling akin to that of destiny, or preordained purpose fills the air.
It's as if the sword, with its radiant zircon, carries a subtle promise that everything is as it should be
and that any, and all challenges can be faced with full-set confidence, and without the slightest of fear."""

    writer(
        f"""\n\nYou enter the hut and look around. In the dimly lit room, the case you noticed prior catches your attention.
You approach it.
Opening it, you see a {Player.weapon}, rested upon a red, velvety cushion.
{description}\n"""
    )


def dragon_fight():
    if Player.weapon == "":
        writer("""You feel yourself tremble, your knees giving way. You try to run, but your legs are frozen in place.
You try to scream, but not a sound comes out. The dragon takes one step towards you, and the ground trembles, sending you to your knees.
Tears fill up your eyes involuntarily. The dragon opens its mouth, and a ball of fire so bright, the surrounding daytime slowly turns into night, steadily forms.

You feel a gut-wrenching impact to your abdomen, as the red-haired woman's shoulder slams into your belly, sending you forwards to the ground with her.
Right in time too, as the harrowing flame soars overhead, scorching your face with the surrounding heat.
A sad look in her eyes meets yours. Your nose is hit by the smell of scorched fabric.
'Run...', she whispers.
Her hand touches your shoulder, as you feel your body being cramped into a space, seemingly a fraction of its actual size.
You feel queasy, sick, nauseous. Your head feels like it's going to rip apart.
In the next moment, you find yourself on a small hill, overlooking the scene. Your heart tells you to return, to help, but your head is filled with her words.
You cannot look. The dragon steps closer.
"Run..."
Her words echo in your mind, as if implanted into your very subconscious.
You turn around. Perhaps you should have heeded her words and your instincts. Perhaps there was more to see. More to discover.
Now all you can do is run.
You find yourself at stone doors, akin to those you once entered this world through. Your hand touches them, and they glow up in blue.
You know what you ought to do. You know there's no turning back. Perhaps time will give you another chance to set things right again.
Perhaps, it is cruel, and there's no take-backs. You do not know. As tears roll down your face, you push through the doors, hoping for a better future. A brighter tomorrow.""")
        time.sleep(0.5)
        writer("""


               -= GAME OVER =-\n\n""")
        Player.game_finished = True

    else:
        writer(f"""You grip your {Player.weapon} with determination. You feel yourself start to tremble, your knees giving way, but the weapon you hold
fills you with a warm, steadfast glow.\n""")
        dragon_battle()
        writer(f"""\nYou find yourself worn down by the battle. Were it not for the artefact you found along the way, things would have been much different.
The beast looms overhead, about to strike. Yet you cannot back down. Not in this moment.
Too much is at stake here.
With your remaining stamina, you focus all your remaining power, and lift up your {Player.weapon}. At least one last attack, before he comes crashing down...
You can spare that much, can't you?

You focus all your vital energy into this one, last strike. Your very bones screaming in pain. You close your eyes, and unleash one final blow...

A cleaving sound rips through the air. You open your eyes and see a tall man with short brown hair, a battleaxe larger than him held in both hands.
The dragon's head, bloody and lifeless lays at his feet, as the gushing blood from its neck carpets the rocky wasteland.
Suddenly, as if sprung back into life by this deed, the whole expanse flowers in white, red and green.

As you stand upon this flowery field, and regain your footing, the man extends his hand to you with a firm, and soft smile.
You somehow feel, that things are going to get a lot more interesting, and exciting from here...



                -= GAME OVER FOR NOW =-
                THANK YOU FOR PLAYING!\n\n""")
        Player.game_finished = True

def dragon_battle():
    print("\n" + "======================")
    writer("The battle begins")
    time.sleep(0.5)
    print_stats()
    time.sleep(0.3)
    writer("\nWhat shall you do?\n")
    time.sleep(0.5)

    counter = 0
    Ev_counter = 0

    while counter < 3:
        print("\nOptions:")
        print("\n - Attack -      - Guard -       - Assistance -\n")
        combat = input("> ").lower()

        if combat == "attack":
            writer(f"\nYou raise your {Player.weapon}\n")
            writer("The dragon is struck with a mighty blow\n")
            Dragon.hp = Dragon.hp - 500
            if Player.archetype == "mage":
                Player.mana = Player.mana - 20
            else:
                Player.stamina = Player.stamina - 20
            dragon_move(counter)
            counter += 1
            print_stats()
        elif combat == "guard":
            writer(f"\nYou raise your {Player.weapon} up to your chest, taking on a defensive stance\n")
            if Player.archetype == "mage":
                Player.mana = Player.mana - 60
            else:
                Player.stamina = Player.stamina - 60
            Player.status_effects.append("guarded")
            dragon_move(counter)
            Player.status_effects.remove("guarded")
            writer("Your shield wears off...")
            counter += 1
            print_stats()
        elif combat == "assistance":
            writer(f"\nYou ask the red haired woman for help\n")
            if Ev_counter == 0:
                writer("She draws her sword, and charges in, dodging the beast's claw strike and countering with a riposte.\n")
                Dragon.hp = Dragon.hp - 5000
                dragon_move(counter)
                counter += 1
                Ev_counter += 1
                print_stats()
            else:
                writer("You notice her stamina is completely drained and decide to take matters into your own hands.\n")
        else:
            writer("\nInvalid option\n")
            time.sleep(0.3)
            continue
        if counter == 4:
            combat = input("> ").lower()

def dragon_move(counter):
    if counter == 0:
        writer(f"{Dragon.name} charges their attack, a giant ball of flame gathering in its open mouth\n\n")
    elif counter == 1:
        if "guarded" not in Player.status_effects:
            writer(f"{Dragon.name} unleashes a mighty blast of fire in your location. It barely misses, but you are caught in the explosion.\n\n")
            Player.hp - 89
        else:
            writer(f"""A golden glow emanating from your weapon envelops you.
{Dragon.name} unleashes a mighty blast of fire in your location, however the fire envelops you, doing no harm.
The beast's eyes shine in rage. You know he's furious, and not going to let you off after this one...\n\n""")
    else:
        writer(f"{Dragon.name} jumps up ferociously, preparing to unleash their final, finishing blow\n\n")

def print_stats():
    width = 50
    stat_placeholder = " XX"

    print("\n" + "======================")
    print(f"{Dragon.name}{'':{width+len(stat_placeholder)-len(str(Dragon.name))}}{Player.name}")
    print(f"{Dragon.hp} HP{'':{width-len(str(Dragon.hp))}}{Player.hp} HP")
    print(f"{Dragon.stamina} SP{'':{width-len(str(Dragon.stamina))}}{Player.stamina} SP")
    print(f"{Dragon.mana} MP{'':{width-len(str(Dragon.mana))}}{Player.mana} MP")

# Main game functionality
def game_loop():
    while Player.game_finished == False:
        prompt()


def char_create():
    # INTRO
    os.system("clear")
    writer(
        "You feel your body jerk forward, as the same blue light from before fills and envelops all your senses. Then, everything grows dark...\n"
    )
    time.sleep(2)
    writer(
        "A deep voice echos around you... or perhaps... perhaps this is all happening in your head..."
    )
    time.sleep(2)

    # NAME
    os.system("clear")
    nameq = "'What is your name, traveler?'\n\n"
    writer(nameq)
    Player.name = input("> ").capitalize()
    writer("\nHello, " + Player.name + ".")
    time.sleep(1.5)

    # Gender
    """
    os.system("clear")
    genderq = "'And what pronouns do you use?'\n\n"
    writer(genderq)
    Player.gender = input("> ").lower()
    writer("\nI see... '" + Player.gender + "', is that right?\n\n")
    if input("> ").strip().lower() not in ["yes", "y", "yep", "yes!", "yep!"]:
        genderq = "'Hmm... I'm not quite sure I understood... What pronouns do you use?'\n\n"
        writer(genderq)
        Player.gender = input("> ")
    time.sleep(1.5)
    """

    # ARCHETYPE
    os.system("clear")
    writer("'What is your archetype?\n\n")

    writer(
        "Are you a masterful trickster of shadows and deceit, skilled in the art of subterfuge? - Rogue -\n\n"
    )
    time.sleep(0.5)
    writer(
        "Or perhaps, do you embody the wisdom of arcane arts, being a scholar versed in the mysterious forces that weave through reality? - Mage -\n\n"
    )
    time.sleep(0.5)
    writer(
        "Then again, might you be a stalwart figure, toughened by the embrace of steel and iron, a true embodiment of resilience and martial prowess? - Warrior -'\n\n"
    )
    time.sleep(0.5)
    archetypes = ["rogue", "mage", "warrior"]
    chosen_archetype = input("> ").lower()
    while chosen_archetype not in archetypes:
        chosen_archetype = input("> ").lower()
    if chosen_archetype in archetypes:
        Player.archetype = chosen_archetype.lower()
        if Player.archetype == "rogue":
            writer(
                "\nTrue... and quite a " + chosen_archetype + " you will become...\n"
            )
            time.sleep(0.5)
            writer(
                "May your every step be unseen, and your every strike find its mark in the dance of shadows. Walk the unseen path, "
                + Player.name
                + "...\n"
            )
            time.sleep(2)
        elif Player.archetype == "mage":
            writer(
                "\nTrue... and quite a " + chosen_archetype + " you will become...\n"
            )
            time.sleep(0.5)
            writer(
                "May your intellect shine as brightly as the magical forces you command, and may the mysteries of the cosmos unveil their secrets before you, "
                + Player.name
                + "...\n"
            )
            time.sleep(2)
        elif Player.archetype == "warrior":
            writer(
                "\nTrue... and quite a " + chosen_archetype + " you will become...\n"
            )
            time.sleep(0.5)
            writer(
                "May the echoes of triumph resound in every step you take. May your blade be true, and your courage unmatched, as you stride fearlessly into the fray, "
                + Player.name
                + "...\n"
            )
            time.sleep(2)

    # Stats
    if Player.archetype == "rogue":
        Player.hp = 100
        Player.mana = 50
        Player.stamina = 100
    elif Player.archetype == "mage":
        Player.hp = 100
        Player.mana = 100
        Player.stamina = 50
    elif Player.archetype == "warrior":
        Player.hp = 100
        Player.mana = 50
        Player.stamina = 100

    Player.status_effects = []

    os.system("clear")
    game_world_intro()


def game_world_intro():
    writer(
        f"""Your vision goes black again\n
After some time... you awake
Your vision is blurry, you can barely see anything
A head of scarlet red hair disturbs your slumber.
You blink... and your eyes clear. You feel a comforting presence, as if a shroud of darkness, warmly enveloped you.
'{Player.name}... are you ok?'\n\n""")
    time.sleep(0.5)

    writer("""You instinctively put a hand to your forehead... it hurts, you're a bit dazed, but her presence reassures you.
She holds out her hand with a soft smile.\n\n""")
    time.sleep(0.5)

    writer("""
'Come on'
'You must not remember anything, judging by the look on your face, but we've got quite a job ahead of us!'
'But first, get your feet moving and let's look around!'
"""
    )

    time.sleep(2)
    help_menu()
    time.sleep(4)
    os.system("clear")

    game_loop()


def writer(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        global debug
        if debug:
            time.sleep(0.00)
        else:
            time.sleep(0.03)


if __name__ == "__main__":
    main()
