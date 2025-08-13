from flask import Flask, request
from pyngrok import ngrok

app = Flask(__name__)

@app.route("/payment-response", methods=["GET", "POST"])
def payment_response():
    # Try both GET & POST in case gateway sends either
    msg = request.args.get("msg") or request.form.get("msg")
    print("Encrypted payment message:", msg)
    
    # Here you would normally call MFPayment/VerifyPGResponse with 'msg'
    return "Payment response received"

if __name__ == "__main__":
    # Open a public ngrok tunnel on port 5000
    public_url = ngrok.connect(5000)
    print(f"Public URL for CP_Payment_Response_Return_URL: {public_url}")
    app.run(port=5000)
