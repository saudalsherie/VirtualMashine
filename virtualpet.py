class VirtualPet:
    """ A represantation of a pet """
    def __init__(self,name):
        self.name = name
        self.hunger = 3
        self.energy = 3
        self.boredom = 1
        print('I have been born- my name is {0}'.format(self.name))
    def talk(self):
        print('Hi, I am your virtual pet')
    def rest(self):
        resting = input('I feel tired can I sleep? (y-n): ')
        resting = resting[0].lower()
        if resting == 'y':
            print('Thanks Zzz ...')
            self.hunger = self.hunger -1
            self.energy = self.energy +1
        elif resting == 'n':
            print('Ohh')
            self.hunger = self.hunger +1
            self.energy = self.energy -1
            self.boredom = self.boredom +2
        else:
            print('Too late I am dead')
    def feed(self, food):
        self.hunger = self.hunger -1
        self.energy = self.energy +1
    def mood(self):
        unhappiness = self.hunger + self.boredom + self.boredom 
        if unhappiness < 5:
            PetMood = "Happy"
        elif 5 <= unhappiness <= 10:
            PetMood = "Okay"
        elif 11 <= unhappiness <= 15:
            PetMood = "Frustrated"
        else:
            PetMood = "Mad"
        print('I am feeling {0}'.format(PetMood))
 
def main():
    name = input('Please enter a name for your pet: ')
    pet_one = VirtualPet(name)
    pet_one.talk()
    pet_one.feed('Cake')
    print('My energy at the moment is {0}'.format(pet_one.energy))
    print('My hunger at the moment is {0}'.format(pet_one.hunger))
    pet_one.mood()
    pet_one.rest()
    print('My energy at the moment is {0}'.format(pet_one.energy))
    print('My hunger at the moment is {0}'.format(pet_one.hunger))
    pet_one.mood()

if __name__ == '__main__':
    main()
