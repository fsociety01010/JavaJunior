problem = [
    '...?.....?............#',
    '......?.......?....####',
    '.?........?.....#####?#',
    '.......?.....#####?####',
    '..?..?....#############',
    '.......######?######?##',
    '....#####?#######?#####',
    '.###################?##']

wx = 20
wy = 5
wb = -209

def neuron(x, y, bias=1):
    f = wx * x + wy * y + wb * bias
    if f < 0:
        return -1
    return 1

y = 0
for line in problem:
    x = 0
    new_line = ''
    for char in line:
        if char == '?':
            r = neuron(x, y)
            if r < 0:
                char = '.'
            else:
                char = '#'
        new_line += char
        x += 1
    print new_line
    y += 1