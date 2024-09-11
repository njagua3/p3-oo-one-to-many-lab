class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Check if pet_type is valid
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = pet_type

        # Check if owner is of type Owner or None
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        
        # Add pet to owner if an owner is provided
        self.owner = owner
        if owner is not None:
            owner.add_pet(self)

        # Add the pet instance to the class-level list
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        # Instance variable to store the owner's pets
        self._pets = []

    def pets(self):
        # Return the owner's list of pets
        return self._pets

    def add_pet(self, pet):
        # Ensure the pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        
        # Assign the owner to the pet if not already assigned
        if pet.owner is None:
            pet.owner = self
        
        # Add the pet to the owner's list of pets if not already added
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        # Return the list of pets sorted by their name
        return sorted(self._pets, key=lambda pet: pet.name)
