from sys import argv


def parser():
    # parse user input
    if len(argv) != 3:
        print("2 arguments required\n"
              "usage: ./hippochecker <project number> <i,j,k...>\n"
              "OR ./hippochecker <project number> <i-z>")
        exit()
    if not argv[1].isdigit():
        print("Invalid format: Project must be a number")
        exit()
    else:
        project = argv[1]
    problems = []
    if argv[2].isdigit():
        problems.append(int(argv[2]))
    elif ',' in argv[2]:
        problems = argv[2].split(',')
        try:
            problems = [int(problem) for problem in problems]
        except ValueError:
            print("Invalid format: All values between commas must be integers")
            exit()
    elif '-' in argv[2]:
        try:
            for i in range(int(argv[2].split('-')[0]), int(argv[2].split('-')[1]) + 1):
                problems.append(i)
        except ValueError:
            print("Invalid format: Values next to hyphen must be integers")
            exit()
    else:
        print("Invalid format: Only numbers, commas, and hyphens allowed")
        exit()
    return [project, problems]