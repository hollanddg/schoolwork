def main():
    print('Welcome!')
    print('Choose a file that you would like to see the contents or enter 3 to exit.')
    print('1. States Devin has lived in')
    print('2. States Devin has visited')
    print('3. Exit')
    choice = int(input())
    if choice == 1:
        c1()
    elif choice == 2:
        c2()
    else:
        print('Bye')
        quit()


def c1():
    states_visited = open('states_visited.txt', 'r')
    state1 = states_visited.readline().rstrip('\n')
    state2 = states_visited.readline().rstrip('\n')
    state3 = states_visited.readline().rstrip('\n')
    state4 = states_visited.readline().rstrip('\n')
    state5 = states_visited.readline().rstrip('\n')
    print(state1, state2, state3, state4, state5)
    states_visited.close()


def c2():
    states_lived_in = open('states_lived_in.txt', 'r')
    state = states_lived_in.readline().rstrip('\n')
    while state != '':
        print(state)
        state = states_lived_in.readline().rstrip('\n')
    states_lived_in.close()


main()

# alt_1 for c1()
# max = 0
# while max != 5:
#   print(state)
#   max =+ 1
#   state = states_visited.readline().rstrip('\n')

# alt_2 for c1()
# states_visited = open('states_visited.txt', 'r')
# states = []
# count = len(states)
# while count != 5:
#    visited_state = states_visited.readline().rstrip('\n')
#    states.append(visited_state)
# states_visited.close()
# print(states)
