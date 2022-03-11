LOST_LOCATION = 'Corn'
LOST_DESCRIPTION = "You're lost in some fields of corn."

MAP = [
  [
    { 'location': 'Clearing', 'description': "You're in a clearing. There is a hut to the north. You see some fields of corn all around you." },
    { 'location': 'Hut', 'description': "You're next to a straw hut. You see some fields of corn all around you. There's a path to the north." },
    { 'location': 'Path', 'description': "You're on a small path through the fields of corn. It continues to the east. There's a straw hut to the south of you." }
  ],
  [
    { 'location': LOST_LOCATION, 'description': LOST_DESCRIPTION },
    { 'location': LOST_LOCATION, 'description': LOST_DESCRIPTION },
    { 'location': 'Path', 'description': "You're on a small east/west path through the fields of corn." }
  ],
  [
    { 'location': LOST_LOCATION, 'description': LOST_DESCRIPTION },
    { 'location': LOST_LOCATION, 'description': LOST_DESCRIPTION },
    { 'location': 'Tractor', 'description': "You've arrived at a rusting, abandoned tractor." }
  ],
]

def describe_location(here):
  x = here[0]
  y = here[1]

  try:
    location = MAP[x][y]['location']
    description = MAP[x][y]['description']
  except IndexError:
    location = LOST_LOCATION
    description = LOST_DESCRIPTION

  print(f'\nLocation: {location}')
  print(description)

def show_menu():
  print('\nWhere would you like to go?\n')
  print('1) Go North')
  print('2) Go East')
  print('3) Go South')
  print('4) Go West')
  print('5) Quit Game\n')

def get_menu_choice():
  choice = None
  while choice == None:
    try:
      choice = int(input('> '))
    except ValueError:
      print('That was not a valid number, please try again!')
      continue

    # You're guaranteed to have a number by the time the progrom gets here
    if choice < 1 or choice > 5:
      print('That was not a valid choice, please try again!')
      choice = None

  return choice

def main():
  print('================')
  print('Welcome to BORK!')
  print('================')

  current_position = [0, 0]

  while True:
    describe_location(current_position)
    show_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      current_position[1] += 1
    elif menu_choice == 2:
      current_position[0] += 1
    elif menu_choice == 3:
      current_position[1] -= 1
    elif menu_choice == 4:
      current_position[0] -= 1
    elif menu_choice == 5:
      print('\nGoodbye!\n\n')
      break

main()