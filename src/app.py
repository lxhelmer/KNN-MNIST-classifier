from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import datetime
import numpy as np
from .lataaja import lataa_kuvat, lataa_nimikkeet
from .data.pistejoukko_gen import pistejoukko, ruudut
from .hausdorffvertailu import HausdorffVertailu
from .klahimmat import KLahimmat
from .ui.piirrin import Piirrin
HARJOITUS_POLKU = "../../train/train-"

html="""
<h1>
    TEST:
    <div id="clock">
       <h1> 
       error
       </h1>
    </div>
    <div>
        <form action="" onsubmit="sendMessage(event)">
        <input type="text" id="messageText" autocomplete="off"/>
        <button>Send</button>
        </form>
    </div>
    <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var str = '<h1> document.createTextNode(event.data) </h1>';
                var Obj = document.getElementById('TargetObject'); //any element to be fully replaced

                if(Obj.outerHTML) { //if outerHTML is supported
                    Obj.outerHTML=str; ///it's simple replacement of whole element with contents of str var
            };
                function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
    </script>
</h1>
"""

async def lifespan(app: FastAPI):
    harjoitus_mnist = lataa_kuvat(HARJOITUS_POLKU)
    #harjoitusdata on 2D Numpy array
    #jossa jokainen rivi on yksi kordinaattijoukko
    harjoitusdata = np.array(
            [pistejoukko(x) for x in harjoitus_mnist],
            dtype=object)
    print("Harjoitus pistejoukot luotu")
    #nimikkeet ovat 1D Numpy array
    harjoitusnimikkeet = lataa_nimikkeet(HARJOITUS_POLKU)
    print("Harjoitus nimikkeet ladattu")
    #ruudut ovat 3D-Numpy array
    #jossa jokainen rivi sisältää 28x28 2D Numpy arrayn
    harjoitusruudut = np.array(
            [ruudut(x) for x in harjoitus_mnist])
    print("Harjoitus ruudut luotu")

    testidata = lataa_kuvat(TESTI_POLKU)
    print("Testidata ladattu")

    testinimikkeet = lataa_nimikkeet(TESTI_POLKU)   #ladataan testinimikkeet normaali lista
    print("Testi nimikkeet ladattu")


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    websocket.accept()
    while True:
        if datetime.datetime.second() % 2 == 0:
            await websocket.send_text("Hello")
        else:
            await websocket.send_text("Goodbye")

@app.get("/")
def endpoint():
    return HTMLResponse(html)



def ajaKnn(luokiteltava):
    tulokset = []
    harjoitusdata = harjoitusdata.tolist()
    harjoitusruudut = harjoitusruudut.tolist()
    kaikki = 0
    oikein = 0

    for i in range(luok_num,loppu):
        luokiteltava_mnist = testidata[i]
        luokiteltava = pistejoukko(luokiteltava_mnist).tolist() #luodaan pixelitoteutuksesta kordinaatti joukko
        luokiteltava_ruudut = ruudut(luokiteltava_mnist).tolist()

        print("alkaa")
        alku_aika = time.time()

        #arvioidaan luokiteltavan kuvan nimike
        arvio = KNN.k_lahimmat(
                k,
                luokiteltava,
                harjoitusdata,
                harjoitusnimikkeet,
                harjoitusruudut,
                luokiteltava_ruudut
                )

        loppu_aika = time.time()


#        tulokset.append([arvio,testinimikkeet[i]])
#
#        if arvio == testinimikkeet[i]:
#            oikein += 1
#        kaikki += 1

#        raportti(oikein, kaikki, tulokset, luokiteltava_ruudut, loppu_aika-alku_aika)

    #Näytetään lopuksi luokittelut kootusti
    for res in tulokset:
        print("Arvioitu luku: " + str(res[0]) + " | Todellinen luku: " + str(res[1]),end="")
        if res[0] == res[1]:
            print(" |  SAMA!!!")
        else:
            print("")

