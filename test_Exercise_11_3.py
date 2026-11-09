from employee import Employee
import pytest 

@pytest.fixture
def employee():
    """Membuat objek karyawan untuk diuji."""
    return Employee("Najla", "Halimah", 50000)

def test_give_default_raise(employee):
    """Menguji apakah kenaikan gaji default ($5000) berfungsi."""
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    """Menguji apakah kenaikan gaji kustom ($10000) berfungsi."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000