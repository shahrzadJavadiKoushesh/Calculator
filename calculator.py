import tkinter as tk
import tkinter.messagebox

calc_keys = [
    {
        'text': '7',
        'command': lambda: insert_number_in_calc_result('7'),
    },
    {
        'text': '8',
        'command': lambda: insert_number_in_calc_result('8'),
    },
    {
        'text': '9',
        'command': lambda: insert_number_in_calc_result('9'),
    },
    {
        'text': '+',
        'command': lambda: insert_number_in_calc_result('+'),
    },
    {
        'text': '4',
        'command': lambda: insert_number_in_calc_result('4'),
    },
    {
        'text': '5',
        'command': lambda: insert_number_in_calc_result('5'),
    },
    {
        'text': '6',
        'command': lambda: insert_number_in_calc_result('6'),
    },
    {
        'text': '-',
        'command': lambda: insert_number_in_calc_result('-'),
    },
    {
        'text': '1',
        'command': lambda: insert_number_in_calc_result('1'),
    },
    {
        'text': '2',
        'command': lambda: insert_number_in_calc_result('2'),
    },
    {
        'text': '3',
        'command': lambda: insert_number_in_calc_result('3'),
    },
    {
        'text': '*',
        'command': lambda: insert_number_in_calc_result('*'),
    },
    {
        'text': '.',
        'command': lambda: insert_number_in_calc_result('.'),
    },
    {
        'text': '0',
        'command': lambda: insert_number_in_calc_result('0'),
    },
    {
        'text': 'c',
        'command': lambda: insert_number_in_calc_result('c'),
    },
    {
        'text': '=',
        'command': lambda: insert_number_in_calc_result('='),
    },
]
final_results = [] * 10  # to store last 10 calculations

window = tk.Tk()

lbl_calculator_result = tk.Label(
    master=window,
    text='0',
    width=30,
    height=5,
)
last_op_index = -1
last_dot_index = -1


def equal_alert():
    tkinter.messagebox.showinfo('Error', "You must enter an expression to calculate")


def insert_number_in_calc_result(btn_txt):
    current = lbl_calculator_result['text']
    global last_op_index, last_dot_index
    if current[0] != '=':
        if btn_txt in ['+', '-', '*']:
            last_op_index = len(current)
        # print(last_op_index, last_dot_index)
        if btn_txt == 'c':
            lbl_calculator_result['text'] = '0'
            last_op_index, last_dot_index = 0, 0
        elif current == '0':
            lbl_calculator_result['text'] = btn_txt
        elif btn_txt == '=':
            result = f"{eval(current)}"
            final_results.append(result)
            # print(final_results)
            lbl_calculator_result['text'] = result
            last_op_index, last_dot_index = 0, 0
            if '.' in result:
                last_dot_index = result.index('.')
        elif btn_txt == '.' and (not (last_dot_index > last_op_index or current[-1] == '.')):
            lbl_calculator_result['text'] += btn_txt
            last_dot_index = len(current)
        elif btn_txt in ['+', '-', '*'] and current[-1] in ['+', '-', '*']:
            lbl_calculator_result['text'] = current[:-1] + btn_txt
        else:
            lbl_calculator_result['text'] += btn_txt
    else:
        equal_alert()
        lbl_calculator_result['text'] = "0"


def show_history():
    history_window = tk.Toplevel(window)
    history_window.title('History')
    history_window.geometry("200x200")
    list_of_lbls = []
    for i in range(len(final_results)):
        lbl = tk.Label(
            master=history_window,
            text=final_results[i],
            height=5,
            pady=10
        )
        list_of_lbls.append(lbl)
    for k, lbl in enumerate(list_of_lbls):
        lbl.grid(row=k, sticky='nswe')


result_btn = tk.Button(
    master=window,
    text='history',
    height=5,
    command=show_history
).grid(row=5, columnspan=4, sticky='nswe')

calc_keys_objects = []
for calc_key_data in calc_keys:
    btn = tk.Button(
        master=window,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        height=3,
    )
    calc_keys_objects.append(btn)

for i, calc_key_obj in enumerate(calc_keys_objects):
    calc_key_obj.grid(row=i // 4 + 1, column=i % 4, sticky='nswe')

lbl_calculator_result.grid(row=0, column=0, columnspan=4)

window.title('calculator')
window.mainloop()
