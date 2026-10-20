import re
PADRAO_EMAIL = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
def validar_email(email: str) -> bool:
    return bool(PADRAO_EMAIL.match(email.strip()))


# TODO: Implementar validação de email mais robusta, incluindo verificação de domínio e formato adequado.

