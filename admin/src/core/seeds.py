from src.core import board
from src.core import auth


def run():
    item1 = board.create_item(
        name="Sofá",
        description="Sofá verde de 2 cuerpos",
        price=100000,
    )
    item2 = board.create_item(
        name="Tele",
        description="Tele Samsung 43 pulgadas",
        price=120000,
    )
    item3 = board.create_item(
        name="Mesa ratona",
        description="Mesa ratona de madera elevable",
        price=80000,
    )

    issue1 = board.create_issue(
        email="jose@mail.com",
        title="Mi computadora no funciona.",
        description="Mi departamente me compró una nueva computadora y necesito configurarla con todos mis emails y documentos de mi vieja computadora.",
        status="new",
    )
    issue2 = board.create_issue(
        email="maria@mail.com",
        title="No puedo obtener mis emails.",
        description="Estoy tratando de acceder a mi correo desde casa, pero no puedo obtenerlos. Estoy tratando con Outlook en mi casa pero en la oficina tengo Thunderbird.",
        status="in_progress",
    )
    issue3 = board.create_issue(
        email="ruben@mail.com",
        title="No puedo imprimir",
        description="Cada vez que trato de imprimir mi presentación el programa se cierra. Esto sólo me pasa con PowerPoint en Word puedo imprimir. Ya me aseguré que la impresora está prendida. Tengo una HP LaserJet 5.",
        status="done",
    )

    label1 = board.create_label(
        title="Urgente",
        description="Issues que tienen que resolverse dentro de 24hs",
    )
    label2 = board.create_label(
        title="Importante",
        description="Issues de alta prioridad",
    )
    label3 = board.create_label(
        title="Soporte",
        description="Issues relacionados con soporte técnico",
    )
    label4 = board.create_label(
        title="Ventas",
        description="Issues relacionado con el área de ventas",
    )

    fede = auth.create_user(email="fede@mail.com", password="1234")
    agus = auth.create_user(email="agus@mail.com", password="1234")
    miguel = auth.create_user(email="miguel@mail.com", password="1234")

    board.assign_user(issue1, fede)
    board.assign_user(issue2, agus)
    board.assign_user(issue3, miguel)

    board.assign_labels(issue1, [label1, label2])
    board.assign_labels(issue2, [label3, label4])
    board.assign_labels(issue3, [label1, label4])
