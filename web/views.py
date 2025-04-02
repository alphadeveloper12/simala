from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage


@csrf_exempt  # For testing; use CSRF token in production
def submit_contact(request):
  if request.method == "POST":
    full_name = request.POST.get("full-name")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone-number", "")
    message = request.POST.get("message")

    if not full_name or not email or not message:
      return JsonResponse({"message": "All required fields must be filled."}, status=400)

    # Save to database
    ContactMessage.objects.create(full_name=full_name, email=email, phone_number=phone_number, message=message, )

    return JsonResponse({"message": "Your message has been submitted successfully!"})

  return JsonResponse({"message": "Invalid request method."}, status=400)


def index(request):
  return render(request, "index.html")  # Ensure index.html exists in templates folder
