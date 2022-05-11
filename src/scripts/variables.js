let obj = {
    sender: "",
    recipient: "",
    amount: "",
    balance: ""
}

let privateKey = "";
let publicKey = "";
let bankPublicKey = "";
let balance = "";

function checkAmount(cb) 
{
    const Http = new XMLHttpRequest();
    Http.responseType = 'json';
    const url='http://localhost:5000/chain';
    Http.open("GET", url, true);
    Http.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); 
    Http.setRequestHeader('Access-Control-Allow-Origin', '*');
    Http.send(null);
    console.log(publicKey);
    Http.onload = function() {
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
        }
        cb(balance);
    };
}