# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:09:44 2024

@author: juang
"""
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  # Importar la librería Pillow para manejar imágenes

# Diccionario con los personajes y sus categorías
catalogo_personajes = {
    "Super Mario": ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Bowser", "Wario", "Waluigi", "Daisy", "Rosalina"],
    "Zelda": ["Link", "Zelda", "Ganondorf"],
    "Pokemon": ["Pikachu", "Charizard", "Bulbasaur", "Lucario", "Mewtwo", "Squirtle", "Rattata"],
}

# Clase principal de la aplicación
class CatalogoNintendoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Personajes de Nintendo")
        self.root.config(bg="#FFF4B7")

        # Cargar una imagen (asegurate de poner la ruta correcta de la imagen)
        self.imagen_fondo = Image.open("C:/Users/juang/Downloads/mario1.PNG")  # Asegúrate de poner la ruta completa de la imagen

        self.imagen_fondo = self.imagen_fondo.resize((300,300))  # Ajustar el tamaño de la imagen
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_fondo)

        # Crear un widget Label para mostrar la imagen en la interfaz
        self.label_imagen = tk.Label(root, image=self.imagen_fondo)
        self.label_imagen.grid(row=0, column=2, padx=20, pady=20)

        # Crear una lista para mostrar las categorías
        self.lista_categorias = tk.Listbox(root, width=50, height=20, bg="#003161", fg="#FFFFFF", selectbackground="#3DA835")
        self.lista_categorias.grid(row=0, column=0, padx=20, pady=20)

        # Llenar la lista de categorías con las claves del diccionario
        for categoria in catalogo_personajes:
            self.lista_categorias.insert(tk.END, categoria)

        # Conectar la selección de la categoría a la función que muestra personajes
        self.lista_categorias.bind("<<ListboxSelect>>", self.mostrar_personajes)

        # Crear una lista para mostrar los personajes de la categoría seleccionada
        self.lista_personajes = tk.Listbox(root, width=50, height=20, bg="#006A67", fg="#000000", selectbackground="#FF5733")
        self.lista_personajes.grid(row=0, column=1, padx=20, pady=20)

        # Botón para agregar personajes
        self.btn_agregar = tk.Button(root, text="Agregar Personaje", command=self.agregar_personaje, bg="#57A639", fg="#FFFFFF")
        self.btn_agregar.grid(row=1, column=0, pady=5)

        # Botón para eliminar personajes
        self.btn_eliminar = tk.Button(root, text="Eliminar Personaje", command=self.eliminar_personaje, bg="#FF5733", fg="white")
        self.btn_eliminar.grid(row=1, column=1, pady=5)

        # Botón para modificar personajes
        self.btn_modificar = tk.Button(root, text="Modificar Personaje", command=self.modificar_personaje, bg="#3D85C6", fg="black")
        self.btn_modificar.grid(row=1, column=2, pady=5)

    def mostrar_personajes(self, event):
        """Mostrar los personajes de la categoría seleccionada."""
        # Obtener el índice de la categoría seleccionada
        seleccion = self.lista_categorias.curselection()
        if seleccion:
            categoria = self.lista_categorias.get(seleccion)

            # Limpiar la lista de personajes antes de mostrar los nuevos
            self.lista_personajes.delete(0, tk.END)
            for personaje in catalogo_personajes.get(categoria, []):
                self.lista_personajes.insert(tk.END, personaje)

    def agregar_personaje(self):
        """Agregar un nuevo personaje al catálogo."""
        # Pedir al usuario el nombre del personaje y la categoría
        nombre_personaje = simpledialog.askstring("Agregar Personaje", "Nombre del personaje:")
        categoria = simpledialog.askstring("Agregar Personaje", "Categoría del personaje:")

        if nombre_personaje and categoria:
            # Si la categoría no existe, la creamos
            if categoria not in catalogo_personajes:
                catalogo_personajes[categoria] = []

            # Agregar el personaje a la categoría
            catalogo_personajes[categoria].append(nombre_personaje)

            # Actualizar la lista de categorías y mostrar mensaje de confirmación
            self.actualizar_lista_categorias()
            messagebox.showinfo("Personaje Agregado", f"{nombre_personaje} ha sido agregado a {categoria}.")

    def actualizar_lista_categorias(self):
        """Actualizar la lista de categorías en el Listbox."""
        self.lista_categorias.delete(0, tk.END)
        for categoria in catalogo_personajes:
            self.lista_categorias.insert(tk.END, categoria)

    def eliminar_personaje(self):
        """Eliminar el personaje seleccionado."""
        # Obtener la categoría y personaje seleccionados
        seleccion_categoria = self.lista_categorias.curselection()
        seleccion_personaje = self.lista_personajes.curselection()

        if seleccion_categoria and seleccion_personaje:
            # Obtener el nombre de la categoría y el personaje
            categoria = self.lista_categorias.get(seleccion_categoria)
            personaje = self.lista_personajes.get(seleccion_personaje)

            # Confirmar si el usuario desea eliminar
            confirmar = messagebox.askyesno("Eliminar Personaje", f"¿Deseas eliminar a {personaje} de {categoria}?")
            if confirmar:
                # Verificar si el personaje está en la lista de la categoría antes de intentar eliminar
                if personaje in catalogo_personajes[categoria]:
                    # Eliminar el personaje y actualizar la lista
                    catalogo_personajes[categoria].remove(personaje)
                    self.mostrar_personajes(None)  # Actualizar la lista de personajes
                    messagebox.showinfo("Personaje Eliminado", f"{personaje} ha sido eliminado de {categoria}.")
                else:
                    messagebox.showwarning("Error", f"{personaje} no se encuentra en la categoría {categoria}.")
        else:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona un personaje para eliminar.")

    def modificar_personaje(self):
        """Modificar el personaje seleccionado."""
        # Obtener la categoría y personaje seleccionados
        seleccion_categoria = self.lista_categorias.curselection()
        seleccion_personaje = self.lista_personajes.curselection()

        if seleccion_categoria and seleccion_personaje:
            # Obtener el nombre de la categoría y el personaje
            categoria = self.lista_categorias.get(seleccion_categoria)
            personaje = self.lista_personajes.get(seleccion_personaje)

            # Pedir el nuevo nombre para el personaje
            nuevo_nombre = simpledialog.askstring("Modificar Personaje", f"Nuevo nombre para {personaje}:")
            if nuevo_nombre:
                # Actualizar el nombre del personaje en la lista
                indice = catalogo_personajes[categoria].index(personaje)
                catalogo_personajes[categoria][indice] = nuevo_nombre

                # Actualizar la lista de personajes
                self.mostrar_personajes(None)
                messagebox.showinfo("Personaje Modificado", f"{personaje} ha sido cambiado a {nuevo_nombre}.")
        else:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona un personaje para modificar.")

# Crear la ventana principal y ejecutar la aplicación
root = tk.Tk()
app = CatalogoNintendoApp(root)
root.mainloop()




    