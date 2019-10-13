import matplotlib.pyplot as plt
from matplotlib import colors
from storage import Storage
import numpy as np
import collections

class Viz():
    def __init__(self):
        self.db = Storage()
        self.words_dict = self.db.get_all_words()
        self.days = self.db.data["dayEmotions"]

    def makeGrid(self):
        arr = []
        sad_counter = 0
        for i in range(0,30):
            emotion = 0
            if self.days[str(i)] == "happiness":
                emotion = 1
                if sad_counter < 5:
                    sad_counter = 0
            elif self.days[str(i)] == "neutral":
                emotion = 0
                if sad_counter < 5:
                    sad_counter = 0
            elif self.days[str(i)] == "surprise":
                emotion = 0
                if sad_counter < 5:
                    sad_counter = 0
            else:
                emotion = -1
                sad_counter += 1

            arr.append(emotion)
    
        # data = np.array(arr)
        # data = np.reshape(data, (5,6))
        # # create discrete colormap
        # cmap = colors.ListedColormap([[238/255.0,186/255.0,198/255.0], [83/255.0, 89/255.0, 154/255.0]])
        # bounds = [-1,0,1]
        # norm = colors.BoundaryNorm(bounds, cmap.N)

        # fig, ax = plt.subplots()
        # ax.imshow(data, cmap=cmap, norm=norm)

        # # draw gridlines
        # ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        # ax.set_xticks(np.arange(-.5, 5.5, 1))
        # ax.set_yticks(np.arange(-.5, 5.5, 1))
        # #ax.set_axis_off()
        # ax.set_xticklabels([])
        # ax.set_yticklabels([])

        # plt.savefig('../viz/grid.png')
        if sad_counter > 5:
            return "You have been feeling down lately, consider looking into some help"
        else:
            return "Glad you're doing okay! Keep it up!"

    def wordAssociation(self):
        sorted_x = sorted(self.words_dict.items(), key=lambda kv: int(kv[1]))
        saddest = sorted_x[0][0]
        happiest = sorted_x[len(sorted_x)-1][0]
        middle1 = sorted_x[int(len(sorted_x)/2)][0]
        middle2 = sorted_x[int(len(sorted_x)/2 + 1)][0]
        return [happiest, middle1, middle2, saddest]



