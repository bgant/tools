### 1 Merge nested if statements
# instead of this
if a:
    if b:
        pass

# do this
if a and b:
    pass

### 2 Use any instead of loop
# instead of this
numbers = [-1,-2,-4,0,3,-7]
has_positives = False
for n in numbers:
    if n > 0:
        has_positives = True
        break

# do this
numbers = [-1,-2,-4,0,3,-7]
has_positives = any(n > 0 for n in numbers)  # any returns True or False

### 3 Pull statements out of for/while loops
# instead of this
for building in buildings:
    city = 'London'
    addresses.append(building.street_address, city)

# do this
city = 'London'
for building in buildings:
    addresses.append(building.street_address, city)

### 4 Remove inline variable that is only used once
# instead of this
def state_attributes(self):
    """Return the state attributes."""
    state_attr = {
        ATTR_CODE_FORMAT: self.code_format,
        ATTR_CHANGED_BY: self.changed_by,
    }
    return state_attr

# do this
def state_attributes(self):
    """Return the state attributes."""
    return {
        ATTR_CODE_FORMAT: self.code_format,
        ATTR_CHANGED_BY: self.changed_by,
    }

### 5 Replace if statement with if expression
# instead of this
if condition:
    x = 1
else:
    x = 2

# do this
x = 1 if condition else 2

### 6 Add a guard clause
# instead of
def should_i_wear_a_hat(self, hat):
    if isinstance(hat, Hat):
        <do stuff>
    else:
        return False

# do this
def should_i_wear_a_hat(self, hat):
    if not isinstance(hat, Hat):  # Guard Clause
        return False

    <do stuff>  

### 7 Move assignments closer to their usage

### 8 Simplify sequence checks/comparisons
# instead of 
if len(list_of_hats) > 0:
    hat_to_wear = choose_hat(list_of_hats)

# do this
if list_of_hats:  # returns False if False, 0, 0.0, "", (), {}, [], set(), range(0)
    hat_to_wear = choose_hat(list_of_hats)

