let block = {
    sender: "",
    recipient: "",
    amount: "",
    digitalSignature: "",
}

let privateKey = "";
let publicKey = "";
let bankPublicKey = "";
let loggedIn = false;
let loadingOverlay

function checkAmount(cb) 
{
    let balance;
    const Http = new XMLHttpRequest();
    Http.responseType = 'json';
    const url='http://localhost:5000/chain';
    Http.open("GET", url, true);
    Http.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); 
    Http.setRequestHeader('Access-Control-Allow-Origin', '*');
    Http.send(null);
    Http.onerror = function()
    {
        alert("Il server non risponde");
        loadingScreen();
        cb(-1);
        return;
    }
    Http.onload = function() {
        if (Http.status != 200) {
            alert("C'è stato un errore con la connessione alla blockchain"); 
            loadingOverlay.classList.add('hidden');
            return;
        }
        var jsonResponse = Http.response;
        let i = 0;
        for (let e in jsonResponse.chain)
        {
            for (let j in jsonResponse.chain[e].transactions)
            {
                if (jsonResponse.chain[e].transactions[j].recipient == publicKey && jsonResponse.chain[e].index > i) 
                {
                    i = jsonResponse.chain[e].index;
                    balance = jsonResponse.chain[e].transactions[j].balance;
                }
            }
        }
        if (i == 0) 
        {
            alert("Utente non trovato");
            loadingScreen();
            cb(-1);
        }
        cb(balance);
    };
}

function loadingScreen()
{
    loadingOverlay = document.querySelector('.loading');
                
    document.activeElement.blur();
    
    if (loadingOverlay.classList.contains('hidden'))
    {
        loadingOverlay.classList.remove('hidden');
    } 
    else
    {
        loadingOverlay.classList.add('hidden');
    }
}

function sendTransaction()
{
    const Http = new XMLHttpRequest();
    const url='http://localhost:5000/transactions/new';
    Http.open("POST", url);
    Http.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    Http.setRequestHeader('Content-Type', 'application/json');
    Http.setRequestHeader('Access-Control-Allow-Origin', '*');
    Http.send(JSON.stringify(block));
    Http.onerror = function()
    {
        alert("Il server non risponde");
        loadingScreen();
        return;
    }
    Http.onload = function() 
    {
        if(this.readyState == 4 && this.status == 200) 
        {
            alert(this.responseText);
            loadingScreen();
        }
    }
}