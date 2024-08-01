from ninja import Router
from project.utils import validation
from access.models import User


router = Router()


@router.get("/")
def test_route(request):
    return {"hello": "world"}


@router.get("/validate-email")
def validate_email(request, email: str):

    if not validation.validate_email(email):
        return router.api.create_response(
            request,
            {"message": "Invalid email address."},
            status=400,
        )

    exists = User.objects.filter(email=email.strip()).exists()
    if exists:
        return router.api.create_response(
            request,
            {"message": "User with this email exists."},
            status=400,
        )

    return router.api.create_response(
        request,
        {"message": "Email available"},
        status=200,
    )
