# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line



# Part 1: Greet Template

from unicodedata import name


def greet(name, template=f"Hello, <name>!"):
    if template == f"Hello, <name>!":
        return f"Hello, {name}!"
    else:
        result = template.replace("<name>", f"{name}")
        return result


print(greet("jon"))                             # hello, jon!
print(greet("jon", "hello dude"))               # hello dude
print(greet("Bob", "What's up, <name>!"))       # What's up, Bob!



# Part 2: Force

def force(mass, body='earth'):
    body_dictionary = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    Isfloat = isinstance(mass, float)
    if not Isfloat:
        return f"The mass should be provided as a float"
    elif body not in body_dictionary:
        return f"The gravity of {body} is not in our dictionary. The name of the body should be provided with correct spelling and without any capitals"
    else:
        return round(mass * body_dictionary[body], 2)

print(force(0.1))                   # 0.98
print(force(1, "earth"))            # The mass should be provided as a float
print(force(0.1, "Earth"))          # The gravity of {body} is not in our dictionary. The name of the body should be provided with correct spelling and without any capitals
print(force(0.1, "earth"))          # 0.98
print(force(37.6, "neptune"))       # 421.12
print(force(3846.6, "mercury"))     # 14232.42



# Part 3: Gravity

def pull(m1:float, m2:float, d:float) -> float:
    Isfloat_m1 = isinstance(m1, float)
    Isfloat_m2 = isinstance(m2, float)
    Isfloat_d = isinstance(d, float)
    if not Isfloat_m1:
        return f"The first object mass in kg should be provided as a float"
    elif not Isfloat_m2:
        return f"The second object mass in kg should be provided as a float"
    elif not Isfloat_d:
        return f"The distance in meters between the objects should be provided as a float"

    d2 = d * d
    g = 6674 * (10**-11)
    res = m1 * m2
    res1 = res / d2
    res2 = g * res1
    return round(res2, 10)


print(pull(6, 22.4, 6.9))                                           # The first object mass should be provided as a float
print(pull(6.1, 22, 6.9))                                           # The second object should be provided as a float
print(pull(6.1, 22.4, 7))                                           # The distance in meters should be provided as a float
print(pull(800.0, 1500.0, 3.0))                                     # 0.0088986667
print(pull(0.1, 5972000000000000000000000000.0, 6371000000.0))      # 0.9819532033
