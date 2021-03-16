from flask import Flask , request
import time
from binance_connect import SIGNALS_BY_SYMBOLS
import threading





try:
    from config import *
except:
    from config_prod import *

app = Flask(__name__)



run = True

# def worker():
    
#     while run:
#         print(run)
#         print("=======SCANNOW=======")
#         job()
#         time.sleep(10)
#         print("=====================")

class SIGNALS_MORNITORING(threading.Thread):
    
    def __init__(self,coins_list = []):
        self.need_to_break = False
        self.coins_list = []
    
    def job(self):
        print("CHECKING FOR SIGNALS PLEASE WAITS")

        coin_list = ["BTCUSDT","ETHUSDT","BCHUSDT","LTCUSDT","DOGEUSDT","DOTUSDT","ADAUSDT","BNBUSDT"]
        for coin in coin_list:
            print(coin)
            r = SIGNALS_BY_SYMBOLS(coin)
            if r == "BUY":
                print("BUY NOW")
            
            elif r == "SELL":
                print("SELL NOW")
            
            else:
                print("NO SIGNALS")
    
    def run(self):
        print(self.need_to_break)
        while not self.need_to_break:
            print("=======SCANNOW=======")
            self.job()
            time.sleep(10)
            print("=====================")
    
    def stop(self):
        print("Stop Signals")
        self.need_to_break = True
    
    def resume(self,command):
        print("Resume Signals")
        self.need_to_break = command
    
    
    
    



SM = SIGNALS_MORNITORING()
SM_t = threading.Thread(target=SM.run,daemon=True)
SM_t.start()

@app.route("/<START>", methods=['POST'])
def stop_app(START):
    if START=="START":
        SM.resume(command=False)
        SM.run()
        # SM_t.start()
    else:
        SM.stop()

    
    return "ok"


@app.route("/", methods=['GET','POST'])
def test_signals():
    
    if request.method == "POST":
        msg = request.data.decode("utf-8")

        """
        PYBOTT : EASY EMA: order
        {{strategy.order.action}}
        @ {{strategy.order.contracts}}
        filled on {{ticker}}.
        New strategy position is
        {{strategy.position_size}}
        """
        #สรุปว่า BTCUSDT ขาย
        #if symbol , signals
            #PlaceSELL
        #else
            #PlaceBUY
        
        return "This is buying signals"

    else:
        return "กรุณานำ Link ไปใส่ไว้ที่ Webhook Tradingview"

@app.route("/<pairname>")
def pair_signals(pairname):

    """
    binance , Talibs , matplotlib
    """
    return "This is {} buying signals".format(pairname)

if __name__ == '__main__':
    app.run()
