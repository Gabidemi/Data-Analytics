with open("about_me.txt", "r") as file:
    # content = file.read(50)
    # content2 = file.read(50)

    # content = file.readline(10)
    # content2 = file.readline()

    # content = file.readlines()
    # content2 = file.readlines(1)
    # content3 = file.readlines(10)
    # content4 = file.readlines(10)
    # content5 = file.readlines(100)
    # content6 = file.readlines(-1)
    # print(content)
    # print(content2)
    # print(content3)
    # print(content4)
    # print(content5)
    # print(content6)

    first_characters = file.read(50)

    next_four_lines = []

    for i in range(1, 5):
        next_four_lines.append(file.readline())

    next_hundred_characters = file.readlines(100)

    print(f"First 50 characters: \n{first_characters}")
    print(f"Next four lines, as list by line: \n{next_four_lines}")
    print(f"Next 100 characters, as list by line, rounded up to complete lines: "
        f"{next_hundred_characters}"
    )