# Sample list of words
words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
    "ant", "bee", "cat", "dog", "elephant", "frog", "giraffe", "horse", "iguana", "jaguar",
    "kangaroo", "lion", "monkey", "newt", "octopus", "parrot", "quail", "rat", "snake", "turtle",
    "umbrella", "vulture", "whale", "xenops", "yak", "zebra", "airplane", "boat", "car", "drone",
    "elevator", "ferry", "gondola", "helicopter", "iceberg", "jet", "kayak", "limo", "motorbike",
    "nurse", "ocean", "plane", "quicksand", "robot", "submarine", "train", "u-boat", "van",
    "wagon", "x-ray", "yacht", "zodiac", "art", "book", "cathedral", "drama", "exhibit",
    "film", "gallery", "history", "installation", "jazz", "kaleidoscope", "literature", "music",
    "novel", "opera", "poetry", "quilt", "rug", "sculpture", "theater", "ukulele", "vase",
    "watercolor", "xylophone", "yarn", "zine", "action", "beauty", "culture", "dare",
    "evolve", "flourish", "grow", "heal", "ignite", "journey", "kindle", "learn", "mature",
    "nurture", "overcome", "play", "question", "reflect", "succeed", "thrive", "understand",
    "value", "wonder", "explore", "create", "discover", "engage", "connect", "inspire",
    "imagine", "invent", "motivate", "transform", "unite", "achieve", "believe", "contribute",
    "dream", "embrace", "focus", "join", "listen", "mentor", "navigate", "optimize",
    "pursue", "quantify", "revive", "share", "challenge", "enjoy", "grow", "lead", "manifest",
    "narrate", "organize", "propose", "question", "research", "simplify", "transmit",
    "validate", "wonder", "amaze", "bloom", "cherish", "delight", "excel", "foster",
    "galvanize", "harness", "invest", "jubilate", "kickstart", "luminate", "mobilize",
    "nurture", "optimize", "proliferate", "quench", "radiate", "spark", "train", "uplift",
    "vitalize", "weave", "xpress", "yearn", "zeal"]



print(words[-1])

#list slizing

list = [3, 22, 5, 8, 54, 9]

print(list[:])

print(list[1:4])


#Update a list
science = ["art", "chemistry", "math"]

science[0] = "Biology"

(science)

science[2] = "geology"

print(science)

integers = [2, 5, 9, 20, 27]

integers[-1] = 30.5

print(integers)

integers.remove(5)

print(integers)

integers.pop(0)

print(integers)

list_fruits = ["lemon", "Orange", "melon"]

#pop, remove, del

del list_fruits[0]

print(list_fruits)

#name_apemd

list_names = ["Juan", "pepe", "Felix"]

list_names.append("el donovan se la come")

print(list_names)

list_of_squares = []
for int in range(1,10):
    square = int **2
    list_of_squares.append(square)
   
print(list_of_squares)

#expression for item in list if condition

square2=[item**2 for item in range(1,10)]

print(square2)


numbers=[1,2,3,4,5,6,7,8,9]

cubics = [number**3 for number in numbers]
print(cubics)

list_of_number = [1,2,3,4,5,6,7,8,9]
double = [item*2 for item in list_of_number if item%2 == 0]
print(double)



