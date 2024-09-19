create DATABASE banco_zl;
GRANT ALL PRIVILEGES ON banco_zl * To 'root' '@' localhost;
use banco_zl;
create TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(20) NOT NULL,
    login VARCHAR(20) NOT NULL
);