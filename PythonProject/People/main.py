from Person import Person


def main():
    user1 = Person("a1", "Anna", 15, False)

    print(user1)
    print(user1.name)
    print(user1.smoking)

    user2 = Person("a2", "Bob", 15, False)
    print(user1>user2)

if __name__ == '__main__':
    main()
