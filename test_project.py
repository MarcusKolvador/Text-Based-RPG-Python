import pytest
from project import lock_mechanism, zones, dragon_move, Dragon, writer, movement

def test_lock_mechanism_correct():
    assert lock_mechanism("Z3") == True

def test_lock_mechanism_incorrect():
    assert lock_mechanism("z3") == False

def test_dragon_move():
    assert dragon_move("0") == writer(f"{Dragon.name} charges their attack, a giant ball of flame gathering in its open mouth\n\n")

def test_dragon_move2():
    assert dragon_move("2") == writer(f"{Dragon.name} unleashes a mighty blast of fire in your location. It barely misses, but you are caught in the explosion.\n\n")

def test_movement():
    assert movement("a1") == writer("\nYou move to a stalagmite formation.\n\n")
