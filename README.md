## Prática 5 - SystemD e personalização de serviços de inicialização em Linux embarcado 

Essa prática versa sobre o funcionamento do sistema de inicialização de sistemas embarcados. Na Raspberry Pi, após o power on, se inicia um processo de bootloader que consiste em três estágios. O primeiro estágio inicializa a GPU e o arquivo bootcode.bin é buscado. Em seguida, a SDRAM é habilitada, o firmware da GPU é buscado e os periféricos são inicializados. Então, o firmware da GPU é carregado e executado, e o kernel Linux é carregado na RAM e executado na CPU. Após esses três estágios do bootloader, é executado o init system, responsável por carregar o sistema operacional. No caso da Raspberry Pi, o init system utilizado é o systemD. Ele é responsável por executar arquivos com extensão .service, que definem aplicativos que devem funcionar a partir do momento que a placa é ligada. Assim, nessa prática, será criado um arquivo .service de modo a adicionar um novo processo que deve ser executado pela Raspberry Pi assim que ela inicializa.
  
Foi criado um arquivo denominado `blink.py`, que consiste no código a ser executado quando a Raspberry inicializa. Ainda, foi criado também o arquivo `stopblink.py`, que é executado quando a placa é desligada. Eles consistem em códigos que fazem um circuito com um LED montado em protoboard piscar a cada um segundo, e outro que para esse processo, respectivamente. O arquivo `blink.service` referencia os locais em que estão os códigos Python, e qual deles deve ser compilado ao inicializar a placa e qual é compilado ao desligá-la. Este código é, portanto, responsável pelo funcionamento do programa na inicialização sendo lido no momento em que a Raspberry for ligada. Esse arquivo é colocado na pasta systemd/system, que contém todos os arquivos .service a serem executados quando a placa é ligada. A figura a seguir mostra o status do serviço blink em execução.

![scrotservice](https://github.com/user-attachments/assets/6edc7feb-0aa2-40c0-9ee7-38eea881ab97)

Já a figura abaixo mostra a montagem e o funcioamento do circuito do LED, comentado anteriormente, na protoboard que conecta o pino de GPIO utilizado no código Python com um LED, por meio de um resistor.

![20241111_115342](https://github.com/user-attachments/assets/4bbe89b6-7cc0-4f55-9c83-307f2b7dd725)

Por fim, o processo foi documentado neste repositório github. Aqui, portanto, estão disponíveis os três códigos que foram utilizados para o funcionamento desejado. Em seguida, foram explorados os comandos atrelados ao git, como 
``` 
git add
git commit
git push
```
para que os códigos fossem salvos no repositório. Além disso, foi coletado o histórios de _commits_ utilizados, que também está em um arquivo deste repositório, `historicogit.txt`, bem como um arquivo `.gitignore` que faz com que, se um outro usuário clonar o repositório, o arquivo de extensão .txt contando o token de acesso não seja clonado junto.
