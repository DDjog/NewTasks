
OR = [3, 5, 4, 8, 1, 3, 9, 7, 4, 7]
H = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def sorting_by_counting(OR, H, DS):
    try:
        if all(value > 0 for value in OR):
            for idx in range(len(OR)):
                H[OR[idx]] += 1

            idx2 = 0
            for idx in range(len(H)):
                for _ in range(H[idx]):
                    DS[idx2] = idx
                    idx2 += 1
            return DS
        else:
            raise ValueError("List contains numbers < 0")

    except Exception as e:
        print("Valid only for numbers > 0")
        print(e)
        return None


rslt = sorting_by_counting(OR, H, DS)
print(rslt)
