from flask import Flask, request

app = Flask(__name__)

@app.route("/payment-response", methods=["GET", "POST"])
def payment_response():
    msg = request.args.get("msg") or request.form.get("msg")
    print("Encrypted payment message:", msg)
    return "Payment response received", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
