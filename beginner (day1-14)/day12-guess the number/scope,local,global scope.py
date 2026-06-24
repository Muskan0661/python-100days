# Global variable
enemies = 1
player_health = 10

print(f"Initial enemies: {enemies}")
print(f"Player health: {player_health}\n")


# Local Scope Example
def local_scope_demo():
    potion_strength = 2  # Local variable
    print("LOCAL SCOPE")
    print(f"Potion strength: {potion_strength}")

local_scope_demo()

# Uncommenting the next line would cause a NameError
# print(potion_strength)

print()


# Global Scope Example
def global_scope_demo():
    print("GLOBAL SCOPE")
    print(f"Player health inside function: {player_health}")

global_scope_demo()

print()


# Modifying a Global Variable
def increase_enemies():
    global enemies
    enemies += 1
    print("MODIFYING GLOBAL VARIABLE")
    print(f"Enemies inside function: {enemies}")

increase_enemies()

print()
print(f"Enemies outside function: {enemies}")