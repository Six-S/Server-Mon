import matplotlib.pyplot as plt
import numpy as np

class View():

    def __init__(self):
        self.data = None
        self.cpu_data = {}

    def update_cpu_details(self):
        #CPU frequency graph
        fig, ax = plt.subplots()
        ax.plot(self.data['cpu_freq'])

    def update_and_refresh(self, data):
        #Update the data we have.
        self.data = data

        #Update the CPU Graphs.

        