#what is prompt?: An instruction given to the AI


#f-strings
name = "himani"
city = "raigad"

message = f"Hello, my name is {name} and i live in {city}"
print(message)

#the f before the opening quotes tells python to replace the curly braces with values

topic = input("Enter a topic: ")
level = input("Enter a level: ")

sentence = f"Explain {topic} to a {level} student"
print(sentence)
