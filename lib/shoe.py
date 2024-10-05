#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand  # This will call the setter for brand
        self.size = size    # This will call the setter for size
        self._condition = "Used"  # Initial condition set to "Used"
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and 1 <= len(brand) <= 50:  # Validate brand length
            self._brand = brand
        else:
            print("brand must be a string")
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    @property
    def condition(self):
        return self._condition
    
    def cobble(self):  # Changed this to a method instead of a setter
        self._condition = "New"  # Update condition to "New"
        print("Your shoe is as good as new!")  # Print message for cobbling

# Example usage
shoes = Shoe("Puma", 10)
print(shoes.brand)      # Outputs: Puma
print(shoes.size)       # Outputs: 10
shoes.cobble()          # Outputs: Your shoe is as good as new!
print(shoes.condition)   # Outputs: New
