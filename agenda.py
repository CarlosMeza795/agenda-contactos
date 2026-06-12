from rich.console import Console
from rich.table import Table
import database

console = Console()

def mostrar_menu():
    console.print("\n[bold cyan]===== AGENDA DE CONTACTOS =====[/bold cyan]")
    console.print("[1] Agregar contacto")
    console.print("[2] Buscar contacto")
    console.print("[3] Eliminar contacto")
    console.print("[4] Listar todos los contactos")
    console.print("[5] Salir")
    console.print("[bold cyan]================================[/bold cyan]")

def mostrar_tabla(contactos):
    if not contactos:
        console.print("[yellow]No se encontraron contactos.[/yellow]")
        return

    tabla = Table(show_header=True, header_style="bold magenta")
    tabla.add_column("ID", style="dim", width=5)
    tabla.add_column("Nombre", width=20)
    tabla.add_column("Telefono", width=15)
    tabla.add_column("Email", width=25)

    for contacto in contactos:
        tabla.add_row(str(contacto[0]), contacto[1], contacto[2], contacto[3])

    console.print(tabla)

def agregar():
    console.print("\n[bold]--- Agregar Contacto ---[/bold]")
    nombre = input("Nombre: ").strip()
    telefono = input("Telefono: ").strip()
    email = input("Email: ").strip()

    if not nombre:
        console.print("[red]El nombre no puede estar vacio.[/red]")
        return

    database.agregar_contacto(nombre, telefono, email)
    console.print(f"[green]Contacto '{nombre}' agregado correctamente.[/green]")

def buscar():
    console.print("\n[bold]--- Buscar Contacto ---[/bold]")
    nombre = input("Nombre a buscar: ").strip()
    contactos = database.buscar_contacto(nombre)
    mostrar_tabla(contactos)

def eliminar():
    console.print("\n[bold]--- Eliminar Contacto ---[/bold]")
    listar_todos()

    try:
        id_contacto = int(input("\nIngresa el ID del contacto a eliminar: "))
        confirmacion = input(f"Seguro que queres eliminar el contacto con ID {id_contacto}? (s/n): ")
        if confirmacion.lower() == "s":
            database.eliminar_contacto(id_contacto)
            console.print("[green]Contacto eliminado correctamente.[/green]")
        else:
            console.print("Operacion cancelada.")
    except ValueError:
        console.print("[red]ID invalido. Ingresa un numero.[/red]")

def listar_todos():
    console.print("\n[bold]--- Lista de Contactos ---[/bold]")
    contactos = database.listar_contactos()
    mostrar_tabla(contactos)

def main():
    database.crear_tabla()

    while True:
        mostrar_menu()
        opcion = input("Elegi una opcion: ").strip()

        if opcion == "1":
            agregar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            eliminar()
        elif opcion == "4":
            listar_todos()
        elif opcion == "5":
            console.print("[bold]Saliendo... Hasta luego![/bold]")
            break
        else:
            console.print("[red]Opcion no valida.[/red]")

main()