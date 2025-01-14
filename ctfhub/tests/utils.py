import django.contrib.messages.api
import django.utils.crypto
from django.contrib.auth.models import User
from ctfhub.models import Member, Team, Ctf


def get_messages(response) -> list[str]:
    request = response.context["request"]
    messages = django.contrib.messages.api.get_messages(request)
    messages_as_str = [str(msg) for msg in messages]
    return messages_as_str


def MockTeam() -> Team:
    team = Team.objects.create(
        name="TestTeam",
        email="test@test.com",
        ctftime_id=1234,
    )
    return team


def MockTeamWithAdmin() -> tuple[Team, Member]:
    team = MockTeam()

    admin = Member.objects.create(
        user=User.objects.create_superuser(
            username="admin",
            password="admin",
            email="admin@admin.com",
        ),
        team=team,
    )
    return (team, admin)


def MockTeamWithMembers(nb: int = 10) -> tuple[Team, list[Member]]:
    members = []
    nb = max(2, nb)

    team, admin = MockTeamWithAdmin()
    members.append(admin)
    assert admin.has_superpowers

    for i in range(nb - 1):
        member = Member.objects.create(
            user=User.objects.create_user(
                username=f"user{i}",
                password=f"user{i}",
                email="user{i}@user.com",
            ),
            team=team,
        )
        assert not member.has_superpowers
        members.append(member)

    return (team, members)


def MockCtf() -> Ctf:
    ctf = Ctf.objects.create(
        name=django.utils.crypto.get_random_string(10),
    )
    return ctf
