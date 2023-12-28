from .models import UserTestResult, Medicine


def get_medicines_for_user(user_id):
    # Get the UserTestResult instances for the user
    user_test_results = UserTestResult.objects.filter(user=user_id)

    # Extract the 'treats' field (which is a ForeignKey to Medicine) from the UserTestResult instances
    medicine_ids = user_test_results.values_list('answers__Какие имеются несовершенства', flat=True)

    # Get the medicines associated with the user based on the 'treats' field
    medicines = Medicine.objects.filter(id__in=medicine_ids)

    return user_test_results


