def check_overlapping(line_1, line_2):

    """ function accepts two lines as tuples (x1, x2) and (x3, x4) on the x-axis
    and returns 'Yes' if they overlaps otherwise returns 'No' """

    if not isinstance(line_1, tuple) or not isinstance(line_2, tuple):
        raise TypeError('Please provide line parameter tuple e.g. (x1, x2) format ')

    if len(line_1) != 2 or len(line_2) != 2:
        raise ValueError('Invalid length for the line parameter')

    if line_1[1] < line_2[0] or line_2[1] < line_1[0]:
        return 'No'
    else:
        return 'Yes'

if __name__ == '__main__':
    line_1 = (1, 5)
    line_2 = (2, 6)
    print('Is {} and {} overlaps? --> '.format(line_1, line_2) + check_overlapping(line_1, line_2))

    line_1 = (1, 5)
    line_2 = (7, 30)
    print('Is {} and {} overlaps? --> '.format(line_1, line_2) + check_overlapping(line_1, line_2))