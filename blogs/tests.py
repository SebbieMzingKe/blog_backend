from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import BlogListCreateView
from django.contrib.auth import get_user_model


User = get_user_model()


class HelloWorldTestCase(APITestCase):

    def test_hello_world(self):
        response = self.client.get(reverse('blogs_home'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello World")


class BlogListCreateTestCase(APITestCase):

    def setUp(self):
    #     self.factory = APIRequestFactory()
    #     self.view = BlogListCreateView.as_view()
        self.url = reverse("list_blogs")
    #     self.user = User.objects.create(
    #         username = "sebbiemzing",
    #         email = "sebbie@gmail.com",
    #         password = "Seb@1234"
    #     )


    def authenticate(self):
        self.client.post(reverse("signup"),{
            "email": "mzing@gmail.com",
            "password":"Seb@1234",
           " username": "mzing",

        })

        response = self.client.post(reverse("login"),{
            "email": "mzing@gmail.com",
            "password":"Seb@1234",
        })

        print(response.data)
        token = response.data['tokens']['access']

        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {token}")


    def test_list_blog(self):
        response = self.client.get(self.url)

        # response = self.view(request)


        

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if isinstance(response.data, dict):
            # self.assertIsInstance(response.data, dict)
            self.assertEqual(response.data.get("count"),0)
            self.assertEqual(response.data["results"], [])

    def test_blog_creation(self):
        self.authenticate()

        sample_data = {
            "title":"Sample Title",
            "content": "Sample Content"
        }

        response = self.client.post(reverse('list_blogs'),
            sample_data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], sample_data["title"])




        # sample_blog = {
        #     "title":"Sample Blog",
        #     "content":"Sample Blog"
        # }
        # request = self.factory.post(self.url, sample_blog)

        # request.user = self.user

        # response = self.view(request)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)