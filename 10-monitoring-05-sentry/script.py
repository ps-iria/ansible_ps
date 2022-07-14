import sentry_sdk

sentry_sdk.init(
    dsn="https://6871ab857fa14b25a8c7602a61a1e07d@o1318131.ingest.sentry.io/6572170",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

START = 10
END = -1


for item in range(START, END-1, -1):
    print (10 // item)