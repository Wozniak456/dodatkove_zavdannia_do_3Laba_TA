import library
import numpy as np
import matplotlib.pyplot as plt


sizes = [5, 10, 15, 20, 100, 250, 500]
types = ["random"]
data_plot = {'random': {'Merge':{}, 'insertion':{},'hybrid':{}},
             'best': {},
             'worst': {}}
for n in sizes:
    print("\nDATA SIZE: ", n)
    for gen_type in types:
        print("\n\tDATA TYPE:", gen_type)
        data = library.generate_data(n, gen_type)
        data_bubble = np.copy(data)
        bubble_op_count = library.Merge_sort(data_bubble)[1]
        print("\tMerge sort operation count:", bubble_op_count)
        data_plot[gen_type]['Merge'][n] = bubble_op_count

        data_insertion = np.copy(data)
        insertion_op_count = library.insertion_sort(data_insertion)[1]
        print("\tInsertion sort operation count:", insertion_op_count)
        data_plot[gen_type]['insertion'][n] = bubble_op_count

        data_hybrid = np.copy(data)
        Hybrid_op_count = library.Hybrid_Merge_sort(data_hybrid)[1]
        print("\tHybrid sort operation count:", Hybrid_op_count)
        data_plot[gen_type]['hybrid'][n] = Hybrid_op_count


        data_plot[gen_type]['insertion'][n] = insertion_op_count
library.plot_data(data_plot, logarithmic=True, oneplot=True)
