from app import app
from chalice.test import Client


def test_warm_up_db_everyday():
    with Client(app) as client:
        response = client.lambda_.invoke(
            "warm_up_db_everyday",
            client.events.generate_cw_event(
                source="", detail_type="", detail="", resources=""
            ),
        )

        assert response.payload == "This should be invoked every weekday at 6pm"
