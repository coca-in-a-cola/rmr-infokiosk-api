from flask import Flask, request, current_app

def disable_request_stats():
    return any(substr in request.url for substr in current_app.config["DISABLE_METRICS_FOR"])