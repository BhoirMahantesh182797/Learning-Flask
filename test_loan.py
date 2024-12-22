import pytest
from loan import app

@pytest.fixture
def client():
    return app.test_client()

def test_client(client):
    resp = client.get('/')
    assert resp.status_code ==200
    assert resp.text=="<h1>Loan Approval Application V2!!!</h1>"

def test_predict(client):
    test_data = {
                "ApplicantIncome":100,
                "Credit_History":1.0,
                "Gender":"Male",
                "LoanAmount":1200000,
                "Married":"No"
                }
    resp=client.post('/Predict', json = test_data)
    assert resp.status_code ==200
    assert resp.json == {'loan_approval_status':'Rejected'}

