def running_while_loop(start_value, terminate_value, incrementer):
    i = start_value
    number =[]
    while i<terminate_value:
        print(f"At the top of list is {i}")
        number.append(i)

        i = i + incrementer

        print("Numbers now: ", number)

    for n in number:
        print(n)


running_while_loop(1, 10, 2)