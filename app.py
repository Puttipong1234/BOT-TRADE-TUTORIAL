from flask import Flask
import time
from binance_connect import SIGNALS_BY_SYMBOLS

try:
    from config import *
except:
    from config_prod import *

app = Flask(__name__)

def job():
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



@app.route("/", methods=['POST'])
def test_signals():
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

@app.route("/<pairname>")
def pair_signals(pairname):

    """
    binance , Talibs , matplotlib
    """
    return "This is {} buying signals".format(pairname)

if __name__ == '__main__':
    #app.run(debug=True)
    
    input("PRESS ENTER TO RUN BOT")
    #sched.add_job(job, 'interval', minutes=1, id='SIGNALS_JOBS')
    #schedule.every(10).seconds.do(job)
    while True:
        print("=======SCANNOW=======")
        job()
        time.sleep(60)
        print("=====================")
        #schedule.run_pending()
        #if input("PRESS ENTER TO EXIT"):
        #    sched.remove_job('SIGNALS_JOBS')
        #    sched.shutdown()
        #   break

    print("THANK FOR YOUR KIND ATTENDTION")
        
        

    
