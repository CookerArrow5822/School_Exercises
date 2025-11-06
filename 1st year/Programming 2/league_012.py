import sys

h1 =  'POS'
h2 = 'CLUB'
h3 = 'P'
h4 = 'W'
h5 = 'D'
h6 = 'L'
h7 = 'GF'
h8 = 'GA'
h9 = 'GD'
h10 = 'PTS'

def format_line(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c2w):
    line = (f'{c1:>3s} {c2:{c2w:d}s} {c3:>2s} {c4:>3s} {c5:>3s} '
        f'{c6:>3s} {c7:>3s} {c8:>3s} {c9:>3s} {c10:>3s}')
    return line


lines = sys.stdin.readlines()

clubNs = []
for line in lines:
    clubNs.append(len(' '.join(line.split()[1:-8])))

longest = max(clubNs)

print(format_line(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, longest))

for line in lines:
    tokens = line.strip().split()
    pos = tokens[0]
    club = ' '.join(tokens[1:-8])
    [p, w, d, l, f, a, gd, pts] = tokens[-8:]
    print(format_line(pos, club, p, w, d, l, f, a, gd, pts, longest))