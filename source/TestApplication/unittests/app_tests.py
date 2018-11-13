from ..app import app

def test_get_tasks():
    with app.test_client() as c:
        resp = c.get('/todo/api/v1.0/tasks/1')
        assert resp.status_code == 200