from Building.models import Building, Flat, Measure, Cartography, HousingCooperative


def test_should_create_building(app_building_factory: Building, payment_period_helper) -> None:
    payment_period_helper
    app_building_factory(10)

    assert Building.objects.all().count() == 1
    assert Flat.objects.all().count() == 10
    assert Measure.objects.all().count() == 120
    assert str(Building.objects.all().first()) in str(Flat.objects.all().first())


def test_should_create_cartography(app_building_factory: Building, app_cartography_factory: Cartography,
                                     payment_period_helper) -> None:
    payment_period_helper
    building = app_building_factory(1)
    carto = app_cartography_factory(building)

    assert Cartography.objects.all().count() == 1
    assert carto.building == building


def test_should_create_coop(app_building_factory: Building, app_coop_factory: HousingCooperative,
                                     payment_period_helper) -> None:
    payment_period_helper
    building = app_building_factory(1)
    coop = app_coop_factory
    coop.building_set.add(building)

    assert HousingCooperative.objects.all().count() == 1
    assert building.housing_cooperative.name == coop.name

