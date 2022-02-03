import tkinter as tk
from tkinter import ttk
from db_worker import DbWorker
from tkinter import filedialog as fd


class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('SQL-worker')
        self.FONT = 'Helvetica 10 bold'
        self.geometry('1200x700')
        self._db = DbWorker()
        self.frames()

    def frames(self):
        self.frame_for_txt()
        self.frame_tables_lists()
        self.frame_editor()
        self.frame_midle_btns()
        self.frame_lower_btn()

    def frame_for_txt(self):
        frame_for_txt = tk.Frame(self, height=30, width=1000, bg='#A9A9A9')
        frame_for_txt.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        l_db = tk.Label(master=frame_for_txt, text='Базы данных', bg='#A9A9A9', font=self.FONT)
        l_editor = tk.Label(master=frame_for_txt, text='Редактор SQL', bg='#A9A9A9', font=self.FONT)
        l_editor.place(relx=0.6, rely=0.2)
        l_db.place(relx=0.1, rely=0.2)

    def frame_tables_lists(self):
        db_list = self._db.get_all_tables()
        frame_tables_lists = tk.Frame(self, height=670, width=300, bg='#C0C0C0')
        frame_tables_lists.place(relx=0, rely=0.05, relwidth=0.3, relheight=0.95)
        self.tables_lst = ttk.Combobox(frame_tables_lists, values=db_list)
        self.tables_lst.place(relx=0, rely=0)
        get_btn = tk.Button(master=frame_tables_lists, text='Получательная кнопочка',
                            bg='#FF69B4', fg='#00FF00', activebackground='#00BFFF', font=self.FONT,
                            activeforeground='#FF0000', command=lambda: self.frame_current_table())
        get_btn.place(relx=0.3, rely=0.6)
        db_btn = tk.Button(master=frame_tables_lists, text='Подключение',
                            bg='#00FF00', fg='#C71585', activebackground='#FFFF00', font=self.FONT,
                            activeforeground='#FF0000', command=self.__db_con)
        db_btn.place(relx=0.5, rely=0.4)

    def frame_editor(self):
        frame_editor = tk.Frame(self, height=240,  width=700)
        frame_editor.place(relx=0.30, rely=0.05, relwidth=0.7, relheight=0.45)
        self.query = tk.Text(master=frame_editor)
        self.query.place(relx=0, rely=0, relwidth=1)

    def frame_midle_btns(self):
        frame_midle_btns = tk.Frame(self, height=30, width=700, bg='#A9A9A9')
        frame_midle_btns.place(relx=0.30, rely=0.45, relwidth=0.7, relheight=0.05)
        editor_btn = tk.Button(master=frame_midle_btns, text='Выполнить', bg='#778899', font=self.FONT,
                               command=lambda: [self._db.execute_query(self.query.get('1.0', tk.END).strip()), self.frame_current_table()])
        drop_btn = tk.Button(master=frame_midle_btns, text='Очистить', bg='#778899', font=self.FONT,
                             command=lambda: self.query.delete('1.0', tk.END))
        editor_btn.place(relx=0.87, rely=0.1)
        drop_btn.place(relx=0.7, rely=0.1)

    def frame_current_table(self):
        frame_current_table = tk.Frame(self, height=270, width=700)
        frame_current_table.place(relx=0.30, rely=0.5, relwidth=0.7, relheight=0.46)
        lst = self._db.show_table(self.tables_lst.get())
        table = ttk.Treeview(master=frame_current_table, show='headings')
        heads = self._db.get_column_names(self.tables_lst.get())
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

    def __db_con(self):
        self._db.con = fd.askopenfilename()
        self.frame_tables_lists()


window = Window()
window.mainloop()
