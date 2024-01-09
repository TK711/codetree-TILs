num = int(input())

class st:
    def __init__(self, hei, wei, idx):
        self.H = hei
        self.W = wei
        self.I = idx

stds = []

for idx, i in enumerate(range(num), start = 1):
    hei, wei = tuple(input().split())
    stds.append(st(int(hei),int(wei),idx))

stds.sort(key = lambda x: (x.H,-x.W))

for x in stds:
    print("%d %d %d" % (x.H,x.W,x.I))