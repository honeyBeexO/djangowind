document.addEventListener("DOMContentLoaded", function() {
console.log("Sanity check!");

// Get the button element
const submitBtn = document.querySelector("#submitBtn");

// Get URLs from data attributes
const configUrl = submitBtn.getAttribute('data-config-url');
const checkoutSessionUrl = submitBtn.getAttribute('data-checkout-session-url');

// Get Stripe publishable key
fetch(configUrl)
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler
  submitBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch(checkoutSessionUrl)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log('Checkout session data:', data);  // Log the received data
      if (data.error) {
        console.error('Error creating checkout session:', data.error);
        return;
      }
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId});
    })
    .then((res) => {
      if (res.error) {
        console.error('Error redirecting to checkout:', res.error);
      }
    })
    .catch((error) => {
      console.error('Error in fetch chain:', error);
    });
  });
});
});
