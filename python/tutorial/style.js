function getKeyMatrix(key,keyMatrix)
{
    let  k = 0;
    for (let i = 0; i < 3; i++)
    {
        for (let j = 0; j < 3; j++)
        {
            keyMatrix[i][j] = (key[k]).charCodeAt(0) % 65;
            k++;
        }
    }
}
 
// mã hoá 
function encrypt(cipherMatrix,keyMatrix,messageVector)
{
    let x, i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 1; j++)
        {
            cipherMatrix[i][j] = 0;
           
            for (x = 0; x < 3; x++)
            {
                cipherMatrix[i][j] +=
                    keyMatrix[i][x] * messageVector[x][j];
            }
           
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26;
        }
    }
}
 

function HillCipher(message, key)
{
    // Nhận ma trận khóa từ chuỗi khóa
    let keyMatrix = new Array(3);
    for(let i=0;i<3;i++)
    {
        keyMatrix[i]=new Array(3);
        for(let j=0;j<3;j++)
            keyMatrix[i][j]=0;
    }
    getKeyMatrix(key, keyMatrix);
   
    let messageVector = new Array(3);
    for(let i=0;i<3;i++)
    {
        messageVector[i]=new Array(1);
        messageVector[i][0]=0;
    }
   
    // Tạo vectơ cho tin nhắn
    for (let i = 0; i < 3; i++)
        messageVector[i][0] = (message[i]).charCodeAt(0) % 65;
   
    let cipherMatrix = new Array(3);
    for(let i=0;i<3;i++)
    {
        cipherMatrix[i]=new Array(1);
        cipherMatrix[i][0]=0;
    }
   
    // Hàm sau tạo ra
    // vectơ được mã hóa
    encrypt(cipherMatrix, keyMatrix, messageVector);
   
    let CipherText="";
   
    // Tạo văn bản được mã hóa từ
    // vectơ được mã hóa
    for (let i = 0; i < 3; i++)
        CipherText += String.fromCharCode(cipherMatrix[i][0] + 65);
   
    //
    document.write(" Ciphertext: " + CipherText);
}
 

// var message = document.getElementById('name');
// message.onchange = function(e){
//    mes =  console.log(e.target.value);
// }
// var key = document.getElementById('key');
// key.onchange = function(e){
//     var k= console.log(e.target.value);
// }
let message = "PHAMVANUAN";

let key = "GYBNQKURPK";
 
HillCipher(message, key);
 
 

