import tkinter as tk
from tkinter import messagebox, simpledialog

class Alumno:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.tutor = tutor
        self.notas = notas
        self.faltas = faltas
        self.amonestaciones = amonestaciones

    def mostrar_datos(self):
        datos = (f"Nombre: {self.nombre}\n"
                 f"Apellido: {self.apellido}\n"
                 f"DNI: {self.dni}\n"
                 f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
                 f"Tutor: {self.tutor}\n"
                 f"Notas: {self.notas}\n"
                 f"Faltas: {self.faltas}\n"
                 f"Amonestaciones: {self.amonestaciones}")
        return datos

    def modificar_dato(self, campo, nuevo_valor):
        if hasattr(self, campo):
            setattr(self, campo, nuevo_valor)
            return f"Dato {campo} modificado exitosamente."
        else:
            return f"No existe el campo {campo} en los datos del alumno."

class SistemaGestionAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
        messagebox.showinfo("Exito", "Alumno agregado correctamente.")

    def expulsar_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                self.alumnos.remove(alumno)
                messagebox.showinfo("Exito", f"Alumno con DNI {dni} expulsado.")
                return
        messagebox.showerror("Error", f"No se encontro ningun alumno con DNI {dni}.")

    def mostrar_datos_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                messagebox.showinfo("Datos del Alumno", alumno.mostrar_datos())
                return
        messagebox.showerror("Error", f"No se encontro ningun alumno con DNI {dni}.")

    def modificar_datos_alumno(self, dni, campo, nuevo_valor):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                resultado = alumno.modificar_dato(campo, nuevo_valor)
                messagebox.showinfo("Resultado", resultado)
                return
        messagebox.showerror("Error", f"No se encontro ningun alumno con DNI {dni}.")

    def mostrar_lista_alumnos(self):
        lista = "\n".join(f"{alumno.nombre} {alumno.apellido} - DNI: {alumno.dni}" for alumno in self.alumnos)
        if lista:
            messagebox.showinfo("Lista de Alumnos", lista)
        else:
            messagebox.showinfo("Lista de Alumnos", "No hay alumnos registrados.")

class App:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Gestion de Alumnos")

        self.menu_principal()

    def menu_principal(self):
        self.clear_frame()

        tk.Label(self.root, text="=== Menu Principal ===", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.root, text="Mostrar datos de un alumno", command=self.mostrar_datos_alumno).pack(pady=5)
        tk.Button(self.root, text="Modificar datos de un alumno", command=self.modificar_datos_alumno).pack(pady=5)
        tk.Button(self.root, text="Mostrar lista de alumnos", command=self.sistema.mostrar_lista_alumnos).pack(pady=5)
        tk.Button(self.root, text="Agregar nuevo alumno", command=self.agregar_alumno).pack(pady=5)
        tk.Button(self.root, text="Expulsar alumno", command=self.expulsar_alumno).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_datos_alumno(self):
        dni = simpledialog.askstring("DNI", "Ingrese el DNI del alumno:")
        if dni:
            self.sistema.mostrar_datos_alumno(dni)

    def modificar_datos_alumno(self):
        dni = simpledialog.askstring("DNI", "Ingrese el DNI del alumno:")
        if dni:
            campo = simpledialog.askstring("Campo", "Ingrese el campo que desea modificar:")
            if campo:
                nuevo_valor = simpledialog.askstring("Nuevo Valor", "Ingrese el nuevo valor:")
                if nuevo_valor:
                    self.sistema.modificar_datos_alumno(dni, campo, nuevo_valor)

    def agregar_alumno(self):
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del alumno:")
        apellido = simpledialog.askstring("Apellido", "Ingrese el apellido del alumno:")
        dni = simpledialog.askstring("DNI", "Ingrese el DNI del alumno:")
        fecha_nacimiento = simpledialog.askstring("Fecha de nacimiento", "Ingrese la fecha de nacimiento (DD/MM/AAAA):")
        tutor = simpledialog.askstring("Tutor", "Ingrese el nombre del tutor:")
        notas_str = simpledialog.askstring("Notas", "Ingrese las notas (separadas por comas):")
        notas = [int(nota.strip()) for nota in notas_str.split(",")] if notas_str else []
        faltas = simpledialog.askinteger("Faltas", "Ingrese la cantidad de faltas:")
        amonestaciones = simpledialog.askinteger("Amonestaciones", "Ingrese la cantidad de amonestaciones:")

        if nombre and apellido and dni and fecha_nacimiento and tutor and notas is not None and faltas is not None and amonestaciones is not None:
            nuevo_alumno = Alumno(nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones)
            self.sistema.agregar_alumno(nuevo_alumno)

    def expulsar_alumno(self):
        dni = simpledialog.askstring("DNI", "Ingrese el DNI del alumno a expulsar:")
        if dni:
            self.sistema.expulsar_alumno(dni)

if __name__ == "__main__":
    root = tk.Tk()
    sistema = SistemaGestionAlumnos()
    app = App(root, sistema)
    root.mainloop()
