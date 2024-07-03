console.log("Sanity check!");

// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/")
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
