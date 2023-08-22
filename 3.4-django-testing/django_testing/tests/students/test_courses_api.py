import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory



@pytest.mark.django_db
def test_first_course(client, courses_factory):
    courses_factory(_quantity=1)                        #id 1
    response = client.get('/api/v1/courses/1/')
    #data = response.json()
    assert response.status_code == 200
    assert Course.objects.all()[0].pk == 1


@pytest.mark.django_db
def test_list_courses(client, courses_factory):
    quantity = 2
    courses_factory(_quantity=quantity)                 #id 2-3
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == quantity


@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    quantity = 2                                        
    courses_factory(_quantity = quantity)               #id 4-5
    response = client.get('/api/v1/courses/?id=4')
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_name(client, courses_factory):
    quantity = 2                                        
    courses_factory(_quantity = quantity)               #id 6-7
    courses = Course.objects.all()
    
    for course in courses:
        response = client.get(f'/api/v1/courses/?name={course.name}')
        assert response.status_code == 200
        assert response.data[0]["name"] == course.name
    

@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={"name":"foo"})     #id 8
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert response.data["name"] == "foo"
    

@pytest.mark.django_db
def test_patch_course(client, courses_factory):
    courses_factory(_quantity = 1)                                      #id 9
    response = client.patch('/api/v1/courses/9/', data={"name":"new"})
    assert response.status_code == 200
    assert response.data["name"] == "new"


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    courses_factory(_quantity = 1)                         #id 10
    count = Course.objects.count()
    response = client.delete('/api/v1/courses/10/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    assert response.data == None