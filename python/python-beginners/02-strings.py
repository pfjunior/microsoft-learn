# .title(): Return the string in initial caps
# .split(): Split a string
# in: Search a word, character or a group of character in a string
# .count(): Return the total number of occurrences of a certain word in a string
# .lower(): Convert a string to lowecase letter
# .upper(): Convert a string to upercase letter
# .join(): Put together characters


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

setences = text.split(". ")
# print(setences)

# for sentence in setences:
    # if "temperature" in sentence:
        # print(sentence)

name = "Ganymede"
planet = "Mars"
gravity = "1.43"

template = """Gravity Facts about {name}
--------------------------
Planet Name: {planet}
Gravity on {name}: m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))