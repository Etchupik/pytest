from other_code.services import count_service
from pytest import fixture, raises


@fixture
def re_usable_db_mocker(mocker):
    """
    Fixtures can invoke mocker to yield "re-usable" mocks
    """
    mock_db_service = mocker.patch("other_code.services.db_service", autospec=True)
    mock_db_service.return_value = [(0, "fake row", 0.0)]
    return mock_db_service


