### 1 Merge append into list declaration
# instead of
players = []
players.append("Patrick")
players.append("Max")
players.append("Jessi")

# do this
players = ["Patrick","Max","Jessi"]

### 2 Use items() to directly unpack dictionary values
# instead of
teams_by_color = {"blue": ["Patrick","Jessi"]}
for team_color in teams_by_color:
    players = teams_by_color[team_color]
    if is_winning(team_color):
        advance_level(players)

# do this
teams_by_color = {"blue": ["Patrick","Jessi"]}
for team_color, players in teams_by_color.items():
    if is_winning(team_color):
        advance_level(players)

### 3 Replace range(len) with enumerate
# instead of 
for i in range(len(players)):
    print(i, players[i])

# do this
for i, player in enumerate(players):
    print(i, player)

### 4 Replace manual loop counter with call to enumerate
# instead of 
i = 1
for player in players:
    print(i, player)
    i += 1

# do this
for i, player in enumerate(players, start=1):
    print(i, player)

### 4.2 Don't manually update counter
# instead of 
num_players = 0
for player in players:
    num_players += 1

# do this
num_players = len(players)

### 5 Simplify conditional into return statement
# instead of
def function():
    if isinstance(a, b) or issubclass(b, a):
        return True
    return False

# do this
def function():
    return isinstance(a, b) or issubclass(b, a)

# instead of
def any_pythonistas():
    pythonistas = [coder for coder in coders if is_good_in_python(coder)]
    if pythonistas or self.is_pythonista():
        return True
    return False

# do this
def any_pythonistas():
    pythonistas = [coder for coder in coders if is_good_in_python(coder)]
    return pythonistas or self.is_pythonista()

### 6 Merge duplicate blocks in conditional
# instead of 
def process_payment(payment, currency):
    if currency == "USD":
        process_standard_payment(payment)
    elif currency == "EUR":
        process_standard_payment(payment)
    else:
        process_international_payment(payment)

# do this
def process_payment(payment, currency):
    if currency == "USD" or currency == "EUR":
        process_standard_payment(payment)
    else:
        process_international_payment(payment)

### 7 Replace multiple comparisons of same variable with *in*
# instead of 
if currency == "USD" or currency == "EUR":

# do this
if currency in ["USD","EUR"]:

### 8 Replace yield inside for loop with yielf from
# instead of 
def get_content(entry):
    for block in entry.get_blocks():
        yield block

# do this
def get_content(entry):
    yield from entry.get_blocks()


