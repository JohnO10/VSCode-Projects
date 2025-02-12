
const QRCode = require('qrcode');

function gerarSenha(tamanho) {
  const caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{}|;:,.<>?!@#$%^&*()_+[]{}|;:,.<>?'
  let senha = '';
  for (let i = 0; i < tamanho; i++) {
    senha += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
  }
  return senha;
} 

const senha = gerarSenha(16)
console.log('Senha gerada:', senha);

function verificarForca(senha) {
  let forca = 0;
  if (senha.length >= 16) forca++;
  if (/[A-Z]/.test(senha)) forca++;
  if (/[a-z]/.test(senha)) forca++;
  if (/[0-9]/.test (senha)) forca++;
  if (/[^A-Za-z0-9]/.test(senha)) forca++;

    switch (forca) {
      case 5:
        return 'Muito forte';
      case 4:
        return 'Forte';
      case 3:
        return 'Moderada'
      case 2:
        return 'Fraca'
      default:
        return 'Muito Fraca'
    }
}

console.log(verificarForca(senha));
QRCode.toDataURL(senha, { errorCorrectionLevel: 'H' }, function(err,data_url) {
  if (err) throw err;
  console.log(data_url);
});