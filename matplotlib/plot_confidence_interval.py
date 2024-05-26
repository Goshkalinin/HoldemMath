import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def get_probabilities(actions):
    probabilities = []
    samples = 0
    successes = 0

    for action in actions:
        samples += 1
        if action == 'B' or action == 'R':
            successes += 1 
        
        probabilities.append(successes/samples)
    return probabilities


def get_bounds(probabilities, mode):
    z = 1.96
    bounds = []
    for index, p in enumerate(probabilities):
        index += 1
        bound = p + (z * (((p * (1 - p)) / index) ** (1/2))) * mode
        bounds.append(bound)

    return bounds

def get_standart_deviation(probabilities):
    standart_deviations = []
    for index, p in enumerate(probabilities):
        index += 1
        deviation = ((p * (1 - p)) / index) ** (1/2)
        standart_deviations.append(deviation)

    return standart_deviations



def plot_graph(lists):
    fig, ax = plt.subplots()
    
    for l in lists:
        ax.plot(
                range(1, len(l['l']) + 1),
                l['l'],
                label=l['name'],
                linestyle='-',
                linewidth=0.5)

    ax.set(xlabel='Sample Number', ylabel='PFR')
    ax.yaxis.set_minor_locator(MultipleLocator(0.02))
    ax.grid(True, which='minor', linestyle='--', linewidth=0.5)
    ax.grid(True, which='major', linestyle='--', linewidth=1)
    ax.legend()

    plt.show()

user = 'Bitcoin11'
actions = 'FFFFFFFFFFBBFFFBFFFFRBFFFRRBFFBFFBFFRFFFFFBBFFBFFFFFFCFFFCBFFFCFFFFFFFFFFBFFBFFFCRFFFFFBFFFBFFBFFRBFFFRFFFFFFBFFBCFRFFF'


probabilities = {'l': get_probabilities(actions), 'name': 'probabilities'}

by_vpip = [
    {'l': get_standart_deviation([0.01]*500), 'name': '0.01'},
    {'l': get_standart_deviation([0.05]*500), 'name': '0.05'},
    {'l': get_standart_deviation([0.15]*500), 'name': '0.15'},
    {'l': get_standart_deviation([0.25]*500), 'name': '0.25'},
    {'l': get_standart_deviation([0.35]*500), 'name': '0.35'},
    {'l': get_standart_deviation([0.45]*500), 'name': '0.45'},
    {'l': get_standart_deviation([0.50]*500), 'name': '0.50'},
    ]


upper_bounds = {'l': get_bounds(probabilities['l'], -1), 'name': 'upper_bounds'}
lower_bounds = {'l': get_bounds(probabilities['l'], 1), 'name': 'lower_bounds'}
standart_deviation = {'l': get_standart_deviation(probabilities['l']), 'name': 'standart_deviation'}


vals = [probabilities, upper_bounds, lower_bounds, standart_deviation]
plot_graph(vals)
