from logger import get_logger

logger = get_logger()

class TradingBot:
    def __init__(self):
        logger.info("Trading Bot started")
        print("Trading Bot started 🚀")

    def place_order(self, side, symbol="BTCUSDT", quantity=0.001):
        try:
            logger.info(f"Received order: {side}")

            print(f"Placing {side} order")
            print(f"Symbol: {symbol}, Quantity: {quantity}")

            logger.info(f"Order simulated: {side} {symbol} {quantity}")
            print("Order simulated successfully ✅")

        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error occurred: {e}")
            