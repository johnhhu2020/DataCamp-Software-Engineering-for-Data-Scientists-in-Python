# Import needed functionality
from collections import Counter
import matplotlib.pyplot as plt


def plot_counter(counter, n_most_common=5):
    
    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    
    # Plot `top_items`
    #plot_counter_most_common(top_items)  ###########################################################################
    plt.plot(list(counter.keys())[:n_most_common], 
             list(counter.values())[:n_most_common])  ###############################################################
    plt.show(block=True)
    
    

    
def sum_counters(counters):
    # Sum the inputted counters
    #return sum(counters.values(), Counter())  ### I think its a mistake ############################################
    
    print(sum(counters.values()))
