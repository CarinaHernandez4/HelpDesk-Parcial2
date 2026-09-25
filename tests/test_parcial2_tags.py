import pytest
from app.domain.errors import ValidationError
from app.models.entities import Ticket
from app.models.enums import TicketStatus


def make_ticket(ticket_id=1):
    return Ticket(
        id=ticket_id,
        title="Ticket de prueba",
        description="desc",
        category="Hardware",
        priority="Low",
        requester_id=1,
        status=TicketStatus.OPEN,
    )


def test_add_tag_normalizes_and_avoids_duplicates():
    ticket = make_ticket()
    ticket.add_tag("  Urgente  ")
    ticket.add_tag("URGENTE")  # duplicado tras normalizar
    assert ticket.tags == ("urgente",)


def test_add_tag_rejects_blank():
    ticket = make_ticket()
    with pytest.raises(ValidationError):
        ticket.add_tag("   ")


def test_tags_are_independent_between_tickets():
    t1 = make_ticket(1)
    t2 = make_ticket(2)
    t1.add_tag("red")
    assert t1.tags == ("red",)
    assert t2.tags == ()


def test_tags_assignment_is_rejected():
    ticket = make_ticket()
    with pytest.raises(AttributeError):
        ticket.tags = ["hack"]