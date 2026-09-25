import pytest
from app.domain.errors import TicketNotFoundError
from app.models.enums import Role
from app.repositories.memory import InMemoryTicketRepository, InMemoryUserRepository
from app.services.tickets import TicketService
from app.services.users import UserService


def build_service():
    ticket_repo = InMemoryTicketRepository()
    user_repo = InMemoryUserRepository()
    users = UserService(user_repo)
    tickets = TicketService(ticket_repo, users)
    return tickets, users


def test_watchers_without_technician_returns_only_requester():
    tickets, users = build_service()
    requester = users.register("ana@example.com", "Ana", role=Role.REQUESTER)
    ticket = tickets.create(
        title="Sin sonido",
        description="No suena el audio",
        category="Hardware",
        priority="Low",
        requester_id=requester.id,
    )

    result = tickets.watchers(ticket.id)

    assert result == [requester]


def test_watchers_with_technician_returns_both_distinct_users():
    tickets, users = build_service()
    requester = users.register("ana@example.com", "Ana", role=Role.REQUESTER)
    technician = users.register("tomas@example.com", "Tomas", role=Role.TECHNICIAN)
    ticket = tickets.create(
        title="Sin acceso",
        description="No entra al sistema",
        category="Security",
        priority="High",
        requester_id=requester.id,
    )
    tickets.assign(ticket.id, technician_id=technician.id)

    result = tickets.watchers(ticket.id)

    assert result == [requester, technician]


def test_watchers_propagates_ticket_not_found():
    tickets, _users = build_service()
    with pytest.raises(TicketNotFoundError):
        tickets.watchers(999)