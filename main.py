from bot import TradingBot

if __name__ == "__main__":
    bot = TradingBot()

    while True:
        side = input("Enter BUY or SELL (or exit): ").upper()

        if side == "EXIT":
            print("Shutting down bot 👋")
            break

        bot.place_order(side)