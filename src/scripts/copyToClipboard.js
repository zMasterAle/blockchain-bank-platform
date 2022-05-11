function copy(n)
{
    let copyText;
    if (!n)
    {
        copyText = document.getElementById("public_key");
    }
    else 
    {
        copyText = document.getElementById("private_key");
    }
    copyText.select();
    navigator.clipboard.writeText(copyText.value);
}