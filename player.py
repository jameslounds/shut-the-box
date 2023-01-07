def bit_field_to_num(bit_field: int) -> int:
    return [i+1 for i in range(9) if not bit_field & (1 << i)]


class Player:
    def __init__(self, pieces=0):
        self.pieces = pieces
        self.isOut = False

    def choose_move(self, roll: int) -> int:
        available_numbers = bit_field_to_num(self.pieces)
        for i in available_numbers:
            if i == roll:
                return 1 << (i-1)
            for j in available_numbers:
                if j in (i,):
                    continue
                if i + j == roll:
                    return (1 << (i-1)) | (1 << (j-1))
                for k in available_numbers:
                    if k in (i, j):
                        continue
                    if i + j + k == roll:
                        return (1 << (i-1)) | (1 << (j-1)) | (1 << (k-1))
                    for l in available_numbers:
                        if l in (i, j, k):
                            continue
                        if i + j + k + l == roll:
                            return (1 << (i-1)) | (1 << (j-1)) | (1 << (k-1)) | (1 << (l-1))
                        # we can only go 4 deep, so we can stop here, since roll <= 12, 1 + 2 + 3 + 4 = 10, 1 + 2 + 3 + 4 + 5 = 15
        self.isOut = True
        return 0
