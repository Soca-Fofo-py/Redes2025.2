## Questão 1: Download de Arquivos (40 pontos)

<hr/>

<p><strong>Contexto: </strong></p>

<p>Você foi solicitado a desenvolver uma aplicação em Python utilizando a biblioteca <i>requests</i> para efetuar o download dos headers e dos conteúdos de uma URL.</p>

<hr/>

<p><strong>Objetivo: </strong></p>

<p>Desenvolver um programa que:</p>

<ol type="i">
  <li>Solicite ao usuário uma URL (obter URL´s diversas efetuando pesquisas no Google);<br/><br/></li>
  <li>Será necessário um tratamento na URL para separar algumas informações que serão necessárias para os itens a seguir;<br/><br/></li> 
  <li>Após a URL ser informada, o HEADER da requisição deverá ser baixado emn uma pasta chamada <i>headers</i>. 
    O programa deverá verificar se a pasta existe, se não existir ela deve ser criada através do programa. Essa pasta
    deverá ser criada no mesmo diretório que o programa que está sendo desenvolvido;<br/><br/></li>
  <li>O nome do arquivo de header a ser criado deve ser a parte que corresponde ao host na URL, substituindo os pontos por - (hífen) e o conteúdo deverá ser convertido para formato JSON.<br/>
    Exemplo: se a URL for <strong>https://suap.ifrn.edu.br/accounts/login/?next=/</strong>, o nome do arquivo header será <strong>suap_ifrn_edu_br.json</strong>.<br/><br/></li>
  <li>Para salvar o conteúdo da requisição (<i>content</i>) deverá ser observado a chave <i>Content-Type</i> do header. Considerando que:<br/><br/></li>
    <ul>
      <li>Se o tipo de conteúdo for <i>text/html</i>, o arquivo deverá ser salvo com o nome seguindo a mesma orientação do item (iv), sendo que a extensão deverá ser <i>.html</i>, 
        e em um diretório chamado <i>content_html</i> (deverá ser observado o mesmo procedimento adotado no item (iii) a respeito da necessidade de criação do diretório);</i><br/><br/></li>
      <li>Se o tipo de conteúdo for <i>image/jpeg</i>, o arquivo deverá ser salvo com o nome que consta na URL (geralmente a última parte da URL), sendo que a extensão deverá ser <i>.jpg</i>,  
        e em um diretório chamado <i>content_jpg</i> (deverá ser observado o mesmo procedimento adotado no item (iii) a respeito da necessidade de criação do diretório);</i><br/><br/></li>
      <li>Seguir esse racioncínio para os demais tipos de conteúdos que venham a surgir;<br/><br/></li>
      <li>Para qualquer tipo de arquivo, deve-se efetuar a troca de quaisquer caracteres especiais (%, #, ?, ...) por _ (underline) no nome do arquivo;<br/><br/></li>
    </ul>
  <li>Não esquecer de tratar as exceções no programa;<br/><br/></li>
  <li>A modularização das funções que o programa deverá executar irá requerer a criação de <i>User Defined Functions - UDF</i>. As UDF´s deverão ser criadas em um arquivo em separado do programa. Para isso já foi disponibilizado um arquivo chamado <i>funcoes.py</i>.<br/><br/></li> 
</ol>

<hr/>

<p><strong>Observação:</strong></p>

<p>Só serão aceitas as seguintes biblioteca do Python: <i>requests</i>, <i>json</i>, <i>os</i>, <i>sys</i>, além da biblioteca de UDF´s criadas por vocês (<i>funcoes.py</i>).</p>

<hr/>
