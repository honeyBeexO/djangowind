# payments/views.py

from django.conf import settings # type: ignore # new
from django.http.response import JsonResponse, HttpResponse # type: ignore # new
from django.views.decorators.csrf import csrf_exempt # type: ignore # new
from django.views.generic.base import TemplateView # type: ignore
import stripe # type: ignore
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'home.html'


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # stripe.Coupon.create(
        #     percent_off=20,
        #     duration="once",
        # )
        
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'buy/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'buy/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                #allow_promotion_codes=True,
                # discounts=[
                #     {
                #         "coupon": 'yaEA65kR',
                #      }
                # ],
                # line_items=[
                #     {
                #         'price_data': {
                #             'currency': 'GBP',
                #             'product_data': {
                #                 'name': 'K-BiS',
                #             },
                #             'unit_amount': 2000,
                #         },
                #         'quantity': 1,
                #     }
                # ]
                line_items=[
                    {
                        "price": 'price_1PYUnoJ3teq29stwDxDL9VFV', 
                        "quantity": 1
                        
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
   
# def sucess_view(request):
#     messages.success(request, f'Payement Successfully Completed!')
#     return redirect(request,reverse('index'))     

class SuccessView(TemplateView):
    #HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    #messages.success(request, f'Account was successfully registered for {username}! You can now login with using your details')
    #return redirect('login')
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
    
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
