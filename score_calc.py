def score_calculator(dice):
    ones = dice.count(1)
    twos = dice.count(2)
    threes = dice.count(3)
    fours = dice.count(4)
    fives = dice.count(5)
    sixs = dice.count(6)

    score_for_roll = 0
    point_dice = 0
    dice_for_points = []

    number_of_each = [ones, twos, threes, fours, fives, sixs]

    individual_location = 1

    new_num_of_each = []

    for each in number_of_each:
        if each != 0:
            new_num_of_each.append(str(each) + "," + str(individual_location))
        individual_location += 1

    if len(new_num_of_each) == 6:
        score_for_roll = 1200
        point_dice = 6
        for i in range(6):
            dice_for_points.append(i + 1)
    else:

        for num_each in new_num_of_each:

            num = int(num_each[0])
            each = int(num_each[2])

            if num >= 3:
                if each == 1:
                    if num == 3:
                        score_for_roll += 1000
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                    elif num == 4:
                        score_for_roll += 2000
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                    elif num == 5:
                        score_for_roll += 4000
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                    elif num == 6:
                        score_for_roll += 8000
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                else:
                    if num == 3:
                        score_for_roll += each * 100
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                    elif num == 4:
                        score_for_roll += each * 200
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                    elif num == 5:
                        score_for_roll += each * 400
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
                    elif num == 6:
                        score_for_roll += each * 800
                        point_dice += num
                        for a in range(num):
                            dice_for_points.append(each)
            else:
                if each == 1:
                    score_for_roll += num * 100
                    point_dice += num
                    for a in range(num):
                        dice_for_points.append(each)
                elif each == 5:
                    score_for_roll += num * 50
                    point_dice += num
                    for a in range(num):
                        dice_for_points.append(each)

    score_and_dice = [score_for_roll, point_dice, dice_for_points]

    return score_and_dice
