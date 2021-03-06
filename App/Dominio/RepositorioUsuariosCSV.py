import csv
import os
from typing import Union
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Dominio.Usuario import Usuario


class RepositorioUsuariosCSV(RepositorioUsuarios):
    def __init__(self, rutaArchivo: str) -> None:
        self._rutaArchivo: str = rutaArchivo

        # CREAR ARCHIVO SI NO EXISTE
        if not os.path.exists(self._rutaArchivo):
            # Crea directorios padre
            os.makedirs(os.path.dirname(self._rutaArchivo))

            # Escribe las cabeceras del CSV
            with open(self._rutaArchivo, mode='a') as archivoUsuarios:
                writer = csv.writer(archivoUsuarios)
                writer.writerow(['correo', 'nombre', 'apellido',
                                'edad', 'sexo', 'contrasena'])

    def guardar(self, usuario: Usuario) -> None:
        # VERIFICA QUE EL CORREO NO ESTE EN USO
        if self.buscar(str(usuario.correo)):
            raise Exception(
                'El usuario con correo {0} ya existe'.format(usuario.correo))

        # GUARDA EL USUARIO
        with open(self._rutaArchivo, mode='a') as archivoUsuarios:
            writer = csv.writer(archivoUsuarios)

            writer.writerow([
                str(usuario.correo.valor()),
                str(usuario.nombre.valor()),
                str(usuario.apellido.valor()),
                str(usuario.edad.valor()),
                str(usuario.sexo.valor()),
                str(usuario._contraseña.valor())
            ])

    def buscar(self, correo: str) -> Union[Usuario, None]:
        with open(self._rutaArchivo, mode='r') as archivoUsuarios:
            reader = csv.DictReader(archivoUsuarios)

            for row in reader:
                if (row['correo'] == correo):
                    return Usuario.of(
                        row['correo'],
                        row['contrasena'],
                        row['nombre'],
                        row['apellido'],
                        row['edad'],
                        row['sexo'],
                    )
            else:
                return None
