## Questão 2: Análise de Arquivos .pcap (60 pontos)

<hr/>

<p><strong>Contexto: </strong></p>

<p>Você foi solicitado a desenvolver uma aplicação em Python utilizando a biblioteca <i>requests</i> para efetuar o download de arquivos gerados pelo <i>TCP-DUMP</i> (arquivos .pcap).</p>

<p>Os arquivos a serem utilizados estão na URL https://malware-traffic-analysis.net (os arquivos estão na seção <i>My Blog Posts:</i>).</p>

<hr/>

<p><strong>Objetivo: </strong></p>

<p>Desenvolver um programa que:</p>

<ol type="a">
  <li>Solicite ao usuário a URL de um arquivo .pcap;<br/><br/></li>
  <li>O arquivo deverá ser baixado no mesmo diretório do programa que está sendo executado;<br/><br/></li>
  <li>Após o arquivo ter sido baixado, o programa deverá descompactá-lo (utilizar o módulo padrão <i>zipfile</i>).<br/>
    Para descompactar o arquivo a senha é <i>infected_AAAAMMDD</i>. Onde AAAA (com 4 dígitos) é o ano do arquivo, MM é o mês do arquivo (com 2 dígitos) e DD é o dia do arquivo (com 2 dígitos);<br/><br/></li>
  <li>Após a descompactação, o programa deverá efetuar a leitura e a análise do arquivo <i>.pcap</i> e deverá exibir as seguintes informações;<br/><br/></li>
  <ol type="i">
    <li>Mostre o conteúdo de cada um dos campos nos headers dos pacotes IPv4 capturados:<br/>
      (vide https://pt.wikipedia.org/wiki/Protocolo_de_Internet)<br/><br/></li>
    <li>Em que momento inicia/termina a captura de pacotes?<br/><br/></li>
    <li>Qual o tamanho do maior TCP pacote capturado?<br/><br/></li>
    <li>Há pacotes que não foram salvos nas suas totalidades? Quantos?<br/><br/></li>
    <li>Qual o tamanho médio dos pacotes UDP capturados?<br/><br/></li>
    <li>Qual o par de IP com maior tráfego entre eles?<br/><br/></li>
    <li>Com quantos outros IPs o IP da interface capturada interagiu?<br/><br/></li>
  </ol>
  <li>Para simplificar a implementação do item (d), recomenda-se utilizar o módulo <i>struct</i>;<br/><br/></li>
  <li>Não esquecer de tratar as exceções no programa;<br/><br/></li>
  <li>A modularização das funções que o programa deverá executar irá requerer a criação de <i>User Defined Functions - UDF</i>. As UDF´s deverão ser criadas em um arquivo em separado do programa. Para isso já foi disponibilizado um arquivo chamado <i>funcoes.py</i>.<br/><br/></li> 
</li>
</ol>

<hr/>

<p><strong>Observação:</strong></p>

<p>Só serão aceitas as seguintes biblioteca do Python: <i>requests</i>, <i>struct</i>, <i>zipfile</i>, <i>os</i>, <i>sys</i>, além da biblioteca de UDF´s criadas por vocês (<i>funcoes.py</i>).</p>

<hr/>
