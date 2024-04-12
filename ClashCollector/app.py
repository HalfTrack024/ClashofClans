import tkinter as tk
from multiprocessing import Process, Queue
import RunClash
        

# Function to update the GUI
def update_gui(q):
    def check_queue():
        while not q.empty():
            item = q.get()  # Get counter from the queue
            
            if item is None:
                break
            attacks = item.get('attacks')
            cycles = item.get('cycles')
            if attacks is not None:
                attack.config(text=str(attacks))  # Update label
            if cycles is not None:
                cycle.config(text=str(cycles))
        root.after(100, check_queue)  # Schedule next update

    # Create the main window
    root = tk.Tk()
    root.title('Counter')
 #   root.geometry('200x100+0+0')
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.8)
    root.overrideredirect(True)

    attack_name = tk.Label(root, text='Attack Count:  ', fg='#32CD32', font=("Arial", 14))
    attack_name.grid(row=0, column=0)

    # Create a label to display the counter
    attack = tk.Label(root, text='0', fg='#32CD32', font=("Arial", 14))
    attack.grid(row=0, column=1)

    cycle_name = tk.Label(root, text='Collection Count:  ', fg='#32CD32', font=("Arial", 14))
    cycle_name.grid(row=1, column=0)

    # Create a label to display the counter
    cycle = tk.Label(root, text='0', fg='#32CD32', font=("Arial", 14))
    cycle.grid(row=1, column=1)

    # Start checking the queue
    check_queue()

    # Start the GUI loop
    root.mainloop()


if __name__ == '__main__': 

    # Create a queue for communication
    q = Queue()
    
    # Start the GUI in a separate process
    p2 = Process(target=update_gui, args=(q,))
    p2.start()

    # Start the GUI in a separate process
    p3 = Process(target=RunClash.main, args=(q,))
    p3.start()

    # Wait for both processes to finish
    p2.join()
    p3.join()
