import tkinter as tk
from tkinter import ttk
from db_worker import DbWorker



class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('SQL-worker')
        self.bold_font = 'Helvetica 13 bold'
        self.geometry('1200x700')
        self.frames()

    def frames(self):
        self.frame_for_txt()
        self.frame_tables_lists()
        self.frame_editor()
        self.frame_midle_btn()
        self.frame_current_table()
        self.frame_lower_btn()

    def frame_for_txt(self):
        frame_for_txt = tk.Frame(self, height=30, width=1000, bg='#A9A9A9')
        frame_for_txt.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        l_db = tk.Label(master=frame_for_txt, text='Базы данных', bg='#A9A9A9')
        l_editor = tk.Label(master=frame_for_txt, text='Редактор SQL', bg='#A9A9A9')
        l_editor.place(relx=0.6, rely=0.2)
        l_db.place(relx=0.1, rely=0.2)

    def frame_tables_lists(self):
        frame_tables_lists = tk.Frame(self, height=670, width=300, bg='#C0C0C0')
        frame_tables_lists.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.95)
        db_list = DbWorker().get_all_tables()
        self.tables_lst = ttk.Combobox(frame_tables_lists, values=db_list)
        self.tables_lst.place(relx=0, rely=0)
        get_btn = tk.Button(master=frame_tables_lists, text='Получательная кнопочка',
                            bg='#FF69B4', fg='#00FF00', activebackground='#00BFFF',
                            activeforeground='#FF0000')
        get_btn.place(relx=0.3, rely=0.6)


    def frame_editor(self):
        frame_editor = tk.Frame(self, height=240,  width=700)
        frame_editor.place(relx=0.30, rely=0.05, relwidth=0.7, relheight=0.45)
        query = tk.Text(master=frame_editor)
        query.place(relx=0, rely=0, relwidth=1)

    def frame_midle_btn(self):
        frame_midle_btn = tk.Frame(self, height=30, width=700, bg='#A9A9A9')
        frame_midle_btn.place(relx=0.30, rely=0.45, relwidth=0.7, relheight=0.05)
        editor_btn = tk.Button(master=frame_midle_btn, text='Выполнить', bg='#778899')
        drop_btn = tk.Button(master=frame_midle_btn, text='Очистить', bg='#778899')
        editor_btn.place(relx=0.87, rely=0.1)
        drop_btn.place(relx=0.7, rely=0.1)

    def frame_current_table(self):
        frame_current_table = tk.Frame(self, height=270, width=700)
        frame_current_table.place(relx=0.30, rely=0.5, relwidth=0.7, relheight=0.46)
        lst = DbWorker().show_table('concerts')
        table = ttk.Treeview(master=frame_current_table, show='headings')
        heads = DbWorker().get_column_names()
        table['column'] = heads
        for header in heads:
            table.heading(column=header, text=header[1], anchor='center')
            table.column(column=header, anchor='center')
        for row in lst:
            table.insert('', tk.END, values=row)
        table.pack(expand=tk.YES, fill=tk.BOTH)

    def frame_lower_btn(self):
        frame_lower_btn = tk.Frame(self, height=30, width=700, bg='#A9A9A9')
        frame_lower_btn.place(relx=0.30, rely=0.95, relwidth=0.7, relheight=0.05)


window = Window()
window.mainloop()




























# root = tk.Tk()
# root.title('СУБДшечка')
# root.geometry('1200x700')
#
#
# frame_for_txt = tk.Frame(root, height=30, width=1000, bg='#A9A9A9')
# frame_tables_lists = tk.Frame(root, height=670, width=300, bg='#C0C0C0')
# frame_editor = tk.Frame(root, height=240,  width=700)
# frame_midle_btn = tk.Frame(root, height=30, width=700, bg='#A9A9A9')
# frame_current_table = tk.Frame(root, height=270, width=700)
# frame_lower_btn = tk.Frame(root, height=30, width=700, bg='#A9A9A9')
#
# frame_for_txt.place(relx=0, rely=0, relwidth=1, relheight=0.05)
# frame_tables_lists.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.95)
# frame_editor.place(relx=0.30, rely=0.05, relwidth=0.7, relheight=0.45)
# frame_midle_btn.place(relx=0.30, rely=0.45, relwidth=0.7, relheight=0.05)
# frame_current_table.place(relx=0.30, rely=0.5, relwidth=0.7, relheight=0.46)
# frame_lower_btn.place(relx=0.30, rely=0.95, relwidth=0.7, relheight=0.05)
#
# l_db = tk.Label(master=frame_for_txt, text='Базы данных', bg='#A9A9A9')
# l_editor = tk.Label(master=frame_for_txt, text='Редактор SQL', bg='#A9A9A9')
# query = tk.Text(master=frame_editor)
# editor_btn = tk.Button(master=frame_midle_btn, text='Выполнить', bg='#778899')
# drop_btn = tk.Button(master=frame_midle_btn, text='Очистить', bg='#778899')
# get_btn = tk.Button(master=frame_tables_lists, text='выбрать таблицу',
#                     bg='#FF69B4', fg='#00FF00', activebackground='#00BFFF',
#                     command=lambda: print(345678))
#
# l_editor.place(relx=0.6, rely=0.2)
# l_db.place(relx=0.1, rely=0.2)
# query.place(relx=0, rely=0, relwidth=1)
# editor_btn.place(relx=0.87, rely=0.1)
# drop_btn.place(relx=0.7, rely=0.1)
# get_btn.place(relx = 0.5, rely = 0.7)
#
# db_list = DbWorker().get_all_tables()
# cmbx = ttk.Combobox(frame_tables_lists, values=db_list).place(relx=0, rely=0)
#
#
#
# lst = DbWorker().show_table()
#
# table = ttk.Treeview(master=frame_current_table, show='headings')
# heads = DbWorker().get_column_names()
# table['column'] = heads
# for header in heads:
#     table.heading(column=header, text=header[1], anchor='center')
#     table.column(column=header, anchor='center')
#
#
# for row in lst:
#     table.insert('', tk.END, values=row)
#
# table.pack(expand=tk.YES, fill=tk.BOTH)
#
# root.mainloop()



# [(1, 'a', ';lkjhg', 'aaa'),
#        (2, 'b', 'hghf', 'bbb'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (4, 'd', 'et7ide76i', 'ddd'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyfffffffffffffffffffffffffffntttttttttttttttttttttttttttttttt', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (3, 'c', 'f,fukydtyn', 'ccc'),
#        (16, 'c', 'f,fukydtyn', 'ccc')]