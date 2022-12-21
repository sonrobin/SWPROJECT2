from fastapi import FastAPI
import uvicorn
import yfinance as yf
import json

class Yfindices:
    
    def __init__(self):
        
        self.ameIND = {"S&P 500":"^GSPC", "Nasdaq":"^IXIC", "Dow":"^DJI",
                       "Russell 2000":"^RUT"}
        
        self.jpIND = {"Nikkei":"^N225"}
        
        self.chIND = {"HANG SENG INDEX":"^HSI"}
        
        self.dhIND = {"DAX":"^GDAXI"}
    
        self.frIND = {"CAC 40":"^FCHI"}
        
        self.iniIND = {"Jakarta Composite Index":"^JKSE"}
        
        self.malIND = {"FTSE Bursa Malaysia":"^KLSE"}

        self.korIND = {"KOSPI":"^KS11"}

        self.allIND = [self.ameIND, self.jpIND, self.chIND, self.dhIND, self.frIND,
                       self.iniIND, self.malIND, self.korIND]
        
        #self.countryTick(self.chIND)
        #self.allcountryTick()
        
    def countryTick(self,ctArr):
        indNAME = list(ctArr.keys())
        symNAME = list(ctArr.values())

        tickers = yf.Tickers(symNAME)
        
        
        for i in range(len(indNAME)):
            #print(indNAME[i])
            symtic = tickers.tickers[symNAME[i]].history(period="5d")
            
            #print(list(map(int,symtic["Close"])))
            #tickJSON[indNAME[i]] = list(map(int,symtic["Close"]))
        
        return indNAME[i], list(map(int,symtic["Close"]))
            
    #all of symbols values
    def allcountryTick(self):
        tickJSON ={}
        for ct in self.allIND:
            inct = list(ct.keys())
            insy = list(ct.values())
            
            tickers = yf.Tickers(insy)
            
            for i in range(len(inct)):
                symtic = tickers.tickers[insy[i]].history(period="5d")
                #print(inct[i])
                #print(symtic)
                tickJSON[inct[i]] = list(map(int,symtic["Close"]))
        
        return json.dumps(tickJSON)
    
yfi = Yfindices()
app = FastAPI()


@app.get("/")
async def root():
    return yfi.allcountryTick()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)