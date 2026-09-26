class Person:
    id: str
    name: str
    age: int
    smoking: bool

    def __init__(self, id: str, name: str, age: int, smoking: bool) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.smoking = smoking

    def __str__(self):
        



if __name__ == '__main__':
        main()
