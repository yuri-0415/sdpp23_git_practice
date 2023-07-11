import sys

def main(animal):
    aminal = "aminal"
    if aminal == "cat":
        print("Meow!")
    else:
        print("What does the " + aminal + " say?")

if __name__ == "__main__":
    main(sys.argv[1])
