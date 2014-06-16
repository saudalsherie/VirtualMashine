from crop import *
class Wheat(Crop):
    """A Wheat crop"""
    def __init__(self):
        super().__init__(2,4,6)  #Polymorphism
        slef._type = 'Wheat'    #overriding

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == 'Seeding' and water > self._water_need:
                self._growth += self._growth_rate *1.5
            elif self._status == 'Young' and water > self._water_need:
                self._growth += self._growth_rate *1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def main():
    wheat_crop = potato()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    
if __name__ == "__main":
    main()
