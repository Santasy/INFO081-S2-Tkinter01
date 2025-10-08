import tkinter as tk


def mostrar_ingreso_producto(root):
    ventana = tk.Toplevel(root)
    # ventana = tk.Tk()
    ventana.title("Ingreso:")

    tk.Label(ventana, text="Nombre de producto:").pack()
    e_nombre = tk.Entry(ventana, width=30)
    e_nombre.pack()

    tk.Label(ventana, text="Precio costo:").pack()
    e_costo = tk.Entry(ventana, width=30)
    e_costo.pack()

    tk.Button(ventana, text="Guardar").pack()

    ventana.mainloop()


if __name__ == "__main__":
    print("Principal es Main!")
    mostrar_ingreso_producto()
