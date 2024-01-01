class Solution:
    def imageSmoother(self, img):
        resulting_image = []

        for r, row in enumerate(img):
            resulting_image.append([])
            for c, col in enumerate(row):
                result = 0
                count = 0
                for rr in range(r - 1, r + 2):
                    if rr < 0 or rr == len(img):
                        continue
                    for cc in range(c - 1, c + 2):
                        if cc < 0 or cc == len(row):
                            continue

                        result += img[rr][cc]
                        count += 1
                resulting_image[-1].append(result // count)
        return resulting_image