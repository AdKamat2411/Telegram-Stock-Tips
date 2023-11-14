#Final Exec
import scraper
import analyser
import time

def final():
    if __name__=="__main__":
        scraper.data()
        pe,ce=analyser.strike()

    if len(pe)>len(ce):
        print("avg. pe:", sum(pe)/len(pe))
        print("stop loss:" ,sum(pe)/len(pe)+34.22)
    ##    print("max. pe:", max(pe))
    ##    print("median pe:", pe[len(pe//2)])
    ##    print("min. pe:", min(pe))
        print("pe:",pe)
        print("-------------------------------------------------------------------------------------------------------------------")
    elif len(ce)>len(pe):
        print("avg. ce:", sum(ce)/len(ce))
        print("stop loss:" ,sum(ce)/len(ce)-34.22)
    ##    print("max. ce:", max(ce))
    ##    print("median ce:", ce[len(ce//2)])
    ##    print("min. ce:", min(ce))
        print("ce:",ce)
        print("-------------------------------------------------------------------------------------------------------------------")
    else:
        print("Not enough data")
        print("-------------------------------------------------------------------------------------------------------------------")

while True:
    final()
    time.sleep(10)



    
    
    
