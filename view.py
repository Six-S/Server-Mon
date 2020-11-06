# import matplotlib.pylot as plt
import numpy as np

class View():

    def __init__(self, data):
        self.data = data
    
    def create_graph(self):

        fig, ax = plt.subplots()
        ax.plot(self.data['cpu_freq'])
        