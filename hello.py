import sys

def main(animal):
    if animal == "cat":
        print("Meow!")
    else:
        print("What does the " + animal + " say?")

if __name__ == "__main__":
    main(sys.argv[1])
