from time import sleep
count = 10
for x in range(10):
    for y in range(2):
        print(str(count) + " green bottles, hanging on the wall")
        
    print("And if 1 green bottle should acidentally fall,")
    print("They'll be " + str(count-1) + " green bottles hanging on the wall.\n")
    sleep(1)
    count -= 1
