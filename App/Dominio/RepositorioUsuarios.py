from typing import Union
from Dominio.Usuario import Usuario


class RepositorioUsuarios:
    def guardar(self, usuario: Usuario) -> None:
        pass

    def buscar(self, correo: str) -> Union[Usuario, None]:
        pass