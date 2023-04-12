from __future__ import annotations

import djclick as click

from apps.sections.models import Section
from apps.utils.factories.pages import PageFactory


@click.command()
def seed():
    import factory
    from faker_education import SchoolProvider

    factory.Faker.add_provider(SchoolProvider)
    # pprint.pprint(SectionMembershipWithUserFactory.create_batch(15))
    # secho(BuddyRequestWithKnownUserFactory.create_batch(15))

    PageFactory.create_batch(10, section=Section.objects.filter(name="ESN VUT Brno").first())
