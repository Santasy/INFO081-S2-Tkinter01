import tkinter as tk

from .producto_ingreso import mostrar_ingreso_producto


def mostrar_menu():
    root = tk.Tk()
    root.title("Ventana Principal")

    tk.Button(
        root,
        text="Ingresar producto",
        command=lambda: mostrar_ingreso_producto(root),
    ).pack()

    root.mainloop()


if __name__ == "__main__":
    print("Menú es Main!")
    mostrar_menu()
