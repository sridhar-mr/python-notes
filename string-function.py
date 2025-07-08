user_name = "srIdhar"
user_mobile = "7358286168"
masked = user_mobile[:2] + "XXXXXX" + user_mobile[-2:] # we can use that start and end
print(masked)
#[] --> get the value by letter by letter

print(user_name.lower())
print(user_name.upper())
print(user_name.capitalize())

song = "shape OF you"
artist = " SRIDHAR mr"

fromatted = f"{song.title()} - {artist.title()}"
print(fromatted)
#tittle() --> means make that all captilize u give in the string

location = "guduvancherry"
fixed_location = location.replace("guduvancherry", "kayerambedu")
print(fixed_location)
#replace --> means repace the value you given with the 2 arrgivement


message = "Your Uber id is : UB23423. please keep it safe"
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)
#split --> means sperate the value use given inside the string delimied means sperating the word and special charater
#strip --> means  it will delete the blank space


promo_msg = "Use Zomoto100 to get 100 off  on your first order"

if "Zomoto100" in promo_msg:
    print("You applied Zomoto100")
#we can handel the string using if else using "in" membership operator


feedback = "the driver was polite and ride was smooth "

print(feedback.find("polite"))

#find() --> to find the position of the particular word




name = "sridhar murugan"
initial = "".join([word[0].upper() for word in name.split()])
print(initial)


word1 = "the trip was super and the car was clean"
word_count = len(word1.split())
print(word_count)



























