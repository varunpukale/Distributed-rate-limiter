from flask import Flask, request, jsonify
from limiter.rate_limiter import RateLimiter

app = Flask(__name__)
limiter = RateLimiter(limit=5, window=60)

@app.route("/request", methods=["GET"])
def handle_request():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    if limiter.is_allowed(user_id):
        return jsonify({"message": "Request allowed"})
    else:
        return jsonify({"error": "Rate limit exceeded"}), 429

if __name__ == "__main__":
    app.run(port=5000)
