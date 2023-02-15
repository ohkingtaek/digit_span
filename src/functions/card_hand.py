def circulate(self, card, finger):
    xmin = card.loc[0]['xmin']
    ymin = card.loc[0]['ymin']
    xmax = card.loc[0]['xmax']
    ymax = card.loc[0]['ymax']
    finger_x = finger[0]
    finger_y = finger[1]
    if xmin < finger_x < xmax:
        if ymin < finger_y < ymax:
            return 'Match'
        elif ymax < finger_y < ymin:
            return 'Match'
    elif xmax < finger_x < xmin:
        if ymin < finger_y < ymax:
            return 'Match'
        elif ymax < finger_y < ymin:
            return 'Match'
    else:
        return 'Not Match'