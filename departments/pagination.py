from rest_framework.pagination import PageNumberPagination

class DepartmentPagination(PageNumberPagination):
    page_size = 8
    page_query_param = "page"
    page_size_query_param = 'size'
    max_page_size = 10