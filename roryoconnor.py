import deuces 


def contains_royal_flush(hand):
    "returns whether or not hand contains a royal flush"
    if not contains_flush(hand): 
        return False
    # Sorted Royal flush { 'Ax', 'Jx', 'Kx', 'Qx', 'Tx' }
    hand.sort()
    flush_cards = ['A', 'J', 'K', 'Q', 'T']
    for i in range(5):
        if hand[i][0] != flush_cards[i]:
            return False
    return True


def contains_flush(hand):
    suit = hand[0][1]
    for i in range(5):
        if (hand[i][1] != suit):
            return False
    return True


def contains_straight(hand):
    "returns whether or not hand contains a straigth"

    numbers = convert_hand_to_num_array(hand)
    numbers.sort()
    for i in range(5):
        if i == 0: i += 1
        # Account for Ace being both high and low 
        if i == 4 and numbers[0] == 2 and numbers[i] == 14:
            return True
        if numbers[i] != numbers[i-1] + 1:
            return False
    return True


def contains_pair(hand):
    for i in range(5):
        for j in range(5):
            if hand[i][0] == hand[j][0] and i != j:
                return True
    return False 


def convert_hand_to_num_array(hand): 
    new_hand = []
    for each_card in hand:
        new_hand.append(card_to_number_mapper(each_card))
    return new_hand


def card_to_number_mapper(card):
    "maps card values to numbers"
    if card[0] == "2":
        return 2
    if card[0] == "3":
        return 3
    if card[0] == "4":
        return 4
    if card[0] == "5":
        return 5
    if card[0] == "6":
        return 6
    if card[0] == "7":
        return 7
    if card[0] == "8":
        return 8
    if card[0] == "9":
        return 9
    if card[0] == "T":
        return 10
    if card[0] == "J":
        return 11
    if card[0] == "Q":
        return 12
    if card[0] == "K":
        return 13
    if card[0] == "A":
        return 14


def get_pair_indices(hand): 
    # returns the index of the max pair 
    max_index = (0, 0)
    max_pair = 0
    new_hand = convert_hand_to_num_array(hand)
    for i in range(5):
        for j in range(5):
            if i != j: 
                if new_hand[i] == new_hand[j]:
                    if new_hand[i] > max_pair: 
                        max_pair = new_hand[i]
                        max_index = (i, j)
    return (max_pair, max_index)



def number_of_a_kind(hand): 
    max = 0
    for i in range(5):
        current_num = 0
        for j in range(5):
            if i != j: 
                if hand[i][0] == hand[j][0]:
                    current_num += 1
        if (current_num > max):
            max = current_num
    # Because max doesn't count the first card, we actuallt have a max+1 of a
    # kind 
    return max+1

def get_max_index(hand): 
    new_hand = convert_hand_to_num_array(hand)
    max_val = 0
    max_index = -1
    for i in range(5): 
        cur_card = new_hand[i]
        if cur_card > max_val: 
            max_val = cur_card
            max_index = i
    return max_index


# Student Hand is of the form: ['Ah', 'Kc', 'Qs', 'Tc', '5d'] where 'Ah'
# denotes Ace of Heart, Kc is Queen of Clubs, etc 
class roryoconnor:
    student_Name = ""
    student_Hand = []

    def student_function(self):
       # Keep our cards if we have a hand that is likely to win
       # Royal Flush 
       if contains_royal_flush(self.student_Hand):
            return [False, False, False, False, False]
        # Straight Flush 
       if contains_flush(self.student_Hand) and contains_straight(student_Hand):
            return [False, False, False, False, False]
        # Straight 
       if contains_straight(self.student_Hand):
            return [False, False, False, False, False]
       # Flush 
       if contains_flush(self.student_Hand):
            return [False, False, False, False, False]
       if number_of_a_kind(self.student_Hand) == 4: 
             return [False, False, False, False, False]
       if number_of_a_kind(self.student_Hand) == 3:
             return [False, False, False, False, False]
       if number_of_a_kind(self.student_Hand) == 2: 
             max_pair, indices = get_pair_indices(self.student_Hand)
             array_to_return = [True, True, True, True, True]
             array_to_return[indices[0]] = False
             array_to_return[indices[1]] = False
             return array_to_return
       # There are no pairs, so we should try to get the highest
       max_index = get_max_index(self.student_Hand)
       array_to_return = [True, True, True, True, True]
       array_to_return[max_index] = False
       return array_to_return
       


"""
print "hello world"
my_class = roryoconnor()

#my_class.student_Hand = [ "Jh", "Kh", "9h", "Th", "Qh" ]
my_class.student_Hand = ["2h", "3h", "5h", "4h", "Ah"]

print("contains flush: " + str(contains_flush(my_class.student_Hand))) 

print "contains straight: " + str(contains_straight(my_class.student_Hand))


my_class.student_Hand = ["2h", "2d", "3h", "2c", "2s"]
print "hand: " + str(my_class.student_Hand)
print("x of a kind: " + str(number_of_a_kind(my_class.student_Hand)))


my_class.student_Hand = ["2h", "3h", "5c", "3c", "5h"]
print("hand: " + str(my_class.student_Hand))
array = my_class.student_function()
print "array: " + str(array)
print "done"

"""


