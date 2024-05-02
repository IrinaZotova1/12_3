import tkinter as tk

class IceCreamStand(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ice Cream Stand")
        self.geometry("600x400")  # Устанавливаем размер окна

        self.configure(background='#FFC0CB')  # Устанавливаем цвет фона на розовый

        pink_frame = tk.Frame(self, bg='#FFC0CB')  # Создаем розовый фрейм
        pink_frame.pack(pady=30, padx=30, fill='both', expand=True)  # Устанавливаем отступы, и заполняем окно всем доступным местом

        info_text = "Добро пожаловать в кафе Сладкое королевство!\n\nСорта нашего мороженого:\nВанильное\nШоколадное\nМятное\nКлубничное\n\nЧасы работы:\n10-19 "
        info_label = tk.Label(pink_frame, text=info_text, bg='white', font=('Arial', 12), padx=10, pady=10)  # Создаем метку с информацией о кафе
        info_label.pack()
if __name__ == "__main__":
    app = IceCreamStand()
    app.mainloop()